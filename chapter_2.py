import matplotlib.pyplot as plt

from chapter_1_2 import is_in_interval, get_weight_coin_space


def listing_2_2():
    """Графическая отрисовка линейного соотношения"""
    x = range(0, 10)
    y = [val * 2 for val in x]
    plt.plot(x, y)
    plt.show()


def listing_2_3():
    """Графическая отрисовка отдельных точек"""
    x = range(0, 10)
    y = [val * 2 for val in x]
    plt.scatter(x, y)
    plt.show()


def listing_2_4():
    """Затенение интервала под отрисованным графиком"""
    x = range(0, 10)
    y = [val * 2 for val in x]
    plt.plot(x, y)
    where = [is_in_interval(val, 2, 6) for val in x]
    plt.fill_between(x, y, where=where)
    plt.show()


def listing_2_5():
    """Отображение отдельных точек данных на линейном графиком"""
    x = range(0, 10)
    y = [val * 2 for val in x]
    plt.scatter(x, y)   # отрисовать отельные точки данных
    plt.plot(x, y)      # отрисовать линейный график
    # выделение интервала под отрисованным графиком
    where = [is_in_interval(val, 2, 6) for val in x]
    plt.fill_between(x, y, where=where)

    plt.show()          # отображение графика


def listing_2_6():
    """Добавление подписей к осям графика"""
    x = range(0, 10)
    y = [val * 2 for val in x]
    plt.scatter(x, y)   # отрисовать отельные точки данных
    plt.plot(x, y)      # отрисовать линейный график
    # выделение интервала под отрисованным графиком
    where = [is_in_interval(val, 2, 6) for val in x]
    plt.fill_between(x, y, where=where)
    # добавить подписи к осям
    plt.xlabel('Values between zero and ten')
    plt.ylabel('Twice the values of x')

    plt.show()          # отображение графика


def listing_2_7():
    weight_coin_space = get_weight_coin_space(num_flips=10)
    x_10_flips = list(weight_coin_space.keys())
    y_10_flips = list(weight_coin_space.values())

    plt.scatter(x_10_flips, y_10_flips)
    plt.xlabel('Head-count')
    plt.ylabel('Number of coin-flip combinations with x heads')

    plt.show()


def listing_2_8():
    """Отрисовка вероятностей исходов подбрасываний монеты"""
    weight_coin_space = get_weight_coin_space(num_flips=10)
    coin_space_size = sum(weight_coin_space.values())
    x_10_flips = list(weight_coin_space.keys())
    y_10_flips = list(weight_coin_space.values())
    prob_x_10_flips = [val / coin_space_size for val in y_10_flips]
    assert sum(prob_x_10_flips) == 1  # сумма всех вероятностей всегда равна 1

    plt.scatter(x_10_flips, prob_x_10_flips)
    plt.xlabel('Head-count')
    plt.ylabel('Probability of x heads')

    plt.show()


def listing_2_10():
    """Затенение интервала под кривой вероятностей"""
    weight_coin_space = get_weight_coin_space(num_flips=10)
    coin_space_size = sum(weight_coin_space.values())
    x_10_flips = list(weight_coin_space.keys())
    y_10_flips = list(weight_coin_space.values())
    prob_x_10_flips = [val / coin_space_size for val in y_10_flips]

    plt.scatter(x_10_flips, prob_x_10_flips)
    plt.plot(x_10_flips, prob_x_10_flips)
    where = [is_in_interval(val, 8, 10) for val in x_10_flips]
    plt.fill_between(x_10_flips, prob_x_10_flips, where=where)

    plt.xlabel('Head-count')
    plt.ylabel('Probability of x heads')

    plt.show()


def listing_2_11():
    """Затенение интервала под экстремальными значениями кривой вероятностей"""
    weight_coin_space = get_weight_coin_space(num_flips=10)
    coin_space_size = sum(weight_coin_space.values())
    x_10_flips = list(weight_coin_space.keys())
    y_10_flips = list(weight_coin_space.values())
    prob_x_10_flips = [val / coin_space_size for val in y_10_flips]

    plt.scatter(x_10_flips, prob_x_10_flips)
    plt.plot(x_10_flips, prob_x_10_flips)

    where = [not is_in_interval(val, 3, 7) for val in x_10_flips]
    plt.fill_between(x_10_flips, prob_x_10_flips, where=where)

    plt.xlabel('Head-count')
    plt.ylabel('Probability of x heads')

    plt.show()


def listing_2_12():
    """ Отрисовка двух распределений одновременно"""

    # 10 flips
    weight_coin_space = get_weight_coin_space(num_flips=10)
    coin_space_size = sum(weight_coin_space.values())
    x_10_flips = list(weight_coin_space.keys())
    y_10_flips = list(weight_coin_space.values())
    prob_x_10_flips = [val / coin_space_size for val in y_10_flips]
    # 20 flips
    weight_coin_space = get_weight_coin_space(num_flips=20)
    coin_space_size = sum(weight_coin_space.values())
    x_20_flips = list(weight_coin_space.keys())
    y_20_flips = list(weight_coin_space.values())
    prob_x_20_flips = [val / coin_space_size for val in y_20_flips]

    plt.scatter(x_10_flips, prob_x_10_flips)
    plt.plot(x_10_flips, prob_x_10_flips, label='A: 10 coin-flips')

    plt.scatter(x_20_flips, prob_x_20_flips,  marker='x')
    plt.plot(x_20_flips, prob_x_20_flips, linestyle='--', label='B: 20 coin-flips')

    plt.xlabel('Head-count')
    plt.ylabel('Probability of x heads')
    plt.legend()
    plt.show()


