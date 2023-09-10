import PySimpleGUI

label1 = PySimpleGUI.Text("Enter feet:")
input1 = PySimpleGUI.InputText()

label2 = PySimpleGUI.Text("Enter inches:")
input2 = PySimpleGUI.InputText()

convert_button = PySimpleGUI.Button("Convert")

window = PySimpleGUI.Window("Convertor", layout=[[label1, input1], [label2,input2],[convert_button]])
window.read()

window.close()

