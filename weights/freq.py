from utils.preprocessor import Preprocessor
from sys import stdout


class input_this:

    def input_from_file(self, input_file):
        input_this.text = open(input_file, 'r+').read()
        return input_this.text


class output_this:

    def display(self, word):
        print (word)

    def write_to_file(self, output_file, word):
        with open(output_file, 'w') as f:
            f.write(word)


class weights:

    __tot_freq = []
    __term_freq_matrix = []

    def ret_tot_freq(self):
        return weights.__tot_freq

    def ret_tot_files(self):
        return weights.__tot_files

    def get_tot_files(self, number):
        weights.__tot_files = number

    def update_term_freq_matrix(self, number):
        for i in range(1, number):
            sentence = open('out%i.txt' % i, 'r+').read()
            arr = []
            for each_word in feature_set.unique_features.split():
                arr.append(sentence.count(each_word))
            weights.__term_freq_matrix[i].append(arr)

    def ret_term_freq_matrix(self):
        return weights.__term_freq_matrix




class feature_set:

    all_features = " "
    # all_features consists of multiple occurences

    unique_features = " "
    __tot_files = 0

    def get_all_features(self,word):
        all_features = word

    def ret_all_features(self):
        return feature_set.all_features

    def update_features(self):
        for word in feature_set.all_features.split():
            if word not in feature_set.unique_features:
                feature_set.unique_features += word + ' '

    def ret_features(self):
        return feature_set.unique_features

    def ret_tot_files(self):
        return feature_set.__tot_files

    def get_tot_files(self, number):
        feature_set.__tot_files = number


def main():
    a = input_this()
    b = output_this()
    prep1 = Preprocessor()
    i = 1
    inputdataset = " "
    c = weights()
    f = feature_set()
    while 1:
        try:
            with open('%d.txt' % i):
                inputdataset = a.input_from_file('%d.txt' % i)
                filter1 = prep1.to_lower_case(inputdataset)
                filter2 = prep1.stop_word_eliminate(filter1)
                filter3 = prep1.stem_word(filter2)
                b.write_to_file('out%i.txt' % i, filter3)
                f.all_features += filter3 + ' '
                i += 1
        except IOError:
            break
    f.get_tot_files(i-1)


    for each_word in f.unique_features.split():
        c.ret_tot_freq().append(f.all_features.count(each_word))

    #j = 0
    #for each_word in c.features.split():
    #    stdout.write(each_word + ' ' + str(c.ret_tot_freq()[j]) + '\n')
    #    j += 1

    c.update_term_freq_matrix(f.ret_tot_files())

main()
