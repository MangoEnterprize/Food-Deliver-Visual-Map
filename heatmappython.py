import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set_theme(style='whitegrid')
df = pd.read_csv('online food delivery dataset.csv')
if 'Unnamed: 13' in df.columns:
  df = df.drop(columns=['Unnamed: 13'])
df = df.drop_duplicates()

plt.figure(figsize=(10, 6))
heatmap_data = pd.crosstab(df['Marital Status'], df['Monthly Income'])
sns.heatmap(heatmap_data, annot=True, fmt='d', cmap='Blues', cbar=True)
plt.title(
    'Customer Concentration: Marital Status vs. Monthly Income',
    fontsize=14,
    fontweight='bold',
)
plt.xlabel('Monthly Income Bracket')
plt.ylabel('Marital Status')
plt.xticks(rotation=30)
plt.savefig('viz1.png', dpi=300)
plt.show()