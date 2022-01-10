import requests
from bs4 import BeautifulSoup
import re
import urllib.request

### 원하는 url 정보를 넘겨줌
url = 'https://emojipedia.org/nature/'
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

link = soup.find(attrs={"class":"emoji-list"})
# print(link.find_all("a"))

### 크롤링할 사이트 리스트
link_list = list(map(lambda x:x['href'], link.find_all("a")))

### 가져올 이미지 리스트
### 이미지가 얼굴만 있는 이미지랑 몸 전체가 있는 이미지가 있다보니 loss가 안 잡힌다.
# animals_list = ['dog', 'dat', 'poodle', 'wolf',
#                 'fox', 'raccoon', 'lion', 'tiger',
#                 'leopard', 'horse', 'unicorn', 'zebra',
#                 'deer', 'cow', 'bison', 'buffalo', 'pig',
#                 'boar', 'ram', 'ewe', 'goat', 'camel', 'llama',
#                 'giraffe', 'elephant', 'mammoth', 'rhinoceros',
#                 'hippopotamus', 'mouse', 'rat', 'hamster', 'rabbit',
#                 'chipmunk', 'beaver', 'hedgehog', 'bear', 'koala',
#                 'panda', 'sloth', 'otter', 'monkey']

animals_face_list = ['/See-No-Evil-Monkey/', '/Hear-No-Evil-Monkey/', '/Speak-No-Evil-Monkey/',
                    '/Monkey-Face/', '/Dog-Face/', '/Wolf/', '/Fox/', '/Raccoon/', '/Cat-Face/', '/Lion/',
                    '/Tiger-Face/', '/Horse-Face/', '/Unicorn/', '/Cow-Face/', '/Pig-Face/', '/Boar/',
                    '/Pig-Nose/', '/Mouse-Face/', '/Hamster/', '/Rabbit-Face/', '/Bear/', '/Polar-Bear/',
                    '/Koala/', '/Panda/', '/Chicken/', '/Hatching-Chick/', '/Frog/', '/Dragon-Face/']

lower_animals_face_list = []
for text in animals_face_list:
    lower_animals_face_list.append(text.lower())


# ### 정한 이미지 리스트에서 맞는 이미지 사이트만 가져오기
# scrapping_list = []
# for i in range(len(link_list)):
#     for a in animals_face_list:
#         if a in link_list[i]:
#             scrapping_list.append(link_list[i])

# scrapping_list.pop()
# # print(scrapping_list)

### 이미지 크롤링
for idx, source in enumerate(lower_animals_face_list):
    source_url = "https://emojipedia.org" + source
    print(source_url)
    title = re.findall('[a-zA-Z]+', source) # 불러온 링크에 정규표현식으로 나눠서 title로 설정
    res_1 = requests.get(source_url)
    res_1.raise_for_status()
    soup = BeautifulSoup(res_1.text, "lxml")
    images = soup.find_all("div", attrs={"class":"vendor-image"})


    for img in images:
        real_img = img.img["src"]
        if real_img.startswith("/"): # 여러 버전의 이미지는 가져오지 못 했음
            continue
        if "skype" in real_img: # skype 이미지는 가끔씩 움직이는 이미지가 있어서 제외
            continue
        print(real_img) # 이미지 크기 120x120
        """이미지 파일을 라이브러리를 이용해서 저장"""
        urllib.request.urlretrieve(real_img,
        f"C:/Users/jaksi/Section4/Project/animals_face/{'_'.join(title)}_{idx}.png")
        idx += 1