

class Logger:
    @staticmethod
    def start_program() -> None:
        with open("log/log.txt", "a") as log_file:
            log_file.write("program started success\n")

    @staticmethod
    def end_program() -> None:
        with open("log/log.txt", "a") as log_file:
            log_file.write("program ended success\n")