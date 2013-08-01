from prep import preprocessor


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
    prep1 = preprocessor()
    i = 1
    inputdataset = ""
    while (1):
        #inputdataset = a.input_from_file('%d.txt' % i)
        try:
            with open('%d.txt' % i):
                inputdataset = a.input_from_file('%d.txt' % i)
                filter1 = prep1.to_lower_case(inputdataset)
                #print filter1
                filter2 = prep1.stop_word_eliminate(filter1)
                print filter2
                # No output after stop_word_eliminate <BUG>
                filter3 = prep1.stem_word(filter2)
                i += 1
                b.display(filter3)
                print '\n'*2
        except IOError, e:
            break


    '''try:
        while inputdataset != '\0':
            inputdataset = a.input_from_file('%d.txt' % i)
            filter1 = prep1.to_lower_case(inputdataset)
            filter2 = prep1.stop_word_eliminate(filter1)
            filter3 = prep1.stem_word(filter2)
            i += 1
            b.display(filter3)
            print '\n'*2
    except IOError, e:
       pass'''


main()
