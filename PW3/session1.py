import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

data = pd.read_csv("Heart_disease_cleveland_new.csv")
print(data.shape)
print(data.head(10))
#?
cont = data[["age", "chol", "trestbps", "thalach"]]

fig, axes = plt.subplots(2,2, figsize = (10, 8))
for ax, col in zip(axes.ravel(), cont.columns):
    ax.hist(cont[col], bins = 20, edgecolor = "yellow")
    ax.set_title(col)
plt.savefig("distributions.png")

fig, axes = plt.subplots(2,2, figsize = (10, 8))
for ax, col in zip(axes.ravel(), cont.columns):
    stats.probplot(cont[col], plot = ax)
    ax.set_title(col)
plt.tight_layout()
plt.savefig("qq.png")
plt.close()

for col in cont.columns:
    stat, p = stats.shapiro(cont[col])
    print(f"{col}: p = {p:.4f}")





