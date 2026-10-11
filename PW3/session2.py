import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv("Heart_disease_cleveland_new.csv")  

#task 4
sick = df[df["target"] == 1]["thalach"]
healthy = df[df["target"] == 0]["thalach"]
print(len(sick), len(healthy))

x, p = stats.mannwhitneyu(sick, healthy, alternative = "two-sided")
print(f"U = {x}, p = {p:.2e}")

means = [sick.mean(), healthy.mean()]
sems = [stats.sem(sick), stats.sem(healthy)]
print("disease:", means[0], "+/-", sems[0])
print("healthy:", means[1], "+/-", sems[1])

plt.errorbar(["disease", "healthy"], means, yerr = sems, fmt = "o", capsize = 8)
plt.ylabel("thalach (mean +- SEM)")
plt.savefig("means.png")
plt.close()

#task 5
rho, p_sp = stats.spearmanr(df["age"], df["thalach"])
print(f"rho = {rho:.3f}, p = {p_sp:.2e}")


plt.scatter(df["age"], df["thalach"], alpha=0.6)
plt.xlabel("age")
plt.ylabel("thalach")
plt.savefig("age_thalach.png")
plt.close()

#task 6-7
c = pd.read_csv("chemical_cancer.csv")
print(c.columns)
print(c.head())

print(c.corr(numeric_only = True)["malignancy"])


print(c.corr(numeric_only=True)["pollution_index"])


sub = c[(c["pollution_index"] > 40) & (c["pollution_index"] < 60)]
print(len(sub))
print(sub[["benzene", "cadmium", "malignancy"]].corr()["malignancy"])

#bonus : entropiya
p = df["target"].value_counts(normalize=True)
H = -(p * np.log2(p)).sum()
print(p)
print(H)