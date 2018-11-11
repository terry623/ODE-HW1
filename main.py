import numpy as np
import matplotlib.pyplot as plt


def A_Function(i):
    up = 2200 * i - 900
    down = 5.5 * i * i - 1
    return up / down


def B_Function(i):
    up = 2250 * i - 1000
    down = 5.5 * i * i - 1
    return up / down


def draw(calculate):
    x = np.linspace(0, 1, 10)  # 表示在 0 到 1 之间生成數個 x 值
    y = [calculate(i) for i in x]  # 求對應的 y 值

    plt.plot(x, y)  # 用生成的值去對應
    plt.show()  # 繪製圖像


print('A(1) =', A_Function(1))
print('B(1) =', B_Function(1))

draw(A_Function)
draw(B_Function)
