from typing import Dict
from pprint import pprint

ALPHABET = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

def exercise_12_1():
    test_str = "parrot"
    hist_dic = most_frequent(test_str)


def exercise_12_2():
    # transform a list of words similar to test list into a dict which 
    # has the letters from ALPHABET as keys and the words containing 
    # that special keys as list assigned ({'a': ["parrot", "oawi", ..], "b": ..})
    test_list = ["parrot", "asugba", "torpar", "dbs", "wof", "oawi", "sdb", "bds"]
    lexic = {letter: [] for letter in ALPHABET}
    for letter, val in lexic.items():
        for word in test_list:
            if letter in word:
                val.append(word)
    pprint(lexic)

    result_dict = {}

    # loop over the keys from lexic and check only the word list
    # assigned to key for an anagram. Since anagrams must have the
    # same length it's sufficient to check a word only to a sublist 
    # of words with the same length
    for letter, letter_list in lexic.items():
        # loop over specific letter list
        # (= list corresponding to one letter)
        for word in letter_list:
            # filter only for words with the same length
            tmp_list = [
                item_word
                for item_word in letter_list
                if (len(item_word) == len(word)) and item_word != word
            ]

            # Loop over the words with same length to test is_anagram.
            # If an anagram is found we normalize the word to a string
            # with chars in alphabetical order. The normalized string
            # builds the keys for the found anagram words that will 
            # be assigned as list
            for eq_len_word in tmp_list:
                if is_anagram(eq_len_word, word):
                    key_str = to_alphabetical(word)
                    val_set = result_dict.setdefault(key_str, set())
                    val_set.add(eq_len_word)
                    #print(result_dict[key_str])
                    #print(letter, word, eq_len_word)
    pprint(result_dict)

def hist(str1: str) -> Dict:
    hist_dic = {}
    for char in str1:
        hist_dic[char] = hist_dic.get(char, 0) + 1
    return hist_dic


def most_frequent(str1: str) -> Dict:
    hist_dict = hist(str1)

    sorted_hist = sorted(hist_dict.items(), key=lambda item: item[0])
    return sorted_hist


def is_anagram(str1: str, str2: str):
    return most_frequent(str1) == most_frequent(str2)

def to_alphabetical(str1: str) -> str:
    sorted_ls = sorted(str1)
    return ''.join(sorted_ls)


if __name__ == "__main__":
    exercise_12_2()
