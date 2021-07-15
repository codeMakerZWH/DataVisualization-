import pandas as pd
TXT_PATH = './orders.txt'
CSV_PATH = './orders.csv'
XLSX_PATH = './orders.xlsx'
JSON_PATH = './geo.json'
pd.set_option('display.width',None)#设置数据展示宽度
txt = pd.read_csv(TXT_PATH)
csv = pd.read_csv(CSV_PATH)
xlsx = pd.read_excel(XLSX_PATH,keep_default_na=False) #读取指定的seet表格,指定行，遇到空不显示NaN
json = pd.read_json(JSON_PATH)
print(txt.head(5))
print("________________________________________________________________________________________________________________")
print("________________________________________________________________________________________________________________")
print(csv.head(5))
print("________________________________________________________________________________________________________________")
print("________________________________________________________________________________________________________________")
print(xlsx.head(5))
print("________________________________________________________________________________________________________________")
print("________________________________________________________________________________________________________________")
print(json.head(5))