from get_history_info import get_exist_info


def mode_num() -> tuple:
    """
    统计历史号码的众数
    :return: 结果
    """
    exist_info, _ = get_exist_info()

    front_mode_dict = {}
    back_mode_dict = {}
    for exist in exist_info[1:]:
        exist = exist.split(' ')
        for x in exist[1:6]:
            if front_mode_dict.get(x):
                front_mode_dict[x] += 1
            else:
                front_mode_dict[x] = 1

        for x in exist[-2:]:
            if back_mode_dict.get(x):
                back_mode_dict[x] += 1
            else:
                back_mode_dict[x] = 1
    front_mode_dict = sorted(front_mode_dict.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
    back_mode_dict = sorted(back_mode_dict.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
    return front_mode_dict, back_mode_dict


if __name__ == '__main__':
    front_mode_dict, back_mode_dict = mode_num()
    print('前区号码情况：')
    for k in front_mode_dict:
        print('号码： ' + k[0] + '   次数  ' + str(k[1]))
    print('后区号码情况：')
    for k in back_mode_dict:
        print('号码： ' + k[0] + '   次数  ' + str(k[1]))