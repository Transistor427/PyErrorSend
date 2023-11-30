import sys

from backup_log import BackupLog

path = [
    "/home/rock/klipper_logs/klippy.log",
    "/home/rock/klipper_config/printer.cfg"
]


def main():
    BL = BackupLog(path_files=path, serial='ZBS352517')
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
