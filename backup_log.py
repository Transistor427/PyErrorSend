import os
import shutil
from datetime import datetime
from os.path import splitext, basename


class BackupLog:
    """Класс для создания копии логов с добавлением серийного номера и текущей даты без привязки к количеству файлов

    Принимаемые аргументы:
        1) path_files : list - список с абсолютными путями до файлов, которые необходимо скопировать
        2) serial : str - серийный номер принтера (задается вручную для каждого принтера, например ZBS358901)
        3) end_path : str - путь до директории, куда будут сохраняться файлы
    """

    def __init__(self, path_files: list, serial: str = "ZBS352517", end_path: str = f"{os.getcwd()}/"):
        self.path_files = path_files
        self.modify_path_files = []
        self.serial = serial
        self.end_path = end_path

    def __str__(self):
        return "Класс для создания копии логов с добавлением серийного номера и " \
               "текущей даты без привязки к количеству файлов"

    @staticmethod
    def cur_time():
        """Метод для получения текущей даты и времени"""

        return datetime.now().strftime('_%d-%m-%Y_%H:%M:%S')

    def check_files(self):
        """Метод проверки существования файлов методом перебора в цикле всех путей до файлов
         и проверки их на доступность. Если путь не верный, то удаляет его из исходного списка."""

        try:
            for check_path in self.path_files:
                if not os.path.isfile(check_path):
                    self.path_files.remove(check_path)
            return True
        except Exception as ex:
            return ex

    def serial_dir(self) -> str:
        """Метод для создания директории с серийным номером"""

        data_serial = f"data_{self.serial}/"
        try:
            if not os.path.exists(data_serial):
                os.mkdir(data_serial)
            return data_serial
        except Exception as ex:
            return f"{ex}"

    def renaming_files(self):
        """Метод переименования файлов и запись новых путей до них в новый список путем """

        try:
            for name in self.path_files:
                filename, extension = splitext(basename(name))
                self.modify_path_files.append(self.end_path + self.serial_dir() + filename + "_" + self.serial +
                                              self.cur_time() + extension)
            return self.modify_path_files
        except Exception as ex:
            return ex

    def copy_files(self):
        """Метод копирования файлов в директорию с серийным номером и измененным названием"""

        try:
            index = 0
            for file in self.path_files:
                modify_file = self.modify_path_files[index]
                shutil.copy2(src=file, dst=modify_file, follow_symlinks=True)
                index += 1
        except Exception as ex:
            return ex

    def main(self):
        self.check_files()
        self.renaming_files()
        self.copy_files()


if __name__ == '__main__':
    path = [
        "/home/rock/klipper_logs/klippy.log",
        "/home/rock/klipper_config/printer.cfg"
    ]
    BackupLog(path_files=path).main()
