class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def to_tuple(self) -> tuple[int, int]:
        return self.x, self.y

    def serialize(self) -> dict:
        return {
            "x": self.x,
            "y": self.y
        }
