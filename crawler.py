from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
import os
from openpyxl import Workbook

start = time.time()

# 폴더 생성
os.makedirs('result', exist_ok=True)
wb = Workbook(write_only=True)
ws = wb.create_sheet()

df = pd.read_csv('test.csv', sep=',', encoding='CP949')
df = df[['name', 'address']]
df.columns = ['name', 'address']
df['search'] = df['address'] + df['name']

# 링크
url = 'https://www.google.co.kr/maps/'
keyword = '부산' + '카페 루프탑 청사포'

# 실행
options = webdriver.ChromeOptions()
options.add_argument('--disable-gpu')
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument('--window-size=1920x1080')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get(url)

search_box = driver.find_element(by=By.CSS_SELECTOR, value="input#searchboxinput")
search_box.send_keys(keyword)
search_button = driver.find_element(by=By.CSS_SELECTOR, value="button#searchbox-searchbutton")
search_button.click()

#토탈 별점: ceNzKf
#주소:"Io6YTe fontBodyMedium"

time.sleep(5)

# 리뷰 전체 보기
total_num_review = driver.find_element(by=By.CSS_SELECTOR, value="#QA0Szd > div > div > div.w6VYqd > div.bJzME.tTVLSc > div > div.e07Vkf.kA9KIf > div > div > div.TIHn2 > div.tAiQdd > div.lMbq3e > div.LBgpqf > div > div.fontBodyMedium.dmRWX > div.F7nice.mmu3tf > span:nth-child(2) > span:nth-child(1) > button")
total_num_review.click()
time.sleep(5)

# 정렬-최신
sort = driver.find_element(by=By.XPATH,
                           value='//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]'
                                 '/div/div/div[2]/div[7]/div[2]/button/span')
sort.click()
time.sleep(1)

new = driver.find_element(by=By.XPATH, value='//*[@id="action-menu"]/ul/li[2]')
new.click()
time.sleep(1)

#자동 스크롤
SCROLL_PAUSE_TIME = 1

#스크롤 높이 구하기
last_height = driver.execute_script("return document.body.scrollHeight")
number = 0

while True:
    number = number + 1

    # 스크롤 아래로 내리기
    ele = driver.find_element(by=By.XPATH, value='//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]')
    driver.execute_script('arguments[0].scrollBy(0, 5000);', ele)

    # 페이징 로딩 시간 기다리기
    time.sleep(SCROLL_PAUSE_TIME)

    # 새 높이 계산하고 기존 높이랑 비교
    print(f'last height: {last_height}')

    ele = driver.find_element(by=By.XPATH, value='//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]')

    new_height = driver.execute_script("return arguments[0].scrollHeight", ele)

    print(f'new height: {new_height}')

    if number == 19:
        break

    if new_height == last_height:
        break

    print('cont')
    last_height = new_height

item = driver.find_elements(by=By.XPATH, value='//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[9]')
time.sleep(1)

stars_list = []
review_list = []
duration_list = []

for i in item:

    button = i.find_elements(by=By.TAG_NAME, value='button')
    for m in button:
        if m.text == "자세히":
            m.click()
    time.sleep(1)

    #title = i.find_element(by=By.CSS_SELECTOR, value="h3.section-result-title")
    stars = i.find_elements(by=By.CLASS_NAME, value="kvMYJc")
    review = i.find_elements(by=By.CLASS_NAME, value="wiI7pd")
    duration = i.find_elements(by=By.CLASS_NAME, value="rsqaWe")


for j, l, k in zip(duration, stars, review):
        duration_list.append(j.text)
        stars_list.append(l.get_attribute("aria-label"))
        review_list.append(k.text)

review = pd.DataFrame({
    'rating': stars_list,
     'review': review_list,
     'duration': duration_list})

review.to_csv(keyword+'.csv', index=False, encoding='utf8') 
print(review)
print("time :", time.time() - start)