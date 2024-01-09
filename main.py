#Author: Coco-Jambo
#Start date: January 8th 2024
#Project name: FunkyCam

#importing the opencv library
import cv2 

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
       
       cv2.imshow("Funky Cam", frame)

    
    # Close and break the loop after pressing "x" key, or after clicking x on the window
    if (cv2.waitKey(1) and 0xFF == ord('x')):
        break


# close the already opened camera
cap.release()
# close the window and de-allocate any associated memory usage
cv2.destroyAllWindows()