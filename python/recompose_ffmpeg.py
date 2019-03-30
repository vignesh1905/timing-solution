import os
from subprocess import call
import glob

#Creating a list of the filenames according to their created order to give to ffmpeg
f1 = open('list.txt', 'w+')

files = glob.glob("/Volumes/Vignesh_Drive/timing_solution/video_frames/*.jpg")
files.sort(key=os.path.getmtime) #Sorting files using create time
for file in files:
    print("\nfile '{}'".format(file), file=f1) # should be in this format for ffmpeg to work
f1.close()

#Calling ffmpeg on the files list to create the required video
# -safe is to avoid error saying that it is not a safe file name
# -r is the output video frame rate

ffmpeg_command = "ffmpeg -f concat -safe 0 -i list.txt -c:v libx264 -r 30 -pix_fmt yuv420p out_4.mp4"
call([ffmpeg_command], shell=True)
