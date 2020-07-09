In this folder are two files: EXAMPLE.config.json and timelapse_maker.EXAMPLE

EXAMPLE.config.json is an example config file. The config file looks like the following:

{
    "real_days": 0,
    "real_hours": 0,
    "real_mins": 30,
    "real_seconds": 0,
    "target_length_min": 0,
    "target_length_sec": 30,
    "target_fps": 30,
    "camera_ip": "192.168.2.231",
    "camera_port": 3400,
    "camera_username": "henrypump",
    "camera_password": "HPCamera1903",
    "output_file": "test1.avi"
}

Where:
    real_days: the number of real time days to capture images 
    real_hours: the number of real time hours to capture images
    real_mins: the number of real time minutes to capture images
    real_seconds: the number of real time seconds to capture images
    target_length_min: the number of minutes the output file should be (this is used in conjunction with target_length_sec to get the full length of the output)
    target_length_sec: the number of seconds the output file should be (this is used in conjunction with target_length_min to get the full length of the output)
    target_fps: the frames per second the output file should be run at (10fps  is choppy, 15fps is less-choppy, 24fps is cinematic, 30fps is smooth, 60fps is really smooth)
    camera_ip: the ip address of the camera (the " marks are important)
    camera_port: the port number for the camera
    camera_username: the username to login to the camera (the " marks are important)
    camera_password: the password to login to the camera (the " marks are important)
    output_file: the name of the output file (the " marks are important also be sure to include .avi else Windows won't recognize it)

The name of the config file should be:
    config.json

Once the config file is setup just double click timelapse_maker.exe and the software should run itself.
Some caveats:
    The software is only guaranteed for Panasonic iPro cameras
    The software will not recover in anyway in the event of a windows reboot or the software being closed.
    The software is better suited to longer run times ie: setting longer real time runs is better than shorter ones
    The software defaults to making a timelapse folder in its current folder where it stores all the images once the video is made this folder can be deleted
    DO NOT close the window else you'll have to start over, the images won't be lost but the run will be skewed
    The software processes all the images in the timelapse folder regardless of what run they are from
    Technically the software could be run remotely and given a public IP that is port forwarded but is NOT recommened 
