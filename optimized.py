from utils import action_cost, action_benefit, action_number, print_time, list_actions

data = list_actions()

def optimized_algo(invest_max, actions):
    matrice = [[0 for x in range (invest_max + 1)] for x in range(len(actions)+1)]
    for i in range(1, len(actions) + 1):
        for invest in range(1, invest_max + 1):
            if action_cost(i-1) <= invest:
                matrice[i][invest] = max(action_benefit(i-1) + matrice[i-1][invest-action_cost(i-1)], matrice[i-1][invest])
            else:
                matrice[i][invest] = matrice[i-1][invest]

    print(matrice)

optimized_algo(200, data)