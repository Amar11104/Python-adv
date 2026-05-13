import pandas as pd

data = {
    'Name': ['Alice','Bob','John'],
    'Age':[25,30,26],
    'City':['New York','Prishtina','San francisco']
}

df = pd.DataFrame(data)
print(df)