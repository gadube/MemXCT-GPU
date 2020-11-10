import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def change_width(ax, new_value) :
    for patch in ax.patches :
        current_width = patch.get_width()
        diff = current_width - new_value

        # we change the bar width
        patch.set_width(new_value)

        # we recenter the bar
        patch.set_x(patch.get_x() + diff * .5)

sns.set_style("whitegrid")

df = pd.read_csv("stat.csv")

print(df)
df['GFLOPS'] = df['totGFLOPS']
df['GPU'] = df['gpu']

sns.factorplot(x='GPU',y='GFLOPS',hue='dataset',data=df,kind='bar')
plt.title('Single CPU-GPU Performance')
ax = plt.gca()
# change_width(ax,.5)
plt.show()