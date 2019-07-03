line = []
linepregnant = []
lineold = []
people = 0
aux = 0
longest = 1
environment = '''
______________________
|     PythonBank     |
|____________________|
'''
message = int(input("To add someone in the line, press 1, to make the line walk, press 0: "))
if message == 1:
    preference = int(input("If you have more than 59 years, press 2, if you are pregnant, press 3, else, press 4: "))
    while True:
        if preference == 4: # Colocando não preferenciais na fila
                people += 1
                line.append(people)
                x = len(line)
                y = len(lineold)
                z = len(linepregnant)
                longest = max(x, y, z)
                while aux < longest:
                    print(environment)
                    if len(line) >= aux:
                        print("\t", (line[aux]))
                    if len(linepregnant) >= aux:
                        print("\t \t", (linepregnant[aux]))
                    if len(lineold) >= aux:
                        print("\t \t \t", (lineold[aux]))
                    aux += 1
        if preference == 3: # Colocando grávidas na fila
                people += 1
                linepregnant.append(people)
                x = len(line)
                y = len(lineold)
                z = len(linepregnant)
                while aux < longest:
                    print(environment)
                    if len(line) >= aux:
                        print("\t", (line[aux]))
                    if len(linepregnant) >= aux:
                        print("\t \t", (linepregnant[aux]))
                    if len(lineold) >= aux:
                        print("\t \t \t", (lineold[aux]))
                    aux += 1
        if preference == 2: # Colocando idosos na fila
                people += 1
                lineold.append(people)
                x = len(line)
                y = len(lineold)
                z = len(linepregnant)
                while aux < longest:
                    print(environment)
                    if len(line) >= aux:
                        print("\t", (line[aux]))
                    if len(linepregnant) >= aux:
                        print("\t \t", (linepregnant[aux]))
                    if len(lineold) >= aux:
                        print("\t \t \t", (lineold[aux]))
                    aux += 1
        message = int(input("To add someone in the line, press 1, to make the line walk, press 0: "))
        aux = 0
        if message == 1:
            preference = int(input("If you have more than 59 years, press 2, if you are pregnant, press 3, else, press 4: "))
















