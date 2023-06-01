import PySimpleGUI as sg
from PySimpleGUI import Column, VSeparator
from omRelatorio import baixar_relatorios


sg.theme('SystemDefault')

layout_esquerdo = [
    [sg.Image('./assets/logo.png')]
]

layout_direito = [
    [sg.Push(), sg.Text('Insira os dados', font=("Helvetica", 10, "bold")), sg.Push()],
    [sg.Text('Usuário:'), sg.Push(),sg.Input(key='-USUARIO-')],
    [sg.Text('Senha:'), sg.Push(), sg.Input(key='-SENHA-', password_char='*')],
    [sg.Text('Insira o código das OS separada por "," :'), sg.Push(), sg.Input(key='-OS-')],
    [sg.Push(), sg.Button('Concluir', size=(10,1), button_color=('white', '#28478E'),border_width=0)]
]

layout = [
    [
        Column(layout_esquerdo),
        VSeparator(),
        Column(layout_direito)
    ]
]

window = sg.Window(
    'Download de relatorios de OM',
    layout=layout,
    element_justification='c',
    icon='./assets/icontelebras_resized.ico'
)

while True:
    evento, valores = window.read()

    if evento == sg.WINDOW_CLOSED:
        break
    elif evento == 'Concluir':
        baixar_relatorios(valores['-USUARIO-'], valores['-SENHA-'], valores['-OS-'])
        sg.popup('Finalizado', icon='./assets/icontelebras_resized.ico')
        break