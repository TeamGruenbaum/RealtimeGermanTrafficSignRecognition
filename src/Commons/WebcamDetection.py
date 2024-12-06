import cv2
import numpy

from Commons.AbstractDetector import AbstractDetector


class WebcamDetection:
    def __init__(self, detector: AbstractDetector, box_color: tuple[int, int, int], box_thickness: int, font: int, font_scale: int, font_color: tuple[int, int, int], font_thickness: int, window_name: str, window_close_key: str):
        self.__detector = detector
        self.__box_color = box_color
        self.__box_thickness = box_thickness
        self.__font = font
        self.__font_scale = font_scale
        self.__font_color = font_color
        self.__font_thickness = font_thickness
        self.__window_name = window_name
        self.__window_close_key = window_close_key
        self.__video_capture = cv2.VideoCapture(0)

    def start_detection(self) -> None:
        while self.__video_capture.isOpened():
            has_returned, frame = self.__video_capture.read()
            if not has_returned:
                print("FEHLER: Lesen von der Webcam nicht möglich.")
                break

            image_detection_results = self.__detector.detect(frame)

            frame_described = frame.copy()
            for image_detection_result in image_detection_results:
                frame_coordinates_list = [
                    image_detection_result.frame_coordinates.top_left.to_tuple(),
                    image_detection_result.frame_coordinates.top_right.to_tuple(),
                    image_detection_result.frame_coordinates.bottom_right.to_tuple(),
                    image_detection_result.frame_coordinates.bottom_left.to_tuple()
                ]
                frame_described = cv2.polylines(frame, numpy.int32([numpy.int32(frame_coordinates_list)]), True, self.__box_color, self.__box_thickness)
                cv2.putText(frame_described, image_detection_result.content + (f" ({image_detection_result.confidence})" if image_detection_result.confidence is not None else ""), image_detection_result.frame_coordinates.bottom_right.to_tuple(), self.__font, self.__font_scale, self.__font_color, self.__font_thickness, cv2.LINE_AA)

            cv2.imshow(self.__window_name, frame_described)

            if (cv2.waitKey(1) & 0xFF) == ord(self.__window_close_key):
                break

        self.__video_capture.release()
        cv2.destroyAllWindows()
