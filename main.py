from moviepy.editor import *
import os
#create array of images and convert them into jpg!!!!!!!!!!!!!

imgs = os.listdir('pics/')
clipsArr = []

for img in imgs:
    clip = ImageClip("pics/"+img)
    clip = clip.resize( (1920,1080) )
    clip = clip.set_duration(t = 5)
    clipsArr.append(clip)

#change params of IMAGECLIP to the array!!!!!!!!!!!!!!!!!!!!
print(clipsArr)
finalClip = concatenate_videoclips(clipsArr)
finalClip.write_videofile("movie.mp4",audio=False,fps = 24)
