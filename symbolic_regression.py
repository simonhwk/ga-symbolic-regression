
# How to plot a .txt file in Matplotlib

# Plotting with Matplot lib


import matplotlib.pyplot as plt

x = []
y = []

for line in open('data2022_Gold.txt', 'r'):
    lines = [i for i in line.split(", ")]
    x.append(float(lines[0]))
    y.append(float(lines[1]))

plt.title("Symbolic Regression (RS)")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x,y, marker = 'o', c='g')

plt.show()