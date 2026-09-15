def sets_intersection(*sets):
    if not sets:
        return set()

    if len(sets) == 1:
        return sets[0].copy()

    super_set = sets[0]
    for current_set in sets:
        super_set = super_set & current_set

    return super_set


if __name__ == '__main__':
    print(sets_intersection({55, 6}, {2, 6}, {6, 44}))
