import matplotlib.pyplot as plt

plt.plot(time, measure, label='measure')
plt.plot(time, estimation, label='estimation')
plt.ylabel('temperature')
plt.xlabel('time (minutes)')
plt.legend()
plt.show()
