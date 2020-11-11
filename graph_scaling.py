import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

sns.set_style("white")

df = pd.read_csv("stat_2.csv")

df['GPU'] = df['gpu']
df['Timing'] = df['timing_p'] + df['timing_b']
df1 = df[df['Dataset'] == 'CDS1']
df2 = df[df['Dataset'] == 'CDS2']

g = sns.relplot(x='Nodes',y='Timing',hue='time_type',data=df1,marker='o',ci=None,kind='line')
g._legend.remove()
plt.plot([1,2,3,4],[1,1/2,1/3,1/4],color='k',linestyle='-',linewidth=1)
plt.text(1,.95,"O(1/P)",rotation=-15)
plt.yscale('log')
leg = plt.legend(fancybox=True, framealpha=1)
plt.ylim([.01,10])
plt.xlabel('Number of Nodes')
plt.ylabel('Solution Time (s)')
plt.xticks([1,2,3,4])
plt.grid(b=True,which='minor',linestyle='-')
plt.grid(b=True,which='major',linestyle='-')
plt.grid(xdata=True,which='major',linestyle='-')
plt.tight_layout()
plt.title('CDS1 Azure Strong Scaling')
plt.rcParams['axes.edgecolor'] = 'black'
plt.rcParams['axes.linewidth'] = 1
plt.show()

g = sns.relplot(x='Nodes',y='Timing',hue='time_type',data=df2,marker='o',ci=None,kind='line')
g._legend.remove()
plt.plot([1,2,3,4],[1,1/2,1/3,1/4],color='k',linestyle='-',linewidth=1)
plt.text(1,.55,"O(1/P)",rotation=-15)
plt.yscale('log')
leg = plt.legend(fancybox=True, framealpha=1)
plt.ylim([.01,10])
plt.xlabel('Number of Nodes')
plt.ylabel('Solution Time (s)')
plt.xticks([1,2,3,4])
plt.grid(b=True,which='minor',linestyle='-')
plt.grid(b=True,which='major',linestyle='-')
plt.grid(xdata=True,which='major',linestyle='-')
plt.tight_layout()
plt.title('CDS2 Azure Strong Scaling')
plt.rcParams['axes.edgecolor'] = 'black'
plt.rcParams['axes.linewidth'] = 1
plt.show()