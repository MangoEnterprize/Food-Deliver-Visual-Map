import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set_theme(style='whitegrid')
df = pd.read_csv('online food delivery dataset.csv')
if 'Unnamed: 13' in df.columns:
  df = df.drop(columns=['Unnamed: 13'])
df = df.drop_duplicates()

plt.figure(figsize=(10, 6))
sns.histplot(
    data=df,
    x='Age',
    hue='Output',
    element='step',
    common_norm=False,
    palette='muted',
    kde=True,
)
plt.title(
    'Customer Age Distribution Segmented by Continued Ordering (Output)',
    fontsize=14,
    fontweight='bold',
)
plt.xlabel('Age')
plt.ylabel('Density / Count')
plt.savefig('viz7.png', dpi=300)
plt.show()