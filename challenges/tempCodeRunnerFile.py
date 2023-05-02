def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    active_users = 0
    for period in permanence_period:
        if target_time in list(range(period[0], period[1])):
            print(target_time, list(range(period[0], period[1])))
            active_users += 1
    return active_users


permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
print(study_schedule(permanence_period, 5))
