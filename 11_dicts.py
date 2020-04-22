from datetime import datetime
from typing import Any, List


def to_dict(word_list: list):
    return dict((word, 0) for word in word_list)


def in_bisect(sorted_ls: list, target: Any) -> bool:
    if len(sorted_ls) <= 2:
        return target in sorted_ls

    # divide list in two parts
    # Note: choose +1 as index to avoid an empty list
    median_index = int(len(sorted_ls) / 2)
    if target <= sorted_ls[median_index]:
        return in_bisect(sorted_ls[:median_index], target)
    else:
        return in_bisect(sorted_ls[median_index:], target)


def find_reversed_pairs(word_list: list):
    reversed_pairs = []

    dt_start = datetime.now()
    for word in word_list:
        if in_bisect(word_list, word[::-1]):
            reversed_pairs.append((word, word[::-1]))
    dt_end = datetime.now()
    print(f"Method 'bisect' required {(dt_end - dt_start).seconds} seconds")

    dt_start = datetime.now()
    for word in word_list:
        if word[::-1] in word_list:
            reversed_pairs.append((word, word[::-1]))
    dt_end = datetime.now()
    print(f"Method 'in' required {(dt_end - dt_start).seconds} seconds")

    dt_start = datetime.now()
    word_list_dict = to_dict(word_list)
    for word in word_list:
        if word[::-1] in word_list_dict:
            reversed_pairs.append((word, word[::-1]))
    dt_end = datetime.now()
    print(f"Method 'dict' required {(dt_end - dt_start).seconds} seconds")

    return reversed_pairs


def invert_dict(dic_to_invert: dict):
    inverse_dict = {}
    for key in dic_to_invert:
        val = dic_to_invert[key]
        inverse_dict.setdefault(val, []).append(key)
    return inverse_dict


def has_duplicates(word_list: list):
    word_dict = dict((i, word) for i, word in enumerate(word_list))
    inverted_dict = invert_dict(word_dict)
    for val in inverted_dict.values():
        if len(val) >= 2:
            return True
    return False


def ack(m: int, n: int):
    global mem_dic

    if (m, n) in mem_dic:
        return mem_dic[m, n]

    if m == 0:
        return n + 1

    elif n == 0:
        tmp_ack = ack(m - 1, 1)
        mem_dic[(m, n)] = tmp_ack
        return tmp_ack
    else:
        tmp_ack = ack(m - 1, ack(m, n - 1))
        mem_dic[(m, n)] = tmp_ack
        return tmp_ack


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


def get_roation_dist(char1: str, char2: str):
    global ALPHABET
    assert len(char1) == len(char2) == 1, "Chars too long"
    idx_1 = ALPHABET.index(char1.lower())
    idx_2 = ALPHABET.index(char2.lower())
    return idx_2 - idx_1


def exercise_11_1(word_list: list):
    words_dict = to_dict(word_list)
    find_reversed_pairs(word_list)


def exercise_11_2():

    dic_to_invert = {"a": 1, "b": 2, "c": 3, "e": 1}
    inverse_dict = invert_dict(dic_to_invert)
    print(inverse_dict)


def exercise_11_3():
    print(ack(3, 4))


def exercise_11_4():
    test_ls = ["a", "b", "c", "a"]
    print(has_duplicates(test_ls))


def add_dist(word: str, dist: int) -> str:
    global ALPHABET
    added_ls = []
    for char in word:
        idx_on_adding = (ALPHABET.index(char) + dist) % 26
        added_ls.append(ALPHABET[idx_on_adding])
    return "".join(added_ls)


def rotate_pairs(word_list: list) -> List:
    for word in word_list:
        # get distances to first char of all other words
        dist_list = [
            get_roation_dist(word[0], word_iter[0])
            for word_iter in word_list
            if word_iter != word
        ]
        rot_list = [add_dist(word, dist) for dist in dist_list]

        for rot_word in rot_list:
            if rot_word in word_list:
                return True
    return False


def exercise_11_5():
    # dist = get_roation_dist("a", "Z")
    # print("defg" == add_dist("abcd", 3))
    word_list = ["abcd", "df", "efgh"]
    print(rotate_pairs(word_list))


if __name__ == "__main__":
    # word_ist = []
    # with open("words.txt", "r") as file:
    #     for line in file:
    #         word_list.append(line.strip())
    # exercise_11_1(word_list)

    # mem_dic = {}
    # exercise_11_3()

    exercise_11_5()
