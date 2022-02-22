import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Построение случайного блуждания.
rw = RandomWalk(50_000)
rw.fill_walk()

# Нанесение точек на диаграмму
plt.style.use('classic')
fig, ax = plt.subplots()
point_numbers = range(rw.num_points)
ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
	edgecolors='none', s=1)

# Выделение первой и последней точек
ax.scatter(0, 0, c='green', edgecolors='none', s=100, label='Start')
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100, label='End')

plt.legend()
# Удаление осей
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.savefig('random_walk.png', bbox_inches='tight')