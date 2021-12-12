# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys


def uniroyalresistor(Value):
    if Value[-1:] == "L":
        return "0." + Value[:1] + "R"
    if Value[-1:] == "K":
        return Value[:1] + "." + Value[1:2] + "R"
    if Value[-1:] == "J":
        return Value[:2] + "R"
    if Value[-1:] == "0":
        return Value[:3] + "R"
    if Value[-1:] == "1":
        return Value[:1] + "." + Value[1:2] + "k"
    if Value[-1:] == "2":
        return Value[:2] + "k"
    if Value[-1:] == "3":
        return Value[:3] + "k"
    if Value[-1:] == "4":
        return Value[:1] + "." + Value[1:2] + "M"
    if Value[-1:] == "5":
        return Value[:2] + "M"
    print(Value)
    return Value


def capacitor(Value):
    if Value[1:2] == "R":
        return Value[:1] + "." + Value[2:3] + "p"
    if Value[-1:] == "0":
        return Value[:2] + "p"
    if Value[-1:] == "1":
        return Value[:2] + "0p"
    if Value[-1:] == "2":
        return Value[:1] + "." + Value[1:2] + "n"
    if Value[-1:] == "3":
        return Value[:2] + "n"
    if Value[-1:] == "4":
        return Value[:2] + "0n"
    if Value[-1:] == "5":
        return Value[:1] + "." + Value[1:2] + "u"
    if Value[-1:] == "6":
        return Value[:2] + "u"
    print(Value)
    return Value


def voltage(Value):
    if Value.find("2kV") > 0:
        return ",2kV"
    if Value.find("500V") > 0:
        return ",500V"
    if Value.find("100V") > 0:
        return ",100V"
    if Value.find("50V") > 0:
        return ",50V"
    if Value.find("25V") > 0:
        return ",25V"
    if Value.find("16V") > 0:
        return ",16V"
    if Value.find("10V") > 0:
        return ",10V"
    if Value.find("6.3V") > 0:
        return ",6.3V"
    return ""


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    try:
        filename_input = sys.argv[1]
    except:
        print("1st argument missing: File name of input CSV file")
        exit()
    input_csv = open(filename_input, "r", encoding="utf-8")
    try:
        input_csv = open(filename_input, "r", encoding="utf-8")
    except:
        print("File doesn't exist: ", filename_input)
        exit()
    try:
        output_csv = open(filename_input[0:-4] + "_BasicParts.csv", "w", encoding="utf-8")
    except:
        print("Can't open output file: ", filename_input[0:-4] + "_BasicParts.csv")
        exit()
    NumberOfBasicParts = 0
    for index, line in enumerate(input_csv):
        if line.find("Basic") > 0:
            if line.find("Uniroyal Elec") > 0:
                if line.find("1206W") > 0:  # UNI-ROYAL resistor
                    value = uniroyalresistor(line[line.find("1206W") + 7:line.find("1206W") + 11])
                    line = line[:-1] + ",R1206," + value + line[-1:]
                if line.find("0805W") > 0:  # UNI-ROYAL resistor
                    value = uniroyalresistor(line[line.find("0805W") + 7:line.find("0805W") + 11])
                    line = line[:-1] + ",R0805," + value + line[-1:]
                if line.find("0603W") > 0:  # UNI-ROYAL resistor
                    value = uniroyalresistor(line[line.find("0603W") + 7:line.find("0603W") + 11])
                    line = line[:-1] + ",R0603," + value + line[-1:]
                if line.find("0402W") > 0:  # UNI-ROYAL resistor
                    value = uniroyalresistor(line[line.find("0402W") + 7:line.find("0402W") + 11])
                    line = line[:-1] + ",R0402," + value + line[-1:]
            if line.find("Guangdong Fenghua Advanced Tech") > 0:
                if line.find("CG") > 0:
                    offset = 6
                else:
                    offset = 5
                if line.find("1206") > 0:
                    value = capacitor(line[line.find("1206") + offset:line.find("1206") + offset + 3])
                    line = line[:-1] + ",C1206," + value + voltage(line) + line[-1:]
                if line.find("0805") > 0:
                    value = capacitor(line[line.find("0805") + offset:line.find("0805") + offset + 3])
                    line = line[:-1] + ",C0805," + value + voltage(line) + line[-1:]
                if line.find("0603") > 0:
                    value = capacitor(line[line.find("0603") + offset:line.find("0603") + offset + 3])
                    line = line[:-1] + ",C0603," + value + voltage(line) + line[-1:]
                if line.find("0402") > 0:
                    value = capacitor(line[line.find("0402") + offset:line.find("0402") + offset + 3])
                    line = line[:-1] + ",C0402," + value + voltage(line) + line[-1:]
            if line.find("Samsung") > 0:
                offset = 5
                if line.find("CL31") > 0:
                    value = capacitor(line[line.find("CL31") + offset:line.find("CL31") + offset + 3])
                    line = line[:-1] + ",C1206," + value + voltage(line) + line[-1:]
                if line.find("CL21") > 0:
                    value = capacitor(line[line.find("CL21") + offset:line.find("CL21") + offset + 3])
                    line = line[:-1] + ",C0805," + value + voltage(line) + line[-1:]
                if line.find("CL10") > 0:
                    value = capacitor(line[line.find("CL10") + offset:line.find("CL10") + offset + 3])
                    line = line[:-1] + ",C0603," + value + voltage(line) + line[-1:]
                if line.find("CL05") > 0:
                    value = capacitor(line[line.find("CL05") + offset:line.find("CL05") + offset + 3])
                    line = line[:-1] + ",C0402," + value + voltage(line) + line[-1:]
            if line.find("CC0805KRX7R9BB104") > 0:
                line = line[:-1] + ",C0805,100n,50V" + line[-1:]
            if line.find("CC0603KRX7R9BB104") > 0:
                line = line[:-1] + ",C0603,100n,50V" + line[-1:]
            output_csv.writelines(line)
            NumberOfBasicParts += 1
        if index % 10000 == 0:
            print(index, " parts processed...")
    print(NumberOfBasicParts, " basic parts found.")
    input_csv.close()
    output_csv.close()
