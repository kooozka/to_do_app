
import welcome_window

if __name__ == "__main__":
    import sys, os, logic.data_manager as data_manager
    db_name = data_manager.DatabaseConfig.DATABASE_NAME
    if not os.path.exists(f"/home/student/Dokumenty/to_do_app/{db_name}"):
        data_manager.create_database()
    welcome_window.Ui_MainWindow.run()