import pandas as pd
url = 'https://raw.githubusercontent.com/Muralimekala/python/master/Resp2.csv'
df1 = pd.read_csv(url)
print(df1.head())
#Dataset is now stored  in a Pandas Dataframe

url = 'https://raw.githubusercontent.com/Muralimekala/python/master/Salaries.csv'
sf = pd.read_csv(url)
print(sf.head())

print("ID e Nome de empregados")
lista = pd.DataFrame(sf.head(),columns=['Id','EmployeeName'])

print(lista)

print("Nome pela lista")
print(lista['EmployeeName'])