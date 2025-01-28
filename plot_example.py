import matplotlib.pyplot as plt
import numpy as np

#Line plot
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("sin x")
plt.title('Line show of Sin(x)')
plt.show()

#Scatter Plots
x = np.random.randn(100)
y = np.random.randn(100)

plt.scatter(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Plot for Random Data')
plt.show()

# Bar Graph
x = ['Apples', 'Mango', 'Banana']
y = [10, 20, 30]

plt.bar(x, y)
plt.xlabel('Fruits')
plt.ylabel('Quantity')
plt.title('Fruits Bar Chart')
plt.show()

#Histogram
data = np.random.randn(1000)

plt.hist(data, bins=30)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Random Data')
plt.show()

# sub plots
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))

ax1.plot(x, y1)
ax1.set_xlabel('x')
ax1.set_ylabel('sin x')
ax1.set_title('Line plot of sin x')

ax2.plot(x, y2)
ax2.set_xlabel('x')
ax2.set_ylabel('cos x')
ax2.set_title('Line plot of cos x')

plt.tight_layout()
plt.show()