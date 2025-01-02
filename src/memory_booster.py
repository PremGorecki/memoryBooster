import os


def show_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('===============================')
    print('0 - Display')
    print('1 - Repeat')
    print('2 - Learn')
    print('3 - Add')
    print('4 - Train')
    print('7 - Load')
    print('8 - Save')
    print('9 - Exit')

    try:
        menu_option = int(input('Choose an option: '))
        return menu_option
    except ValueError:
        print('Invalid input. Please enter a number.')
        return None


if __name__ == "__main__":
    while True:
        menu_option = show_menu()
        match menu_option:
            case 0:
                pass
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 7:
                pass
            case 8:
                pass
            case 9:
                break

