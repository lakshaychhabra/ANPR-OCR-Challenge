import numpy as np
import cv2
from paddleocr import PaddleOCR, draw_ocr
import pandas as pd
import os
from math import sqrt
from utils import process_bb

ocr = PaddleOCR(use_angle_cls=True,lang="en")



def run_ocr(img):

    combined_output = " "
    result = ocr.ocr(img)

    boxes = [line[0] for line in result]
    txts = [line[1][0] for line in result]
    scores = [line[1][1] for line in result]

    combined_output = txts[0]

    if len(txts) > 1:
        combined_output = process_bb(boxes, txts)
    
    # . - : " " These are some values that are added that have to be removed
    return ''.join(e for e in combined_output if e.isalnum())

def length(p1,p2):
    return sqrt((p1[0]-p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_area(p1,p2,p3,p4):
    l = length(p1, p2)
    b = length(p2, p3)
    return l*b


def run_process_on_images(path):
    new_dict = {}
    root_folder = os.listdir(path)
    count = 0
    for i in root_folder:
        if i == ".DS_Store":
            continue
        path_to_images = os.listdir(path + "/" + i)
        for image in path_to_images:
            if image == ".DS_Store":
                continue
            final_image_path = path + "/" + i + "/" + image
            img = cv2.imread(final_image_path)
            img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            key_ = i + "/" + image
            print(key_)
            try:
                result = run_ocr(img)
            except:
                # Didnt find any detection
                count+=1
                result = ""
            new_dict[key_] = result

    print("Not detected numbers ", count)
    return new_dict

def process_challenge():
    hdr_dict = run_process_on_images("hdr")
    normal_dict = run_process_on_images("normal")
    final_dict = dict(list(hdr_dict.items()) + list(normal_dict.items()))

    return final_dict

final_dict = process_challenge()
df = pd.DataFrame(final_dict.items(),columns=['path','y_predicted'])

df.to_csv("dataset_predicted_updated.csv",index=False)


