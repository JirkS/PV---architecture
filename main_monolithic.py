from monolithic.application import Application

if __name__ == "__main__":
    application = Application("task_list.txt","utf-8",50)
    application.run()