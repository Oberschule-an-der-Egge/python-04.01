def main():
    print_title()
    run_event_loop()


def print_title():
    """
    Zeigt den Titel der App.
    """
    print('--------------------------------------------')
    print('                TODO-LISTE')
    print('--------------------------------------------')
    print()


def run_event_loop():
    """
    Eingabeschleife, in der die Befehle Anzeigen, Hinzufügen, Löschen und Beenden aufgerufen werden.
    todo_liste wird hier erzeugt.
    """

    cmd_anzeigen = ['a', 'A']
    cmd_hinzufuegen = ['h', 'H']
    cmd_loeschen = ['l', 'L']
    cmd_beenden = ['e', 'E']

    todo_liste = []

    print('Willkommen in deiner TODO-Liste! Was möchtest du tun?')

    while True:
        selection = input('Einträge [A]nzeigen, [H]inzufügen, [L]öschen oder B[e]enden? ')

        if selection in cmd_anzeigen:
            present(todo_liste)
        elif selection in cmd_hinzufuegen:
            add(todo_liste)
        elif selection in cmd_loeschen:
            remove(todo_liste)
        elif selection in cmd_beenden:
            print()
            print('Tschüss!')
            break
        else:
            print('Ungültige Eingabe.')


def present(todo_liste):
    """
    Zeigt, in nummerierter Reihenfolge, die Einträge der aktuellen Liste.
    :param todo_liste: Benötigt das aktuelle list()-Objekt.
    """

    print()
    print(f'Du hast {len(todo_liste)} Einträge auf der Liste.')
    for index, item in enumerate(todo_liste):
        print(f'{index} - {item}')


def add(todo_liste):
    """
    Fügt der Liste einen neuen Eintrag hinzu.
    :param todo_liste: Benötigt das aktuelle list()-Objekt.
    """

    entry = input('Neuer Eintrag: ')
    todo_liste.append(entry)
    print(f'{entry} wurde hinzugefügt.')


def remove(todo_liste):
    """
    Löscht einen vom Nutzer gewählten Eintrag aus der Liste.
    :param todo_liste: Benötigt das aktuelle list()-Objekt.
    """

    for index, item in enumerate(todo_liste):
        print(f'{index} - {item}')
    item_index = int(input('Was soll gelöscht werden? '))
    todo_liste.pop(item_index)
    print(f'{item_index} wurde gelöscht.')


main()