import abc
import numpy

from Commons.ImageDetectionResult import ImageDetectionResult

class AbstractDetector:
    @abc.abstractmethod
    def detect(self, frame: numpy.ndarray) -> list[ImageDetectionResult]:
        pass
