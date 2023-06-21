import cv2
import numpy

""" Sahne Oluşturma """
screen = numpy.zeros((512, 512, 3), dtype=numpy.uint8) + 255


""" Çizgi Çizme """
#cv2.line(screen, (25,25), (100,255), (29,125,255), thickness=10) #sahne, başlangıç , bitiş, renk, kalınlık


""" Dikdörtgen Çizme """
#cv2.rectangle(screen, (75,75), (160,195), (255,0,0), thickness=-5) #sahne, sol üst köşe, sağ lat köşe, renk, thickness -1 ise içi dolu çizer


""" Çember Çizme """
#cv2.circle(screen, (257,257), 50, (245,14,2), -1) #sahne, merkez nokta, yarıçap


""" Elips Çizme """
#cv2.ellipse(screen, (290,390), (10, 50), 45, 0, 360 , (0,0,0), -1 ) #sahne, merkez, (yatayyçap,dikeyyçap), açı, başlangıçaçı , bitişaçı


""" Üçgen Çizme """
# x = (255, 50)
# y = (200, 150)
# z = (300, 150)
renk = (0,0,255)

# cv2.line(screen, x, y, renk, 2)
# cv2.line(screen, y, z, renk, 2)
# cv2.line(screen, x, z, renk, 2)


""" Yazı Yazma """
cv2.putText(screen, "Alihan", (50,500), cv2.FONT_HERSHEY_SIMPLEX, 2, renk, cv2.LINE_4)


cv2.imshow("Ekran", screen)
cv2.waitKey(0)