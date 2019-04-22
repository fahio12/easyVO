from google_images_download import google_images_download
def download():
    topic = input("Enter topic: ")
    numOfPics = input("# of pictures?: ")
    response = google_images_download.googleimagesdownload()
    arguments = {"keywords":topic,"limit":numOfPics}
    paths = response.download(arguments)
