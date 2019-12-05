def day4():
    start = 254032
    end = 789860
    total = 0

    for start in range(start, end):
        my_list = list(str(start))
        sorted_list = sorted(my_list)
        if my_list == sorted_list:
            my_set = set(my_list)
            total += 1
            if len(my_set) == len(my_list):
                # print("found an invalid one")
                total -= 1

    print("Total number of password combinations the little elves are going to have try:", total, "- Poor sods.")


if __name__ == "__main__":
    day4()
