from math import sqrt
class Point:
    ""

class Circle:
    ""

class Rect:
    ""

def point_in_circle(circ: Circle, p: Point) -> bool:
    # calculate distance to center of circ
    dist = sqrt((p.x - circ.center.x)**2 + (p.y - circ.center.y)**2)
    return dist <= circ.radius

def test_point_in_circle() -> bool:
    c = Circle()
    c.radius = 75
    p = Point()
    p.x = 150
    p.y = 100
    c.center = p

    new_p = Point()
    new_p.x = 15500
    new_p.y = 10500

    print(point_in_circle(c, new_p))

def eucl_dist(x1, x2, y1, y2) -> float:
    return sqrt((x1 - x2)**2 + (y1 - y2)**2 )

def rect_in_circle(circ: Circle, rect: Rect) -> bool:
    # TODO: every corner point must lie inside the circle
    # calculate the second corner point
    p = Point()
    p.x = rect.corner.x + rect.width
    p.y = rect.corner.y + rect.height

    # calculate distances to the center
    dist1 = eucl_dist(p.x, circ.center.x, p.y, circ.center.y)
    dist2 = eucl_dist(
        rect.corner.x, circ.center.x, rect.corner.y, circ.center.y
        )
    
    return (dist1 <= circ.radius) and (dist2 <= circ.radius)


def test_rect_in_circle() -> bool:
    c = Circle()
    c.radius = 75
    p = Point()
    p.x = 150
    p.y = 100
    c.center = p

    new_p = Point()
    new_p.x = 145
    new_p.y = 95
    rect = Rect()
    rect.width = 10
    rect.height = 10
    rect.corner = new_p
    print(rect_in_circle(c, rect))

test_rect_in_circle()


