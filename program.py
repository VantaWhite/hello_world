from logger import Logger


class Program:
    @staticmethod
    def start():
        Logger.start_program()
        print("Hello world!")
        Logger.end_program()