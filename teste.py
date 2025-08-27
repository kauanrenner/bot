import pandas as pd

sheet = pd.read_excel('CALIBRACAO PIC.xlsx', sheet_name=['Planilha3'])
cs = sheet['Planilha3']

print(cs['PIC'].count())
