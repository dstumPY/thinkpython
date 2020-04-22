from typing import Dict
from pprint import pprint


def exercise_12_1():
    test_str = "parrot"
    hist_dic = most_frequent(test_str)


def exercise_12_2():
    pass


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


if __name__ == "__main__":
    # exercise_12_2()
    str1 = "parrot"
    str2 = "torpar"
    test_list = [str1, "asugba", str2, "dbs", "wof", "oawi", "sdb", "bds"]
    alphabet = [
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
    lexic = {letter: [] for letter in alphabet}
    for letter, val in lexic.items():
        for word in test_list:
            if letter in word:
                val.append(word)
    pprint(lexic)

    # loop over letter from lexic
    for letter, letter_list in lexic.items():
        # loop over specific letter list
        # (= list corresponding to one letter)
        for word in letter_list:
            # filter only on words with the same lenght
            tmp_list = [
                item_word
                for item_word in letter_list
                if (len(item_word) == len(word)) and item_word != word
            ]

            # loop over the words with same length to test is_anagram
            for eq_len_word in tmp_list:
                if is_anagram(eq_len_word, word):
                    print(letter, word, eq_len_word)
