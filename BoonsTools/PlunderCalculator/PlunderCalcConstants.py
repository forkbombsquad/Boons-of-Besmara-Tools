WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 500

TOTAL_SHARES = "kTotalNumberOfShares-"
PLAYER_LEVEL = "kPlayerLevel-"
COPPER_PLUNDER = "kCopperPlunder-"
SILVER_PLUNDER = "kSilverPlunder-"
GOLD_PLUNDER = "kGoldPlunder-"
PLATINUM_PLUNDER = "kPlatinumPlunder-"
PERCENTAGES = "kPercentages-"

CALCULATE_BUTTON = "Calculate"

PLUNDER_RULES = "kPlunderRules-"
PLUNDER_HAGGLING_DC_PT_1 = "Plunder Haggling DC: "
PLUNDER_HAGGLING_DC_PT_2 = " (Use Deception, Diplomacy, Intimidate, Performance, or Lore Piracy)\n    Critical Success: +2d% to dicepool\n    Success: +1d% to your dicepool\n    Failure: no effect\n    Critical Failure: remove one d% from your dicepool (must have a minim of 1d%)"
PLUNDER_HAGGLING_DC_UNKNOWN = "Unknown. Please Set Player Level to be a number between 1-20."

PERCENTAGE_RULES = "Enter Haggling Percentages Below (Comma Separated):\nexample: 12, 59, 4, 99, 100"

PERCENTAGE_ALLOCATION_KEY = "kPercentageAllocation-"

TOTAL_PROFIT = "Total Profit: "
TOTAL_PROFIT_KEY = "kTotalProfit-"

# Shares
PROFIT_PER_SHARE = "Profit Per Share: "
PROFIT_PER_SHARE_KEY = "kPPS-"

P05 = "    0.5 Shares: "
P05KEY = "k05-"

P075 = "    0.75 Shares: "
P075KEY = "k75-"

P1 = "    1 Share: "
P1KEY = "k1-"

P11 = "    1.1 Shares: "
P11KEY = "k11-"

P12 = "    1.2 Shares: "
P12KEY = "k12-"

P125 = "    1.25 Shares: "
P125KEY = "k125-"

P13 = "    1.3 Shares: "
P13KEY = "k13-"

P14 = "    1.4 Shares: "
P14KEY = "k14-"

P15 = "    1.5 Shares: "
P15KEY = "k15-"

P16 = "    1.6 Shares: "
P16KEY = "k16-"

P17 = "    1.7 Shares: "
P17KEY = "k17-"

P175 = "    1.75 Shares: "
P175KEY = "k175-"

P2 = "    2 Shares: "
P2KEY = "k2-"

P3 = "    3 Shares: "
P3KEY = "k3-"

P4 = "    4 Shares: "
P4KEY = "k4-"

P5 = "    5 Shares: "
P5KEY = "k5-"


LEVEL_BASED_DCS = [15, 16, 18, 19, 20, 22, 23, 24, 26, 27, 28, 30, 31, 32, 34, 35, 36, 38, 39, 40]

COPPER_PRICES = [
    10, 20, 40, 70, 100, 150, 220, 300, 430, 600, 870, 1300, 1900, 2800, 4100, 6200, 9600, 16000, 30000, 40000
]
SILVER_PRICES = [
    20, 30, 50, 90, 140, 200, 290, 400, 570, 800, 1200, 1700, 2500, 3700, 5500, 8300, 13000, 21000, 40000, 50000
]
GOLD_PRICES = [
    30, 50, 80, 130, 200, 300, 440, 600, 860, 1200, 1700, 2500, 3800, 5500, 8200, 12000, 19000, 31000, 55000, 75000
]
PLAT_PRICES = [
    50, 80, 130, 220, 350, 520, 750, 1000, 1500, 2000, 3000, 4300, 6500, 9500, 14000, 21000, 33000, 54000, 92000, 130000
]

_orientations = [
    # Zeroes
    [0, 1, 2, 3],
    [0, 1, 3, 2],
    [0, 2, 1, 3],
    [0, 2, 3, 1],
    [0, 3, 1, 2],
    [0, 3, 2, 1],
    # Ones
    [1, 0, 2, 3],
    [1, 0, 3, 2],
    [1, 2, 0, 3],
    [1, 2, 3, 0],
    [1, 3, 0, 2],
    [1, 3, 2, 0],
    # Twos
    [2, 0, 1, 3],
    [2, 0, 3, 1],
    [2, 1, 0, 3],
    [2, 1, 3, 0],
    [2, 3, 0, 1],
    [2, 3, 1, 0],
    # Threes
    [3, 0, 1, 2],
    [3, 0, 2, 1],
    [3, 1, 0, 2],
    [3, 1, 2, 0],
    [3, 2, 0, 1],
    [3, 2, 1, 0]
]

def determineHighestTotal(copper, silver, gold, plat, percentages, index):
    bestOrientationIndex = 0
    bestTotal = 0
    for orientationIndex in range(len(_orientations)):
        orient = _orientations[orientationIndex]
        cPercent = (percentages[orient[0]] / 100.0) + 1.0
        sPercent = (percentages[orient[1]] / 100.0) + 1.0
        gPercent = (percentages[orient[2]] / 100.0) + 1.0
        pPercent = (percentages[orient[3]] / 100.0) + 1.0

        cTotal = copper * cPercent * COPPER_PRICES[index]
        sTotal = silver * sPercent * SILVER_PRICES[index]
        gTotal = gold * gPercent * GOLD_PRICES[index]
        pTotal = plat * pPercent * PLAT_PRICES[index]

        total = cTotal + sTotal + gTotal + pTotal
        if total > bestTotal:
            bestOrientationIndex = orientationIndex
            bestTotal = total

    return bestOrientationIndex

def toTwoDecimalPlaces(num):
    return float(int(num * 100.0)) / 100.0

def convertToGoldSilverCopper(num):
    c = int(num * 100.0) % 10
    s = int(num * 10.0) % 10
    g = int(num)

    return f"{g}gp {s}sp {c}cp"