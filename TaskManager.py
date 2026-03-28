import sys

task_list = []

def main():

    while True:
        print("1: Přidat nový úkol")
        print("2: Zobrazit všechny úkoly")
        print("3: Odstranit úkol")
        print("4: Konec programu")
        choice = input("Vyberte možnost (1-4): ").strip()
        if choice == "4":
            print("Konec programu.")
            break
        elif choice == "1":
            add_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            remove_task()
        else:
            print("Chyba: Vybraná možnost není v nabídce. Zadejte číslo 1 až 4.")

def add_task():
    global task_list
    task_name = input("\nZadejte název úkolu: ")
    task_description = input("Zadejte popis úkolu: ")
    if task_name == "" and task_description == "":
        print("Chyba: Název úkolu ani popis nesmí být prázdný.")
        add_task()
    elif task_name == "":
        print("Chyba: Název úkolu nesmí být prázdný.")
        add_task()
    elif task_description == "":
        print("Chyba: Popis úkolu nesmí být prázdný.")
        add_task()
    else:
        task_list.append({"name": task_name, "description": task_description})
        print("Úkol " + task_name + " byl přidán\n")

def show_tasks():
    global task_list
    if len(task_list) == 0:
        print("\nNejsou žádné úkoly\n")
        return
    print("\nSeznam úkolů: ")
    for i in range(len(task_list)):
        print(str(i+1) + ". " + task_list[i]["name"] + " - " + task_list[i]["description"])
    print()

def remove_task():
    global task_list
    if len(task_list) == 0:
        print("Nejsou žádné úkoly. Není co smazat.\n")
        return

    show_tasks()
    task_to_delete = input("Zadejte číslo úkolu, které chcete odstranit: ")
    if not task_to_delete.isdigit():
        print("Chyba: Musíte zadat číslo úkolu, který chcete odstranit.")
        return
    if int(task_to_delete) == 0:
        return 
    elif int(task_to_delete) > len(task_list):
        print("Chyba: Zadané číslo úkolu neexistuje.")
    else:
        task = task_list[int(task_to_delete)-1]
        print("Úkol " + task["name"] + " byl odstraněn.")
        del task_list[int(task_to_delete)-1]
    print()

main()