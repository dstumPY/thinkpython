from typing import List, Dict, Any, Tuple, Callable
from collections import defaultdict
from math import log, exp
import matplotlib.pyplot as plt
import string
import random


def get_hist(word_ls: list) -> Dict[str, int]:
    word_dict = {}
    for word in word_ls:
        word_dict[word] = word_dict.get(word, 0) + 1
    return word_dict


def process_line(line: str, hist: Dict) -> Dict:
    """ Cut newlines, transform to lowercase and delete
        string punctuations from the words
    """
    line.replace("-", " ")
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        if word != "":
            hist[word] = hist.get(word, 0) + 1


def process_file(filename: str) -> Dict[str, int]:
    hist = dict()
    with open(filename, "r") as file:
        for line in file:
            process_line(line, hist)
    return hist


def get_list_of_words(filename: str) -> List[str]:
    word_list = []
    with open(filename) as file:
        for line in file:
            line = line.strip()
            word_list.append(line)
    return word_list


def sort_by_frequency(words_dict: Dict, reverse: bool = True) -> List:
    words_dict = sorted(words_dict.items(), key=lambda item: item[1], reverse=reverse)
    return words_dict


def remove_common_words(
    words_dict: Dict[str, int], common_words: List[str]
) -> Dict[str, int]:
    """For a given words frequency dict remove all keys given in the
    common words list

    Arguments:
        words_dict {Dict} -- dictionary with str keys
        common_words {List} -- list with str items
    """
    for word in common_words:
        try:
            del words_dict[word]
        except KeyError:
            continue
    return words_dict


def choose_from_hist(hist: Dict) -> Any:
    return random.choices(list(hist.keys()), hist.values())


def total_words(hist: Dict[str, int]) -> int:
    return sum(hist.values())


def different_words(hist: Dict[str, int]) -> int:
    return len(hist)


def subtract(d1: Dict[str, int], d2: Dict[str, int]) -> Dict[str, int]:

    subtracted = dict()
    for key in d1:
        if key not in d2:
            subtracted[key] = None
    return subtracted


def word_summary(book_filename: str, library__filename: str):
    words_dict = process_file("hudson.txt")
    library_eng_words_ls = get_list_of_words("words.txt")

    print(f"Total number of words: {total_words(words_dict)}")
    print(f"Total number of different words: {different_words(words_dict)}")
    words_dict = remove_common_words(words_dict, library_eng_words_ls)
    print(f"Remaining words after deletion: {len(words_dict)}")

    # # sort words_dict by word frequency and print out the top 20
    # words_dict = print(sort_by_library_eng_words_lsfrequency(words_dict))
    # for item in words_dict[:20]:
    #     print(item)


def most_used_words(num: int = 10):
    words_dict = process_file("hudson.txt")
    words_freq = sort_by_frequency(words_dict)

    print(f"The most used words are")
    for word, freq in words_freq[:num]:
        print(word, freq, sep="\t")
    print("..")


def set_subtract(d1: Dict[str, int], d2: Dict[str, int]) -> Dict[str, int]:
    set1 = set(d1.keys())
    set2 = set(d2.keys())

    return set1.difference(set2)


def not_contained_words(filename1: str, filename2: str):
    d1 = process_file(filename1)
    d2 = process_file(filename2)

    # diff = subtract(d1, d2)
    diff = set_subtract(d1, d2)

    print(len(diff))
    # print("Words not contained in word library:")
    # for word in diff.keys():
    #     print(word, end=" ")


def cumulative_hist(hist_dict: Dict[str, int]) -> Dict[str, int]:
    # sort dict by frequency
    words_dict = sort_by_frequency(hist_dict, False)
    cum_sum = 0
    cumulative_dict = dict()
    for key, value in dict(words_dict).items():
        cum_sum += value
        cumulative_dict[key] = cum_sum
    return cumulative_dict


def random_choice(freq_dict: Dict[str, int]) -> str:
    cum_word_freq = cumulative_hist(words_dict)


def get_random_word_by_frequency(dic1: Dict[str, int], n: int) -> str:
    item_ls = list(dic1.items())

    return item_next_to_n(item_ls, n)


def item_next_to_n(ls: list, n: int):
    if len(ls) < 2:
        return ls[0]
    bisect_idx = int(len(ls) / 2)

    if ls[bisect_idx - 1][1] < n:
        return item_next_to_n(ls[bisect_idx:], n)
    else:
        return item_next_to_n(ls[:bisect_idx], n)


def random_word(filename: str) -> str:
    words_dict = process_file(filename)
    cum_word_freq = cumulative_hist(words_dict)
    n = list(cum_word_freq.values())[-1]

    # random choice in 1..n
    rand_choice = random.choice(range(1, n + 1))

    # cum_sums = list(cum_word_freq.values())
    result = get_random_word_by_frequency(cum_word_freq, rand_choice)
    # idx_key = cum_word_freq.index()
    return result


