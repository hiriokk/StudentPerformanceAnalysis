import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\USER\Downloads\journal.csv")

dates = df[["09.09.2026", "12.09.2026", "25.09.2026", "02.10.2026", "09.10.2026", "16.10.2026"]]
arr = dates.to_numpy(dtype=float)

df["Середній бал"] = dates.mean(axis=1).round(1)
df["Оцінок 1-3"] = ((arr >= 1) & (arr <= 3)).sum(axis=1)
df["Статус"] = np.where(df["Середній бал"] >= 7, "Добре", "Потребує уваги")

df_summary = df[["Прізвище та ініціали студента", "Середній бал", "Оцінок 1-3", "Статус"]]
df_summary.to_csv(r"C:\Users\USER\Downloads\results.csv", index=False)

print(df)
print("Середній бал:", np.nanmean(arr))
print("Найвищий бал:", np.nanmax(arr))
print("Найнижчий бал:", np.nanmin(arr))

print(df_summary)


