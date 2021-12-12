# LED values: white, red, yellow, orange, green, blue, IR

# usage: ParseBOM <list with basic parts.csv> <EasyEDA-generated BOM.csv> <optional: crossing list>

import csv
import sys


def value_match(BOM, stock):
    if BOM[-1:] == "r":
        BOM = BOM[:-1]
    if stock[-1:] == "r":
        stock = stock[:-1]
    if BOM[-1:] == "f":
        BOM = BOM[:-1]
    if stock[-1:] == "f":
        stock = stock[:-1]
    if BOM.find(".0") > 0:
        BOM = BOM[:BOM.find(".0")] + BOM[BOM.find(".0") + 2:]
    if stock.find(".0") > 0:
        stock = stock[:stock.find(".0")] + stock[stock.find(".0") + 2:]
    if BOM == stock:
        return True
    else:
        return False


def use_part(line, basic_line):
    voltage = ""
    try:
        voltage = basic_line[14]
    except:
        pass
    line[8] = basic_line[0]  # copy LCSC part no.
    line[7] = "LCSC"
    line[6] = basic_line[6]  # manufacturer
    line[5] = basic_line[3]  # manufacturer part no.
    if not line[1][-6:] == " (mod)":
        line[1] = line[1] + " " + voltage + " (mod)"
    return line


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    try:
        filename_BP = sys.argv[1]
    except:
        print("1st argument missing: File name of CSV file with basic parts.")
        exit()
    try:
        with open(filename_BP, 'r', encoding="utf-8") as file:
            basic_csv = csv.reader(file, delimiter=',')
            basic_parts = []
            for index, line in enumerate(basic_csv):
                basic_parts.append(line)
        print(index, "basic parts found.")
    except:
        print("File doesn't exist: ", filename_BP)
        exit()

    try:
        filename_BOM = sys.argv[2]
    except:
        print("2nd argument missing: File name of CSV file with BOM.")
        exit()
    try:
        with open(filename_BOM, 'r', encoding="utf-16") as file:
            BOM_csv = csv.reader(file, delimiter='\t')
            BOM_parts = []
            for index, line in enumerate(BOM_csv):
                BOM_parts.append(line)
        print(index, "BOM parts found.")
    except:
        print("Can't open output file: ", filename_BOM)
        exit()

    try:
        with open(filename_BOM[0:-4] + "_modified.csv", 'w', encoding="utf-16") as file:
            BOMmod_csv = csv.writer(file, delimiter='\t')
    except:
        print("Can't open output file: ", filename_BOM[0:-4] + "_modified.csv")
        exit()

    try:
        filename_cross = sys.argv[3]
        with open(filename_cross, 'r', encoding="utf-8") as file:
            BOM_csv = csv.reader(file, delimiter=',')
            for index, line in enumerate(BOM_csv):
                if index == 0:
                    original_BOM_value = line
                if index == 1:
                    basic_replacement = line
    except:
        print("Information: No crossing list found or specified.")

    NumberOfMods = 0
    ExtendedParts = 0
    BasicParts = 0
    for index, line in enumerate(BOM_parts):
        for basic_index, basic_line in enumerate(basic_parts):
            try:
                if line[3] == basic_line[12]:  # footprints matching?
                    if value_match(line[1].lower(), basic_line[13].lower()):
                        line = use_part(line, basic_line)
                        NumberOfMods += 1
            except:
                pass
        try:
            if line[3].find("LED") != -1:  # LED?
                color = line[1].lower()  # definition: value = color
                if color in ['white', 'red', 'yellow', 'green', 'blue', 'orange', 'ir']:
                    footprint = "xyz"
                    if line[3].find("1206") != -1:  # LED?
                        footprint = "1206"
                    if line[3].find("0805") != -1:  # LED?
                        footprint = "0805"
                    if line[3].find("0603") != -1:  # LED?
                        footprint = "0603"
                    if line[3].find("0402") != -1:  # LED?
                        footprint = "0402"
                    if footprint != "xyz":
                        for basic_index, basic_line in enumerate(basic_parts):
                            basic_line[8] = basic_line[8].lower()
                            if basic_line[4] == "LED_" + footprint and basic_line[8].find(color) != -1:
                                line = use_part(line, basic_line)
                                NumberOfMods += 1
        except:
            pass

        for posi, token in enumerate(original_BOM_value):
            if line[1].find(token) != -1:  # part of crossing list?
                for basic_index, basic_line in enumerate(basic_parts):
                    if basic_line[3] == basic_replacement[posi]:
                        line = use_part(line, basic_line)
                        NumberOfMods += 1

        basic = False
        for basic_index, basic_line in enumerate(basic_parts):
            if line[5] == basic_line[3]:
                basic = True
        if basic:
            BasicParts += 1
        else:
            print("not basic:", line)
            ExtendedParts += 1
            if not line[1][-6:] == " (ext)":
                line[1] = line[1] + " (ext)"
        with open(filename_BOM[0:-4] + "_modified.csv", 'a', encoding="utf-8") as file:
            BOMmod_csv = csv.writer(file, delimiter='\t')
            BOMmod_csv.writerow(line)
#        if index % 10000 == 0:
    print(BasicParts, "basic parts - ", ExtendedParts, "extended parts - ", NumberOfMods, "parts modified.")