from utils import action_cost, action_number, action_profit, csv_to_list, list_actions


def build_matrice(invest_max, actions):
    """
    Build a matrice with len(actions) + 1 rows and range(invest_max + 1)
    columns
    """
    matrice = [[0 for x in range(invest_max + 1)] for x in range(len(actions) + 1)]
    for i in range(1, len(actions) + 1):
        for invest in range(1, invest_max + 1):
            if action_cost(i - 1) <= invest:
                matrice[i][invest] = max(
                    action_profit(i - 1) + matrice[i - 1][invest - action_cost(i - 1)],
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
        b = action_profit(n - 1)
        c = action_cost(n - 1)
        if matrice[n][i] == matrice[n - 1][i - c] + b:
            optimal_actions.append(action_number(n - 1))
            i -= c

        n -= 1

    optimal_profit = [action_profit(action - 1) for action in optimal_actions]
    total_cost = sum(action_cost(action - 1) for action in optimal_actions)

    return optimal_actions, optimal_profit, total_cost


def optimized_algo(invest_max, actions):
    """
    Calculate and display the optimal solution for a problem of maximization
    of 1 variable with an other one which is limiting

    Args:
        invest_max (int): the number each combination cost has not to exceed
        actions (list): a list with actions' informations
    """
    (matrice, invest) = build_matrice(invest_max, actions)
    (optimal_actions, optimal_profit, total_cost) = calculate_optimal_solution(
        invest_max, actions, matrice, invest
    )
    print(
        "\nThe list of actions to buy to maximize profit with a limit "
        + "of {} € spent is {}".format(invest_max, sorted(optimal_actions))
    )
    print("The total cost is {} €".format(total_cost))
    print("The total profit is {} €\n".format(sum(optimal_profit)))


data = list_actions()
data1_sienna = csv_to_list("dataset1.csv")


optimized_algo(500, data)
