def is_pal(test_str: str) -> bool:
    if len(test_str) <= 1:
        return True
    if test_str[0] == test_str[-1]:
        return is_pal(test_str[1:-1])
    else:
        return False


def test_pallindrome_sequence(i: int):
    test_str = str(i)
    if is_pal(test_str[2:6]):
        test_str = str(i + 1)
        if is_pal(test_str[1:6]):
            test_str = str(i + 2)
            if is_pal(test_str[1:5]):
                test_str = str(i + 3)
                if is_pal(test_str):
                    return i


def palindrome_test_9_8():
    i = 100000
    while i <= 999999:
        if test_pallindrome_sequence(i):
            print(i)
        i += 1


def is_reversed_age(lower_age: int, upper_age: int) -> bool:
    return str(lower_age) == str(upper_age)[::-1]


def age_puzzle_9_9():
    dist = 1
    while dist < 100:
        lower_age = 0
        upper_age = lower_age + dist
        while upper_age <= 150:
            if is_reversed_age(lower_age, upper_age):

                print(f"dist: {dist} - lower: {lower_age} - upper: {upper_age}")
            lower_age += 1
            upper_age += 1

        dist += 1
    # Answer: 67 / 76
    # dist: 9 - lower: 12 - upper: 21
    # dist: 9 - lower: 23 - upper: 32
    # dist: 9 - lower: 34 - upper: 43
    # dist: 9 - lower: 45 - upper: 54
    # dist: 9 - lower: 56 - upper: 65
    # dist: 9 - lower: 67 - upper: 76
    # dist: 9 - lower: 78 - upper: 87
    # dist: 9 - lower: 89 - upper: 98


if __name__ == "__main__":
    # palindrome_test_9_8()
    age_puzzle_9_9()

# print(test_pallindrome_sequence(101110))
