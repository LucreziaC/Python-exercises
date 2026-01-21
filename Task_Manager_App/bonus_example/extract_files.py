import FreeSimpleGUI as sg
import zip_handler as zh 

label1 = sg.Text("Select archive")
input1 = sg.Input()
choose_button1  = sg.FileBrowse("Choose", key='archive')

label2  = sg.Text("Select destination folder")
input2 = sg.Input()
choose_button2  = sg.FolderBrowse("Choose", key='folder')

extract_button = sg.Button("Extract")
output = sg.Text(key='output', text_color='green')

window = sg.Window("Archive Extractor", layout=[
    [label1, input1, choose_button1], 
    [label2, input2, choose_button2], 
    [extract_button, output]
    ])


while True:
    event, values = window.read()
    print(event, values)
    archive = values['archive']
    folder = values['folder']
    zh.extract_archive(archive, folder)
    window['output'].update(value="Extraction completed!")
    
#window.read()
window.close()
