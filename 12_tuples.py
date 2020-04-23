from typing import Dict
from pprint import pprint


def exercise_12_1():
    test_str = "parrot"
    hist_dic = most_frequent(test_str)


def exercise_12_2():

    d = {}
    with open('words.txt', 'r') as file:
        for line in file:
            word = line.strip()
            k = to_alphabetical(word)
            if k not in d:
                d[k] = {'anagram': [word]}
            else:
                d[k]['anagram'].append(word)

    for _, val in d.items():
        val['len'] = len(val['anagram'])
    
    tmp_dict = sorted(d.items(), key=lambda item: item[1]['len'], reverse=True)
    pprint(tmp_dict)


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
