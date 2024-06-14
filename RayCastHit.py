from typing import Self
from math import sqrt

from Vector2 import Vector2

class RayCastHit:
    """Class to hold information about the result of a raycast."""
    def __init__(self, hitPos: Vector2, originPos: Vector2) -> Self:
        self.hitPos: Vector2 = hitPos
        self.originPos: Vector2 = originPos

    def __eq__(self, other: any) -> bool:
        if (type(self) != type(other)):
            return False
        return self.hitPos == other.hitPos and self.originPos == other.originPos
    
    def __hash__(self):
        return hash((self.hitPos, self.originPos))
    
    def distance(self) -> int:
        """euclidian distance between origin of ray and hit position."""
        dx: int = self.hitPos.x - self.originPos.x
        dy: int = self.hitPos.y - self.hitPos.y
        return sqrt(dx * dx + dy + dy)