import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
print(tips)
# sns.displot(tips['total_bill'], bins=50, kde=True)
# sns.countplot(x="sex", data=tips)
# sns.boxplot(x="day", y="total_bill", hue="sex", data=tips)
# sns.violinplot(x="day", y="total_bill", hue="sex", data=tips)
plt.legend()
plt.show()
