import time

from utils import (
    csv_to_list,
    get_action_cost,
    get_action_name,
    get_action_profit,
    get_optimal_cost,
    get_optimal_profit,
    print_time,
)


def build_matrice(invest_max, actions):
    """
    Build a matrice with len(actions) + 1 rows and range(invest_max + 1)
    columns
    """
    matrice = [[0 for x in range(invest_max + 1)] for x in range(len(actions) + 1)]
    for i in range(1, len(actions) + 1):
        for invest in range(1, invest_max + 1):
            if get_action_cost(i - 1, actions) <= invest:
                matrice[i][invest] = max(
                    get_action_profit(i - 1, actions)
                    + matrice[i - 1][invest - get_action_cost(i - 1, actions)],
                    matrice[i - 1][invest],
                )
            else:
                matrice[i][invest] = matrice[i - 1][invest]
    return matrice, invest


def calculate_optimal_solution(invest_max, actions, matrice, invest):
    i = invest_max
    n = len(actions)
    optimal_actions = []
    while invest >= 0 and n >= 0:
        b = get_action_profit(n - 1, actions)
        c = get_action_cost(n - 1, actions)
        if matrice[n][i] == matrice[n - 1][i - c] + b:
            optimal_actions.append(
                [
                    get_action_name(n - 1, actions),
                    get_action_cost(n - 1, actions),
                    get_action_profit(n - 1, actions),
                ]
            )
            i -= c

        n -= 1
    print(optimal_actions)
    optimal_profit = get_optimal_profit(optimal_actions)
    total_cost = get_optimal_cost(optimal_actions)

    return optimal_profit, total_cost


def optimized_algo(invest_max, actions):
    """
    Calculate and display the optimal solution for a problem of maximization
    of 1 variable with an other one which is limiting

    Args:
        invest_max (int): the number each combination cost has not to exceed
        actions (list): a list with actions' informations
    """
    (matrice, invest) = build_matrice(invest_max, actions)
    (
        optimal_profit,
        total_cost,
    ) = calculate_optimal_solution(invest_max, actions, matrice, invest)
    print("The total cost is {} €".format(total_cost))
    print("The total profit is {} €\n".format(optimal_profit))


data = csv_to_list("actions.csv")
data1_sienna = csv_to_list("dataset1.csv")
data2_sienna = csv_to_list("dataset2.csv")
start_time = time.time()

optimized_algo(500, data)
# optimized_algo(50000, data1_sienna)
# optimized_algo(50000, data2_sienna)
interval = time.time() - start_time
print_time(interval, "optimized")
