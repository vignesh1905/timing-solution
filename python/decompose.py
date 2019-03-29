import cv2
vidcap = cv2.VideoCapture('/Users/vigneshk/Desktop/timing_solution/videos/IMG_0004.mp4')
success,image = vidcap.read()
count = 0
while success:
     cv2.imwrite("/Volumes/G-DRIVE mobile USB-C/timing_solution/video_frames/frame%d.jpg" % count, image)     # save frame as JPEG file
     success,image = vidcap.read()
     print('Read a new frame: ', success)
     count += 1
