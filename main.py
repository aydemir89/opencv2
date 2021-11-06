"""
import cv2
img = cv2.imread('resim.jpg',0)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


k = cv2.waitKey(0) &0xFF
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('messigray.png',img)
    cv2.destroyAllWindows()
"""
import cv2
import time
import numpy as np
"""
#video içeri aktarma 
video_name="MOT17-04-DPM.mp4"
#video içe aktarma
cap=cv2.VideoCapture(video_name)
print("Genişlik",cap.get(3))
print("Yükseklik",cap.get(4))

if cap.isOpened()==False:
    print("HATA")

while True:
    ret,frame=cap.read()
    if ret==True:
        time.sleep(0.01)#uyarı:kullanılmazsa çok hızlı akar
        cv2.imshow("Video",frame)
    else:
        break
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release() #stop capture
cap.destroyAllWindows
"""
"""
#kamera açma ve video kaydı
# capture
cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(width, height)

# video kaydet
writer = cv2.VideoWriter("video_kaydı.mp4", cv2.VideoWriter_fourcc(*"DIVX"), 20, (width, height))

while True:

    ret, frame = cap.read()
    cv2.imshow("Video", frame)

    # save
    writer.write(frame)

    if cv2.waitKey(1) & 0xFF == ord("q"): break

cap.release()
writer.release()
cv2.destroyAllWindows()
"""

"""
#yeniden boyutlandır ve kırp
img = cv2.imread('lenna.png',1)
print("sized Img Shape: ",img.shape)
cv2.imshow('image',img)
cv2.waitKey(0)
img_resize=cv2.resize((img),(800,800))
print("Resized Img Shape: ",img_resize.shape)
cv2.imshow('image',img_resize)
cv2.waitKey(0)
cv2.destroyAllWindows()
#kırpmak
imgCropped = img[:200,0:300] #height - width 
cv2.imshow("Cropped img",imgCropped)
cv2.waitKey(0)
"""
"""
#resimlerin üstüne şekil ve metin eklemek
img=np.zeros((512,512,3),np.uint8)#siyah bir resim
print(img.shape)
#cv2.imshow("Siyah",img)
#cv2.waitKey(0)

#çizgi eklemek
        #başlangıç noktası,bitiş noktası,renk,kalınlık
#cv2.line(img,(100,100),(100,300),(0,255,0),2)
#cv2.imshow("çizgi",img)
#cv2.waitKey(0)

#dikdörtgen
cv2.rectangle(img,(0,0),(256,256),(255,0,0),cv2.FILLED)
cv2.imshow("dikdörtgen",img)
cv2.waitKey(0)

#çember
cv2.circle(img,(300,300),45,(0,0,255),cv2.FILLED)
cv2.imshow("cember",img)
cv2.waitKey(0)

#METİN
cv2.putText(img,"resim",(350,350),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255))
cv2.imshow("metin",img)
cv2.waitKey(0)
"""
"""
#Görüntülerin birleştirilmesi
img = cv2.imread("lenna.png")
cv2.imshow("Orijinal",img)
cv2.waitKey(0)

#yatay
hor=np.hstack((img,img))
cv2.imshow("horizontal",hor)
cv2.waitKey(0)

#dikey
ver=np.vstack((img,img))
cv2.imshow("vertical",ver)
cv2.waitKey(0)
"""

