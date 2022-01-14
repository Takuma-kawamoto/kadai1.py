x = [1452, 1796, 1894, 2584, 2735, 3447]
y = [3231, 3747, 3726, 5853, 8866, 10913]
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.scatter(x, y)
plt.xlabel("applicant") 
plt.ylabel("Number of open campus participants") 
plt.legend()
plt.show()
