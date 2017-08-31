from multiprocessing.pool import ThreadPool


class ThreadManager(ThreadPool):
    def __init__(self, callback=None, data=None):
        super().__init__()
        self.processes = 1
        self.__result = None
        assert isinstance(data, tuple)
        if callback:
            self.__result = self.apply_async(callback, data)

    def result(self):
        return self.__result.get()
