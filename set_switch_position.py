from math import sin, cos, radians


sw_pos = dict()
with open('switch_position.csv') as f:
    for i, line in enumerate(f):
        spline = line.split(',')
        label = spline[0].replace('comma', ',') # workaround since were reading a csv...
        x = float(spline[1])
        y = float(spline[2])
        # set rotation angle based on x coordinate
        if 125<x<210:
            r = -120
        elif 210<x<300:
            r = 120
        else:
            r = 0
        sw_pos[label] = [x, y, r, i+1]

# set switch position
import pcbnew
board = pcbnew.GetBoard()
for key in sw_pos:
    # set switch position
    sw = board.FindModuleByReference(key)
    params = sw_pos[key]
    print key, params
    sw.SetPosition(pcbnew.wxPointMM(params[0],params[1]))
    sw.SetOrientation(params[2])
    # set diode position
    di = board.FindModuleByReference('D{}'.format(params[3]))
    s = sin(radians(params[2]/10))
    c = cos(radians(params[2]/10))
    dx = 8.5 * c + 1.5 * s
    dy = 8.5 * s - 1.5 * c
    x = params[0] + dx
    y = params[1] - dy
    print x, y
    di.SetPosition(pcbnew.wxPointMM(x, y))
    di.SetOrientation(params[2]+900)
