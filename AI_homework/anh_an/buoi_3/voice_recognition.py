import pandas as pd
s_re = pd.read_csv("voice.csv")
X = [n[:-1] for n in s_re.values]
y = [n[-1] for n in s_re.values]
print(s_re.isnull().any())
