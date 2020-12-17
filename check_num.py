from get_history_info import get_exist_info


def check_num(num: list) -> list:
    exist_info, _ = get_exist_info()

    check_num_front = num[0:5]
    check_num_back = num[-2:]
    hit_list = []
    for exist in exist_info[1:]:
        exist = exist.split(' ')
        hit_front_num = [x for x in check_num_front if x in exist[1:5]]  # 前区
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
    return 0


hit_list = check_num(['01','02','03','04','05','06','07'])
for x in hit_list:
    print(x)