import csv

import matplotlib.pyplot as plt

f = open("../nba_play_minute.csv")
data = csv.reader(f)

basket_ball_position = ["point_guard", "shooting_guard", "small_forward", "power_forward", "center"]
play_minute_list = []

for index, row in enumerate(data):
    for player_minute in row[1:]:
        if index >= 1:
            play_minute_list.append(float(player_minute))

all_position_avg_minute_list = []
for index in range(1, 6):
    all_position_avg_minute_list.append(sum(play_minute_list) / 5)


def create_x(t, w, n, d):
    return [t * x + w * n for x in range(d)]


value_a_x = create_x(2, 0.8, 1, 5)
value_b_x = create_x(2, 0.8, 2, 5)
ax = plt.subplot()
ax.bar(value_a_x, all_position_avg_minute_list, label='All Positions Average')
ax.bar(value_b_x, play_minute_list, label='Play Positions Average')
middle_x = [(a + b) / 2 for (a, b) in zip(value_a_x, value_b_x)]
ax.set_xticks(middle_x)
ax.set_xticklabels(basket_ball_position, rotation=10)

plt.ylim([26, 35])

plt.title('The difference between the average time and the overall average time for each position', fontsize=10, pad=15)
plt.ylabel('play_minute', fontsize=14, labelpad=5)

plt.legend(fontsize=9)

plt.show()
