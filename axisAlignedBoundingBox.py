def axisAlignedBoundingBox(x, y):
    xmax = -10
    xmin = 10
    ymax = -10
    ymin = 10
    for i in x:
        if (i>xmax):
            xmax = i
        if (i<xmin):
            xmin = i
    for j in y:
        if (j>ymax):
            ymax = j
        if (j<ymin):
            ymin = j
    return (xmax - xmin)*(ymax -ymin)