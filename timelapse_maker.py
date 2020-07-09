import requests
from requests.auth import HTTPDigestAuth
import time
from cv2 import VideoWriter, imread, VideoWriter_fourcc
import numpy as np
import glob
import os
import json
import progressbar
from natsort import natsorted

def calc_interframetime(real_days,real_hours,real_mins,real_seconds,target_length_min,target_length_sec,target_fps):
    #converts real time inputs into seconds
    rd = real_days*24*60*60
    rh = real_hours*60*60
    rm = real_mins*60
    rs = rd+rh+rm+real_seconds
    #calculate the target frames for the final output
    target_frames = (target_length_min*60 + target_length_sec) * target_fps
    #calculate the wait time between frames
    spf = rs/target_frames
    return target_frames,spf

#url = 'https://httpbin.org/digest-auth/auth/user/pass'
def makevideo():
    
    PERSIST = {}
    try:
        with open("config.json", 'r') as persist_file:
            PERSIST =  json.load(persist_file)
    except Exception:
        return False
    
    target_frames,interframe_time = calc_interframetime(
        PERSIST['real_days'],
        PERSIST['real_hours'],
        PERSIST['real_mins'],
        PERSIST['real_seconds'],
        PERSIST['target_length_min'],
        PERSIST['target_length_sec'],
        PERSIST['target_fps'])
    try:
        now = time.time()
        with open('timelapse/{}.jpg'.format(now), 'wb') as handle:
            pass
        os.remove('timelapse/{}.jpg'.format(now))
    except:
        os.mkdir('timelapse')
    print("Number of frames:{}\nReal Time between frames: {} seconds".format(target_frames,interframe_time))
    
    #for every frame in the range of target_frames
    for x in progressbar.progressbar(range(target_frames),prefix='Collecting Photos: '):
        #open a file and pull the current picture from the camera
        now = time.time()
        try:
            with open('timelapse/{}.jpg'.format(now), 'wb') as handle:
                response = requests.get("http://" + PERSIST['camera_ip'] + ":" + str(PERSIST['camera_port']) + "/cgi-bin/camera", 
                    auth=HTTPDigestAuth(PERSIST['camera_username'],PERSIST['camera_password']),stream=True)
                if not response.ok:
                    print(response)
                
                for block in response.iter_content(1024):
                    if not block:
                        break

                    handle.write(block)
        except:
            print("\nMissed frame {} check connection/settings to camera!".format(x))
            os.remove('timelapse/{}.jpg'.format(now))
        if x != target_frames-1 and interframe_time-(time.time()-now) > 0:
            #wait the calculated time between frames minus the processing time for this frame to start again        
            time.sleep(interframe_time-(time.time()-now))

    
    #filenames = natsorted(filenames)
    img_array = []
    
    #load the pictures with cv2
    for filename in progressbar.progressbar(glob.glob('timelapse/*.jpg'),prefix='Loading Photos: '): #filenames:
        img = imread(filename)
        height, width, _ = img.shape
        size = (width,height)
        img_array.append(img)
    
    #setup the video format
    out = VideoWriter(PERSIST['output_file'], VideoWriter_fourcc(*'MP42'), PERSIST['target_fps'], size)
    
    #output the video
    for i in progressbar.progressbar(range(len(img_array)),prefix='Processing Video: '):
        out.write(img_array[i])
    out.release()
makevideo()
input("Press ENTER to exit program")