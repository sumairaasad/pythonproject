import readFilms, addFilms,deleteFilms, updateFilms,searchReport


def read_file():
    try:
        with open("pythonproject/menuOptions.txt") as fileRead:
            fr = fileRead.read()
        return fr
    except FileNotFoundError as nf:
        print(f"Check {nf}")

def tblFilms_menu():
    option = 0
    optionsList = ["1","2","3","4","5"]

    menuChoices = read_file()

    while option not in optionsList:
        print(menuChoices)
        option = input("Enter an option from the Menu choice above: ")

        if option not in optionsList:
            print(f"{option} is not a valid choice!")

    return option

mainProgram = True

while mainProgram:
    mainMenu = tblFilms_menu()

    # Use if-elif-else instead of match for Python versions below 3.10
    if mainMenu == "1":
        readFilms.read_tblFilms()
    elif mainMenu == "2":
        addFilms.insert_tblFilms()
    elif mainMenu == "3":
        deleteFilms.delete_tblFilms()
    elif mainMenu == "4":
     updateFilms.update_tblFilms()
    elif mainMenu == "5":
     searchReport.search()
    else:
        mainProgram = False

