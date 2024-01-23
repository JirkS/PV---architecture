import os


class FileDatabase:
    def __init__(self, file_path, file_encoding):
        self.file_path = file_path
        self.file_encoding = file_encoding
        self.application = None

    def get_task_list(self):
        task_list = list()
        if os.path.exists(self.file_path):
            with open(self.file_path, "r", encoding=self.file_encoding) as f:
                task_list = f.readlines()
        return task_list

    def add_task(self, new_task):
        if os.path.exists(self.file_path):
            mode = "a"
        else:
            mode = "w"
        with open(self.file_path, mode, encoding=self.file_encoding) as f:
            f.write(new_task + "\r")
            f.flush()

    def remove_task_list(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def get_first_task(self):
        task = ""
        if os.path.exists(self.file_path):
            with open(self.file_path, "r", encoding=self.file_encoding) as f:
                task = f.readline()
        return task

    def remove_first_task(self):
        lines = []
        if os.path.exists(self.file_path):
            with open(self.file_path, "r", encoding=self.file_encoding) as f:
                lines = f.readlines()

        if os.path.exists(self.file_path):
            with open(self.file_path, "w", encoding=self.file_encoding) as f:
                for number, line in enumerate(lines):
                    if number not in [0]:
                        f.write(line)
