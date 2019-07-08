enviroment = '''
_____________
Python Bank |
      $     |
------------|
            |
       o]   | {0} --- Normal People ---
            |
       o]   | {1} --- Pregnant People ---
            |
       o]   | {2} --- Old People ---
____________|
'''
line = []
lineold = []
linepregnant = []
people = 1

while True:
    welcome = (input("Welcome to python bank! To add someone to the line press 'A', to make the line walk, press 'W': ")).upper()
    if welcome == "W":
        if len(lineold) > 0:
            print("O cliente número {0} foi atendito".format(lineold[0]))
            lineold.pop(0)
        elif len(linepregnant) > 0:
            print("O cliente número {0} foi atendito".format(linepregnant[0]))
            linepregnant.pop(0)
        elif len(line) > 0:
            print("O cliente número {0} foi atendito".format(line[0]))
            line.pop(0)
    if welcome == "A":
        preference = int(input("If you have more than 59 years, press '0', if you are pregnant, press '1', else, press '2': "))
        if preference == 0:
            lineold.append(people)
            people += 1
        if preference == 1:
            linepregnant.append(people)
            people += 1
        if preference == 2:
            line.append(people)
            people += 1

    print(enviroment.format(line, linepregnant, lineold))
















