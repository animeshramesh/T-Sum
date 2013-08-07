__author__ = 'Animesh'


class FileReader:

    def read(self, input_file):
        return open(input_file, 'r+').read()