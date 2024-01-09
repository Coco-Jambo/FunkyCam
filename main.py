import cv2 

#Loading camera
cap = cv2.VideoCapture(0)
while True:
    success, frame = cap.read()
    
    
    if success:
       cv2.imshow("Funky Cam", frame)
    
    # Close and break the loop after pressing "x" key
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

# close the already opened camera
cap.release()
# close the window and de-allocate any associated memory usage
cv2.destroyAllWindows()