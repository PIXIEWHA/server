## 📖 딥러닝 영상 처리 서버 관련
모델 학습은 학교 GPU에서 진행하였고,</br>
나머지 영상 처리는 깃허브로 작업하다가 Colab을 주로 사용하기 때문에 드라이브상에서 주로 작업하였습니다.</br></br>
데이터 및 영상 프레임 추출, 중간과정 등</br>
* https://drive.google.com/drive/folders/1zATqZHFnypoVExkp77QxjVRuCCIpcmz5 </br>

최종 소스코드</br>
* https://drive.google.com/drive/folders/1CoSid6ZSXyU4i3QDlncG3IX4IHdvcm97

## ⚙️ 드라이브 디렉토리 구조 및 주요 소스 코드
```
Notebooks
├── 192.168.XXX.XXX                                    - 라즈베리파이 IP 주소(영상 처리 후 저장 위치)
├── OpenCV
│
├── yolov5                                             - Object Detection의 Yolov5
├── Yolov5_DeepSort_Pytorch                            - Tracking Algorithm의 DeepSort
├── openpose                                           - Pose Estimation의 OpenPose
│ 
└──  Main.ipynb                                        - Main 실행
```
