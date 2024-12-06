import math
import numpy
import ultralytics

from Commons.AbstractDetector import AbstractDetector
from Commons.FrameCoordinates import FrameCoordinates
from Commons.ImageDetectionResult import ImageDetectionResult
from Commons.Point import Point


class MachineLearningImageAnalysisDetector(AbstractDetector):
    def __init__(self, model_path: str, class_names: list[str], prediction_image_size: int):
        self.__model = ultralytics.YOLO(model_path)
        self.__class_names = class_names
        self.__prediction_image_size = prediction_image_size

    def detect(self, frame: numpy.ndarray) -> list[ImageDetectionResult]:
        results = list(self.__model.predict(frame, imgsz=self.__prediction_image_size))
        image_detection_result_list = list()

        for result in results:
            boxes = result.boxes

            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0]

                image_detection_result_list.append(
                    ImageDetectionResult(
                        frame_coordinates=FrameCoordinates(
                                                top_left=Point(int(x1), int(y1)),
                                                top_right=Point(int(x2), int(y1)),
                                                bottom_right=Point(int(x2), int(y2)),
                                                bottom_left=Point(int(x1), int(y2))
                                          ),
                        content=self.__class_names[int(box.cls[0])],
                        confidence=math.ceil((box.conf[0] * 100)) / 100
                    )
                )

        return sorted(image_detection_result_list, key=lambda image_detection_result: image_detection_result.content)
