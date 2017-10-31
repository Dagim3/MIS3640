import math

class Point:
    """Represents a point in 2-D space.

    attributes: x, y
    """


def print_point(p):
    """Print a Point object in human-readable format."""
    print('(%g, %g)' % (p.x, p.y))


class Rectangle:
    """Represents a rectangle. 

    attributes: width, height, corner.
    """


def find_center(rect):
    """Returns a Point at the center of a Rectangle.

    rect: Rectangle

    returns: new Point
    """
    p = Point()
    p.x = rect.corner.x + rect.width/2.0
    p.y = rect.corner.y + rect.height/2.0
    return p


def grow_rectangle(rect, dwidth, dheight):
    """Modifies the Rectangle by adding to its width and height.

    rect: Rectangle object.
    dwidth: change in width (can be negative).
    dheight: change in height (can be negative).
    """
    rect.width += dwidth
    rect.height += dheight


def main():
    blank = Point()
    blank.x = 3
    blank.y = 4
    print('blank', end=' ')
    print_point(blank)

    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 0.0
    box.corner.y = 0.0

    center = find_center(box)
    print('center', end=' ')
    print_point(center)

    print(box.width)
    print(box.height)
    print('grow')
    grow_rectangle(box, 50, 100)
    print(box.width)
    print(box.height)


if __name__ == '__main__':
    main()


class Point(object):
    """Represents a point in 2d space."""

point_one = Point()
point_two = Point()

point_one.x, point_one.y = 6.0, 1.0
point_two.x, point_two.y = 2.0, 6.0


def distance_between_points(p1, p2):
    """Returns the distance between two points in 2d space."""
    delta_x = p2.x - p1.x
    delta_y = p2.y - p1.y
    return math.sqrt(delta_x ** 2 + delta_y ** 2)

print ("The distance between point one at (%g,%g)" % (point_one.x, point_one.y))
print ("and point two at (%g,%g)" % (point_two.x, point_two.y))
print ("is %.3f" % distance_between_points(point_one, point_two))