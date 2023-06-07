import data_manager, welcome_window

if __name__ == "__main__":
    #Dodaj ze jak juz utworzona to prosze spierdalac
    #data_manager.create_database()
    #welcome_window
    data_manager.get_tasks()
    print(data_manager.get_users())