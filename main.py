from moviepy.editor import *
import os
import downloader

# change loaction of folder
imgs = os.listdir('pics/')
clipsArr = []
downloader.download()

def createVid():
    for img in imgs:
        clip = ImageClip("pics/"+img)
        clip = clip.resize( (1920,1080) )
        clip = clip.set_duration(t = 5)
        clipsArr.append(clip)

#ask user if finished with selection
print("Delete unwanted images from the downloads folder")
def selectingInput():
    selecting = input("please type 1 when finised: ")
    if selecting != "1":
        selectingInput()
    else:
        createVid()

selectingInput()

#change params of IMAGECLIP to the array!!!!!!!!!!!!!!!!!!!!
print(clipsArr)
finalClip = concatenate_videoclips(clipsArr)
finalClip.write_videofile("movie.mp4",audio=False,fps = 24)
