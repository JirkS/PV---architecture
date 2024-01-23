class TaskListController:

    def __init__(self):
        self.model = None
        self.view = None

    def run(self):
        self.view.reset()
        self.view.message = "Vítejte v programu na evidenci úkolů!"
        self.view.show_message = True
        self.view.update()

    def terminate(self):
        self.view.reset()
        self.view.message = "Program ukončen, nashledanou příště."
        self.view.show_message = True
        self.view.show_menu_input = False
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
        if self.confirm_remove() == "ano":
            self.model.remove_first_task()
            self.view.reset()
            self.view.message = "Prvni ukol byl smazán."
        else:
            self.view.reset()
            self.view.message = "Prvni ukol ze seznamu ukolů nebyl smazán."
        self.view.show_message = True
        self.view.update()

    def remove_task_list(self):
        if self.confirm_remove() == "ano":
            self.model.remove_all()
            self.view.reset()
            self.view.message = "Seznam ukolu byl smazán."
        else:
            self.view.reset()
            self.view.message = "Ukoly nebyly ze seznamu smazány."
        self.view.show_message = True
        self.view.update()

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
