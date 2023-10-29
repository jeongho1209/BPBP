import csv

import matplotlib.pyplot as plt

data = csv.reader(open("nba_play_minute.csv"))

basket_ball_position = ["point_guard", "shooting_guard", "small_forward", "power_forward", "center"]
play_minute_list = []

for index, row in enumerate(data):
    for player_minute in row[1:]:
        if index >= 1:
            play_minute_list.append(float(player_minute))

explode = [0, 0.15, 0, 0, 0.15]

plt.pie(play_minute_list, labels=basket_ball_position, autopct='%.1f%%',
        explode=explode, shadow=True, startangle=90,
        textprops={'size': 13})

plt.title('Average Playtime Percentage by Position', size=20, pad=10)

plt.legend(loc='lower left', bbox_to_anchor=(-0.4, 0.5), fontsize=9)

plt.annotate(f'Max({20.8})Percentage', xy=(-1.25, -0.5), xytext=(-0.9, -1.2),
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.annotate(f'Min({18.3})Percentage', xy=(1, 1), xytext=(1.05, 0.5),
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.show()
