import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set_theme(style='whitegrid')
df = pd.read_csv('online food delivery dataset.csv')
if 'Unnamed: 13' in df.columns:
  df = df.drop(columns=['Unnamed: 13'])
df = df.drop_duplicates()

plt.figure(figsize=(12, 6))
income_occupation = pd.crosstab(df['Occupation'], df['Monthly Income'])
income_occupation.plot(
    kind='bar', stacked=True, colormap='Spectral', figsize=(10, 6)
)
plt.title(
    'Monthly Income Breakdown Across Different Occupations',
    fontsize=14,
    fontweight='bold',
)
plt.xlabel('Occupation')
plt.ylabel('Customer Count')
plt.xticks(rotation=45)
plt.legend(title='Monthly Income', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.savefig('viz6.png', dpi=300)
plt.show()