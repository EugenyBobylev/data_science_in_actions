from collections import defaultdict

import numpy as np
import matplotlib.pyplot as plt


def listing_3_1():
    die_rolls = [np.random.randint(1, 7) for _ in range(3)]
    assert die_rolls == [5, 6, 1]


def frequency_head(coin_flips_sequence):
    """симуляция подбрасывание честной монеты"""
    total_heads = sum([head for head in coin_flips_sequence if head == 1])
    head_frequency = total_heads / len(coin_flips_sequence)
    return head_frequency


def listing_3_5():
    """симуляция 10 подбрасываний честной монеты"""
    coin_flip_sequence = [np.random.randint(0, 2) for _ in range(10)]
    total_heads = frequency_head(coin_flip_sequence)
    print(f'Frequency of heads is {total_heads}')


def listing_3_6():
    """Отрисовка частот исходов с орлом при симулированных подбрасываниях монеты"""
    coin_flips = []
    frequencies = []
    for coin_flip in range(1, 1000):
        coin_flips.append(np.random.randint(0, 2))
        frequencies.append(frequency_head(coin_flips))

    plt.plot(list(range(1, 1000)), frequencies)
    plt.axhline(0.5, color='k')
    plt.xlabel('Number of Coin Flips')
    plt.ylabel('Head-Frequency')
    plt.show()


def listing_3_7():
    """Симуляция подбрасывания монеты со смещением"""
    print("Let's flip the biased coin once.")
    coin_flip = np.random.binomial(1, 0.7)  # симуляция монеты, которая падает орлом вверх в 70 % случаев
    print(f"Biased coin landed on {'heads' if coin_flip == 1 else 'tails'}.")
    print("\nLet's flip the biased coin 10 times.")
    number_coin_flips = 10
    head_count = np.random.binomial(number_coin_flips, .7)
    print(f"{head_count} heads were observed out of {number_coin_flips} biased coin flips")


def listing_3_8():
    """ Вычисление схождения частоты исходов с орлом"""
    head_count = np.random.binomial(1000, 0.7)
    frequency = head_count / 1000
    print(f'Frequency of Heads is {frequency}')


def listing_3_9():
    """Повторное вычисление схождения частоты исходов с орлом"""
    assert np.random.binomial(1000, 0.7) / 1000 == 0.697  #
    for i in range(1, 6):
        head_count = np.random.binomial(1000, 0.7)
        frequency = head_count / 1000
        print(f"Frequency at iteration {i} is {frequency}")
        if frequency == 0.7:
            print("    Frequency equals the probability!\n")


def listing_3_10():
    """ Вычисление частот исходов с орлами в 500 итерациях"""
    head_count_array: np.ndarray = np.random.binomial(1000, 0.7, 500)
    frequency_array: np.ndarray = head_count_array / 1000
    return head_count_array, frequency_array


def listing_3_12():
    """Поиск максимального и минимального значений частот"""
    head_count_array, frequency_array = listing_3_10()
    min_freq = frequency_array.min()
    max_freq = frequency_array.max()
    diff_freq = max_freq - min_freq

    print(f"Minimum frequency observed: {min_freq}")
    print(f"Maximum frequency observed: {max_freq}")
    print(f"Difference across frequency range: {diff_freq}")


def listing_3_17():
    """Отрисовка измеренных частот"""
    head_count_array, frequency_array = listing_3_10()

    frequency_counts = defaultdict(int)
    for frequency in frequency_array:
        frequency_counts[frequency] += 1
    frequencies = list(frequency_counts.keys())
    counts = [frequency_counts[freq] for freq in frequencies]
    plt.scatter(frequencies, counts)
    plt.xlabel('Frequency')
    plt.ylabel('Count')
    plt.show()


def output_bin_coverage(counts: np.ndarray, bin_edges: np.ndarray, idx: int):
    """Получение диапазона частот в интервале и его размера"""
    count = int(counts[idx])  # интервал idx, содержит содержит counts[idx] частот
    range_start, range_end = bin_edges[idx], bin_edges[idx + 1]
    range_string = f"{range_start} — {range_end}"
    print((f"The bin for frequency range {range_string} contains {count} element{'' if count == 1 else 's'}"))


def listing_3_18():
    """Построение гистограммы частот с помощью plt.hist"""
    head_count_array, frequency_array = listing_3_10()
    counts, bin_edges, _ = plt.hist(frequency_array, bins='auto', edgecolor='black')
    plt.xlabel('Binned Frequency')
    plt.ylabel('Count')
    plt.show()

    # Подсчет количества, ширины интервалов в гистограмме
    bin_width = bin_edges[1] - bin_edges[0]
    print(f'Number of beans = {counts.size}; Bin width = {bin_width:.5f}')
    # Получение диапазона частот в интервале и его размера
    output_bin_coverage(counts, bin_edges, 0)
    output_bin_coverage(counts, bin_edges, 5)
    output_bin_coverage(counts, bin_edges, counts.argmax())  # Поиск индекса максимального значения в массиве


