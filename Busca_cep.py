import pycep_correios
from PySimpleGUI import PySimpleGUI as sg


sg.theme('DarkTeal6')
layout = [
    [sg.Text('Digite o CEP:')],
    [sg.Input(key='usuario',size=(20,1))],
    [sg.Button('Buscar')],
    [sg.Output(size=(20,9))]
]

janela = sg.Window('Busca com CEP', layout)

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Buscar':
        try:
            resultado = valores['usuario']
            cep = pycep_correios.get_address_from_cep(resultado)

            output = ''
            line1 = ('Cidade: {}').format(cep['cidade'])
            line2 = ('Endereço: {}').format(cep['logradouro'])
            line3 = ('Bairoo: {}').format(cep['bairro'])
            line4 = ('UF: {}').format(cep['uf'])
            line5 = ('CEP: {}').format(cep['cep'])
            output += line1
            print(line1)
            output += line2
            print(line2)
            output += line3
            print(line3)
            output += line4
            print(line4)
            output += line5
            print(line5)
            print("")
            
        except:

            output = ''
            line = "Cep não encontrado"
            output += line
            print(line)
            print("")
    
            
        



