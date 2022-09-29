def emission_prob_log(p_i, x_i):
    return emission_matrix[p_i][emissions.index(x_i)]


def transition_prob_log(p_i_1, p_i):
    return transition_matrix[p_i_1][states.index(p_i)]


def forward():
    s = [{state: 1 / len(states) for state in states}]  # ?? / |States|

    for i in range(1, len(outcome)):
        s.append({})
        for state in states:
            probs = []
            for prev_state in states:
                if i == 1:
                    probs.append((prev_state,
                                  s[i - 1][prev_state]
                                  * (1 / len(states))
                                  * emission_prob_log(state, outcome[i])))
                else:
                    probs.append((prev_state,
                                  s[i - 1][prev_state]
                                  * transition_prob_log(prev_state, state)
                                  * emission_prob_log(state, outcome[i])))

            prev_state_sum = sum(map(lambda k: k[1], probs))
            s[i][state] = prev_state_sum

    return sum(s[-1].values())


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
    print(forward())