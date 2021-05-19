import os
import argparse
import cv2
import numpy as np
from PIL import Image
from tqdm import tqdm
import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision.transforms import transforms
from efficientnet_pytorch import EfficientNet
from networks.main import build_network


def new_threshold(input_folder, network, model_path, thresh, type_score, device):
    net = build_network(network)
    net = net.to(device)
    model_dict = torch.load(model_path, map_location="cuda")
    center = model_dict['c']
    net.load_state_dict(model_dict['net_dict'])
    net.eval()
    scores=[]
    with torch.no_grad():
       for image_file in tqdm(os.listdir(input_folder)):
         image_path = os.path.join(input_folder, image_file)
         img = cv2.imread(image_path)
         vis_img = np.copy(img)
         img = Image.fromarray(img)
         img = transforms.Resize((240, 240))(img)
         img = transforms.ToTensor()(img)
         img = transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])(img)
         img = img.unsqueeze(0)
         img=img.to(device)
         output=net(img)
         dist = torch.sum((output - center) ** 2)
         score =dist
         score=score.item()
         score=round(score, 2)
         scores.append(score)
    scores.sort()
    scores=np.array(scores)
    if type_score == "median":
      choose_score = np.quantile(socres, .50)
    elif type_score =="third":
      choose_score = np.quantile(scores, .75)
    if abs(thresh - choose_score) <=20:
      new_thresh = max(choose_score, thresh)
    else:
      new_thresh = int((2*choose_score+thresh)/3)
    print("new threshold: ", new_thresh)
    return new_thresh


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('-input_folder', type=str, required=True, help='path to input normal images')
  parser.add_argument('-model_path', type=str, required=True, help='model path')
  parser.add_argument('-device',  help='cuda', default="cuda")
  parser.add_argument('-net',  help='network name', default='efficientnetb1')
  parser.add_argument('-thresh', help='current threshold', type=int, default=15)
  parser.add_argument('-type_score', help='median or third quartile', default="third")
  args = parser.parse_args()
  new_threshold(args.input_folder, args.net, args.model_path, args.thresh, args.type_score, args.device)



