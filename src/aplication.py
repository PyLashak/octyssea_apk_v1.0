from challenge import Challenge
from user import User
import csv
import random


class Application:

    def __init__(self):
        self.registered_users = []
        self.csv_filename = "users.csv"
        self.challenges_filename = "challenges.csv"

        # nacitanie registrovanych uzivatelov z CSV pri starte
        self.load_users_from_csv()

        # nacitanie vyziev z CSV pri starte
        self.load_challenges_from_csv()

    def load_users_from_csv(self):
        """
        Načíta užívatela z users.csv databáze.

        """
        try:
            with open(self.csv_filename, mode='r') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    user_id = row['user_id']
                    name = row['name']
                    password = row['password']
                    score = int(row['score'])

                    user = User(user_id, name, password)
                    user.score = score
                    self.registered_users.append(user)

        except FileNotFoundError:

            pass

    def save_users_to_csv(self):
        """
        Uloží registrovaného užívatela do users.csv databáze.

        """
        with open(self.csv_filename, mode='w', newline='') as file:
            fieldnames = ['user_id', 'name', 'password', 'score']
            csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
            csv_writer.writeheader()

            for user in self.registered_users:
                csv_writer.writerow({
                    'user_id': user.user_id,
                    'name': user.name,
                    'password': user.password,
                    'score': user.score
                })


    def load_challenges_from_csv(self):
        """
        Načíta výzvu z chalenges.csv databázi.

        """
        self.challenges = []
        try:
            with open(self.challenges_filename, mode='r', encoding='utf-8') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    challenge_id = int(row['id'])
                    description = row['description']
                    self.challenges.append(Challenge(challenge_id, description))
        except FileNotFoundError:
            print("Soubor s výzvami nebyl nalezen.")

    def assign_random_challenge(self):
        """
        Skontroluje prihlasenie užívatela a následne mu priradí náhodnú výzvu.

        """
        if hasattr(self, 'current_user'):
            user = self.current_user
            user.current_challenge = random.choice(self.challenges)
            print(f"Zadání nové výzvy: {user.current_challenge.description}")

            print("Potvrďte (1) nebo nepotvrďte (2) splnění výzvy: ")
            choice = input()
            if choice == "1":
                user.complete_challenge()
                print("Výzva byla dokončena.")
                user.current_challenge = None  # Aktuálna výzva je odstránená po dokončení.
            elif choice == "2":
                print("Výzva nebyla dokončena.")
        else:
            print("Nejste přiřazeni k žádné výzvě.")

# Registracia noveho uzivatela.
    def register(self, user_id, name, password):
        new_user = User(user_id, name, password)
        self.registered_users.append(new_user)
        self.save_users_to_csv()

# Prihlasenie do aplikacie.
    def login_user(self, user_id, password):
        for user in self.registered_users:
            if user.user_id == user_id and user.password == password:
                self.current_user = user
                self.assign_random_challenge()  # Při přihlášení přiřadíme novou výzvu

                return True
        return False

#Výpis užívatelov a ich score.
    def list_users_scores(self):
        for user in self.registered_users:
            print(f"Uživatel: {user.name}, Skóre: {user.score}")

#vyhľadá užívatela podla user_ID (user name).
    def find_user(self, search_term):
        for user in self.registered_users:
            if user.user_id == search_term or user.name == search_term:
                return user
        return None