from typing import Self
from numpy import arctan2, rad2deg

class Vector2:
    """Class to represent a 2D vector."""
    def __init__(self, x: int, y: int) -> None:
        self.x: int = x
        self.y: int = y

    def __add__(self, other: Self) -> Self:
        """Returns the sum of self and another vector."""
        return Vector2(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other: Self) -> Self:
        """Returns other subtracted from self, or equivalently, self + (-other)."""
        return Vector2(self.x - other.x, self.y - other.y)
    
    def getAngleRad(self) -> float:
        """Returns signed angle between this vector and a right unit vector in radians."""
        return arctan2(self.y, self.x)
    
    def getAngleDeg(self) -> float:
        """Returns signed angle between this vector and a right unit vector in radians."""
        return rad2deg(self.getAngleRad())

    @staticmethod
    def dotProduct(vecA: Self, vecB: Self) -> int:
        """Returns dot product of two vectors A and B."""
        return vecA.x * vecB.x + vecA.y * vecB.y