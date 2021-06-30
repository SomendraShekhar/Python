from skimage.io import imread, imshow
from skimage.transform import resize
from skimage.feature import hog
from skimage import exposure
import cv2
import matplotlib.pyplot as plt
import os
from os.path import isfile, join

vidcap = cv2.VideoCapture('FaceDetectVideo.avi')

def reconstructHogVideo():
    pathIn= r'D:\PyEVM-master\Hog_image'
    pathOut = 'HOGvideo.avi'
    fps = vidcap.get(cv2.CAP_PROP_FPS)
    frame_array = []
    files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
    #for sorting the file names properly
    for i in range(len(files)):
        files[i] = int(files[i][18:-4])
    files.sort()
    frame_array = []
    for i in range(len(files)):
        filename=pathIn + '\\'+'hog_image_rescaled'+str(files[i])+'.jpg'
        #reading each files
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        
        #inserting the frames into an image array
        frame_array.append(img)
    os.chdir(r'D:\PyEVM-master')
    out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
    for i in range(len(frame_array)):
        # writing to a image array
        out.write(frame_array[i])
    out.release()
    
def HOGfeature(dirpath,fps):
    pathOut = 'HOGvideo.avi'
    count = 1
    HOG_array = []
    files = [f for f in os.listdir(dirpath) if isfile(join(dirpath, f))]
    for i in range(len(files)):
        files[i] = int(files[i][5:-4])
    files.sort()
    print(files)
    for i in range(len(files)):
        filename=pathIn +'\\'+'image'+str(files[i])+'.jpg'
    
        img = imread(filename)
    #resize image
        resized_img = resize(img, (64*4, 64*4))

    #generating HOG features
        fd, hog_image = hog(resized_img, orientations=8, pixels_per_cell=(8, 8),
        cells_per_block=(2, 2), visualize=True, multichannel=True)

    # Rescale histogram for better display 
        hog_image_rescaled = exposure.rescale_intensity(hog_image, in_range=(0, 5)) 
        os.chdir(r'D:\PyEVM-master')
        os.chdir(r'D:\PyEVM-master\Hog_image')
        plt.imsave("hog_image_rescaled"+str(count)+".jpg", hog_image, cmap="gray")
        count+=1
    
def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    directory = r'D:\PyEVM-master\temp2'
    os.chdir(directory)
    if hasFrames:
        cv2.imwrite("image"+str(count)+".jpg", image)
    return hasFrames


sec = 0
frameRate = 0.03
count=1
success = getFrame(sec)
while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)

pathIn = r'D:\PyEVM-master\temp2'
fps = vidcap.get(cv2.CAP_PROP_FPS)
HOGfeature(pathIn,fps)
reconstructHogVideo()
