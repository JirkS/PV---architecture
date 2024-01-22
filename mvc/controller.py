class TaskListController():

    def __init__(self):
        self.model = None
        self.view = None

    def run(self):
        self.view.reset()
        self.view.message = "Vítejte v programu na evidenci úkolů!";
        self.view.show_message = True
        self.view.update()

    def terminate(self):
        self.view.reset()
        self.view.message = "Program ukončen, nashledanou příště."
        self.view.show_message = True
        self.view.show_menu_input = False;
        self.view.update()

    def show_new_task_input(self):
        self.view.reset()
        self.view.show_new_task_input = True
        self.view.show_menu_input = False
        self.view.update()

    def add_new_task(self, new_task):
        self.model.add(new_task)
        self.view.reset()
        self.view.update()

    def show_task_list(self):
        self.view.reset()
        self.view.show_task_list = True
        self.view.update()

    def show_first_task(self):
        self.view.reset()
        self.view.show_first_task = True
        self.view.update()

    def remove_first_task(self):
        pass

    def remove_task_list(self):
        self.model.remove_all()

        self.view.reset()
        self.view.message = "Seznam ukolu byl smazán."
        self.view.show_message = True
        self.view.update()
