import cv2
numberplateCascade = cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")
cap = cv2.VideoCapture('/Users/chandrikajadon/Desktop/Downloads/udemy-ps1-test/IMG_1472.MOV')
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 100)
while True:
    success ,img = cap.read()

    # newImage = cv2.resize(img, (500, 500))
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    nplate = numberplateCascade.detectMultiScale(imgGray, 1.1, 4)

    for (x, y, w, h) in nplate:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(img, "Number Plate", (x, y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,0,255), 2)
        imgRoi = img[y:y+h, x:x+w]
        cv2.imshow("ROI", imgRoi)

    cv2.imshow("image", img)
    # cv2.waitKey(0)
    # cv2.imshow("video", img )
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


