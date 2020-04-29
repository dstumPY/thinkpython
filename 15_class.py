from math import sqrt


class Point:
    ""


class Circle:
    ""


class Rect:
    ""


def point_in_circle(circ: Circle, p: Point) -> bool:
    # calculate distance to center of circ
    dist = sqrt((p.x - circ.center.x) ** 2 + (p.y - circ.center.y) ** 2)
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
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def rect_in_circle(circ: Circle, rect: Rect) -> bool:
    # calculate the second corner point
    p1 = Point()
    p2 = Point()
    p3 = Point()
    p1.x = rect.corner.x + rect.width
    p1.y = rect.corner.y + rect.height
    p2.x = rect.corner.x + rect.width
    p2.y = rect.corner.y
    p3.x = rect.corner.x
    p3.y = rect.corner.y + rect.height
    # calculate distances to the center
    dist1 = eucl_dist(p1.x, circ.center.x, p1.y, circ.center.y)
    dist2 = eucl_dist(p2.x, circ.center.x, p2.y, circ.center.y)
    dist3 = eucl_dist(p3.x, circ.center.x, p3.y, circ.center.y)
    dist4 = eucl_dist(rect.corner.x, circ.center.x, rect.corner.y, circ.center.y)

    return all(dist <= circ.radius for dist in [dist1, dist2, dist3, dist4])


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
