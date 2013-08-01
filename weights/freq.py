from prep import preprocessing


class input_this:

    def input_from_file(self, input_file):
        input_this.text = open(input_file, 'r+').read()
        return input_this.text


class output_this:

    def display(self, word):
        print (word)


def main():
    a = input_this()
    b = output_this()
    #prep = preprocessor()
    i = 1
    inputdataset = ""
    try:
        while inputdataset != '\0':
            inputdataset = a.input_from_file('%d.txt' % i)
            filter1 = prep.to_lower_case(inputdataset)
            filter2 = prep.stop_word_eliminate(filter1)
            filter3 = prep.stem_word(filter2)
            i += 1
            b.display(filter3)
            print '\n'*2
    except IOError, e:
        print e[0], e[1]


main()
