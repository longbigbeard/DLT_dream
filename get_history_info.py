import pathlib, requests, re


def get_exist_info() -> tuple:
    """
    用来读取保存的历史数据
    :return: tuple
    """
    # 初始化，判断文件是否存在
    if pathlib.Path('history_info.txt').is_file():
        with open(r'history_info.txt', encoding='utf-8') as fp:
            exist_info = fp.readlines()
            exist_info = [r.strip('\n') for r in exist_info]
    else:
        exist_info = []
    exist_date=[]  # 开奖期号
    for info in exist_info:
        tmp_info=re.split(r' ', info)
        exist_date.append(tmp_info[0])
    
    return exist_info, exist_date


def update_info(exist_info: list, exist_date: list):
    """
    更新数据
    :param exist_info: 全部数据
    :param exist_date: 开奖日期
    """
    res = requests.get('http://datachart.500.com/dlt/history/history.shtml')
    res_text = re.split(r'<!--<td>2</td>-->|\n', str(res.text))
    history_info = []
    for i in res_text:
        if 'cfont' in i or 't_tr1' in i:
            tmp_info = re.split(r'<td class="t_tr1">|<td class="cfont2">|<td class="cfont4">|</td>', i)
            if tmp_info[0] == '' and len(tmp_info[1]) == 5:
                if tmp_info[1] not in exist_date:
                    oknum = ''
                    for num in range(1, 15):
                        if tmp_info[num] != '':
                            oknum = oknum + tmp_info[num] + ' '
                    oknum = oknum + tmp_info[15]
                    history_info.append(oknum)
    if exist_info:
        new_info = [exist_info[0]] + history_info + exist_info[1:]
    else:
        new_info = ["00000 00 00 00 00 00 00 00"] + history_info

    new_info = "\n".join(new_info)

    with open(r'history_info.txt', 'w', encoding='utf-8') as fp:
        fp.write(new_info)



def run():
    print("开始读取历史数据。。。")
    exist_info, exist_date = get_exist_info()
    print("历史数据读取结束，开始更新数据。。。")
    update_info(exist_info, exist_date)
    print("更新结束。。。")


if __name__ == '__main__':
    run()