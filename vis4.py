import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set_theme(style='whitegrid')
df = pd.read_csv('online food delivery dataset.csv')
if 'Unnamed: 13' in df.columns:
  df = df.drop(columns=['Unnamed: 13'])
df = df.drop_duplicates()

fig, axes = plt.subplots(1, 3, figsize=(16, 6), sharey=True)
customer_types = df['Customer Type'].unique()

for i, c_type in enumerate(customer_types):
  subset = df[df['Customer Type'] == c_type]['Feedback'].value_counts()

  # Capture wedges, labels texts, and percentage autotexts
  wedges, texts, autotexts = axes[i].pie(
      subset,
      labels=subset.index,
      autopct='%1.1f%%',
      startangle=90,
      colors=['#66b3ff', '#ff9999'],
      wedgeprops=dict(width=0.4, edgecolor='w'),
      pctdistance=0.75,  # Controls distance from center (0.7 to 0.8 sits nicely inside the ring)
  )

  # Style the percentage text inside the chart
  for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontweight('bold')
    autotext.set_fontsize(11)

  axes[i].set_title(f'Feedback: {c_type} Customers', fontweight='bold')

plt.savefig('viz4.png', dpi=300)
plt.show()