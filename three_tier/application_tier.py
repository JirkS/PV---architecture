class TaskListApplication:

    def __init__(self):
        self._is_running = False
        self.database = None
        self.user_interface = None

    def run(self):
        self.user_interface.print_message("Vítejte v programu na evidenci úkolů!")
        self._is_running = True
        while self._is_running:
            command = self.user_interface.menu_input()
            command()

    def terminate(self):
        self._is_running = False
        self.user_interface.print_message("Program ukončen, nashledanou příště.")

    def show_task_list(self):
        task_list = self.database.get_task_list()
        self.user_interface.print_task_list(task_list)

    def add_task(self):
        new_task = self.user_interface.new_task_input()
        self.database.add_task(new_task)

    def remove_task_list(self):
        if self.confirm_remove() == "ano":
            self.database.remove_task_list()
            self.user_interface.print_message("Seznam ukolů byl smazán.")
        else:
            self.user_interface.print_message("Seznam ukolů nebyl smazán.")

    def show_first_task(self):
        task = self.database.get_first_task()
        self.user_interface.print_first_task(task)

    def remove_first_task(self):
        if self.confirm_remove() == "ano":
            self.database.remove_first_task()
            self.user_interface.print_message("Prvni ukol byl smazán.")
        else:
            self.user_interface.print_message("Prvni ukol nebyl smazán.")

    @classmethod
    def confirm_remove(cls):
        right_input = True
        sure = None
        while right_input:
            sure = input("Jste si jisty? ")
            try:
                sure = str(sure)
                if sure not in ["ano", "ne"]:
                    raise Exception()
                else:
                    right_input = False
            except Exception as e:
                print("Neplatné zadání musíte zadat \"ano\" nebo \"ne\".")
        return sure
