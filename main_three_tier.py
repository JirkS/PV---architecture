from three_tier.user_interface_tier import ConsoleUserInterface
from three_tier.database_tier import FileDatabase
from three_tier.application_tier import TaskListApplication

if __name__ == "__main__":
    application = TaskListApplication()

    db = FileDatabase("task_list.txt", "utf-8");
    db.application = application
    application.database = db

    ui = ConsoleUserInterface(50);
    ui.application = application
    application.user_interface = ui

    application.run()