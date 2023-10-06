import math
from collections import deque, defaultdict
from fractions import Fraction

def level4part2(dimensions, your_position, trainer_position, distance):
    xw = dimensions[0]
    yw = dimensions[1]
    selfx = your_position[0]
    selfy = your_position[1]
    tx = trainer_position[0]
    ty = trainer_position[1]
    d = distance
    
    def get_reflection_grid(x_over, y_over):
        x_flip = x_over % 2 == 1
        y_flip = y_over % 2 == 1
        selfx_ref = (xw - selfx if x_flip else selfx) + x_over * xw
        selfy_ref = (yw - selfy if y_flip else selfy) + y_over * yw
        tx_ref = (xw - tx if x_flip else tx) + x_over * xw
        ty_ref = (yw - ty if y_flip else ty) + y_over * yw
        return (selfx_ref, selfy_ref, tx_ref, ty_ref)
    
    def calc_shortest_distance(x_over, y_over):
        bw = xw * max(abs(x_over) - 1, 0)
        bh = yw * max(abs(y_over) - 1, 0)
        return getd2(bw, bh)
    
    def getd2(deltax, deltay):
        return math.sqrt(deltax**2 + deltay**2)
    
    blockers = dict()   # (Fraction, x+/-, y+/-) -> min distance
    trainers = dict()  # (Fraction, x+/-, y+/-) -> min distance
    
    max_rooms_high = distance // yw + 1
    max_rooms_wide = distance // xw + 1
    
    for x_over in range(-max_rooms_wide, max_rooms_wide + 1):
        for y_over in range(-max_rooms_high, max_rooms_high + 1):
            if calc_shortest_distance(x_over, y_over) > d:
                continue
            selfx_ref, selfy_ref, tx_ref, ty_ref = get_reflection_grid(x_over, y_over)
            if not (x_over == 0 and y_over == 0):
                self_ref_deltax = selfx_ref - selfx
                self_ref_deltay = selfy_ref - selfy
                self_ref_distance = getd2(self_ref_deltax, self_ref_deltay)
                self_ref_dir = Fraction(abs(self_ref_deltax), abs(self_ref_deltay)) if self_ref_deltay != 0 else (1,0)
                blocker_key = (self_ref_dir, self_ref_deltax >= 0, self_ref_deltay >= 0)
                if self_ref_distance <= d:
                    blockers[blocker_key] = min(self_ref_distance, \
                        blockers[blocker_key] if blocker_key in blockers else self_ref_distance)

            tr_ref_deltax = tx_ref - selfx
            tr_ref_deltay = ty_ref - selfy
            tr_ref_distance = getd2(tr_ref_deltax, tr_ref_deltay)
            tr_ref_dir = Fraction(abs(tr_ref_deltax), abs(tr_ref_deltay)) if tr_ref_deltay != 0 else (1,0)
            tr_ref_key = (tr_ref_dir, tr_ref_deltax >= 0, tr_ref_deltay >= 0)
            if tr_ref_distance <= d:
                trainers[tr_ref_key] = min(tr_ref_distance, \
                    trainers[tr_ref_key] if tr_ref_key in trainers else tr_ref_distance)
    
    skipped = 0
    for trainer in trainers:
        if trainer in blockers and trainers[trainer] > blockers[trainer]:
            skipped += 1
    return len(trainers) - skipped
