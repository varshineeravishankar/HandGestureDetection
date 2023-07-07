import cv2
arr=['A.jpg','B.jpg','C.jpg','D.jpg','E.jpg','F.jpg','G.jpg']
i=0
while(arr!=0):
    img = cv2.imread(arr[i], -1)
    print(img)
    cv2.imshow('image', img)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()
    i+=1
