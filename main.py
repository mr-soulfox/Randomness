from modules.generator import Generator
from PySimpleGUI import PySimpleGUI as sg

if __name__ == '__main__':
    sg.theme('DarkBlue')

    layout = [
        [sg.Text('Repeat: ', size=(8, 1)), sg.Input(key='rpt', size=(30, 5))],
        [sg.Text('Maximum: ', size=(8, 1)), sg.Input(key='max', size=(30, 5))],
        [sg.Checkbox('With sum?', key='sum')],
        [sg.Button('Generate')]
    ]

    window = sg.Window('Randomness', layout, icon='assets/favicon.ico')

    while True:
        events, values = window.read()

        if events == sg.WINDOW_CLOSED:
            break

        if events == 'Generate':

            if values['rpt'].isnumeric() and values['max'].isnumeric():
                rpt = int(values['rpt'])
                num_max = int(values['max'])

                if rpt >= 50 and num_max >= 5:
                    Generator(rpt, num_max, values['sum'])

                else:
                    sg.Popup('At least 50 repetitions and 5 being maximum number', keep_on_top=True)

            else:
                sg.Popup('Incorrect values', keep_on_top=True)
