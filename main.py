import cv2
from matplotlib import pyplot as plt
from PIL import Image, ImageFilter, ImageOps

def initializeWebCam():
    videoDevice = cv2.
    VideoCapture(0, cv2.CAP_DSHOW)
    return videoDevice

def terminateWebCam(videoDevice):
    videoDevice.release()
	
def getImage(videoDevice):
    return_code, cvImage = videoDevice.read()
    if return_code==False:
        exit(-1)
    return Image.fromarray(cvImage)
	
def embossFilter(npImage):
    npImageGray = ImageOps.grayscale(npImage)
    npImage_emboss = npImageGray.filter(ImageFilter.EMBOSS)
    return npImage_emboss
	
def equalizeFilter(npImage):
    return ImageOps.equalize(npImage)
	
def invertFilter(npImage):
    return ImageOps.invert(npImage)
	
def showImage(npImage):
    plt.imshow(npImage, cmap=’gray’)
    plt.show()
	
if __name__ == ‘__main__’:
    webcam = initializeWebCam()
    videoFrame = getImage(webcam)
    Pipeline = [embossFilter, equalizeFilter, invertFilter]
    for filter in Pipeline:
        videoFrame = filter(videoFrame)
    showImage(videoFrame)
    terminateWebCam(webcam)
