import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]


plt.xlabel('x')
plt.ylabel('y')
plt.title('Wykres')
plt.legend('Wykres')
plt.plot(x, y)
plt.show()

# import numpy as np
# import seaborn as sns
# sns.set_theme(style="ticks")
#
# rs = np.random.RandomState(11)
# x = rs.gamma(2, size=1000)
# y = -.5 * x + rs.normal(size=1000)
#
# sns.jointplot(x=x, y=y, kind="hex", color="#4CB391")

