from matplotlib import pyplot as plt
import math

plot_points: int = 60
x_data = [50 * x for x in range(plot_points)]
y_data = [0.9] + [0.9 - 0.06*math.log(x, 2) for x in x_data[1:]]

plt.title('Application\'s Internal Flow Ratio (AIFR)')
plt.xlabel('Data size [MB]')
plt.ylabel('AIFR')
plt.xlim(0, max(x_data))
plt.ylim(0, 1)
plt.plot(x_data, y_data, label='Runtime')
#plt.legend(loc='lower right')
plt.show()
