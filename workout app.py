import csv


dodawanie = True
filename = None
headers = ["grupa mięśni", "ćwiczenie", "ilość powtórzeń", "przerwa po ćwiczeniu"]
data = []


def add_workout():
    ret0 = input("Podaj numer treningu. ").lower()
    ret1 = input("Podaj ilość serii. ").lower()
    return ret0, ret1


def add_exc():
    last = input("Czy chcesz dodać ćwiczenie? (tak/nie) ").lower()
    if last == "tak":
        ret0 = input("Podaj grupę mięśni. ").lower()
        ret1 = input("Podaj nazwę ćwiczenia. ").lower()
        ret2 = input("Podaj ilość powtórzeń w jednej serii. ").lower()
        ret3 = input("Podaj przerwę po ćwiczeniu. [sekundy] ").lower()
        data_append = [ret0, ret1, ret2, ret3]
        return data_append
    elif last == "nie":
        return None


def writer(file_name, trening_number, set_caounts, row_headers, row_data):
    trn_num = ["---", "Trening " + str(trening_number), "---"]
    set_num = ["---", "Ilość serii: " + str(set_caounts), "---"]
    with open(file_name, "w", newline='') as csvfile:
        pisarz = csv.writer(csvfile, delimiter='\t')
        pisarz.writerow(trn_num)
        pisarz.writerow(set_num)
        pisarz.writerow(row_headers)
        for x in row_data:
            pisarz.writerow(x)
    csvfile.close()
    pass


def reader(file_name):
    taken_data = []
    with open(file_name, 'r', newline='') as csvfile:
        czytacz = csv.reader(csvfile, delimiter='\t')
        for x in czytacz:
            taken_data.append(x)
    csvfile.close()
    return taken_data


def show(file_name):
    with open(file_name, 'r', newline='') as csvfile:
        czytacz = csv.reader(csvfile, delimiter='\t')
        for x in czytacz:
            print(x)
    csvfile.close()
    pass


# właściwy program
work = True
while work is True:
    print("************************")
    print("Lista zadań:")
    print("1.Nowy plik.")
    print("2.Wybierz plik do obsługi.")
    print("3.Pokaż trening.")
    print("4.Dodaj trening.")
    print("5.Zamknij program.")
    answer = input("Podaj numer zadania. ")
    if answer == "1":
        ans = input("Podaj nazwę nowego pliku. ")
        ans += ".csv"
        filename = ans
        with open(filename, 'w', newline='') as f:
            f.close()
    elif answer == "2":
        ans = input("Podaj nazwę pliku do obsługi. ")
        ans += ".csv"
        filename = ans
        print("wybrano plik: ", filename)
    elif answer == "3":
        show(filename)
    elif answer == "4":
        d = reader(filename)
        results = add_workout()
        while dodawanie is True:
            res = add_exc()
            if res is None:
                dodawanie = False
            else:
                d.append(res)
        if dodawanie is False:
            writer(filename, results[0], results[1], headers, d)
    elif answer == "5":
        work = False
