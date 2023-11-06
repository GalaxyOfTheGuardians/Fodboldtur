import pickle

filename = 'betalinger.pk'

fodboldtur = {}

def afslut():
    with open(filename, 'wb') as outfile:
        pickle.dump(fodboldtur, outfile)
    print("Programmet er afsluttet!")

def printliste():
    for spiller, belob in fodboldtur.items():
        print(f"{spiller}: {belob}")
    menu()


def indbetaling():
    saving_goal = 4500

    try:
        spiller = input("Hvem betaler? ")
        monthly_income = float(input("Indsæt det beløb der ønskes at blive indbetalt: "))

        if spiller in fodboldtur:
            fodboldtur[spiller] += monthly_income
        else:
            fodboldtur[spiller] = monthly_income

        remaining_amount = saving_goal - fodboldtur[spiller]

        if remaining_amount > 0:
            print(f"{spiller} mangler at indbetale {remaining_amount} kr ud af {saving_goal} kr.")
        else:
            print(f"{spiller} har indbetalt det hele. Tillykke!")

    except ValueError:
        print("Ugyldig indtastning. Indsæt et gyldigt beløb.")

    menu()

def menu():
    print("MENU")
    print("1: Print liste")
    print("2: Indbetal")
    print("3: Afslut program")
    valg = input("Indtast dit valg: ")
    if valg == '1':
        printliste()
    elif valg == '2':
        indbetaling()
    elif valg == '3':
        afslut()

    else:
        print("Ugyldigt valg. Prøv igen.")
        menu()

try:
    with open(filename, 'rb') as infile:
        fodboldtur = pickle.load(infile)
except FileNotFoundError:
    print(f'Filen "{filename}" blev ikke fundet. En ny fil er oprettet.')

menu()
