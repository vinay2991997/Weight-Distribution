
from math import ceil, floor
import random


def weight_distribution_for_one(item_list, total_sum_needed, data, variance=2):

    if -variance <= total_sum_needed <= variance:
        return True
    if len(item_list) == 0:
        return False

    result = weight_distribution_for_one(
        item_list[1:], total_sum_needed-item_list[0].total_weight, data, variance)

    if result:
        data.append(item_list[0])
        return True

    else:
        return weight_distribution_for_one(item_list[1:], total_sum_needed, data, variance)


def weight_distribution_helper(item_list, result, total_sum_needed=[], variance=2):
    local_weight_list = list(item_list)
    random.shuffle(local_weight_list)

    for weight_needed in total_sum_needed:

        data = []
        if not (weight_distribution_for_one(local_weight_list, weight_needed, data, variance)):
            result.clear()
            return False

        result.append(data)

        for i in data:
            local_weight_list.remove(i)

    if len(local_weight_list) > 0:
        result.clear()
        return False
    return True


def weight_distribution(item_list, result, total_sum_needed_list=[]):

    max_weight_of_single_bale = 83

    total_sum_of_weight = sum([item.total_weight for item in item_list])
    no_of_bales = ceil(total_sum_of_weight/max_weight_of_single_bale)
    total_sum_needed = ceil(total_sum_of_weight/no_of_bales)

    if total_sum_needed_list == []:
        total_sum_needed_list = [total_sum_needed] * no_of_bales

    if sum(total_sum_needed_list) < total_sum_of_weight:
        print('WARNING!!!!!!')
        print('TOTAL NEEDED WEIGHT < TOTAL WEIGHT OF ITEMS ==> SOME ITEMS WILL BE LEFT')


    variance = 0
    fail_count = 0
    fail_count_limit = 50
    while not (weight_distribution_helper(item_list, result, total_sum_needed_list, variance)):
        fail_count += 1
        variance = floor(fail_count/fail_count_limit)
         
