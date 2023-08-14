import cv2


cap = cv2.VideoCapture(701)

if not cap.isOpened():
    print("Doesn't exist that camera")
else:
    print("Exist that camera.")

while(cap.isOpened()):
    #Captura frame-by-frame
    ret, frame = cap.read();

    #Muestra el resultado de frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

#Cuando todo este hecho cierra el programa
cap.release()
cv2.destroyAllWindows()