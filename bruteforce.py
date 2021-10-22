import time

from utils import action_cost, action_number, action_profit, print_time


def get_binary_combination(num_item):
    """
    Return a list with all combinations convert in binary number
    Args:
        num_item(int): the number of item use to make combinations
    """
    number_possibilities = [i for i in range(2 ** num_item)]
    table_binary = [bin(i)[2:] for i in number_possibilities]
    return ["0" * (num_item - len(k)) + k for k in table_binary]


def get_good_combinations(num_item, invest_max, binary_combination):
    """
    Return a list a combinations which respect the constraint of invest_max
    Args:
        num_item (int): the number of item use to make combinations
        invest_max (int): the number each combination cost has not to exceed
        binary_combination (list): list of combination in binary number
    """
    good_combinations = []
    for combination in binary_combination:
        cost_combination = 0
        profit_combination = 0
        for i in range(num_item):
            if combination[i] == "1":
                cost_combination += action_cost(i)
                profit_combination += action_profit(i)
        print(combination)
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


def display_optimal_solution(optimal_solution, invest_max):
    """
    Display informations about the best solution
    Args:
        optimal_solution (dict): dictionnary which contains the best solution
        information
        invest_max (int): the number each combination cost has not to exceed
    """
    optimal_actions = []
    optimal_costs = []
    optimal_profits = []
    total_cost = 0
    total_profit = 0
    for i in range(len(optimal_solution["optimal_combination"])):
        if optimal_solution["optimal_combination"][i] == "1":
            optimal_actions.append(action_number(i))
            optimal_costs.append(action_cost(i))
            optimal_profits.append(round(action_profit(i), 2))
            total_cost += action_cost(i)
            total_profit += round(action_profit(i), 2)
    print(
        "\nThe list of actions to buy to maximize profit with a limit "
        + "of {} € spent is {}".format(invest_max, optimal_actions)
    )
    print("The total cost is {} €".format(total_cost))
    print("The total profit is {} €\n".format(round(total_profit, 2)))


def brute_force_algo(num_item, invest_max):
    """
    Calculate and display the optimal solution for a problem of maximization of
    1 variable with an other one which is limiting

    Args:
        num_item (int): the number of item use to make combinations
        invest_max (int): the number each combination cost has not to exceed
    """
    binary_combination = get_binary_combination(num_item)
    good_combinations = get_good_combinations(
        num_item,
        invest_max,
        binary_combination,
    )
    optimal_solution = get_optimal_solution(good_combinations)
    display_optimal_solution(optimal_solution, invest_max)


start_time = time.time()
brute_force_algo(20, 500)
interval = time.time() - start_time
print_time(interval)
