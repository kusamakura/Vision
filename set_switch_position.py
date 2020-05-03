sw_pos = dict()
with open('switch_position.csv') as f:
    for line in f:
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
        sw_pos[label] = [x, y, r]

# set switch position
import pcbnew
board = pcbnew.GetBoard()
for key in sw_pos:
    sw = board.FindModuleByReference(key)
    print key, sw_pos[key]
    sw.SetPosition(pcbnew.wxPointMM(sw_pos[key][0],sw_pos[key][1]))
    sw.SetOrientation(sw_pos[key][2])
