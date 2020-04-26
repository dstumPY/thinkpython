from typing import Dict, List
from pprint import pprint
import pickle
import string


def exercise_12_1():
    test_str = "parrot"
    hist_dic = most_frequent(test_str)


def exercise_12_2():

    d = {}
    with open("words.txt", "r") as file:
        for line in file:
            word = line.strip()
            k = to_alphabetical(word)
            if k not in d:
                d[k] = {"anagram": [word]}
            else:
                d[k]["anagram"].append(word)

    for _, val in d.items():
        val["len"] = len(val["anagram"])

    result_dict = sorted(d.items(), key=lambda item: item[1]["len"], reverse=True)

    with open("anagram_dict.pkl", "wb") as pickle_dumper:
        pickle.dump(result_dict, pickle_dumper)
    # # 12.2.c)
    # for item in result_dict:
    #     if len(item[0]) == 8:
    #         print(item)
    #         break


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
    return "".join(sorted_ls)


def read_anagram():
    with open("anagram_dict.pkl", "rb") as pickle_loader:
        anagram_dict = pickle.load(pickle_loader)
    return anagram_dict


def get_permutations(str_len: int):
    ls = [(i, j) for i in range(str_len) for j in range(str_len) if i < j]
    return ls


def switch_by_perm(str1: str, perm: List[int]) -> List[str]:
    init_ls = list(str1)
    tmp_var = init_ls[perm[0]]
    init_ls[perm[0]] = init_ls[perm[1]]
    init_ls[perm[1]] = tmp_var
    return init_ls


def is_meta_pair(str1: str, str2: str):
    tmp_len = len(str1)
    assert tmp_len == len(str2), "Not same length"
    permutation_ls = get_permutations(tmp_len)
    for perm in permutation_ls:
        test_str1 = switch_by_perm(str1, perm)
        test_str2 = list(str2)
        if test_str1 == test_str2:
            return True
        else:
            continue
    return False


def exercise_12_3():
    anagram_ls = read_anagram()
    # modify dict to sort out items with no matching anagrams
    anagram_ls = [item[1] for item in anagram_ls if item[1]["len"] > 2]
    for anagram_item in anagram_ls:
        working_list = anagram_item["anagram"]
        for index, word in enumerate(working_list):
            for test_word in working_list[index:]:
                if is_meta_pair(word, test_word) and (word != test_word):
                    print(word, test_word)
                else:
                    continue


if __name__ == "__main__":
    # exercise_12_2()
    # exercise_12_3()
    exercise_12_4()
