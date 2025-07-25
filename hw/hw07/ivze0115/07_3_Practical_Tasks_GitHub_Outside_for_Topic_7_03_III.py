class FileMaster():
    def __init__(self, filepath):
        self.filepath = filepath

    def extension(self):
        # Split by '.' and take the last part
        return self.filepath.split('.')[-1]

    def filename(self):
        # Remove directory path and extension
        full = self.filepath.split('/')[-1]
        return full.split('.')[0]

    def dirpath(self):
        # Get everything before the last '/'
        return self.filepath[:self.filepath.rfind('/')+1]
