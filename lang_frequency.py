import sys
import os.path
import re
from collections import Counter


def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as filetext:
        return filetext.read()

def get_most_frequent_words(text, number_of_words_result):
    words = re.findall(r'\w+', text.lower())
    return Counter(words).most_common(number_of_words_result)

def print_help():
    print("Usage: %s %s %s" % (sys.argv[0], "<filename path>", "[<number of words in the list>]"))
    print("<number of words in the list> dafault 10")

def verification_of_parameters():
    number_of_words_result = 10
    if len(sys.argv) < 2:
        print_help()
        sys.exit()
    elif not os.path.exists(sys.argv[1]):
        print("Filename '%s' not found" % (sys.argv[1]))
        print_help()
        sys.exit()
    elif len(sys.argv) == 3:
        if int(sys.argv[2]) < 0:
            print("number of words in the list must be a positive number")
            print_help()
            sys.exit()
        else:
            number_of_words_result = sys.argv[2]
    else:
        pass
    return ({"filepath": sys.argv[1], "number_of_words_result": int(number_of_words_result)})

if __name__ == '__main__':
    parameters = verification_of_parameters()
    filetext = load_data(parameters["filepath"])
    
    for word in get_most_frequent_words(filetext,parameters["number_of_words_result"]):
        print("Word: %s => Frequency: %s" % (word[0], str(word[1])))
