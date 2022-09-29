from collections import defaultdict


class State:
    states = {}

    def __init__(self, name):
        self.name = name
        self.transit_count = defaultdict(int)
        self.emission_count = {char: 0 for char in alphabet}
        self.adjacent_states = []
        State.states[name] = self

    def __str__(self):
        return self.name


def get_seed_alignment():
    for i in range(TEXT_LEN):
        space_count = sum([int(text[i] == '-') for text in alignment])
        yield space_count / len(alignment) < threshold


def add_edges(column_count):
    State.states['S'].adjacent_states = ['M1', 'I0', 'D1']
    State.states[f'I{column_count}'].adjacent_states = [f'I{column_count}', 'E']
    State.states[f'D{column_count}'].adjacent_states = [f'I{column_count}', 'E']
    State.states[f'M{column_count}'].adjacent_states = [f'I{column_count}', 'E']
    for i in range(column_count):
        if i > 0:
            State.states[f'M{i}'].adjacent_states = [f'I{i}', f'M{i + 1}', f'D{i + 1}']
            State.states[f'D{i}'].adjacent_states = [f'I{i}', f'M{i + 1}', f'D{i + 1}']
        State.states[f'I{i}'].adjacent_states = [f'I{i}', f'M{i + 1}', f'D{i + 1}']


def generate_states(non_seed_count):
    states = ['S', 'I0']
    for i in range(TEXT_LEN - non_seed_count):
        states.extend([f'M{i + 1}', f'D{i + 1}', f'I{i + 1}'])
    states.append('E')
    for state in states:
        State(state)
    add_edges(TEXT_LEN - non_seed_count)
    return states


def calc_transition_prob(states_arr, column_in_seed):
    result = {state: {state2: 0 for state2 in states_arr} for state in states_arr}
    state_count = {state: 0 for state in states_arr}
    alignment_states = []
    for text in alignment:
        states = []
        for i in range(TEXT_LEN):
            if column_in_seed[i]:
                states.append('D' if text[i] == '-' else 'M')
            else:
                if text[i] != '-':
                    states.append('I')
        i = j = 0
        while i < TEXT_LEN - column_in_seed.count(False):
            if states[j] == 'I':
                states[j] += str(i)
            else:
                states[j] += str(i + 1)
                i += 1
            j += 1
        # spit for last column not being in seed
        if not column_in_seed[-1] and states[-1] == 'I':
            states[-1] += str(i)
        #
        states = ['S'] + states + ['E']
        alignment_states.append(states)
        # print(states)
        for i in range(len(states) - 1):
            state_count[states[i]] += 1
            result[states[i]][states[i + 1]] += 1

    # map to transition probability
    for k in result.keys():
        if state_count[k] > 0:
            result[k] = list(map(lambda key: key / state_count[k], result[k].values()))
        else:
            result[k] = list(map(float, result[k].values()))

    # Pseudocount
    for state in State.states.values():
        for adj in state.adjacent_states:
            result[state.name][states_arr.index(adj)] += pseudocount
    # Normalization
    for k in result.keys():
        if k != 'E':
            result[k] = list(map(lambda key: key / sum(result[k]), result[k]))

    return result, alignment_states, state_count


def print_transition(states_arr, transition):
    print('\t'.join(states_arr))
    for k, v in transition.items():
        print(k, '  ', end='')
        print(*v)  # round 3


def calc_transition_emission():
    column_in_seed = list(get_seed_alignment())
    states_arr = generate_states(column_in_seed.count(False))
    transition, alignment_states, state_count = calc_transition_prob(states_arr, column_in_seed)
    print_transition(states_arr, transition)
    print('--------')
    calc_emission_prob(alignment_states, state_count, column_in_seed)


def calc_emission_prob(alignment_states, state_count, column_in_seed):
    print(*alphabet)
    for i in range(len(alignment)):
        state_arr = alignment_states[i][1:-1]
        text = alignment[i]
        idx = 0
        for j in range(len(text)):
            if not column_in_seed[j]:
                if text[idx] == '-':
                    text = text[:idx] + text[idx + 1:]
                else:
                    idx += 1
            else:
                idx += 1
        # print(text, state_arr)
        for j in range(len(text)):
            if state_arr[j][0] != 'D':
                State.states[state_arr[j]].emission_count[text[j]] += 1
    # map to transition probability
    for k in State.states.keys():
        if state_count[k] > 0:
            State.states[k].emission_count = list(map(lambda key: key / state_count[k], State.states[k].emission_count.values()))
        else:
            State.states[k].emission_count = list(map(float, State.states[k].emission_count.values()))

    # Pseudocount
    for state in State.states.values():
        if state.name[0] not in ['D', 'E']:
            for k in range(len(state.emission_count)):
                state.emission_count[k] += pseudocount

    # Normalization
    for state in State.states.values():
        if state.name[0] not in ['D', 'E']:
            state.emission_count = list(map(lambda item: item / sum(state.emission_count), state.emission_count))

    for state in State.states.values():
        print(state.name, *state.emission_count)


if __name__ == '__main__':
    threshold, pseudocount = map(float, input().split())
    input()  # ---
    alphabet = input().split()
    input()  # ---
    alignment = []
    while string := input():
        alignment.append(string)
    TEXT_LEN = len(alignment[0])
    calc_transition_emission()