import random
import pandas as pd

sheet = pd.read_excel("C:/Users/Diefra/Documents/CALIBRACAO PIC.xlsx", sheet_name=['Planilha3'])

planilha = sheet['Planilha3']

densidade = {
    17: 0.9988,
    18: 0.9986,
    19: 0.9984,
    20: 0.9982,
    21: 0.9980,
    22: 0.9978,
    23: 0.9976,
    24: 0.9973
}

qtde_pics = 35
lista_pics = []

temperatura = input("Digite a temperatura: ")

class PICS():
    def __init__(self, numero, peso):
        self.numero = numero
        self.peso = peso

for i in range(qtde_pics):
    lista_pics.append(planilha.iat[i, 0])

random.shuffle(lista_pics)

def calcular_mes(numero):
    peso_agua = round(planilha.loc[planilha['PIC'] == numero, 'PESO'], 2).array[0]
