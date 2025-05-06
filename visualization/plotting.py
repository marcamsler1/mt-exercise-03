import matplotlib.pyplot as plt
import re
import pandas as pd

baseline = "baseline.log"
prenorm = "prenorm.txt"
postnorm = "postnorm.txt"


baseline_values = []
prenorm_values = []
postnorm_values = []

with open(baseline, "r") as f1, open(prenorm, "r") as f2, open(postnorm, "r") as f3:
    for line1 in f1:
        match = re.search(r"ppl:   ?([\d.]+)", line1)
        if match:
            baseline_values.append(float(match.group(1)))

    for line2 in f2:
        match = re.search(r"ppl: ([\d.]+)", line2)
        if match:
            prenorm_values.append(float(match.group(1)))

    for line3 in f3:
        match = re.search(r"ppl: ([\d.]+)", line3)
        if match:
            postnorm_values.append(float(match.group(1)))

print(postnorm_values)

# Als Plot
plt.plot(baseline_values, label="Baseline")
plt.plot(prenorm_values, label="Prenorm")
plt.plot(postnorm_values, label="Postnorm")
plt.legend()
plt.xlabel("Step")
plt.ylabel("PPL")
plt.title("Perplexity over Time")
plt.tight_layout()
plt.show()

# Als Tabelle

df = pd.DataFrame({
    "Baseline": baseline_values,
    "Prenorm": prenorm_values,
    "Postnorm": postnorm_values
})
steps = [500 * (i + 1) for i in range(len(df))]
df.index = steps
df.index.name = "Step"
print(df)