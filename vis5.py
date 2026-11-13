import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set_theme(style='whitegrid')
df = pd.read_csv('online food delivery dataset.csv')
if 'Unnamed: 13' in df.columns:
  df = df.drop(columns=['Unnamed: 13'])
df = df.drop_duplicates()

plt.figure(figsize=(10, 6))
sns.boxplot(
    data=df,
    x='Family size',
    y='Age',
    palette='Set2',
    boxprops=dict(alpha=0.8),
)
sns.stripplot(data=df, x='Family size', y='Age', color='black', alpha=0.5, jitter=0.2)
plt.title(
    'Age Spread Across Various Family Sizes', fontsize=14, fontweight='bold'
)
plt.xlabel('Family Size')
plt.ylabel('Age')
plt.savefig('viz5.png', dpi=300)
plt.show()