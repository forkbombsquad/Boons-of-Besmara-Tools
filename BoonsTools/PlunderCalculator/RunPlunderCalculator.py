import PySimpleGUI as sg
import PlunderCalcConstants as c

settingsColumn = [
    [sg.Text("Player Level:"), sg.InputText(enable_events=True, key=c.PLAYER_LEVEL, size=(10, 20))],
    [sg.Text("Total Number of Shares:"), sg.InputText(enable_events=True, key=c.TOTAL_SHARES, size=(10, 20))],
    [sg.Text("Copper Plunder:"), sg.InputText(enable_events=True, key=c.COPPER_PLUNDER, size=(10, 20))],
    [sg.Text("Silver Plunder:"), sg.InputText(enable_events=True, key=c.SILVER_PLUNDER, size=(10, 20))],
    [sg.Text("Gold Plunder:"), sg.InputText(enable_events=True, key=c.GOLD_PLUNDER, size=(10, 20))],
    [sg.Text("Platinum Plunder:"), sg.InputText(enable_events=True, key=c.PLATINUM_PLUNDER, size=(10, 20))],
    [sg.Text(f"{c.PLUNDER_HAGGLING_DC_PT_1}{c.PLUNDER_HAGGLING_DC_UNKNOWN}", key=c.PLUNDER_RULES, pad=(8, 24))],
    [sg.Text(c.PERCENTAGE_RULES)],
    [sg.InputText(enable_events=True, key=c.PERCENTAGES)],
    [sg.Button("Calculate", key=c.CALCULATE_BUTTON)]
]

resultsColumn = [
    [sg.Text("Best Allocation of Percentages:")],
    [sg.Text("\n\n\n", key=c.PERCENTAGE_ALLOCATION_KEY)],
    [sg.Text(c.TOTAL_PROFIT, key=c.TOTAL_PROFIT_KEY)],
    [sg.Text(f"{c.PROFIT_PER_SHARE}\n", key=c.PROFIT_PER_SHARE_KEY)],
    [sg.Text(f"{c.P05}    ", key=c.P05KEY)],
    [sg.Text(f"{c.P075}    ", key=c.P075KEY)],
    [sg.Text(f"{c.P1}    ", key=c.P1KEY)],
    [sg.Text(f"{c.P11}    ", key=c.P11KEY)],
    [sg.Text(f"{c.P12}    ", key=c.P12KEY)],
    [sg.Text(f"{c.P125}    ", key=c.P125KEY)],
    [sg.Text(f"{c.P13}    ", key=c.P13KEY)],
    [sg.Text(f"{c.P14}    ", key=c.P14KEY)],
    [sg.Text(f"{c.P15}    ", key=c.P15KEY)],
    [sg.Text(f"{c.P16}    ", key=c.P16KEY)],
    [sg.Text(f"{c.P17}    ", key=c.P17KEY)],
    [sg.Text(f"{c.P175}    ", key=c.P175KEY)],
    [sg.Text(f"{c.P2}    ", key=c.P2KEY)],
    [sg.Text(f"{c.P3}    ", key=c.P3KEY)],
    [sg.Text(f"{c.P4}    ", key=c.P4KEY)],
    [sg.Text(f"{c.P5}    ", key=c.P5KEY)]
]

layout = [
    [
        sg.Column(settingsColumn),
        sg.VSeparator(),
        sg.Column(resultsColumn)
    ]
]

window = sg.Window(title="Plunder Calculator", layout=[layout])

# Create UI Loop

