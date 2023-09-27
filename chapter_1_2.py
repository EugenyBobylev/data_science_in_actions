from collections import defaultdict
from itertools import product
from chapter_1_1 import compute_probability


possible_children = {'Boy', 'Girl'}  # пол детей в семье


def four_children_space() -> set:
    _children_space = set()
    for child1 in possible_children:
        for child2 in possible_children:
            for child3 in possible_children:
                for child4 in possible_children:
                    _children_space.add((child1, child2, child3, child4))
    return _children_space


def has_two_boys(outcome) -> bool:
    return len([child for child in outcome if child == 'Boy']) == 2


possible_rolls = {1, 2, 3, 4, 5, 6}  # значения игрального кубика
possible_flips = {1, 2}          # значение для орла и решки монеты


def get_weight_roll_space(steps=6):
    def inc_outcome(curr_sum) -> int:
        for i in range(steps-1, -1, -1):
            if outcome[i] < max(possible_rolls):
                outcome[i] += 1
                return curr_sum + 1
            else:
                outcome[i] = 1
                curr_sum = curr_sum - max(possible_rolls) + min(possible_rolls)
        return curr_sum

    _weight_roll_space = defaultdict(int)
    init_outcome = [1 for _ in range(steps)]
    outcome = init_outcome[0:steps]
    outcome_sum = sum(outcome)
    _weight_roll_space[outcome_sum] += 1
    while True:
        outcome_sum = inc_outcome(outcome_sum)
        if outcome == init_outcome:
            break
        _weight_roll_space[outcome_sum] += 1
    return _weight_roll_space


def get_weight_coin_space(num_flips=10):
    _weight_coin_space = defaultdict(int)
    for coin_flips in product(['Head', 'Tails'], repeat=num_flips):
        heads_count = len([outcome for outcome in coin_flips if outcome == 'Head'])
        _weight_coin_space[heads_count] += 1
    return _weight_coin_space


def get_weight_roll_space2() -> dict:
    _weight_roll_space = defaultdict(int)
    _roll_space = set(product(possible_rolls, repeat=6))
    for outcome in _roll_space:
        total = sum(outcome)
        _weight_roll_space[total] += 1
    return _weight_roll_space


def has_sum_of_21(outcome) -> bool:
    return sum(outcome) == 21


def is_in_interval(number, minimum, maximum) -> bool:
    return minimum <= number <= maximum


if __name__ == '__main__':
    children_space1 = four_children_space()
    children_space2 = set(product(possible_children, repeat=4))
    assert len(children_space1) == len(children_space2)

    # ищем вероятность того что в семье с 4-мя детьми будет 2 мальчика
    prob = compute_probability(has_two_boys, children_space1)
    print(f'Probability of two boys is {prob}')

    # ищем вероятность того что сумма выпавших чисел будет 21
    roll_space = set(product(possible_rolls, repeat=6))
    prob1 = compute_probability(has_sum_of_21, roll_space)
    print(f'Probability of sum of 21 is {prob1}')

    # вычисление вероятности с использование лямбды
    prob2 = compute_probability(lambda x: sum(x) == 21, roll_space)
    assert prob2 == prob1
    count_21 = len([x for x in roll_space if sum(x) == 21])

    # вычисление вероятностей исхода бросков кубика с помощью пространств взвешенных исходов
    weight_roll_space = get_weight_roll_space()
    prob3 = compute_probability(lambda x: x == 21, weight_roll_space)
    print(f'Probability of sum of 21 is {prob3}')

    # Вычисление вероятности того, тчо 6 бросков кубика дадут сумму от 10 до 21 включительно
    prob4 = compute_probability(lambda x: is_in_interval(x, 10, 21), weight_roll_space)
    print(f'Probability of interval is {prob4}')

    # вычисление вероятности исходов из 10 подбрасываний монеты
    weight_coin_space = get_weight_coin_space(num_flips=10)
    assert weight_coin_space[10] == 1
    assert weight_coin_space[9] == 10

    prob5 = compute_probability(lambda x: is_in_interval(x, 8, 10), weight_coin_space)
    print(f'Probability of observing more than 7 heads is {prob5}')

    prob6 = compute_probability(lambda x: not is_in_interval(x, 3, 7), weight_coin_space)
    print(f'Probability of observing more than 7 heads or 7 tails is {prob6}')

    # вычисление вероятности исходов из 20 подбрасываний монеты
    weight_coin_space = get_weight_coin_space(num_flips=20)
    # найдем вероятность того, что 20 подбрасываний монеты не дадут от 5 до 15 орлов
    prob7 = compute_probability(lambda x: not is_in_interval(x, 5, 15), weight_coin_space)
    print(f'Probability of observing more than 15 heads or 15 tails is {prob7}')
