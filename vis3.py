import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set_theme(style='whitegrid')
df = pd.read_csv('online food delivery dataset.csv')
if 'Unnamed: 13' in df.columns:
  df = df.drop(columns=['Unnamed: 13'])
df = df.drop_duplicates()

plt.figure(figsize=(12, 6))
sns.countplot(
    data=df,
    x='Educational Qualifications',
    hue='Output',
    palette='Paired',
    order=df['Educational Qualifications'].value_counts().index,
)
plt.title(
    'Online Ordering Status by Educational Qualifications',
    fontsize=14,
    fontweight='bold',
)
plt.xlabel('Educational Qualifications')
plt.ylabel('Count')
plt.xticks(rotation=30)
plt.legend(title='Active Order (Output)')
plt.savefig('viz3.png', dpi=300)
plt.show()