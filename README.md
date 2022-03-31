# Emoji Creator Project With DCGAN, ECGAN :wave:

My First GAN Project :musical_note:

* 제작기간 2022-01-07 ~ 2022-01-11 1차 작업
* 2차 작업 진행 2022-03-02 ~ 2022-03-11

## 프로젝트 기획 배경
GAN을 사용해서 존재하지 않는 이모티콘을 생성할 수 있을까? 라는 의문에서 시작되었습니다.

## 솔루션
GAN 모델 중에서 가장 기본 모델은 DCGAN을 사용해서 웹 사이트에서 유저가 요청을 보낼 때 마다 Generator가 Random Noise를 받아서 매번 새로운 이모티콘을 생성해준다.

## 프로젝트 설계 중 발생한 문제점
1차 작업을 했을 경우 아래의 두 이미지처럼 전혀 모양이 잡히지 않고 Noise 값만 출력되었다. 해결 방법을 찾지 못하고 잠시 프로젝트를 중단하였습니다.

![gan1](https://user-images.githubusercontent.com/76984534/160864359-7eb78b3d-085e-477d-b8bc-bae79f57e810.gif)
![gan2](https://user-images.githubusercontent.com/76984534/160864370-b675998f-5ed0-47ff-bb53-76bc408946bf.gif)

2차 때는 이미지도 어느 정도 형태를 갖춘 이미지가 생성되었지만 Generator에 Random Noise를 넣어주어도 마지막에 생성한 이미지들 중에서만 반복해서 생성하는 것을 발견했습니다. -> 해결에는 실패했습니다...

## 프로젝트 결과

Epoch 30
![30](https://user-images.githubusercontent.com/76984534/160865924-6ee0e33c-24a4-4f45-9838-fa39732275a3.png)

Epoch 60
![60](https://user-images.githubusercontent.com/76984534/160865794-53c6af3f-73e5-4fe8-8a60-9d2ea9739511.png)

Epoch 108
![108](https://user-images.githubusercontent.com/76984534/160865789-fcabaef6-e87b-4b3d-8809-65eca6931bb5.png)

## 발전 과제
* GAN Model 수정
  * 비슷한 이미지만 계속해서 생성하는 문제점을 해결해야 합니다.

## 참고자료 :thumbsup:

* Original paper on DCGAN by Radford and Metz https://arxiv.org/pdf/1511.06434.pdf
* emojigan Github by tomhata https://github.com/tomhata/emojigan
* Learning about the overall GAN https://www.youtube.com/watch?v=oK4SrEdimaU&t=1037s
* Pytorch DCGAN Tutorial https://pytorch.org/tutorials/beginner/dcgan_faces_tutorial.html
