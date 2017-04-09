import sys
import os.path
import re
from collections import Counter

QTY_WORDS = 10

def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as filetext:
        return filetext.read()


def get_most_frequent_words(text):
    words = re.findall(r'\w+', text.lower())
    return Counter(words).most_common(QTY_WORDS)

if __name__ == '__main__':
    fpath = sys.argv[1]

    for word in sorted(get_most_frequent_words(load_data(fpath)), key=lambda wd: wd[1], reverse=True):
        print("Word: %s => Frequency: %s" % (word[0], str(word[1])))
