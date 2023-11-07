import cv2


# Create our body classifier


# Initiate video capture for video file
cap = cv2.VideoCapture('walking.avi')

# Loop once video is successfully loaded
while True:

    # Read first frame
    ret, frame = cap.read()


    #Convert Each Frame into Grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    # Pass frame to our body classifier
    faceCascade = cv2.CascadeClassifier("haarcascade_fullbody.xml")

    # Extract bounding boxes for any bodies identified
    faces = faceCascade.detectMultiScale(gray)
    print(faces)

    for(x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y),(x+w,y+h),(255,127,127),4)

        cv2.imshow("cool name here",frame)

    if cv2.waitKey(1) == 32: #32 is the Space Key
        break

cap.release()
cv2.destroyAllWindows()




