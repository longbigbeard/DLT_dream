from get_history_info import get_exist_info


def check_num(num: list, filter_date='') -> list:
    """
    检查号码的历史中奖信息
    :param num: 待检号码
    :param filter_date: 过滤日期
    :return: 结果
    """
    exist_info, _ = get_exist_info()

    check_num_front = num[0:5]
    check_num_back = num[-2:]
    hit_list = []
    for exist in exist_info[1:]:
        exist = exist.split(' ')
        if filter_date and filter_date > exist[0]:
            print("check end", filter_date)
            break
        hit_front_num = [x for x in check_num_front if x in exist[1:6]]  # 前区
        hit_back_num = [x for x in check_num_back if x in exist[-2:]]    # 后区
        if len(hit_front_num) + len(hit_back_num) >= 2:                  # 至少命中2个数字才有可能
            hit_num_money = calculate_money(len(hit_front_num), len(hit_back_num))
            if hit_num_money > 0:
                data = {
                    "check_num": ' '.join(num),
                    "hit_num": ' '.join(exist[1:]),
                    "hit_front_num": ' '.join(hit_front_num),
                    "hit_back_num": ' '.join(hit_back_num),
                    "hit_num_date": exist[0],
                    "hit_num_money": hit_num_money
                }
                hit_list.append(data)

    return hit_list


def calculate_money(front_count: int, back_count: int) -> int:
    """
    正常来说一等奖和二等奖的奖金都是浮动的，一等奖给500万，二等奖给20万
    实际上，大多数一等奖会超过500万，二等奖会低于20万
    :param front_count: 前区命中数量
    :param back_count: 后区命中数量
    :return: 奖金
    """
    if front_count == 5 and back_count == 2:
        return 50000000
    elif front_count == 5 and back_count == 1:
        return 200000
    elif front_count == 5 and back_count == 0:
        return 10000
    elif front_count == 4 and back_count == 2:
        return 3000
    elif front_count == 4 and back_count == 1:
        return 300
    elif front_count == 3 and back_count == 2:
        return 200
    elif front_count == 4 and back_count == 0:
        return 100
    elif front_count == 3 and back_count == 1 or front_count == 2 and back_count == 2:
        return 15
    elif (front_count + back_count) == 3 or back_count == 2:
        return 5
    else:
        return 0


if __name__ == '__main__':
    #hit_list = check_num(['09','12','13','26','33','04','10'])
    #hit_list = check_num(['05','07','19','29','33','05','07'])
    #hit_list = check_num(['04','07','13','26','33','05','07'])
    #hit_list = check_num(['03','06','16','22','33','05','10'])
    hit_list = check_num(['02','09','15','20','33','02','07'], '21010')
    for x in hit_list:
        print(x)