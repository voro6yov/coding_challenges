import math
from typing import List


def main() -> None:
    with open('INPUT.txt', 'r') as file:
        N: int = int(file.readline().rstrip())
        for _ in range(N):
            line = file.readline().rstrip()
            data = [int(i) for i in line.split(' ')]
            position: Point = Point(data[0], data[1])
            rectangle: Rectangle = Rectangle(
                Point(data[2], data[3]),
                Point(data[4], data[5]),
                Point(data[6], data[7]),
                Point(data[8], data[9]),
            )
            print(rectangle.is_inside(position))


class Point:
    def __init__(self, x: int, y: int) -> None:
        self._x = x
        self._y = y

    @property
    def x(self) -> int:
        return self._x

    @property
    def y(self) -> int:
        return self._y


class Segment:
    def __init__(self, point_a: Point, point_b: Point) -> None:
        self._point_a = point_a
        self._point_b = point_b

    @property
    def point_a(self) -> Point:
        return self._point_a

    @property
    def point_b(self) -> Point:
        return self._point_b

    @property
    def length(self) -> float:
        return math.sqrt(pow((self.point_b.x - self.point_a.x), 2) + 
                         pow((self.point_b.y - self.point_a.y), 2))


class Triangle:
    def __init__(self, 
                 point_a: Point, 
                 point_b: Point, 
                 point_c: Point) -> None:
        self._point_a = point_a
        self._point_b = point_b
        self._point_c = point_c

    @property
    def side_a(self) -> Segment:
        return Segment(self._point_a, self._point_b)

    @property
    def side_b(self) -> Segment:
        return Segment(self._point_b, self._point_c)

    @property
    def side_c(self) -> Segment:
        return Segment(self._point_c, self._point_a)

    @property
    def perimeter(self) -> float:
        return (self.side_a.length + 
                self.side_b.length + 
                self.side_c.length)

    @property
    def area(self) -> float:
        half_perimeter: float = self.perimeter / 2
        return math.sqrt(half_perimeter * 
                        (half_perimeter - self.side_a.length) * 
                        (half_perimeter - self.side_b.length) * 
                        (half_perimeter - self.side_c.length))


class Rectangle:
    def __init__(self, 
                 lower_left: Point, 
                 higher_left: Point, 
                 higher_right: Point, 
                 lower_right: Point) -> None:
        self._lower_left = lower_left
        self._higher_left = higher_left
        self._higher_right = higher_right
        self._lower_right = lower_right

    @property
    def side_a(self) -> Segment:
        return Segment(self._lower_left, self._higher_left)

    @property
    def side_b(self) -> Segment:
        return Segment(self._higher_left, self._higher_right)

    @property
    def side_c(self) -> Segment:
        return Segment(self._higher_right, self._lower_right)

    @property
    def side_d(self) -> Segment:
        return Segment(self._lower_right, self._lower_left)

    @property
    def sides(self) -> List[Segment]:
        return [self.side_a, self.side_b, self.side_c, self.side_d]

    @property
    def area(self) -> int:
        return self.side_a.length * self.side_b.length

    def is_inside(self, position: Point) -> bool:
        area: int = 0
        for side in self.sides:
            area += Triangle(side.point_a, side.point_b, position).area

        if round(area, 2) == round(self.area, 2):
            return True
        else:
            return False



if __name__ == '__main__':
    main()
    