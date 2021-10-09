import os

class CreateData:
    def __init__(self, count = 100):
        self.count = count

    def run(self, save_path_dir):
        self._init_dir(save_path_dir = save_path_dir)


    def _init_dir(self, save_path_dir):
        if os.path.isdir(save_path_dir) == False:
            os.mkdir(save_path_dir)
