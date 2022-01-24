import json

data = {
    "uav_count": 5,
    "formation": {
        0: [0, 0],
        1: [2, 0],
        2: [2, 2],
        3: [0, 2],
        4: [1, 1]
    }
}

with open("conf/example_data.json", "w") as f:
    json.dump(data, f)