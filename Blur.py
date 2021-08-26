import cv2

def blur(path, video_path, video_name):
  # Cascades 디렉토리의 haarcascade_frontalface_default.xml 파일을 Classifier로 사용
  faceCascade = cv2.CascadeClassifier(path+'haarcascades/haarcascade_frontalface_default.xml')
  cap = cv2.VideoCapture(video_path+video_name+".mp4")
  
  if cap.isOpened() == False:
    print(".mp4를 열 수 없음")
    quit()
  
  print("blur 처리 중")

  width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
  height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
  fps = cap.get(cv2.CAP_PROP_FPS)

  fourcc = cv2.VideoWriter_fourcc(*'mp4v')
  filename = video_path+video_name+"_Blur.mp4"

  out = cv2.VideoWriter(filename, fourcc, fps, (int(width), int(height)))

  while True:
    ret, img = cap.read()
        
    if img is None:
      print("img 없음")
      break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    faces = faceCascade.detectMultiScale(
        blur,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(20, 20)
    )

    if len(faces):
      for (x,y,w,h) in faces:
        face_img = img[y:y+h, x:x+w] # 탐지된 얼굴 이미지 crop
        face_img = cv2.resize(face_img, dsize=(0, 0), fx=0.04, fy=0.04) # 축소
        face_img = cv2.resize(face_img, (w, h), interpolation=cv2.INTER_AREA) # 확대
        img[y:y+h, x:x+w] = face_img # 탐지된 얼굴 영역 모자이크 처리

        #cv2.imshow('video',img) # video라는 이름으로 출력

    out.write(img)

    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit # ESC를 누르면 종료
      break

  cap.release()
  out.release()
  cv2.destroyAllWindows()