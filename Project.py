import os

import pyrebase
import firebase_admin
from firebase_admin import messaging
from firebase_admin import credentials

path = "/mnt/c/ui_db/firebase/"
pose_path = path
blur_path = "./opencv/data/"

cred = credentials.Certificate(path+"pixie-b4bf8-firebase-adminsdk-cdjsi-09a89665de.json") # json 파일 필요
firebase_admin.initialize_app(cred)

#import import_ipynb
import OpenPose, Blur, Fcm

config={
	"apiKey": "AIzaSyAn13FTdnfEaWl_KRpU3H1HEwr3NOz9vIE", #webkey
	"authDomain": "pixie-b4bf8.firebaseapp.com", #프로젝트ID
	"databaseURL": "https://pixie-b4bf8-default-rtdb.asia-southeast1.firebasedatabase.app", #database url
	"storageBucket": "pixie-b4bf8.appspot.com", #storage
	"serviceAccount": path+"pixie-b4bf8-firebase-adminsdk-cdjsi-09a89665de.json" # json 파일 필요
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

res = False

def trashDumping(filename, id):
  global res
  global pose
  res = False
  pose = False
  
  # OpenPose
  OpenPose.play(pose_path, path+id, filename)
  print("OpenPose 완료")

  # Yolo
  os.chdir(path+"Yolov5_DeepSort_Pytorch")
  #os.system("python ./yolov5/detect.py --weights ./yolov5/yolov5s.pt --img 1280 --conf 0.4 --source ${path}${id}${filename}_Yolo+.mp4")
  os.system("python3 track.py --source %s%s%s.mp4 --yolo_weights ../yolov5/yolov5s.pt --output %s%s --save-vid" %(path, id, filename, path, id))
  print("Yolo 완료")
  os.chdir(path)

  if res == True and OpenPose.pose == True:
    # Blur
    Blur.blur(blur_path, path+id, filename+"_OpenPose")
    print("OpenPose-Blur 완료")

    # Upload
    storage.child(id+"openpose"+filename+".mp4").put(path+id+filename+"_OpenPose""./mp4")
    print("OpenPose-Blur Upload 완료")

    Fcm.send_to_firebase_cloud_messaging("OpenPose가 쓰레기 무단 투기를 감지하였습니다.", "OpenPose 영상 확인 탭에서 확인해주세요.")


  # 무단 투기 의심 Yolo
  if res == True:
    # Blur
    Blur.blur(blur_path, path+id, filename+"_Yolo")
    print("Yolo-Blur 완료")

    # Upload
    storage.child(id+"yolo"+filename+".mp4").put(path+id+filename+"_Yolo"+".mp4")
    print("Yolo-Blur Upload 완료")

    Fcm.send_to_firebase_cloud_messaging("Yolo가 쓰레기 무단 투기를 감지하였습니다.", "Yolov5 영상 확인 탭에서 확인해주세요.")
     
  # Delete
  #storage.delete(id+filename+".h264")
  #storage.delete(id+filename+".mp4")

  #os.remove(path+id+filename+".h264")
  #os.remove(path+id+filename+".mp4")
  #os.remove(path+id+filename+"_OpenPose"+"./mp4")
  #os.remove(path+id+filename+"_Yolo"+".mp4")
  #os.remove(path+id+filename+"_OpenPose"+"_blur"+"./mp4")
  #os.remove(path+id+filename+"_Yolo"+"_blur"+".mp4")
  print("Delete 완료")

if __name__ == "__main__":
  while(True):
    files = storage.list_files()
    makeSet = []

    for file in files:
      temp = file.name.split("/")
      id = temp[0]
      os.chdir(path)

      if os.path.isdir(id)==False:
        os.mkdir(id)
      os.chdir("./"+id)
      
      if (file.name[-5:]==".h264"):
        filename = temp[len(temp)-1]
        filename = filename[:-5]
        
        if os.path.isfile(filename+".h264")==False:
          print(filename+" downloading")
          file.download_to_filename(filename+".h264") # 다운로드

        if os.path.isfile(filename+".mp4")==False:
          print(filename+" converting mp4")
          os.system("MP4Box -add"+" ./"+filename+".h264"+" ./"+filename+".mp4") # mp4로 변환

        trashDumping(filename, id+"/")