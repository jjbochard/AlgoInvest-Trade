import json


def find_all_couples_of_2(list):
    couple_of_2 = []
    while len(list) != 0:
        for i in range(1, len(list)):
            couple_of_2.append(
                (
                    list[0]["action_number"],
                    list[i]["action_number"],
                )
            )
        list.pop(0)
    return couple_of_2


with open(
    "actions.json",
) as f:
    data = json.load(f)
    all_couples_of_2 = find_all_couples_of_2(data["actions"])
    print(all_couples_of_2)
