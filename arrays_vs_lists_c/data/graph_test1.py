import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data/test1_results.csv")

fig, ax = plt.subplots()
ax.step(data["Elements"], data["Array"], label="Array")
ax.step(data["Elements"], data["List"], label="List")
ax.set_title("Constant Insertion Index (n / 2) - Variable Data Structure Size")
ax.set_xlabel("Elements")
ax.set_ylabel("Time (s)")
ax.legend()

fig.savefig("test1_results.png")
plt.show()