import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

sns.set_style("whitegrid")

df = pd.read_csv("stat.csv")

print(df)
df['GFLOPS'] = df['totGFLOPS']
df['GPU'] = df['gpu']

sns.factorplot(x='GPU',y='GFLOPS',hue='dataset',data=df,kind='bar')
plt.title('Single CPU-GPU Performance')
plt.show()

palette= {"CDS1":"C2", "CDS2":"C3"}
sns.factorplot(x='GPU',y='bw',hue='dataset',data=df,kind='bar',palette=palette)
plt.ylabel("B/W (GB/s)")
plt.title('Memory B/W Utilization')
plt.show()