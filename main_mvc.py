from mvc.controller import TaskListController
from mvc.view import ConsoleView
from mvc.model import TaskListModel

if __name__ == "__main__":
    model = TaskListModel("task_list.txt","utf-8")
    view = ConsoleView(50)
    controller = TaskListController()

    view.model = model
    view.controller = controller

    controller.model = model
    controller.view = view

    controller.run()