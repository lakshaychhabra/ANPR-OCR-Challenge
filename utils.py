from math import sqrt

def get_ratio(a1,a2):
    if a1 > a2:
        ratio = a2/a1
    else:
        ratio = a1/a2
    return ratio

def box_to_points(i):
    p1 = (i[0][0], i[0][1])
    p2 = (i[1][0], i[1][1])
    p3 = (i[2][0], i[2][1])
    p4 = (i[3][0], i[3][1])
    return p1,p2,p3,p4

def length(p1,p2):
    return sqrt((p1[0]-p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_area(p1,p2,p3,p4):
    l = length(p1, p2)
    b = length(p2, p3)
    return l*b

def process_bb(bb,texts):
    final_word = ""

    p1,p2,p3,p4 = box_to_points(bb[0])
    area_1 = calculate_area(p1,p2,p3,p4)

    p1,p2,p3,p4 = box_to_points(bb[1])
    area_2 = calculate_area(p1,p2,p3,p4)

    ratio = get_ratio(area_1,area_2)

    if ratio > 0.6:
        # join the words
        final_word = texts[0] + texts[1]
    else:
        final_word = texts[0]
        
    return final_word


