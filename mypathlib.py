import os

class Path:
    def __init__(self, path):
        self.path = path

    def showpath(self):
        return self.path

    def nest(self, nest):
        if self.path.endswith('/'):
            fullpath = self.path + nest
        else:
            fullpath = self.path + '/' + nest
        return Path(fullpath)

    def write_str(self, string):
        sliced = self.path.split('/')
        dirs = self.path.removesuffix('/'+sliced[-1])
        if os.path.exists(dirs):
            with open(self.path, 'w') as f:
                f.write(string)
        else:
            os.makedirs(dirs)
            with open(self.path, 'w') as f:
                f.write(string)

    def read_str(self):
        with open(self.path, 'r') as f:
            return f.readline()

    def name(self):
        slices = self.path.split('/')
        return slices[-1]

    def parent(self):
        sliced = self.path.split('/')
        return self.path.removesuffix('/'+sliced[-1])