def listing_2_14():
    """ Выделение интервалов под двумя графиками распределений"""

    # 10 flips
    weight_coin_space = get_weight_coin_space(num_flips=10)
    coin_space_size = sum(weight_coin_space.values())
    x_10_flips = list(weight_coin_space.keys())
    y_10_flips = list(weight_coin_space.values())
    prob_x_10_flips = [val / coin_space_size for val in y_10_flips]
    # 20 flips
    weight_coin_space = get_weight_coin_space(num_flips=20)
    coin_space_size = sum(weight_coin_space.values())
    x_20_flips = list(weight_coin_space.keys())
    y_20_flips = list(weight_coin_space.values())
    prob_x_20_flips = [val / coin_space_size for val in y_20_flips]

    # выделить интервалы
    where_10 = [not is_in_interval(val, 3, 7) for val in x_10_flips]
    plt.fill_between(x_10_flips, prob_x_10_flips, where=where_10)
    where_20 = [not is_in_interval(val, 5, 15) for val in x_20_flips]
    plt.fill_between(x_20_flips, prob_x_20_flips, where=where_20)

    # Отрисовка
    plt.scatter(x_10_flips, prob_x_10_flips)
    plt.plot(x_10_flips, prob_x_10_flips, label='A: 10 coin-flips')

    plt.scatter(x_20_flips, prob_x_20_flips,  marker='x')
    plt.plot(x_20_flips, prob_x_20_flips, linestyle='--', label='B: 20 coin-flips')

    plt.xlabel('Head-count')
    plt.ylabel('Probability of x heads')
    plt.legend()
    plt.show()


def listing_2_15():
    """Преобразование числа исходов с орлами в их частоту"""

    # 10 flips
    weight_coin_space = get_weight_coin_space(num_flips=10)
    coin_space_size = sum(weight_coin_space.values())
    x_10_flips = list(weight_coin_space.keys())
    y_10_flips = list(weight_coin_space.values())
    prob_x_10_flips = [val / coin_space_size for val in y_10_flips]
    # 20 flips
    weight_coin_space = get_weight_coin_space(num_flips=20)
    coin_space_size = sum(weight_coin_space.values())
    x_20_flips = list(weight_coin_space.keys())
    y_20_flips = list(weight_coin_space.values())
    prob_x_20_flips = [val / coin_space_size for val in y_20_flips]

    x_10_frequencies = [head_count / 10 for head_count in x_10_flips]
    x_20_frequencies = [head_count / 20 for head_count in x_20_flips]

    plt.scatter(x_10_frequencies, prob_x_10_flips)
    plt.plot(x_10_frequencies, prob_x_10_flips, label='A: 10 coin-flips')

    plt.scatter(x_20_frequencies, prob_x_20_flips,  marker='x')
    plt.plot(x_20_frequencies, prob_x_20_flips, linestyle='--', label='B: 20 coin-flips')

    plt.xlabel('Head frequency')
    plt.ylabel('Probability of x heads')
    plt.legend()
    plt.show()


def listing_2_17():
    """Построение выровненных кривых относительной вероятности"""
    # 10 flips
    weight_coin_space = get_weight_coin_space(num_flips=10)
    coin_space_size = sum(weight_coin_space.values())
    x_10_flips = list(weight_coin_space.keys())
    y_10_flips = list(weight_coin_space.values())
    prob_x_10_flips = [val / coin_space_size for val in y_10_flips]
    # 20 flips
    weight_coin_space = get_weight_coin_space(num_flips=20)
    coin_space_size = sum(weight_coin_space.values())
    x_20_flips = list(weight_coin_space.keys())
    y_20_flips = list(weight_coin_space.values())
    prob_x_20_flips = [val / coin_space_size for val in y_20_flips]
    # 30 flips
    weight_coin_space = get_weight_coin_space(num_flips=30)
    coin_space_size = sum(weight_coin_space.values())
    x_30_flips = list(weight_coin_space.keys())
    y_30_flips = list(weight_coin_space.values())
    prob_x_30_flips = [val / coin_space_size for val in y_30_flips]

    x_10_frequencies = [head_count / 10 for head_count in x_10_flips]
    x_20_frequencies = [head_count / 20 for head_count in x_20_flips]
    x_30_frequencies = [head_count / 50 for head_count in x_30_flips]

    relative_likelihood_10 = [10 * prob for prob in prob_x_10_flips]
    relative_likelihood_20 = [20 * prob for prob in prob_x_20_flips]
    relative_likelihood_30 = [200 * prob for prob in prob_x_30_flips]

    plt.plot(x_10_frequencies, relative_likelihood_10, label='A: 10 coin-flips')
    plt.plot(x_20_frequencies, relative_likelihood_20, linestyle=':', color='k', label='B: 20 coin-flips')
    plt.plot(x_30_frequencies, relative_likelihood_30, linestyle='--', color='r', label='C: 50 coin-flips')

    where_10 = [not is_in_interval(val, 3, 7) for val in x_10_flips]
    where_20 = [not is_in_interval(val, 5, 15) for val in x_20_flips]
    where_30 = [not is_in_interval(val, 5, 15) for val in x_30_flips]

    plt.fill_between(x_10_frequencies, relative_likelihood_10, where=where_10)
    plt.fill_between(x_20_frequencies, relative_likelihood_20, where=where_20)
    plt.fill_between(x_30_frequencies, relative_likelihood_30, where=where_30)

    plt.xlabel('Head frequency')
    plt.ylabel('Probability of x heads')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    # listing_2_2()
    # listing_2_3()
    # listing_2_4()
    # listing_2_5()
    # listing_2_6()
    # listing_2_7()
    # listing_2_8()
    # listing_2_10()
    # listing_2_11()
    # listing_2_12()
    # listing_2_14()
    # listing_2_15()
    listing_2_17()
