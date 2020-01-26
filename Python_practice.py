counties_dict = {"Arapahoe": 43322829, "Denver": 463353, "Jefferson": 432438}

for key in counties_dict.keys():
    print(f"{key} county has {counties_dict[key]:,}")
