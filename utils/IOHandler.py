__author__ = 'Animesh'


class input_handler:

    def input_from_file(self, input_file):
        input.text = open(input_file, 'r+').read()
        return input.text

    def open_file(self, input_file):
        open(input_file)

class output_handler:

    def display(self, word):
        print (word)

    def write_to_file(self, output_file, word):
        with open(output_file, 'w') as f:
            f.write(word)