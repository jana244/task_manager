import sys

def main(tasks):
    if tasks is None:
        tasks = []

    while True:
        print("1: Přidat nový úkol")
        print("2: Zobrazit všechny úkoly")
        print("3: Odstranit úkol")
        print("4: Konec programu")
        hodnota = input("Vyberte možnost (1-4): ")
        if hodnota == "4":
            print("Konec programu.")
            break  
        elif hodnota == "1":
            tasks= pridat_ukol(tasks)
            main(tasks)
        elif hodnota == "2":
            seznam_ukolu(tasks)
            print("")
            main(tasks)
        elif hodnota == "3":
            tasks= odstranit_ukol(tasks)
            main(tasks)
        else:
            print("mimo rozsah")
            main(tasks)
        sys.exit()

def pridat_ukol(tasks):
    print()
    task= input("Zadejte název úkolu: ")
    description= input("Zadejte popis úkolu: ")
    if task =="" or description =="":
        print("prázdné políčko")
        pridat_ukol(tasks)
    else:
        tasks.append(task + " - " + description)

    print("Úkol " + task + " byl přidán")
    print()
    return tasks

def seznam_ukolu(tasks):
    print()
    if len(tasks) == 0:
        print("Nejsou žádné úkoly")
        print()
        return
    print("Seznam úkolů: ")
    for i in range(len(tasks))  :
        print(str(i+1) + ". " + tasks[i])
    print()

def odstranit_ukol(tasks):
    if len(tasks) == 0:
        print("Nejsou žádné úkoly. Není co smazat.")
        print()
        return tasks

    seznam_ukolu(tasks)    
#    del_task=int(input("Zadejte číslo úkolu, které chcete odstranit: "))
    del_task=input("Zadejte číslo úkolu, které chcete odstranit: ")
    if not del_task.isdigit():
        print("špatně zadaný")
        return tasks
    if int(del_task) == 0:
        return tasks
    elif int(del_task) > len(tasks):
        print("mimo rozsah")
    else: 
        task = tasks[int(del_task)-1]
        print("Úkol " + task.split(" -")[0] + " byl odstraněn.")
        del tasks[int(del_task)-1]
    print()
    return tasks

tasks = []
main(tasks)