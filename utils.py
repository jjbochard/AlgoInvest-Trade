import csv


def print_time(raw_interval, algo_name):
    """
    Calculate and print the time in minutes and seconds from a time in seconds
    Args:
        raw_interval (int): A time in seconds
    """
    interval_in_min = raw_interval / 60
    extra_sec = round(interval_in_min % 1, 2)
    interval_in_sec = round(extra_sec * 60)
    print(
        "The "
        + algo_name
        + " solution has been found in "
        + str(round(interval_in_min))
        + " minutes et "
        + str(interval_in_sec)
        + " seconds."
    )


def get_action_profit(action, dict):
    """
    Return the value of the profit of a choosen action from actions.json
    Args:
        action (int): n represent action_number n+1
    """
    if len(dict) > 20:
        return dict[action]["profit"]*dict[action]["cost_per_action"]
    else:
        return dict[action]["profit"]*dict[action]["cost_per_action"]/100


def get_action_cost(action, dict):
    """
    Return the cost of a choosen action from actions.json
    Args:
        action (int): n represent action_number n+1
    """
    if len(dict) > 20:
        return round(dict[action]["cost_per_action"] * 100)
    else:
        return round(dict[action]["cost_per_action"])


def get_action_name(action, dict):
    """
    Return the name of a choosen action from actions.csv
    Args:
        action (int): n represent action_number n+1
    """
    return dict[action]["action_name"]


def get_optimal_profit(optimal_actions):
    if optimal_actions[0][0].startswith("Share"):
        return round(sum((action[2] / 100) for action in optimal_actions), 2)
    else:
        return round(sum((action[2]) for action in optimal_actions), 2)


def get_optimal_cost(optimal_actions):
    if optimal_actions[0][0].startswith("Share"):
        return round(sum((action[1] / 100) for action in optimal_actions), 2)
    else:
        return round(sum((action[1]) for action in optimal_actions), 2)


def csv_to_list(file_name):
    with open(file_name, newline="") as f:
        reader = csv.reader(f)
        raw_data = list(reader)
    raw_data.pop(0)
    return sorted(
        [
            {"action_name": d[0], "cost_per_action": float(d[1]), "profit": float(d[2])}
            for d in raw_data
            if float(d[1]) > 0 and float(d[2]) > 0
        ],
        key=lambda i: i["cost_per_action"],
    )
