from aplication import Application

nadpis = r"""
 ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀  ▀▀▀▀█░█▀▀▀▀ ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌
▐░▌       ▐░▌▐░▌               ▐░▌     ▐░▌       ▐░▌▐░▌          ▐░▌          ▐░▌          ▐░▌       ▐░▌
▐░▌       ▐░▌▐░▌               ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌
▐░▌       ▐░▌▐░▌               ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░▌       ▐░▌▐░▌               ▐░▌      ▀▀▀▀█░█▀▀▀▀  ▀▀▀▀▀▀▀▀▀█░▌ ▀▀▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌
▐░▌       ▐░▌▐░▌               ▐░▌          ▐░▌               ▐░▌          ▐░▌▐░▌          ▐░▌       ▐░▌
▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄      ▐░▌          ▐░▌      ▄▄▄▄▄▄▄▄▄█░▌ ▄▄▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░▌       ▐░▌
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░▌          ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌
 ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀       ▀            ▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀ 
                                                                                                       
_  _ _  _ ____ ____ _  _ ____ ____    ___  ____ _ _    _   _    _  _ _  _ _ ____ _  _ ____ _  _ ____ ____ ____ 
|  | |\ | |    |  | |  | |___ |__/    |  \ |__| | |     \_/     |  | |\ | | |  | |  | |___ |\ | |___ [__  [__  
|__| | \| |___ |__|  \/  |___ |  \    |__/ |  | | |___   |      |__| | \| | |_\| |__| |___ | \| |___ ___] ___] 


The Octyssea app is like a good book;
it should have a place in the library of everyone who cares about their personal growth,
mental hygiene, or simply enjoys a touch of uniqueness on a daily basis.
"""


def main():
    app = Application()
    current_user = None
    print(nadpis)


    while True:

        if current_user is None:
            print("\n1. Registrace")
            print("2. Přihlášení")
            choice = input("Zvolte možnost: ")

            if choice == "1":
                # Registrace
                user_id = input("Zadejte uživatelské jméno: ")
                name = input("Zadejte jméno: ")
                password = input("Zadejte heslo: ")
                app.register(user_id, name, password)
                print("Registrace úspěšná!")

            elif choice == "2":
                # Přihlášení
                user_id = input("Zadejte uživatelské jméno: ")
                password = input("Zadejte heslo: ")
                if app.login_user(user_id, password):
                    current_user = app.find_user(user_id)
                    print("Přihlášení úspěšné!")
                else:
                    print("Neplatné uživatelské jméno nebo heslo.")

        else:
            # Toto je část pro přihlášeného uživatele
            print(f"\nPřihlášený uživatel: {current_user.name}")
            print("3. Výpis všech uživatelů a jejich bodů")
            print("4. Hledání uživatele podle jména nebo ID")
            print("5. Vlastní profil")
            print("0. Konec")
            choice = input("Zvolte možnost: ")

            if choice == "3":
                print("Výpis uzivatelov a score")
                # Výpis všech uživatelů a jejich bodů
                app.list_users_scores()

            elif choice == "4":
                # Hledání uživatele podle jména nebo ID
                search_term = input("Zadejte uživatelské jméno nebo ID: ")
                found_user = app.find_user(search_term)
                if found_user:
                    print(f"Uživatel: {found_user.name}, Skóre: {found_user.score}")
                else:
                    print("Uživatel nenalezen.")

            elif choice == "5":
                # Vlastní profil
                print(f"Jméno: {current_user.name}")
                print(f"Uživatelské ID: {current_user.user_id}")
                print(f"Skóre: {current_user.score}")

            elif choice == "0":
                print("Děkujeme za použití aplikace. Konec.")
                break

            else:
                print("Neplatná volba. Zadejte prosím znovu.")


if __name__ == "__main__":
    main()
