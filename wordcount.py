# put your code here.


def word_counter_master(filename):
    with open(filename, 'r') as f:
        
        word_count = {}

        for line in f.readlines():
        
            #parse by white space
            words_in_line = line.split()

            #guse get function to count
            for word in words_in_line:
                word_count[word] = word_count.get(word, 0) + 1


        #print the counted items
        for word, number in word_count.items():
            print(word, number)


word_counter_master('test.txt')
