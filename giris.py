import cv2
""" Resim Okuma """

# img = cv2.imread('./araba.png')
# img = cv2.imread('./araba.png', cv2.IMREAD_GRAYSCALE)

# cv2.imwrite("araba-gri.png", img) #imagei gri şekilde alabilmek için

# cv2.namedWindow("Araba", cv2.WINDOW_NORMAL) #pencere boyutunun artıp azalabilmesi için
# cv2.imshow("Araba",img) #pencere oluşturmak
# cv2.waitKey(0) #pencerenin biz kapatana kadar kalması için 0, geri kalan değerler ms cinsinde
# cv2.destroyAllWindows() #imshow ile oluşturulan pencerelerin tamamını kapatmak için


""" Video Okuma """
# video = cv2.VideoCapture(0) #burada 0; cihaza bağlı kamerların sırası oluyor.

# while True:
#     durum, frame = video.read()
#     frame = cv2.flip(frame, 1) #görüntüyü ayna gibi döndürmek
#     cv2.imshow("Kamera", frame)
#     cv2.waitKey(10)

#     if cv2.waitKey(10) & 0xFF == ord("q"): #q'ye basınca kapatıyor.
#         break

# video.release()
# cv2.destroyAllWindows()


""" Kaydedilmiş Video Okuma """

video = cv2.VideoCapture("araba.mp4")
while True:
    state, frame = video.read()
    if state == 0: #video sonuna gelince state 0 olacağı için kapatır.
        break
    frame = cv2.resize(frame, (480, 480)) #framei aldıktan sonra yeniden boyutlandırıyor
    cv2.imshow("Kamera", frame)
    if cv2.waitKey(10) & 0xFF == ord("q"): #q'ye basınca kapatıyor.
        break

video.release()
cv2.destroyAllWindows()
