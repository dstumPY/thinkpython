from math import factorial, sqrt


def eval_loop():
    while True:
        eval_str = input("What should be calculated?:")
        if eval_str.lower() == "done":
            break
        evaluation = eval(eval_str)
        print(evaluation)


def calc_part_sum(k):
    result = ((2 * sqrt(2)) / 9801) * (
        (factorial(4 * k) * (1103 + 26390 * k)) / ((factorial(k) ** 4) * 396 ** (4 * k))
    )
    return result


def estimate_pi():
    k = 0
    summe = calc_part_sum(0)
    part_sum = summe
    while part_sum > 1e-30:
        k += 1
        part_sum = calc_part_sum(k)
        summe += part_sum
        print(f"k: {k},partial sum: \t {part_sum}, sum: \t {summe}")
    return summe


estimate_pi()
