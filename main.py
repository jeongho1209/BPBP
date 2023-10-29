import re
import time
import pandas as pd

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

url = "https://www.espn.com/nba/stats/player/_/season/2023/seasontype/2/table/general"
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

scroll_location = driver.execute_script("return document.body.scrollHeight")

for j in range(1, 11):  # 버튼 클릭 횟수
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)
    scroll_height = driver.execute_script("return document.body.scrollHeight")

    if scroll_location == scroll_height:
        break
    else:
        scroll_location = driver.execute_script("return document.body.scrollHeight")

    driver.find_element(By.CSS_SELECTOR,
                        '#fittPageContainer > div:nth-child(3) > div > div > section > div > div:nth-child(3) > div.tc.mv5.loadMore.footer__statsBorder.bb.pb5 > a') \
        .send_keys(Keys.ENTER)

soup = BeautifulSoup(driver.page_source, "html.parser")

position_count = []

pg_play_minute = []
sg_play_minute = []
sf_play_minute = []
pf_play_minute = []
c_play_minute = []

for i in range(1, 536):
    select_url = f"#fittPageContainer > div:nth-child(3) > div > div > section > div > div:nth-child(3) > div > div > div > div.Table__Scroller > table > tbody > tr:nth-child({i})"
    game_play_position = soup.select(f"{select_url} > td.position.Table__TD > div")
    game_play_count = soup.select(f"{select_url} > td:nth-child(2)")
    game_play_minute = soup.select(f"{select_url} > td:nth-child(3)")

    cleaner = re.compile('<.*?>')
    position = re.sub(cleaner, '', str(game_play_position))
    minute = re.sub(cleaner, '', str(game_play_minute))
    clean_minute = minute.strip('[]')
    clean_position = position.strip('[]')
    position_count.append(clean_position)

    for play_count in game_play_count:
        if int(play_count.getText()) >= 10:  # 10게임 이상 참여한 선수만 포함
            if clean_position == 'PG':
                pg_play_minute.append(clean_minute)
            elif clean_position == 'SG':
                sg_play_minute.append(clean_minute)
            elif clean_position == 'SF':
                sf_play_minute.append(clean_minute)
            elif clean_position == 'PF':
                pf_play_minute.append(clean_minute)
            elif clean_position == 'C':
                c_play_minute.append(clean_minute)

avg_pg_play_minute = (sum(float(''.join(pg_minute)) for pg_minute in pg_play_minute)) / len(pg_play_minute)
avg_sg_play_minute = (sum(float(''.join(sg_minute)) for sg_minute in sg_play_minute)) / len(sg_play_minute)
avg_sf_play_minute = (sum(float(''.join(sf_minute)) for sf_minute in sf_play_minute)) / len(sf_play_minute)
avg_pf_play_minute = (sum(float(''.join(pf_minute)) for pf_minute in pf_play_minute)) / len(pf_play_minute)
avg_c_play_minute = (sum(float(''.join(c_minute)) for c_minute in c_play_minute)) / len(c_play_minute)

basket_ball_position = ["point_guard", "shooting_guard", "small_forward", "power_forward", "center"]

data = {
    'position_name': basket_ball_position,
    'avg_play_minute': [avg_pg_play_minute, avg_sg_play_minute, avg_sf_play_minute, avg_pf_play_minute,
                        avg_c_play_minute]
}
pd_data_frame = pd.DataFrame(data)
pd_data_frame.to_csv("nba_play_minute.csv", encoding='utf-8-sig', index=False)

driver.quit()
