import re


if __name__=='__main__':
    # extract switch position from kicad_pcb file
    refloat = re.compile(r'[-+]?\d*\.\d+|\d+')
    swposition = list()
    ymin = 999
    with open('Vision.kicad_pcb') as f:
        for line in f:
            # find r=7mm circles imported from dxf
            tol = 1e-5
            radlow = 7 - tol
            radup = 7 + tol
            if ('gr_circle' in line) and ('layer Dwgs.User' in line):
                coordinates = [float(s) for s in refloat.findall(line)]
                radius = abs(coordinates[0] - coordinates[2])
                if radlow <= radius <= radup:
                    if coordinates[1] < ymin:
                        ymin = coordinates[1]
                    swposition.append(['K_', coordinates[0], coordinates[1]])
    swposition2 = list()
    
    # reorder based on row & col
    for i in range(4):
        ylow = ymin + 19.05 * i
        yup = ylow + 19
        row = list(filter(lambda x: ylow<=x[2]<=yup, swposition))
        row.sort(key=lambda x:x[1])
        swposition2 += row
    
    with open('switch_position_raw.csv', 'w') as f:
        f.write('\n'.join(', '.join(str(i) for i in coordinate) for coordinate in swposition2))
