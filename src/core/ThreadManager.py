import threading


class ThreadManager(threading.Thread):
    def __init__(self, callback=None, data=None):
        super().__init__()
        self.daemon = True
        self.__result = None
        self.__callback = callback
        self.__data = data

    def run(self):
        assert isinstance(self.__data, list)
        if self.__callback:
            self.__result = self.__callback(*self.__data)

    def return_value(self):
        return self.__result
