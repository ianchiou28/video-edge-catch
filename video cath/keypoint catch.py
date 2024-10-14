import cv2
cap = cv2.VideoCapture('C:/Users/ian28/Downloads/1728628346.mp4')

while cap.isOpened():
    ret,frame = cap.read()
    if not ret:
        break
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    edges = cv2.Canny(gray_frame,100, 500)
    
    cv2.imshow('Contour Video', edges)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    
cap.release()
cv2.destroyAllWindows()