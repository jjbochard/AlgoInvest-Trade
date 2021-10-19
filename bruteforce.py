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


def get_binary_combinaison(num_item):
    number_possibilities = [i for i in range(2 ** num_item)]
    table_binary = [bin(i)[2:] for i in number_possibilities]
    return ["0" * (num_item - len(k)) + k for k in table_binary]


def get_good_combinaisons(num_item, invest_max, binary_combinaison):
    good_combinaisons = []
    for combinaison in binary_combinaison:
        cost_combinaison = 0
        benefit_combinaison = 0
        for i in range(num_item):
            if combinaison[i] == "1":
                cost_combinaison += action_cost(i)
                benefit_combinaison += action_benefit(i)
        print(combinaison)
        if cost_combinaison <= invest_max:
            good_combinaisons.append([combinaison, benefit_combinaison])
    return good_combinaisons


def get_optimal_solution(good_combinaisons):
    optimal_solution = {
        "optimal_combinaison": good_combinaisons[0][0],
        "optimal_benefit": good_combinaisons[0][1],
    }
    for combinaison in good_combinaisons:
        if combinaison[1] > optimal_solution["optimal_benefit"]:
            optimal_solution["optimal_combinaison"] = combinaison[0]
            optimal_solution["optimal_benefit"] = combinaison[1]
    return optimal_solution


def display_optimal_solution(optimal_solution, invest_max):
    optimal_actions = []
    optimal_costs = []
    total_cost = 0
    total_benefit = 0
    for i in range(len(optimal_solution)):
        if optimal_solution["optimal_combinaison"][i] == "1":
            optimal_actions.append(action_number(i))
            optimal_costs.append(action_cost(i))
            total_cost += action_cost(i)
            total_benefit += round(action_benefit(i), 2)
    print(
        "The list of actions to buy to maximize benefit with a limit \n"
        "of {} € spent is {}".format(invest_max, optimal_actions)
    )
    print("The cost for each action is {}".format(optimal_costs))
    print("The total cost is {} €".format(total_cost))
    print("The total benefit is {} €".format(round(total_benefit, 2)))


def brute_force_algo(num_item, invest_max):
    binary_combinaison = get_binary_combinaison(num_item)
    good_combinaisons = get_good_combinaisons(
        num_item,
        invest_max,
        binary_combinaison,
    )
    optimal_solution = get_optimal_solution(good_combinaisons)
    display_optimal_solution(optimal_solution, invest_max)


start_time = time.time()
brute_force_algo(3, 100)
interval = time.time() - start_time
print_time(interval)
