from prep.preprocessing import preprocessor
from sys import stdout


class input_this:

    def input_from_file(self, input_file):
        input_this.text = open(input_file, 'r+').read()
        return input_this.text


class output_this:

    def display(self, word):
        print (word)


class weights:

    all_features = " "
    features = " "
    __tot_freq = []
    __tot_files = 0

    def ret_tot_freq(self):
        return weights.__tot_freq
    def ret_tot_files(self):
        return weights.__tot_files


def main():
    a = input_this()
    prep1 = preprocessor()
    i = 1
    inputdataset = " "
    c = weights()
    while 1:
        try:
            with open('%d.txt' % i):
                inputdataset = a.input_from_file('%d.txt' % i)
                filter1 = prep1.to_lower_case(inputdataset)
                filter2 = prep1.stop_word_eliminate(filter1)
                filter3 = prep1.stem_word(filter2)
                c.all_features += filter3 + ' '
                i += 1
        except IOError:
            break

    for word in c.all_features.split():
        if word not in c.features:
            c.features += word + ' '


    for each_word in c.features.split():
        c.ret_tot_freq().append(c.all_features.count(each_word))
    j = 0
    for each_word in c.features.split():
        stdout.write(each_word + ' ' + str(c.ret_tot_freq()[j]) + '\n')
        j += 1

main()
