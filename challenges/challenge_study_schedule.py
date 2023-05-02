def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    active_users = 0
    for period in permanence_period:
        if not isinstance(period, tuple) or period[0] > period[1]:
            return None
        if target_time in list(range(period[0], period[1] + 1)):
            active_users += 1
    return active_users
