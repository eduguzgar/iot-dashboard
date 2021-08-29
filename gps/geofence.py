def point_in_polygon(lat, lon, polygon):
    """Ray-casting algorithm based on:
    http://www.ecse.rpi.edu/Homepages/wrf/Research/Short_Notes/pnpoly.html"""
    x = lon
    y = lat

    inside = False
    for i in range(len(polygon) - 1):
        # i vertex
        xi = polygon[i][1]
        yi = polygon[i][0]
        # j vertex
        xj = polygon[i + 1][1]
        yj = polygon[i + 1][0]
        # conditions and ecuation of a line
        intersect = ((yi > y) != (yj > y)) and (
            x < (xj - xi) * (y - yi) / (yj - yi) + xi
        )
        # if intersections are an odd number, then the point is inside the polygon
        if intersect is True:
            inside = not inside

    return inside
    