while True:
    event, values = window.read()
    # End if close window. Print if press button
    if event == sg.WINDOW_CLOSED:
        break
    if event == c.PLAYER_LEVEL:
        level = str(values[c.PLAYER_LEVEL])
        if level.isnumeric():
            levelInt = int(level)
            if levelInt >= 1 and levelInt <= 20:
                # Do calculations
                window[c.PLUNDER_RULES].update(f"{c.PLUNDER_HAGGLING_DC_PT_1}{c.LEVEL_BASED_DCS[levelInt - 1]}{c.PLUNDER_HAGGLING_DC_PT_2}")
            else:
                window[c.PLUNDER_RULES].update(
                    f"{c.PLUNDER_HAGGLING_DC_PT_1}{c.PLUNDER_HAGGLING_DC_UNKNOWN}")

    if event == c.CALCULATE_BUTTON:
        # Validate
        level = str(values[c.PLAYER_LEVEL])
        shares = str(values[c.TOTAL_SHARES])
        copper = str(values[c.COPPER_PLUNDER])
        silver = str(values[c.SILVER_PLUNDER])
        gold = str(values[c.GOLD_PLUNDER])
        plat = str(values[c.PLATINUM_PLUNDER])
        percentages = str(values[c.PERCENTAGES])

        levelInt = 0
        sharesFloat = 0.0
        copperInt = 0
        silverInt = 0
        goldInt = 0
        platInt = 0
        percentagesNumeric = []

        shouldContinue = True
        errors = ""

        if level.isnumeric():
            levelInt = int(level)
            if levelInt < 1 or levelInt > 20:
                shouldContinue = False
                errors += "Player Level must be a number between 1 and 20\n"
        else:
            errors += "Player Level must be a number between 1 and 20\n"
            shouldContinue = False

        if shares.replace(".", "").isnumeric() and (len(shares.split(".")) == 2 and shares.split(".")[1].isnumeric()) or (len(shares.split(".")) == 1 and shares.split(".")[0].isnumeric()):
            sharesFloat = float(shares)
        else:
            errors += "Shares must be numeric. You may include a decimal\n"
            shouldContinue = False

        if copper.isnumeric():
            copperInt = int(copper)
        else:
            errors += "Copper Plunder must be numeric\n"
            shouldContinue = False

        if silver.isnumeric():
            silverInt = int(silver)
        else:
            errors += "Silver Plunder must be numeric\n"
            shouldContinue = False

        if gold.isnumeric():
            goldInt = int(gold)
        else:
            errors += "Gold Plunder must be numeric\n"
            shouldContinue = False

        if plat.isnumeric():
            platInt = int(plat)
        else:
            errors += "Platinum Plunder must be numeric\n"
            shouldContinue = False

        percentagesSplit = percentages.replace(" ", "").split(",")
        if not (len(percentagesSplit) > 0 and percentagesSplit[0].isnumeric()):
            errors += "You must enter at least one percentage between 1 and 100\n"
            shouldContinue = False

        for per in percentagesSplit:
            if per.isnumeric():
                perInt = int(per)
                if perInt >= 1 and perInt <= 100:
                    percentagesNumeric.append(int(per))
                else:
                    errors += "All percentages must be integers between 1 and 100\n"
                    shouldContinue = False
                    break
            else:
                errors += "All percentages must be integers between 1 and 100\n"
                shouldContinue = False
                break


        if not shouldContinue:
            sg.popup_ok(errors, title="Validation Error(s)!")
        else:
            # Validation successful. Calculate plunders!
            arrayIndex = levelInt - 1

            while len(percentagesNumeric) < 4:
                percentagesNumeric.append(0)

            perSort = sorted(percentagesNumeric, key=int, reverse=True)

            topPercentages = [perSort[0], perSort[1], perSort[2], perSort[3]]
            bestOrientation = c._orientations[c.determineHighestTotal(copperInt, silverInt, goldInt, platInt, topPercentages, arrayIndex)]

            # Display Allocation Percentages
            copperP = topPercentages[bestOrientation[0]] + 100
            silverP = topPercentages[bestOrientation[1]] + 100
            goldP = topPercentages[bestOrientation[2]] + 100
            platP = topPercentages[bestOrientation[3]] + 100

            copperVal = c.toTwoDecimalPlaces(c.COPPER_PRICES[arrayIndex] * (copperP / 100.0) * copperInt)
            silverVal = c.toTwoDecimalPlaces(c.SILVER_PRICES[arrayIndex] * (silverP / 100.0) * silverInt)
            goldVal = c.toTwoDecimalPlaces(c.GOLD_PRICES[arrayIndex] * (goldP / 100.0) * goldInt)
            platVal = c.toTwoDecimalPlaces(c.PLAT_PRICES[arrayIndex] * (platP / 100.0) * platInt)

            totalProfit = c.toTwoDecimalPlaces(copperVal + silverVal + goldVal + platVal)

            window[c.PERCENTAGE_ALLOCATION_KEY].update(f"    Copper at {copperP}% = {copperVal}gp\n    Silver at {silverP}% = {silverVal}gp\n    Gold at {goldP}% = {goldVal}gp\n    Platinum at {platP}% = {platVal}gp")
            window[c.TOTAL_PROFIT_KEY].update(f"{c.TOTAL_PROFIT}{totalProfit}gp")

            # Price per share calculations
            profitPerShare = c.toTwoDecimalPlaces(totalProfit / sharesFloat)
            window[c.PROFIT_PER_SHARE_KEY].update(f"{c.PROFIT_PER_SHARE}{c.convertToGoldSilverCopper(profitPerShare)}")

            window[c.P05KEY].update(f"{c.P05}{c.convertToGoldSilverCopper(c.toTwoDecimalPlaces(profitPerShare * 0.5))}")
            window[c.P075KEY].update(f"{c.P075}{c.convertToGoldSilverCopper(c.toTwoDecimalPlaces(profitPerShare * 0.75))}")
            window[c.P1KEY].update(f"{c.P1}{c.convertToGoldSilverCopper(profitPerShare)}")
            window[c.P11KEY].update(f"{c.P11}{c.convertToGoldSilverCopper(c.toTwoDecimalPlaces(profitPerShare * 1.1))}")
            window[c.P12KEY].update(f"{c.P12}{c.convertToGoldSilverCopper(c.toTwoDecimalPlaces(profitPerShare * 1.2))}")
            window[c.P125KEY].update(f"{c.P125}{c.convertToGoldSilverCopper(c.toTwoDecimalPlaces(profitPerShare * 1.25))}")
            window[c.P13KEY].update(f"{c.P13}{c.convertToGoldSilverCopper(c.toTwoDecimalPlaces(profitPerShare * 1.3))}")
            window[c.P14KEY].update(f"{c.P14}{c.convertToGoldSilverCopper(c.toTwoDecimalPlaces(profitPerShare * 1.4))}")
            window[c.P15KEY].update(f"{c.P15}{c.convertToGoldSilverCopper(c.toTwoDecimalPlaces(profitPerShare * 1.5))}")
            window[c.P16KEY].update(f"{c.P16}{c.convertToGoldSilverCopper(c.toTwoDecimalPlaces(profitPerShare * 1.6))}")
            window[c.P17KEY].update(f"{c.P17}{c.convertToGoldSilverCopper(c.toTwoDecimalPlaces(profitPerShare * 1.7))}")
            window[c.P175KEY].update(f"{c.P175}{c.convertToGoldSilverCopper(c.toTwoDecimalPlaces(profitPerShare * 1.75))}")
            window[c.P2KEY].update(f"{c.P2}{c.convertToGoldSilverCopper(c.toTwoDecimalPlaces(profitPerShare * 2.0))}")
            window[c.P3KEY].update(f"{c.P3}{c.convertToGoldSilverCopper(c.toTwoDecimalPlaces(profitPerShare * 3.0))}")
            window[c.P4KEY].update(f"{c.P4}{c.convertToGoldSilverCopper(c.toTwoDecimalPlaces(profitPerShare * 4.0))}")
            window[c.P5KEY].update(f"{c.P5}{c.convertToGoldSilverCopper(c.toTwoDecimalPlaces(profitPerShare * 5.0))}")

window.close()