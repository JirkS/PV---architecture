

class TaskListApplication():

    def __init__(self):
        self._is_running = False
        self.database = None
        self.user_interface = None

    def run(self):
        self.user_interface.print_message("Vítejte v programu na evidenci úkolů!")
        self._is_running = True
        while(self._is_running):
            command = self.user_interface.menu_input()
            command()

    def terminate(self):
        self._is_running = False
        self.user_interface.print_message("Program ukončen, nashledanou příště.")

    def show_task_list(self):
        task_list = self.database.get_task_list()
        self.user_interface.print_task_list( task_list)

    def add_task(self):
        new_task = self.user_interface.new_task_input()
        self.database.add_task(new_task)

    def remove_task_list(self):
        self.database.remove_task_list()
        self.user_interface.print_message("Seznam ukolů byl smazán.")