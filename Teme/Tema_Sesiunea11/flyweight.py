'''
Structural pattern: Flyweight

Flyweight method - is a structural design pattern that lets you fit more objects into the available amount of
                   RAM by sharing common parts of state between multiple objects instead of keeping
                   all of the data in each object.
One important feature of flyweight objects is that they are immutable. This means that they cannot be
modified once they have been constructed.
Flyweight Method which allows you to fit more objects into the available amount of RAM by sharing common parts of the objects.

Applicability:
              - To Reduce the number of Objects: Generally, Flyweight method is used when our application has
              a lot of heavy weight objects, to solve this problem we use Flyweight method to get rid of unnecessary
              memory consumption.
              - Object independent Applications: When our application if independent of the object created, then we can
              make use of this method inorder to save lot of machine space.
              - Project Cost Reduction: When it is required to reduce the cost of project in terms of space and
              time complexity, it is always preferred to use the Flyweight method.

PROS:
        - Reduced use of RAM: when we have a lot of similar objects present in our application, it's always better
          to use Flyweight method in order to save a lot of space in RAM
        - Improved Data Caching: When the need of client or user is High response time, it is always preferred
        to use Flyweight method because it helps in improving the Data Caching.
        - Improved performance: It ultimately leads to improve in performance because we are using less
        numbers of heavy objects.
CONS:
        - Breaking Encapsulation: Whenever we try to move the state outside the object, we do breaking of encapsulation
        and may become less efficient than keeping the state inside the object.
        - Hard to handle: Usage of Flyweight method depends upon the language we use, easy to use in
        language like Python, Java where all object variables are references but typical to use in language like C,
        C++ where objects can be allocated as local variables on the stack and destroyed as a result of programmer action.
        - Complicated Code: Using Flyweight method always increases the complexity of the code to understand
        for the new developers.

'''

# Problem:
# Imagine mapping application, such as: Open Street Maps, Google Maps, Yelp, Trip Advisor etc.
# There are thousands points of interests such as Cafe, Shops, Restaurants, School etc.
# Icons can take a lot of memory, times number of points on the map
# It might crash with out of memory error (especially on mobile devices)
# Solution:
# Separate the data you want to share from other data
# Pattern will create a dict with point type and its icon
# It will reuse icon for each type
# So it will prevent from storing duplicated data in memory
from dataclasses import dataclass, field
from enum import Enum
from typing import Final


class PointType(Enum):
    HOSPITAL = 1
    CAFE = 2
    RESTAURANT = 3


@dataclass
class PointIcon:
    type: Final[PointType]   # 1064 bytes
    icon: Final[bytearray]   # empty: 56 bytes, but with PNG icon: 20 KB

    def get_type(self):
        return self.type


@dataclass
class PointIconFactory:
    icons: dict[PointType, PointIcon] = field(default_factory=dict)

    def get_point_icon(self, type: PointType) -> PointIcon:
        if not self.icons.get(type):
            self.icons[type] = PointIcon(type, None)  # Here read icon from filesystem
        return self.icons.get(type)


@dataclass
class Point:
    x: int  # 28 bytes
    y: int  # 28 bytes
    icon: PointIcon

    def draw(self) -> None:
        print(f'{self.icon.get_type()} at ({self.x}, {self.y})')


@dataclass
class PointService:
    icon_factory: PointIconFactory

    def get_points(self) -> list[Point]:
        points: list[Point] = list()
        point: Point = Point(1, 2, self.icon_factory.get_point_icon(PointType.CAFE))
        points.append(point)
        return points


if __name__ == '__main__':
    service = PointService(PointIconFactory())
    for point in service.get_points():
        point.draw()
        # PointType.CAFE at (1, 2)

