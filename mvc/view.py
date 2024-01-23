class ConsoleView:

    def __init__(self, line_length):
        self.line_length = line_length
        self.controller = None
        self.model = None
        self.reset()

    def reset(self):
        self.show_menu_input = True
        self.show_message = False
        self.show_task_list = False
        self.show_first_task = False
        self.show_new_task_input = False
        self.message = None

    def print_line(self, symbol="="):
        print(symbol * self.line_length)

    def print_message(self):
        self.print_line()
        print(self.message)

    def print_task_list(self):
        self.print_line()
        print("Seznam úkolů:")
        i = 0
        for task in self.model.get_all():
            i += 1
            print("\t" + str(i) + ". " + task.strip())
        if i == 0:
            print("\t(žádné úkoly)")

    def print_first_task(self):
        self.print_line()
        task = self.model.get_first()
        if len(task) != 0:
            print("\t1. ukol: " + task)
        else:
            print("\t(žádné úkoly)")

    def new_task_input(self):
        self.print_line()
        new_task = None
        while new_task is None:
            new_task = input("Zadejte nový úkol: ").strip()
            if len(new_task) < 1:
                print("Neplatné zadání musíte zadat nějaký text")
                new_task = None
        action = self.controller.add_new_task
        action(new_task)

    def menu_input(self):
        actions = [
            ("Vypsat seznam", self.controller.show_task_list),
            ("Přidat na seznam", self.controller.show_new_task_input),
            ("Smazat celý seznam", self.controller.remove_task_list),
            ("Zobrazení pouze prvního úkolu", self.controller.show_first_task),
            ("Smazání pouze prvního úkolu", self.controller.remove_first_task),
            ("Ukončit program", self.controller.terminate),
        ]

        self.print_line()
        print("Vyberte příkaz:")
        num = 0
        for label,action in actions:
            num += 1
            print("\t" + str(num) + ". " + label)

        choosen_num = None
        while choosen_num is None:
            choosen_num = input("Zadejte číslo příkazu (1-"+str(len(actions))+"): ").strip()
            try:
                choosen_num = int(choosen_num)
                if not 0 < choosen_num <= len(actions):
                    raise Exception()
            except Exception as e:
                print("Neplatné zadání musíte zadat číslo mezi 1 až "+str(len(actions)))
                choosen_num = None
        action = actions[choosen_num-1][1]
        action()

    def update(self):
        if self.show_message is True:
            self.print_message()

        if self.show_task_list is True:
            self.print_task_list()

        if self.show_first_task is True:
            self.print_first_task()

        if self.show_new_task_input is True:
            self.new_task_input()

        if self.show_menu_input is True:
            self.menu_input()
