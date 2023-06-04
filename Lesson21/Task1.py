import sys
from loguru import logger


class CustomFile:
    open_files = dict()

    def __init__(self, filepath, mode='r'):
        self.filepath = filepath
        self.mode = mode
        self.file = None

    def __enter__(self):
        try:
            self.file = open(self.filepath, self.mode)
            CustomFile.open_files[self.filepath] = CustomFile.open_files.get(self.filepath, 0) + 1
            logger.info(f"Відкрито {self.filepath}. Загально відкрито: {CustomFile.open_files[self.filepath]}")
            return self.file
        except Exception as e:
            logger.error(f"Помилка під час відкриття файлу: {e}")
            raise e

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file and not self.file.closed:
            self.file.close()
            logger.info(f"Файл {self.filepath} закрито.")
        if exc_type or exc_val or exc_tb:
            logger.error(f"Помилка під час відкриття файлу: {exc_type} {exc_val} {exc_tb}")
            return False
        return True


logger.add(sys.stderr, format="{time} {level} {message}", level="INFO")

with CustomFile("my_file.txt") as f:
    content = f.read()
