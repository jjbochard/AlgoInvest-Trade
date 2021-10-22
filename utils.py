import csv
import json


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


def action_profit(action):
    """
    Return the value of the profit of a choosen action from actions.json
    Args:
        action (int): n represent action_number n+1
    """
    with open(
        "actions.json",
    ) as f:
        data = json.load(f)
        return data["actions"][action]["profit"]


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


def list_actions():
    with open(
        "actions.json",
    ) as f:
        data = json.load(f)
        return data["actions"]


def csv_to_list(file_name):
    with open(file_name, newline="") as f:
        reader = csv.reader(f)
        raw_data = list(reader)
    raw_data.pop(0)
    return [{"price": float(d[1]), "profit": float(d[2])} for d in raw_data]
