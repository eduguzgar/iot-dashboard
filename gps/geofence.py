def point_in_polygon(lat, lon, polygon):
    """Ray-casting algorithm based on:
    http://www.ecse.rpi.edu/Homepages/wrf/Research/Short_Notes/pnpoly.html"""

    x = lon
    y = lat

    inside = False
    for edge in polygon:
        # i vertex
        xi = edge[1]
        yi = edge[0]

        # j vertex
        xj = edge[3]
        yj = edge[2]

        intersect = ((yi > y) != (yj > y)) and (
            x < (xj - xi) * (y - yi) / (yj - yi) + xi
        )

        # if intersections are an odd number, then the point is inside the polygon
        if intersect is True:
            inside = not inside

    return inside
