#Author: Coco-Jambo
#Start date: January 8th 2024
#Project name: FunkyCam

#All comments are written by me to document this project 
#so that if I ever come back to it I know what every line does

#importing the libraries
import cv2
import sys
import numpy as np

#creating a face cascade
faceCascade = cv2.CascadeClassifier('xml/haarcascade_frontalface_default.xml')

#creating an eye cascade
#eyeCascade = cv2.CascadeClassifier('xml/eyes.xml')

#creating a mouth cascade
#mouthCascade = cv2.CascadeClassifier('xml/mouth.xml')


#Loading funky assets
#cv2.IMREAD_UNCHANGED specifies that the image should be read as is, including an alpha channel if present (if there's transparency)
basic_expression = cv2.imread('assets/SMILE PNG.png', cv2.IMREAD_UNCHANGED)

#the ratio is used when resizing the image (width/height)
ratio = basic_expression.shape[1]/basic_expression.shape[0]

#Loading camera, the int is the id of the device to open if there are multiple
cap = cv2.VideoCapture(0)

#scaling the camera to 720p
cap.set(cv2.CAP_PROP_FRAME_WIDTH , 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT , 720)


#retreiving camera data
success, frame = cap.read()

#Main loop
#while the video frame has been captured open the camera window
while  success:
    #This is what deals with the face detection stuff
    #First this converts the input from rgb to grayscale and puts the image in gray
    #gray images are better for face detection sicne they simplify the image and reduce computational load
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    
    #we use the method detectMultiscale to do face detection
    # - gray is the parameter holding the current frame (the input image)
    # - scaleFactor is the parameter that compensates for when faces appear smaller when they are far
    #       or big when they are close, it scales the image to 1.1 to help detect the faces at different
    #       distances
    # - minNeighbors is the parameter that specifies how many neighbors (other overlapping rectangles) minimum to be a valid face,
    #       to reduce the amount of false positives the algorithm may detect. For example it can detect many faces inside a face and 
    #       draw multiple rectangles inside a face that overlap, minNeighbors filters out these detections and refines 
    #       the result. If the count of overlapping rectangles is greater than or equal to it, then it is a valid face,
    #       otherwise it is a false positive. It's like a sensitivity parameter
    # - minSize is a tuple that specifies the minimum size of a face (in pixels)
    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw a rectangle around the faces detected
    # faces is the list of detected faces
    # (x,y) is the top-left corner
    # frame is the input image where the rectangles will be drawn
    # (x+w, y+h) bottom-right corner (w is width and h is height)
    # (0, 255, 0) is the color of the rectangle
    # 2 is the thickness of the border
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)


    #Putting the image on the detected face
    for (x, y, w, h) in faces:
        
        # Resizing the image
        h = int(w / ratio)
        y += int(h / 2)
        smallerImage = cv2.resize(basic_expression, (w, h))

        # Extract the region where the image will be overlaid
        region_extracted = frame[y:y+h, x:x+w]

        # Extract the alpha channel of the smallerImage
        alpha_channel = smallerImage[:, :, 3]

        # Resize the alpha channel to match the shape of smallerImage
        alpha_channel_resized = cv2.resize(alpha_channel, (smallerImage.shape[1], smallerImage.shape[0]))

        # Expand the dimensions of alpha_channel_resized to match smallerImage
        alpha_channel_resized_expanded = np.repeat(np.expand_dims(alpha_channel_resized, axis=2), 3, axis=2)

        # Resize region_extracted to match the shape of smallerImage
        region_extracted_resized = cv2.resize(region_extracted, (smallerImage.shape[1], smallerImage.shape[0]))

        # Perform alpha blending
        blended_result = (smallerImage[:, :, :3] * alpha_channel_resized_expanded) + (region_extracted_resized * (1 - alpha_channel_resized_expanded))

        # Ensure the result is in the range [0, 255] and cast it to uint8
        blended_result = np.clip(blended_result, 0, 255).astype(np.uint8)

        # Update the region in the frame with the blended result
        frame[y:y+h, x:x+w] = blended_result



    #displaying frame
    cv2.imshow("Funky Cam", frame)

    #get next frame
    success, frame  = cap.read()

    # Close and break the loop after pressing "x" key, or after clicking x on the window
    if (cv2.waitKey(1) & 0xFF == ord('x')):
     
        break   


# close the already opened camera
cap.release()
# close the window and de-allocate any associated memory usage
cv2.destroyAllWindows()