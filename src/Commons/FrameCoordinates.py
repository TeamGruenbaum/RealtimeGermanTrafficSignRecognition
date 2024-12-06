from Commons.Point import Point

class FrameCoordinates:
    def __init__(self, top_left: Point, top_right: Point, bottom_right: Point, bottom_left: Point):
        self.top_left = top_left
        self.top_right = top_right
        self.bottom_right = bottom_right
        self.bottom_left = bottom_left

    def serialize(self) -> dict:
        return {
            "topLeft": self.top_left.serialize(),
            "topRight": self.top_right.serialize(),
            "bottomRight": self.bottom_right.serialize(),
            "bottomLeft": self.bottom_left.serialize()
        }
