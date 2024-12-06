from Commons.FrameCoordinates import FrameCoordinates


class ImageDetectionResult:
    def __init__(self, frame_coordinates: FrameCoordinates, content: str, confidence: float | None = None):
        self.frame_coordinates = frame_coordinates
        self.content = content
        self.confidence = confidence

    def serialize(self) -> dict:
        return {
            "frameCoordinates": self.frame_coordinates.serialize(),
            "content": self.content,
            "confidence": self.confidence
        }