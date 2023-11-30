import sys

from backup_log import BackupLog

path = [
    "/run/media/vladislav/a4a3fb78-36b4-4827-8168-25f38beac446/"
    "Test_GUI/LEARNING_PYTHON/moonraker_upload_files_v1-2/files/klippy.log",
    "/run/media/vladislav/a4a3fb78-36b4-4827-8168-25f38beac446/"
    "Test_GUI/LEARNING_PYTHON/moonraker_upload_files_v1-2/files/printer.cfg"
]


def main():
    BL = BackupLog(path_files=path, serial='ZBS350001')
    BL.main()


if __name__ == '__main__':
    inp = str(input("Введите Yes или No: "))
    match inp:
        case "Yes":
            main()
        case "No":
            sys.exit(1)
        case _:
            print("Неизвестная команда!")

