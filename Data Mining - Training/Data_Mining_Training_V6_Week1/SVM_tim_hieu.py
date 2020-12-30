# training model: use the info to draw a graph
# testing model: check to see how well the graph
# bias: how well it fits training model, variant: how well it fits testing model
import pandas as pd
from sklearn.datasets import load_iris
from matplotlib import pyplot as plt

iris = load_iris()
print(iris.target_names)
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["target"] = iris.target  # target's values (0,1,2) represent iris' name in target_names
df["flower_name"] = df["target"].apply(lambda x: iris.target_names[x])

df0 = df[df.target == 0]
df1 = df[df.target == 1]
df2 = df[df.target == 2]

fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()

ax1.scatter(df0["sepal length (cm)"], df0["sepal width (cm)"], c=df0["petal length (cm)"], cmap="summer")
ax1.scatter(df1["sepal length (cm)"], df1["sepal width (cm)"], c=df1["petal length (cm)"], cmap="summer")
cbar1 = fig1.colorbar(ax1)

cbar1.set_label('Petal length ratio')
ax1.set_title('Iris 0 vs 2')
ax1.set_xlabel('Sepal length')
ax1.set_ylabel('Sepal width')

ax2.scatter(df0["sepal length (cm)"], df0["sepal width (cm)"], c=df0["petal length (cm)"], cmap="summer")
ax2.scatter(df2["sepal length (cm)"], df2["sepal width (cm)"], c=df2["petal length (cm)"], cmap="summer")
cbar2 = fig2.colorbar(ax2)

cbar2.set_label('Petal length ratio')
ax2.set_title('Iris 0 vs 2')
ax2.set_xlabel('Sepal length')
ax2.set_ylabel('Sepal width')


plt.tight_layout()
plt.show()