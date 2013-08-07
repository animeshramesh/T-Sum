__author__ = 'Animesh'


class FileWriter:

    def write(self, output_file, output_data):
        with open(output_file, 'w') as f:
            f.write(output_data)