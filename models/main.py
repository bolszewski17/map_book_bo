from utils.crud import read


        users: list[dict] = [
            {"name": "Bartek", "surname": "Olszewski", "posts": 20},
            {"name": "Maciej", "surname": "Przybytek", "posts": 45},
            {"name": "Bartosz", "surname": "Pietrasik", "posts": 15},
            {"name": "Tymoteusz", "surname": "Miszczak", "posts": 30},
            {"name": "Mateusz", "surname": "Matysiak", "posts": 10},

        ]



        print(F"Witaj {users[0]['name']}!")
        while True:
            print("Menu:")
            print("0. Zakończ program")
            print("1. Pokaż co u znajomych: ")
            menu_option:str=input("Wybierz dostępną funkcję z menu: ")
            if menu_option == "0":
                break
            if menu_option == "1":
                read(users)
