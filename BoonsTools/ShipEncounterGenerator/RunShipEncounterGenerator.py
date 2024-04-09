import PySimpleGUI as sg
import ShipEncounterConstants as c

from PySimpleGUI import Push as Spacer

titleFont = ("Arial", 24, "bold", "underline")
textFont = ("Arial", 20)

playerSettingsColumn = [
    [sg.Text("Player Information", font=titleFont)],
    [sg.Text("Player Level", font=textFont), Spacer(), sg.Combo(c.PLAYER_LEVEL_OPTIONS, font=textFont, readonly=True, default_value=1)],
    [sg.Text("Number of Players", font=textFont), Spacer(), sg.Combo(c.PLAYER_COUNT_OPTIONS, font=textFont, readonly=True, default_value=5)],
]

enemyTweaksColumn = [
    [sg.Text("Enemy Tweakables", font=titleFont)]
]

topLayout = [
    [
        sg.Column(playerSettingsColumn),
        sg.VSeparator(),
        sg.Column(enemyTweaksColumn)
    ]
]

layout = [
    [topLayout],
    [sg.HSeparator()],
    [Spacer(), sg.Button("Generate", font=("Arial", 20, "bold")), Spacer()]
]

window = sg.Window(title="Ship Encounter Generator", layout=[layout])

while True:
    event, values = window.read()
    # End if close window. Print if press button
    if event == sg.WINDOW_CLOSED:
        break

window.close()