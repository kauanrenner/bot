import random
import pandas as pd

def bot_Umidade():
    lista = [212, 162, 171, 100, 81, 151, 511, 322, 517, 513, 516, 208, 425, 13, 197, 251, 21, 320, 506, 267, 923, 67, 502, 510, 509, 350, 18, 503, 104, 225, 115, 155, 235, 505, 512, 507, 517, 505, 276, 982, 511, 935, 267, 197, 259]
    taras = [26.71, 31.35, 20.5, 29.68, 29.79, 24.74, 30.6, 28.53, 26.69, 28.63, 13.8, 30.85, 24.68, 26.57, 28.7, 30.16, 31.51, 31.32, 13.41, 29.8, 30.54, 26.39, 12.83, 29.67, 14, 29.65, 23.79, 15.38, 29.55, 29.12, 13.62, 30.57, 15.48, 12.91, 26.11, 13.54, 26.67, 12.91, 29.67, 13.41, 30.60, 29.90, 29.80, 28.70, 30.75]

    sheet = pd.read_excel('CALIBRACAO PIC.xlsx',sheet_name=['Planilha3'])
    planilha = sheet['Planilha3']

    pics, pesos = [], []

    for i in range(35):
        pic, peso = planilha.iat[i, 0], planilha.iat[i, 1]
        pics.append(pic)
        pesos.append(round(peso, 2))

    densidade_agua = {
        '17': 0.9988,
        '18': 0.9986,
        '19': 0.9984,
        '20': 0.9982,
        '21': 0.9980,
        '22': 0.9978,
        '23': 0.9976,
        '24': 0.9973
    }

    temperatura = input("Digite a temperatura em número inteiro: ")

    class Pics:
        def __init__(self, numero, peso_agua, amumida):
            self.numero = numero
            self.peso_agua = peso_agua
            self.umida = amumida

    lista_pics = []
    for c in range(len(pics)):
        picnometro = Pics(pics[c], pesos[c], round(random.uniform(60, 60.10), 2))
        lista_pics.append(picnometro)

    class Capsulas:
        def __init__(self, numero, tara, peso_umido):
            self.numero = numero
            self.tara = tara
            self.peso_umido = peso_umido

    lista_cap = []
    for c in range(len(lista)):
        capsula = Capsulas(lista[c], taras[c], round(random.uniform(60,99.99), 2))
        lista_cap.append(capsula)

    random.shuffle(lista_cap)
    random.shuffle(lista_pics)
        
    lista_amostras = []
    amostras_pics = []

    for a in range(15):
        lista_amostras.append(list())
        amostras_pics.append(list())

    c = 0
    p = 0
    for i in range(15):
        while len(lista_amostras[i]) < 3:
            lista_amostras[i].append(lista_cap[c])
            c += 1
        while len(amostras_pics[i]) < 2:
            amostras_pics[i].append(lista_pics[p])
            p += 1

    def calc_peso_seco(amostra, picnometros_lista):
        a = amostra

        umidade_c1 = round(random.uniform(0.35, 1.90), 2)
        todas_umidades = [umidade_c1, round(umidade_c1 + random.uniform(-0.1, 0.1), 2), round(umidade_c1 + random.uniform(-0.06, 0.06), 2)]
        media_umidade = (todas_umidades[0] + todas_umidades[1] + todas_umidades[2]) / 3
        peso_seco_c1 = round((a[0].peso_umido - a[0].tara) / (1 + todas_umidades[0] / 100) + a[0].tara, 2)
        a[0].__setattr__("peso_seco", peso_seco_c1)
        peso_seco_c2 = round((a[1].peso_umido - a[1].tara) / (1 + todas_umidades[1] / 100) + a[1].tara, 2)
        a[1].__setattr__("peso_seco", peso_seco_c2)
        peso_seco_c3 = round((a[2].peso_umido - a[2].tara) / (1 + todas_umidades[2] / 100) + a[2].tara, 2)
        a[2].__setattr__("peso_seco", peso_seco_c3)
        am_seca1, am_seca2 = picnometros_lista[0].umida / (1 + media_umidade/100), picnometros_lista[1].umida / (1 + media_umidade/100)
        mes_media = round(random.uniform(3.030, 3.120), 3)
        mes1, mes2 = mes_media + random.uniform(-0.005, 0.005), mes_media + random.uniform(-0.005, 0.005)
        dens = densidade_agua[temperatura]
        vol1, vol2 = (am_seca1 * dens) / mes1, (am_seca2 * dens) / mes2
        peso_material1, peso_material2 = picnometros_lista[0].peso_agua + am_seca1 - vol1, picnometros_lista[1].peso_agua + am_seca2 - vol2
        picnometros_lista[0].__setattr__("peso_material", peso_material1)
        picnometros_lista[0].__setattr__("mes", mes1)
        picnometros_lista[1].__setattr__("peso_material", peso_material2)
        picnometros_lista[1].__setattr__("mes", mes2)

    for i in range(len(lista_amostras)):
        calc_peso_seco(lista_amostras[i], amostras_pics[i])
    
    c = 1
    for l in lista_amostras:
        print(f'Amostra {c}')
        for i in range(1):
            print(f'Cápsulas: {l[i].numero}  {l[i+1].numero}  {l[i+2].numero}')
            print(f'Peso Úmido: {l[i].peso_umido}  {l[i+1].peso_umido}  {l[i+2].peso_umido}')
            print(f'Peso Seco: {l[i].peso_seco}  {l[i+1].peso_seco}  {l[i+2].peso_seco}')
        c += 1
        print()
        print('----------------------------------')
        print()

    input('Pressione qualquer tecla para fechar: ')

if __name__ == '__main__':
    bot_Umidade()