def book_analysis(filename: str) -> Any:
    # Get word summary for a given book
    word_summary("words.txt")

    # Find most used words
    most_used_words()

    # get a random word by respecting the frequency of the words
    # within the book
    not_contained_words("hudson.txt", "words.txt")
    result = random_word("hudson.txt")

    print(result[0])


def n_partition(words: List[str], n_length: int) -> Dict[Tuple[str], List[str]]:
    """The function divides a given words list into different 
       partitions of length n_length. Each partition will be set as a
       key from a dict wich maps to the word in the words list at 
       the following index position n_length + 1.

       Since same word partitions may be followed by different words, 
       all the possible following words will be stored in a list.
       This list collection with multiple following words is set as
       value to the partition key in the dict.

    Arguments:  
        words {List[]str} -- words from a given text are stored in a list, 
                             ordered by occurence within the text
        n_length {int}    -- length of the partition keys

    Returns:
        Dict[Tuple[str], List[str]] -- Dict mapping from partitions to 
                                       valid next words
    """
    part_dict = dict()
    for index, word in enumerate(words):
        try:
            # get next partition with length n_length as dict key
            partition_key = tuple(words[index + j] for j in range(n_length))
            value = part_dict.setdefault(partition_key, [])
            # map the next word to the partition_key which is not contained
            # in the partition key itself as element
            value.append(words[index + n_length])
        except IndexError:
            continue
    return part_dict


def random_step(
    part_key: Tuple[str], partitions: Dict[Tuple[str], List[str]]
) -> List[str]:
    """Choose randomly from the next valid words. 

    Arguments:
        part_key {Tuple} -- key in partitions
        partitions {List[Tuple]} -- dictionary with possible next 
                                    steps for a key

    Returns:
        {List} -- next word, randomly chosen from a given set of 
                  valid answers
    """
    next_walk = partitions.get(part_key, [])
    # choose randomly only if there are two choices at least
    if len(next_walk) > 1:
        next_walk = [random.choice(next_walk)]
    return part_key[1:] + tuple(next_walk), next_walk


def random_walk(
    init_partition: Tuple[str], partitions: Dict[Tuple[str], List[str]]
) -> List[List[str]]:
    """Perform a random walk, according to a given partitions dict 
       which maps from a given set of partitions to a valid set
       of possible next words. Within this set it will be choosen 
       randomly. 

    Arguments:
        init_partition {Tuple[str]} -- initial key to start the random walk
        partitions {Dict[Tuple[str], List[str]]} -- random walk map with 
                                                    possible choices

    Returns:
        List[List[str]] -- Randomly choosen words, gained through a
                           random walk
    """
    # modify structure of initial input to match the output structure
    walk_list = [[word] for word in init_partition]
    iter_tuple = init_partition
    next_word = [""]
    while next_word != []:
        iter_tuple, next_word = random_step(iter_tuple, partitions)
        walk_list.append(next_word)
    return walk_list


def read_file(filename):
    words = []
    with open(filename, "r") as file:
        for line in file:
            line = line.replace("-", " ")
            for word in line.split():
                word = word.strip(string.punctuation + string.whitespace)
                word = word.lower()
                words.append(word)
    return words


def exercise_13_8():
    # store words in list
    words = read_file("hudson.txt")

    # transform words in partitions which will serves as keys for a
    # random walk
    n_length = 2
    partitions = n_partition(words, n_length)

    # choose an initial partition for the random walk
    init_part = random.choice(list(partitions.keys()))
    walk_list = random_walk(init_part, partitions)

    random_walk = (item[0] for item in walk_list if item != [])
    random_walk_text = " ".join(random_walk)

    print(words)


def exercise_13_9(filename: str):
    words = []
    with open(filename, "r") as file:
        for line in file:
            line.replace("-", " ")
            for word in line.split():
                word = word.strip(string.punctuation + string.whitespace)
                word = word.lower()
                words.append(word)

    # calculate frequency
    histogram = get_hist(words)
    histogram = sort_by_frequency(histogram)

    # form a set of
    # log_dict = log_rank_freq(histogram, min)
    # constant = 9.5
    # slope = constant/9.825
    # plot_values(log_dict, constant, slope)
    


    log_dict = log_rank_freq(histogram, max)
    constant = 10.2
    slope = constant/9.825
    plot_values(log_dict, constant, slope)



def plot_values(rank_freq: Dict, c: int, s: int):
    x = list(rank_freq.keys())
    y = list(rank_freq.values())

    lin_func = lambda x: c - s*x
    y_line = list(map(lin_func, x))

    plt.plot(x, y)
    plt.plot(x, y_line)
    plt.show()


def log_rank_freq(histogram: Dict, agg_func: Callable) -> Dict:
    # form a set of
    d = defaultdict(list)
    log_d = dict()
    for index, (_, v) in enumerate(histogram):
        d[v].append(index + 1)

    for k, v in d.items():
        tmp = agg_func(v)
        d[k] = tmp
        log_d[log(k)] = log(tmp)
    return log_d


if __name__ == "__main__":
    exercise_13_9("hudson.txt")
