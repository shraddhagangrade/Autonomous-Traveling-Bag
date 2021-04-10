import torch.nn.functional as F
import time
from jetbot import Robot
import torchvision.transforms as transforms
import cv2
import PIL.Image
import numpy as np

import torch
device = torch.device('cuda')
import torchvision
from torch2trt import TRTModule

model_trt = TRTModule()
model_trt.load_state_dict(torch.load('best_model_trt.pth'))
mean = torch.Tensor([0.485, 0.456, 0.406]).cuda().half()
std = torch.Tensor([0.229, 0.224, 0.225]).cuda().half()

normalize = torchvision.transforms.Normalize(mean, std)

def preprocess(image):
    image = PIL.Image.fromarray(image)
    image = transforms.functional.to_tensor(image).to(device).half()
    image.sub_(mean[:, None, None]).div_(std[:, None, None])
    return image[None, ...]
robot = Robot()
def update(change):
    global blocked_slider, robot
    x = change['new'] 
    x = preprocess(x)
    y = model_trt(x)
    #print(y)
    
    # we apply the `softmax` function to normalize the output vector so it sums to 1.0 (which makes it a probability distribution)
    y = F.softmax(y, dim=1)
    #print(y)
    
    prob_blocked = float(y.flatten()[0])
    #print(prob_blocked)
    
    blocked_slider.value = prob_blocked
    
    if prob_blocked < 0.5:
        robot.forward(speed_slider.value)
    else:
        robot.left(speed_slider.value)
    
    time.sleep(0.001)
        
update({'new': camera.value})  # we call the function once to intialize
camera.observe(update, names='value')  # this attaches the 'update' function to the 'value' traitlet of our camera
