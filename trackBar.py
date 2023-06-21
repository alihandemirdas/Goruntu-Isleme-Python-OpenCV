import cv2
import numpy

def bos(x):
    pass

cv2.namedWindow('Ekran')
cv2.createTrackbar("F-Size", "Ekran", 25,250, bos)

fs = 0.25
while True:
    screen = numpy.zeros((512,512,3), dtype=numpy.uint8) + 255
    cv2.putText(screen, "OPEN-CV", (100,255), cv2.FONT_HERSHEY_SIMPLEX, fs, (0,0,255), cv2.LINE_4)
    cv2.imshow("Ekran", screen)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    fs = cv2.getTrackbarPos("F-Size", "Ekran")
    fs = fs /100

cv2.destroyAllWindows()


