import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')

print(titanic.head())

df = pd.DataFrame(titanic)
df.to_excel('./titanic seaborn.xlsx')