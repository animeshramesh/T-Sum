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
    all_features = ""
    while 1:
        try:
            with open('%d.txt' % i):
                inputdataset = a.input_from_file('%d.txt' % i)
                filter1 = prep1.to_lower_case(inputdataset)
                filter2 = prep1.stop_word_eliminate(filter1)
                filter3 = prep1.stem_word(filter2)
                all_features+=filter3 + ' '
                print '\n'*2
                i += 1
        except IOError:
            break
    print all_features
    features = set(all_features)
    #print features
    tot_freq = []
    no_of_files = i-1
    '''for j in range (0,len(features)-1):
        tot_freq.append(all_features.count(features[j]))
        i+=1
    print tot_freq'''




main()
