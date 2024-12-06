import cv2
import concurrent.futures
import numpy

from Commons.AbstractDetector import AbstractDetector
from Commons.FrameCoordinates import FrameCoordinates
from Commons.ImageDetectionResult import ImageDetectionResult
from Commons.Point import Point
from TraditionalImageAnalysis.TemplateImage import TemplateImage


class TraditionalImageAnalysisDetector(AbstractDetector):
    def __init__(self, template_images: list[TemplateImage], needed_matches: int):
        self.__orb = cv2.ORB_create()
        self.__bf_matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
        self.__template_images = template_images
        self.__needed_matches = needed_matches

        for template_image in self.__template_images:
            template_image.file = cv2.cvtColor(cv2.imread(template_image.path), cv2.COLOR_BGR2GRAY)
            template_image.keypoints, template_image.descriptors = self.__orb.detectAndCompute(template_image.file, None)

        self.__thread_pool = concurrent.futures.ThreadPoolExecutor(max_workers=self.__template_images.__len__())

    def __detect_template_image(self, descriptors, keypoints, template_image):
        if descriptors is not None:
            matches = self.__bf_matcher.match(template_image.descriptors, descriptors)

            if len(matches) > self.__needed_matches:
                template_image_matching_points = numpy.float32([template_image.keypoints[match.queryIdx].pt for match in matches])
                original_frame_matching_points = numpy.float32([keypoints[m.trainIdx].pt for m in matches])
                homography_matrix, _ = cv2.findHomography(template_image_matching_points, original_frame_matching_points, cv2.RANSAC, 5.0)

                template_image_height, template_image_width = template_image.file.shape
                template_image_corners_coordinates = numpy.float32([[0, 0], [0, template_image_height - 1], [template_image_width - 1, template_image_height - 1], [template_image_width - 1, 0]])

                return cv2.perspectiveTransform(template_image_corners_coordinates.reshape(-1, 1, 2), homography_matrix), template_image.content

    def detect(self, frame: numpy.ndarray) -> list[ImageDetectionResult]:
        grayscaled_frame_keypoints, grayscaled_frame_descriptors = self.__orb.detectAndCompute(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), None)

        futures = []
        for template_image in self.__template_images:
            futures.append(self.__thread_pool.submit(self.__detect_template_image,
                                                     grayscaled_frame_descriptors,
                                                     grayscaled_frame_keypoints,
                                                     template_image))

        future_results = []
        for future in concurrent.futures.as_completed(futures):
            future_results.append(future.result())

        image_detection_result_list = []
        for future_result in future_results:
            if future_result is None:
                continue

            frame_target_points, template_image_content = future_result
            if frame_target_points is not None:
                frame_target_points_converted=numpy.int32(numpy.squeeze(frame_target_points)).tolist()

                image_detection_result_list.append(
                    ImageDetectionResult(
                        frame_coordinates=FrameCoordinates(
                            top_left=Point(frame_target_points_converted[0][0], frame_target_points_converted[0][1]),
                            top_right=Point(frame_target_points_converted[3][0], frame_target_points_converted[3][1]),
                            bottom_right=Point(frame_target_points_converted[2][0], frame_target_points_converted[2][1]),
                            bottom_left=Point(frame_target_points_converted[1][0], frame_target_points_converted[1][1])
                        ),
                        content=template_image_content
                    )
                )

            image_detection_result_list.sort(key=lambda image_detection_result: image_detection_result.content)

        return sorted(image_detection_result_list, key=lambda image_detection_result: image_detection_result.content)
