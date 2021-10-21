import json
import time


def print_time(raw_interval):
    """
    Calculate and print the time in minutes and seconds from a time in seconds
    Args:
        raw_interval (int): A time in seconds
    """
    interval_in_min = raw_interval / 60
    extra_sec = round(interval_in_min % 1, 2)
    interval_in_sec = round(extra_sec * 60)
    print(
        "The brute force solution has been found in "
        + str(round(interval_in_min))
        + " minutes et "
        + str(interval_in_sec)
        + " seconds."
    )


def action_benefit(action):
    """
    Return the value of the cost * 2years_benefit of a choosen action from
    actions.json
    Args:
        action (int): n represent action_number n+1
    """
    with open(
        "actions.json",
    ) as f:
        data = json.load(f)
        return (
            data["actions"][action]["cost_per_action"]
            * data["actions"][action]["2year_benefit"]
        )


def action_cost(action):
    """
    Return the cost of a choosen action from actions.json
    Args:
        action (int): n represent action_number n+1
    """
    with open(
        "actions.json",
    ) as f:
        data = json.load(f)
        return data["actions"][action]["cost_per_action"]


def action_number(action):
    """
    Return the number of a choosen action from actions.json
    Args:
        action (int): n represent action_number n+1
    """
    with open(
        "actions.json",
    ) as f:
        data = json.load(f)
        return data["actions"][action]["action_number"]


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
    Return a list a combinations wich respect the constraint of invest_max
    Args:
        num_item (int): the number of item use to make combinations
        invest_max (int): the number each combination cost has not to exceed
        binary_combination (list): list of combination in binary number
    """
    good_combinations = []
    for combination in binary_combination:
        cost_combination = 0
        benefit_combination = 0
        for i in range(num_item):
            if combination[i] == "1":
                cost_combination += action_cost(i)
                benefit_combination += action_benefit(i)
        print(combination)
        if cost_combination <= invest_max:
            good_combinations.append([combination, benefit_combination])
    return good_combinations


def get_optimal_solution(good_combinations):
    """
    Return a dictionary which contains the optimal combination and optimal
    benefit
    Args:
        good_combination (list): list of combinations in binary number
    """

    optimal_solution = {
        "optimal_combination": good_combinations[0][0],
        "optimal_benefit": good_combinations[0][1],
    }
    for combination in good_combinations:
        if combination[1] > optimal_solution["optimal_benefit"]:
            optimal_solution["optimal_combination"] = combination[0]
            optimal_solution["optimal_benefit"] = combination[1]
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
    total_cost = 0
    total_benefit = 0
    for i in range(len(optimal_solution)):
        if optimal_solution["optimal_combination"][i] == "1":
            optimal_actions.append(action_number(i))
            optimal_costs.append(action_cost(i))
            total_cost += action_cost(i)
            total_benefit += round(action_benefit(i), 2)
    print(
        "The list of actions to buy to maximize benefit with a limit "
        + "of {} € spent is {}".format(invest_max, optimal_actions)
    )
    print("The cost for each action is {}".format(optimal_costs))
    print("The total cost is {} €".format(total_cost))
    print("The total benefit is {} €".format(round(total_benefit, 2)))


def brute_force_algo(num_item, invest_max):
    """
    Calculate and display the optimal solution for a problem of maximization
    and minimization of 2 variables

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
brute_force_algo(20, 200)
interval = time.time() - start_time
print_time(interval)
