from math import log


def emission_prob_log(p_i, x_i):
    return log(emission_matrix[p_i][emissions.index(x_i)])


def transition_prob_log(p_i_1, p_i):
    return log(transition_matrix[p_i_1][states.index(p_i)])


def viterbi():
    s = [{state: 0 for state in states}]  # store columns and init source
    max_states = []
    for i in range(1, len(outcome)):
        s.append({})
        col_max_prev = []
        for state in states:
            probs = []
            for prev_state in states:
                if i == 1:
                    probs.append((prev_state,
                                  s[i - 1][prev_state]
                                  + (1 / len(states))
                                  + emission_prob_log(state, outcome[i])))
                else:
                    probs.append((prev_state,
                                  s[i - 1][prev_state]
                                  + transition_prob_log(prev_state, state)
                                  + emission_prob_log(state, outcome[i])))
            max_prev_state = max(probs, key=lambda tpl: tpl[1])
            s[i][state] = max_prev_state[1]
            col_max_prev.append(max_prev_state[0])  # to be able to backtrack
        max_states.append(col_max_prev)
    return print_path(max(states, key=lambda state: s[-1][state]), max_states)


def print_path(best_state, max_states):
    result = best_state
    for column in max_states[::-1]:
        best_state = column[states.index(best_state)]
        result = best_state + result
    return result[1:]


if __name__ == '__main__':
    outcome = '-' + input()
    input()  # ---
    emissions = input().split()
    input()  # ---
    states = input().split()
    input(), input()  # ---
    transition_matrix = {}
    for state in states:
        transition_matrix[state] = list(map(float, input().split()[1:]))
    input(), input()  # ---
    emission_matrix = {}
    for state in states:
        emission_matrix[state] = list(map(float, input().split()[1:]))

    print(viterbi())