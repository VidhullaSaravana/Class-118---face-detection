import cv2 

img = cv2.imread("4f.jpg")

gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #blue,green,red to gray

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') #algorithm to detect the face

faces = face_cascade.detectMultiScale(gray, 1.1, 5)
print(len(faces)) #printing the length of the face

for (x,y,w,h) in faces:
       cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2) 
       roi_color = img[y:y+h, x:x+w] #roi region of interest
       cv2.imwrite("face.jpg", roi_color)
             
cv2.imshow('img',img)
cv2.waitKey(0)



