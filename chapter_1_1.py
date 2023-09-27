

coin_space = {'Heads', 'Tails'}  # пространство события для монетки
weight_coin_space = {'Heads': 4, 'Tails': 1}


def is_heads_or_tails(outcome) -> bool:
    return outcome in coin_space


def is_neither_heads_or_tails(outcome) -> bool:
    return not is_heads_or_tails(outcome)


def is_heads(outcome) -> bool:
    return outcome == 'Heads'


def is_tails(outcome) -> bool:
    return outcome == 'Tails'


def get_matching_event(event_condition, generic_sample_space):
    return set([outcome for outcome in generic_sample_space if event_condition(outcome)])


def compute_probability(event_condition: callable, generic_sample_space: set|dict) -> float:
    event = get_matching_event(event_condition, generic_sample_space)
    if isinstance(generic_sample_space, set):
        return len(event) / len(generic_sample_space)

    # generic sample space is a dict
    event_size = sum(generic_sample_space[outcome] for outcome in event)
    return event_size / sum(generic_sample_space.values())


if __name__ == '__main__':
    event_conditions = [is_heads_or_tails, is_heads, is_tails, is_neither_heads_or_tails]
    for event_condition in event_conditions:
        prob = compute_probability(event_condition, weight_coin_space)
        name = event_condition.__name__
        print(f'Probability of event arising from {name} is {prob}')

    space_size = sum(weight_coin_space.values())
    assert space_size == 5
