import time

from sys import argv

from utils import (
    csv_to_list,
    get_action_cost,
    get_action_name,
    get_action_profit,
    print_time,
)


def get_binary_combination(num_item):
    """
    Return a list with all combinations convert in binary number
    Args:
        num_item(int): the number of item use to make combinations
    """
    number_possibilities = [i for i in range(2 ** num_item)]
    table_binary = [bin(i)[2:] for i in number_possibilities]
    return ["0" * (num_item - len(k)) + k for k in table_binary]


def get_good_combinations(num_item, invest_max, binary_combination, actions):
    """
    Return a list a combinations which respect the constraint of invest_max
    Args:
        num_item (int): the number of item use to make combinations
        invest_max (int): the number each combination cost has not to exceed
        binary_combination (list): list of combination in binary number
        actions (list): list of actions to optimize
    """
    good_combinations = []
    for combination in binary_combination:
        cost_combination = 0
        profit_combination = 0
        for i in range(num_item):
            if combination[i] == "1":
                cost_combination += get_action_cost(i, actions)
                profit_combination += get_action_profit(i, actions)
        if cost_combination <= invest_max:
            good_combinations.append([combination, profit_combination])
    return good_combinations


def get_optimal_solution(good_combinations):
    """
    Return a dictionary which contains the optimal combination and optimal profit
    Args:
        good_combination (list): list of combinations in binary number
    """

    optimal_solution = {
        "optimal_combination": good_combinations[0][0],
        "optimal_profit": good_combinations[0][1],
    }
    for combination in good_combinations:
        if combination[1] > optimal_solution["optimal_profit"]:
            optimal_solution["optimal_combination"] = combination[0]
            optimal_solution["optimal_profit"] = combination[1]
    return optimal_solution


def display_optimal_solution(optimal_solution, invest_max, actions):
    """
    Display informations about the best solution
    Args:
        optimal_solution (dict): dictionnary which contains the best solution
        information
        invest_max (int): the number each combination cost has not to exceed
        actions (list): list of actions to optimize
    """
    optimal_actions = []
    optimal_costs = []
    optimal_profits = []
    total_cost = 0
    total_profit = 0
    for i in range(len(optimal_solution["optimal_combination"])):
        if optimal_solution["optimal_combination"][i] == "1":
            optimal_actions.append(get_action_name(i, actions))
            optimal_costs.append(get_action_cost(i, actions))
            optimal_profits.append(round(get_action_profit(i, actions), 2))
            total_cost += get_action_cost(i, actions)
            total_profit += round(get_action_profit(i, actions), 2)
    print(
        "\nThe list of actions to buy to maximize profit with a limit "
        + "of {} € spent is {}".format(invest_max, optimal_actions)
    )
    print("The total cost is {} €".format(total_cost))
    print("The total profit is {} €\n".format(round(total_profit, 2)))


def brute_force_algo(num_item, invest_max, actions):
    """
    Calculate and display the optimal solution for a problem of maximization of
    1 variable with an other one which is limiting
    Args:
        num_item (int): the number of item use to make combinations
        invest_max (int): the number each combination cost has not to exceed
        actions (list): list of actions to optimize
    """
    binary_combination = get_binary_combination(num_item)
    good_combinations = get_good_combinations(
        num_item, invest_max, binary_combination, actions
    )
    optimal_solution = get_optimal_solution(good_combinations)
    display_optimal_solution(optimal_solution, invest_max, actions)


start_time = time.time()

bruteforce, num_item, invest_max, actions = argv
num_item = int(argv[1])
invest_max = int(argv[2])
actions = csv_to_list(argv[3])

brute_force_algo(num_item, invest_max, actions)

interval = time.time() - start_time
print_time(interval, "brute force")
