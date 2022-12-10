<div align="center">
  <h1>딥러닝 기반 저비용 주택가 쓰레기 무단 투기 인식 시스템(PIXIE)</h1>
  <img src="https://user-images.githubusercontent.com/67186222/120105425-c8506f80-c193-11eb-8533-0be46aef75b4.jpg" alt="pixie" width="300px" height="200px">    <img src="https://user-images.githubusercontent.com/67186222/144769445-dba8e1d7-5bfe-40d8-a6df-c95ec628c409.png" alt="pixie" width="200px" height="200px">
  <br />
</div>
<br />

## 목차
1. [**딥러닝 영상 처리**](#1)
1. [**기술 스택**](#2)
1. [**주요 기능**](#3)
1. [**실행 방법**](#4)
1. [**디렉토리 구조**](#5)

<!-- 버전기록 특이사항 SEO HeadingsMap 웹성능최적화 구글애널리틱스통계-->
<br />

<div id="1"></div>

## 📖 딥러닝 영상 처리
모델 학습은 학교 GPU에서 진행하였고,</br>
나머지 영상 처리는 깃허브로 작업하다가 Colab을 주로 사용하기 때문에 드라이브상에서 주로 작업하였습니다.</br></br>
<br />

<div id="2"></div>

## ⚙️ 기술 스택
![](https://img.shields.io/badge/%20-raspberrypi4-red)
![](https://img.shields.io/badge/%20%20yolo-v5.0-black)
![](https://img.shields.io/badge/%20-deepsort-navy)
![](https://img.shields.io/badge/opencv-v4.5.2-brightgreen)
![](https://img.shields.io/badge/%20python-3.9.13-black)
![](https://img.shields.io/badge/pytorch-v1.9.0-black)
![](https://img.shields.io/badge/%20-colab-orange)
<br /><br />

<div id="3"></div>

## 📲 주요 기능

| <div align="center"/>기능                      | <div align="center"/>내용                                                  |
| :------------------------ | :---------------------------------------------------------------------------------------------------------------------------------- |
| <div align="center"/>HW RaspberryPI|- WIFI<br/>- 영상 녹화 및 Firebase에 업로드|
| <div align="center"/>🔗[**SW 알고리즘(server)**](https://github.com/yhyeonjg/server)|- Object Detection<br/>&nbsp;&nbsp;&nbsp;&nbsp;- 데이터 크롤링 및 AI Hub 영상 데이터 프레임 추출<br/>&nbsp;&nbsp;&nbsp;&nbsp;- 사람 & 손 혹은 팔과 함께 있는 물건 라벨링<br/>&nbsp;&nbsp;&nbsp;&nbsp;- 무단 투기 행위 학습<br/> - Tracking Algorithm<br/>&nbsp;&nbsp;&nbsp;&nbsp;- 객체 좌표 추출 및 Box Collision<br/>&nbsp;&nbsp;&nbsp;&nbsp;- 영상 인식 테스트<br/>- OpenPose<br/>&nbsp;&nbsp;&nbsp;&nbsp;- Coco Model로 사람 관절 인식<br/>&nbsp;&nbsp;&nbsp;&nbsp;- 영상 테스트<br/>&nbsp;&nbsp;&nbsp;&nbsp;- 사람과 물체 ID 좌표를 프레임별로 저장<br/>&nbsp;&nbsp;&nbsp;&nbsp;- 이전 프레임과 비교하여 사람은 있으나 물건 없고, 목-골반 선 < 45도 or 손목-발목 선 < 45도 투기 인식|

<br />

<div id="4"></div>

## 💡 실행 방법
### 개발환경
**1. 원격 저장소 복제**

```bash
$ git clone https://github.com/PIXIEWHA/server
$ git clone https://github.com/opencv/opencv
$ git clone https://github.com/CMU-Perceptual-Computing-Lab/openpose
$ git clone https://github.com/ultralytics/yolov5
$ git clone https://github.com/oaqoe-DWQ/Yolov5_DeepSort_Pytorch
```
**2. firebase appKey 등록**
> firebase.json 등록
<br/>

<div id="5"></div>

## 📂 디렉토리 구조

```
Notebooks
├── 192.168.XXX.XXX                                    - 라즈베리파이 IP 주소(영상 처리 후 저장 위치)
├── opencv
├── openpose                                           - Pose Estimation의 OpenPose
├── yolov5                                             - Object Detection의 Yolov5
├── Yolov5_DeepSort_Pytorch                            - Tracking Algorithm의 DeepSort
├── Blur.py                                            - 얼굴 블러 처리
├── Fcm.py                                             - 무단 투기 인식하면 어플 알림
├── OpenPose.py                                        - 사람 관절 인식
├── Main.py                                            - Main 실행(무단 투기 인식)
└── firebase.json                                      - firebase appKey 등록
```
<br/>