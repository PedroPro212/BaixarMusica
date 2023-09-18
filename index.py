from PySimpleGUI import PySimpleGUI as sg
from classes.classBaixar import Baixar;

sg.theme('Reddit')

layout = [
    [sg.Text('Url:'), sg.Input(key='url')],
    [sg.Checkbox('Audio', key='audio'), sg.Checkbox('Video', key='video')],
    [sg.Button('Baixar')]
]

janela = sg.Window('Baixar Músicas', layout)

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break   
    if eventos == 'Baixar':
        baixar = Baixar(valores['url'])
        baixar.download()
        print('Baixado com Sucesso!!')
        janela['url'].update('')