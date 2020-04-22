from random import randint
from datetime import datetime
from typing import Any


def nested_sum(sum_list: list) -> float:
    sums = [sum(ls) for ls in sum_list]
    return sum(sums)


def cumsum(sum_list: list):
    tmp_sum = 0
    result_ls = []
    for sum_item in sum_list:
        tmp_sum += sum_item
        result_ls.append(tmp_sum)
    return result_ls


def is_sorted(ls: list):
    if len(ls) <= 1:
        return True
    if ls[0] <= ls[1]:
        return is_sorted(ls[1:])
    else:
        return False


def chop(ls: list) -> list:
    if len(ls) > 1:
        ls.pop()

        ls.reverse()
        ls.pop()
        ls.reverse()


def middle(ls: list):
    return ls[1:-1]


def is_anagram(str1: str, str2: str):
    ls1 = list(str1)
    ls2 = list(str2)
    ls1.sort()
    ls2.sort()
    return ls1 == ls2


def has_duplicates(str1: str) -> bool:
    unique_char = set(str1)
    count_ls = [str1.count(_char) for _char in unique_char]
    return any(x > 1 for x in count_ls)


def prob_same_bd(n: int) -> float:
    # create n random birthday dates
    bd_list = [randint(1, 365) for _ in range(n)]

    # calc probability
    u_list = [365 - i for i in range(n)]
    print(u_list)
    u_prod = 1
    for n_iter in u_list:
        u_prod *= n_iter
    n_prod = 365 ** n
    print(f"Amount of combinations with different bds: {u_prod}")
    print(f"Amount of combinations with all bds: {n_prod}")
    print(f"Probability of matching bds: {1 - (u_prod / n_prod)}")
    print("-" * 20)
    print(f"Example: random bd list:\n {sorted(bd_list)}")


def read_in_list():
    print("START WITH APPENDING METHOD")
    word_list = []
    dt_start = datetime.now()
    with open("words.txt", "r") as file:
        for line in file:
            word_list.append(line.strip())
    dt_end = datetime.now()
    print(f"List length: {len(word_list)}")
    print(f"Required {((dt_end - dt_start).seconds)} seconds")

    print("\n\n")
    print("START WITH CONCATENATION METHOD")
    word_list = []
    dt_start = datetime.now()
    with open("words.txt", "r") as file:
        for line in file:
            word_list = word_list + [line.strip()]
    dt_end = datetime.now()
    print(f"List length: {len(word_list)}")
    print(f"Required {((dt_end - dt_start).seconds)} seconds")


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

    return reversed_pairs


def exercise_10_1():
    return nested_sum([[1, 2], [3], [4, 5, 6]])


def exercise_10_2():
    return cumsum([1, 2, 3, 100])


def exercise_10_3():
    t = [1, 2, 3, 4]
    return middle(t)


def exercise_10_4():
    t = [1, 2, 3, 4, 5]
    chop(t)
    print(t)


def exercise_10_5():
    t = [1, 2, 2]
    # t = ["b", "a"]
    return is_sorted(t)


def exercise_10_6():
    str1 = "string"
    str2 = "grnits"
    return is_anagram(str1, str2)


def exercise_10_7():
    str1 = "balb"
    print(has_duplicates(str1))


def exercise_10_8():
    rand_days = 23
    prob_same_bd(rand_days)


def exercise_10_9():
    read_in_list()


def exercise_10_10():
    ls = []
    with open("words.txt", "r") as file:
        for line in file:
            ls.append(line.strip())
    print(in_bisect(ls, "cranks"))


def exercise_10_11():
    word_list = []
    with open("words.txt", "r") as file:
        for line in file:
            word_list.append(line.strip())
    print(find_reversed_pairs(word_list))


if __name__ == "__main__":
    exercise_10_11()
