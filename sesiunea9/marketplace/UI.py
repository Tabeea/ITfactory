# UI - User Interface
from sesiunea9.marketplace.marketplace_repository import CSVMarketPlaceRepository, JsonMarketPlaceRepository
from pprint import  pprint

def choose_db():
    db_menu = """
            DB MENU
            1. CSV
            2.JSON

    """
    print(db_menu)
    cmd = int(input("Enter the DB type: "))
    file_type = 'csv' if cmd == 1 else 'json'
    file_name = f'Users.{file_type}'
    return (
            CSVMarketPlaceRepository(file_name)
            if file_type == 'csv' else JsonMarketPlaceRepository(file_name)
        ), file_type


def print_menu():
    menu = """
            MENU
        1. Add user
        2. Delete user
        3. Show users
        4. Exit MENU        
    """
    print(menu)


def add_user(repository, repo_type):
    name = input('Please enter the user name: ')
    age = int(input('Please enter the user age: '))
    user_ID = hash(name) + hash(age)
    if repo_type == 'csv':
        repository.add([user_ID, name, age])
    else:
        repository.add({'ID': user_ID, 'name': name, 'age': age})


def detele_user(repository):
    user_ID = input('Enter the user ID to be deleted: ')
    repository.delete(user_ID)


def show_users(repository):
    pprint(repository.read())


def run():
    repo, repo_type = choose_db()
    while True:
        print('*' * 50)
        print_menu()
        user_input = int(input(f'Please enter your choise: '))
        if user_input == 1:
            add_user(repo, repo_type)
        elif user_input == 2:
            detele_user(repo)
        elif user_input == 3:
            show_users(repo)
        elif user_import == 4:
            exit(0)
        else:
            print('Comanda invalida !!!')


run()
