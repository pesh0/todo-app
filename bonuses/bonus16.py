import PySimpleGUI
from zip_creator import make_archive

label1 = PySimpleGUI.Text("Enter feet:")
input1 = PySimpleGUI.InputText()
choose_button1 = PySimpleGUI.FilesBrowse("Choose", key = "files")

label2 = PySimpleGUI.Text("Enter inches:")
input2 = PySimpleGUI.InputText()
choose_button2 = PySimpleGUI.FolderBrowse("Choose", key="folder")

convert_button = PySimpleGUI.Button("Convert")
output_laybel = PySimpleGUI.Text("", key="output",
                                 text_color="green")

window = PySimpleGUI.Window("Convertor", layout=[[label1, input1, choose_button1],
                                                 [label2, input2, choose_button2],
                                                 [convert_button, output_laybel]])

while True:
    event, values = window.read()
    filepaths = values["files"].split(";")
    folder = values["folder"]

    make_archive(filepaths, folder)
    window["output"].update(value= "Compression completed")

window.close()
