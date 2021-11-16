import time

from sys import argv

from utils import (
    csv_to_list,
    get_sienna_action_cost,
    get_action_name,
    get_sienna_action_profit,
    get_sienna_optimal_cost,
    get_sienna_optimal_profit,
    print_time,
)


def build_matrice(invest_max, actions):
    """
    Build a matrice with len(actions) + 1 rows and range(invest_max + 1) columns
    Args:
        invest_max (int): the number each combination cost has not to exceed
        actions (list): list of actions to optimize
    """
    # A matrice of len(actions) +1 rows and range (invest_max +1) is build
    matrice = [[0 for x in range(invest_max + 1)] for x in range(len(actions) + 1)]
    # For every rows (actions cost) in the matrice (except the first which is 0)
    for i in range(1, len(actions) + 1):
        # For every columns (price) in the matrice (except the first which is 0)
        for invest in range(1, invest_max + 1):
            # If the cost of the current action is inferior to the current price
            if get_sienna_action_cost(i, actions) <= invest:
                # We keep the max between the profit of the current action
                # and the profit of the action i-1 with a cost of invest - the cost of the current action
                matrice[i][invest] = max(
                    get_sienna_action_profit(i, actions)
                    + matrice[i - 1][invest - get_sienna_action_cost(i, actions)],
                    matrice[i - 1][invest],
                )
            else:
                # Else we keep the profit of the previous action
                matrice[i][invest] = matrice[i - 1][invest]
    return matrice, invest


def calculate_optimal_solution(actions, matrice, invest):
    """
    Return the optimal profit and the total cost from a matrice
    Args:
        actions (list): list of actions to optimize
        matrice (matrice): matrice of the action cost by invest
        invest (int): the current invest we check
    """
    n = len(actions)
    optimal_actions = []
    while invest >= 0 and n >= 0:
        b = get_sienna_action_profit(n, actions)
        c = get_sienna_action_cost(n, actions)
        # If the profit for an action n at a price invest is equal to
        # the profit of the action n-1 at a price invest - the price of the action n
        # + the profit of the action n,
        # that meens that we keep the action n
        if matrice[n][invest] == matrice[n - 1][invest - c] + b:
            optimal_actions.append(
                [
                    get_action_name(n, actions),
                    get_sienna_action_cost(n, actions),
                    get_sienna_action_profit(n, actions),
                ]
            )
            invest -= c

        n -= 1
    optimal_profit = get_sienna_optimal_profit(optimal_actions)
    total_cost = get_sienna_optimal_cost(optimal_actions)

    return optimal_profit, total_cost


def optimized_algo(invest_max, actions):
    """
    Calculate and display the optimal solution for a problem of maximization of 1 variable
    with an other one which is limiting

    Args:
        invest_max (int): the number each combination cost has not to exceed
        actions (list): a list with actions informations
    """
    (matrice, invest) = build_matrice(invest_max, actions)
    (
        optimal_profit,
        total_cost,
    ) = calculate_optimal_solution(actions, matrice, invest)
    print("The total cost is {} €".format(total_cost))
    print("The total profit is {} €\n".format(optimal_profit))


start_time = time.time()

sienna_optimized, invest_max, actions = argv
invest_max = int(argv[1])
actions = csv_to_list(argv[2])

optimized_algo(invest_max, actions)

interval = time.time() - start_time
print_time(interval, "optimized")
