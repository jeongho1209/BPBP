import csv

import matplotlib.pyplot as plt
import numpy as np

data = csv.reader(open("../nba_play_minute.csv"))

basket_ball_position = ["point_guard", "shooting_guard", "small_forward", "power_forward", "center"]
play_minute_list = []

for index, row in enumerate(data):
    for player_minute in row[1:]:
        if index >= 1:
            play_minute_list.append(float(player_minute))

length = np.arange(5)

plt.bar(length, play_minute_list, width=0.2, align='edge',
        color='blue', tick_label=basket_ball_position)

plt.annotate(f'Max({max(play_minute_list).__round__(1)})minute', xy=(1, max(play_minute_list)), xytext=(1.3, 34.7),
             arrowprops=dict(facecolor='black', shrink=0.05)) # xy -> 가르키는곳, xytext -> 글씨 위치

plt.ylim([26, 35])

plt.title('Average Playtime by Position', pad=20)
plt.xlabel('position', fontsize=14, labelpad=3)
plt.ylabel('play_minute', fontsize=14, labelpad=5)

plt.show()
