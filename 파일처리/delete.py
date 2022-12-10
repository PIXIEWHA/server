# 파일 삭제
import shutil
import os

path = "/mnt/c/Users/yhyeo/OneDrive/바탕 화면/YOLO/export2/labels/"
files = os.listdir(path)
txtf = []

for file in files:
    if file[-4:]==".txt":
        file = file[:-4]
        txtf.append(file)

for txt in txtf:
    shutil.move("/mnt/c/Users/yhyeo/OneDrive/바탕 화면/YOLO/export2/images/"+txt+".jpg", "/mnt/c/Users/yhyeo/OneDrive/바탕 화면/YOLO/labeled/"+txt+".jpg")
    shutil.move(path+txt+".txt", "/mnt/c/Users/yhyeo/OneDrive/바탕 화면/YOLO/labeled/"+txt+".txt")