def listing_3_24():
    """Отрисовка относительных вероятностей гистограммы"""
    head_count_array, frequency_array = listing_3_10()
    likelihoods, bin_edges, _ = plt.hist(frequency_array, bins='auto', edgecolor='black', density=True)
    plt.xlabel('Binned Frequency')
    plt.ylabel('Relative Likelihood')
    plt.show()

    # суммируем площади прямоугольников всех интервалов, каждая из которых равняется значению
    # вертикальной вероятности интервала, умноженному на bin_width
    bin_width = bin_edges[1] - bin_edges[0]
    assert likelihoods.sum() * bin_width == 1.0

    #  Вычисление вероятности получения частот пика
    index = likelihoods.argmax()
    area = likelihoods[index] * bin_width
    range_start, range_end = bin_edges[index], bin_edges[index + 1]
    range_string = f"{range_start} — {range_end}"
    print(f"Sampled frequency falls within interval {range_string} with probability {area}")


def compute_high_confidence_interval(likelihoods, bin_edges):
    """Вычисление доверительного интервала"""
    peak_index = likelihoods.argmax()

    bin_width = bin_edges[1] - bin_edges[0]
    area = likelihoods[peak_index] * bin_width
    start_index, end_index = peak_index, peak_index + 1
    while area < 0.95:
        if start_index > 0:
            start_index -= 1
        if end_index < likelihoods.size - 1:
            end_index += 1
        area = likelihoods[start_index: end_index + 1].sum() * bin_width

    range_start, range_end = bin_edges[start_index], bin_edges[end_index]
    range_string = f"{range_start:.6f} — {range_end:.6f}"
    print(f"The frequency range {range_string} represents a {100 * area:.2f} % confidence interval")
    return start_index, end_index


def listing_3_28():
    """Вычисление высокого доверительного интервала"""
    head_count_array, frequency_array = listing_3_10()
    likelihoods, bin_edges, _ = plt.hist(frequency_array, bins='auto', edgecolor='black', density=True)
    compute_high_confidence_interval(likelihoods, bin_edges)


def listing_3_29():
    """ Вычисление частот исходов с орлами в 100_000 итерациях"""
    head_count_array: np.ndarray = np.random.binomial(1000, 0.7, 100_000)
    frequency_array: np.ndarray = head_count_array / 1000
    return head_count_array, frequency_array


def listing_3_30():
    """"""
    head_count_array, frequency_array = listing_3_29()
    likelihoods, bin_edges, patches = plt.hist(frequency_array, bins='auto', edgecolor='black', density=True)
    start_index, end_index = compute_high_confidence_interval(likelihoods, bin_edges)

    # Закрашивание столбцов гистограммы в интервале
    for i in range(start_index, end_index):
        patches[i].set_facecolor('yellow')
    plt.xlabel('Binned Frequency')
    plt.ylabel('Relative Likelihood')
    plt.show()


def listing_3_31():
    """ Анализ 5 млрд подбрасываний монеты"""
    head_count_array: np.ndarray = np.random.binomial(50_000, 0.7, 100_000)
    frequency_array: np.ndarray = head_count_array / 50_000

    likelihoods, bin_edges, patches = plt.hist(frequency_array, bins='auto', edgecolor='black', density=True)
    start_index, end_index = compute_high_confidence_interval(likelihoods, bin_edges)
    range_start, range_end = bin_edges[start_index], bin_edges[end_index]
    print(f"{range_start:.2f} — {range_end:.2f}")

    # Закрашивание столбцов гистограммы в интервале
    for i in range(start_index, end_index):
        patches[i].set_facecolor('yellow')
    plt.xlabel('Binned Frequency')
    plt.ylabel('Relative Likelihood')
    plt.show()


def listing_3_32():
    """Вычисление гистограммы с помощью np.histogram"""
    head_count_array: np.ndarray = np.random.binomial(50_000, 0.7, 100_000)
    frequency_array: np.ndarray = head_count_array / 50_000
    
    likelihoods, bin_edges = np.histogram(frequency_array, bins='auto', density=True)
    compute_high_confidence_interval(likelihoods, bin_edges)


if __name__ == '__main__':
    np.random.seed(0)
    # listing_3_1()
    # listing_3_5()
    # listing_3_6()
    # listing_3_7()
    # listing_3_8()
    # listing_3_9()
    # listing_3_10()
    # listing_3_17()
    # listing_3_18()
    # listing_3_24()
    # listing_3_28()
    # listing_3_30()
    # listing_3_31()
    listing_3_32()
