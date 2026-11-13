import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set_theme(style='whitegrid')
df = pd.read_csv('online food delivery dataset.csv')
if 'Unnamed: 13' in df.columns:
  df = df.drop(columns=['Unnamed: 13'])
df = df.drop_duplicates()

plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=df,
    x='longitude',
    y='latitude',
    hue='Feedback',
    style='Gender',
    s=80,
    palette='viridis',
    alpha=0.8,
)
plt.title(
    'Geographic Distribution of Customers (Lat vs Long)',
    fontsize=14,
    fontweight='bold',
)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.savefig('viz6_geo_scatter.png', dpi=300)
plt.show()