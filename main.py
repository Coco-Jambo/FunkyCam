#Author: Coco-Jambo
#Start date: January 8th 2024
#Project name: FunkyCam

#All comments are written by me to document this project 
#so that if I ever come back to it I know what every line does

#importing the libraries
import cv2
import sys

#creating a face cascade
cascadePath = sys.argv[1]
faceCascade = cv2.CascadeClassifier(cascadePath)

#Loading camera, the int is the id of the device to open if there are multiple
cap = cv2.VideoCapture(0)

#scaling the camera to 1080p
cap.set(cv2.CAP_PROP_FRAME_WIDTH , 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT , 1080)

#Main loop
while  True:
    #retreiving camera data
    success, frame = cap.read()

   #If the video frame has been captured open the camera window
    if success:
        

        #This is what deals with the face detection stuff
        #First this converts the input from rgb to grayscale and puts the image in gray
        #gray images are better for face detection sicne they simplify the image and reduce computational load
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.cv.CV_HAAR_SCALE_IMAGE
        )

        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        #displaying frame
            cv2.imshow("Funky Cam", frame)

    # Close and break the loop after pressing "x" key, or after clicking x on the window
    if (cv2.waitKey(1) and 0xFF == ord('x')):
        break


# close the already opened camera
cap.release()
# close the window and de-allocate any associated memory usage
cv2.destroyAllWindows()