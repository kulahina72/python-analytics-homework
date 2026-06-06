import pandas as pd
data = {"city": ["Kyiv", "Lviv", "Odesa"], "sales": [1200, 950, 550]}
df = pd.DataFrame(data)
print("Продажі по містах:")
print(df)
print("Середнє значення:", df["sales"].mean())
