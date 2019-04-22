from moviepy.editor import *
import os
import downloader


topic = downloader.download()
clipsArr = []
def createVid():
    imgs = os.listdir('downloads/'+topic)
    for img in imgs:
        clip = ImageClip("downloads/"+topic+"/"+img)
        clip = clip.resize( (1920,1080) )
        clip = clip.set_duration(t = 5)
        clipsArr.append(clip)

def selectingInput():
    selecting = input("please type 1 when finised: ")
    if selecting != "1":
        selectingInput()
    elif selecting == "1":
        createVid()

#ask user if finished with selection
print("Delete unwanted images from the downloads folder")
selectingInput()

finalClip = concatenate_videoclips(clipsArr)
finalClip.write_videofile("movie.mp4",audio=False,fps = 24)
