import random
from check_num import check_num
front_num = []
back_num = []

while len(front_num) < 5:
    num = random.randint(1, 35)
    if num not in front_num:
        front_num.append(num)

while len(back_num) < 2:
    num = random.randint(1, 12)
    if num not in back_num:
        back_num.append(num)

num = sorted(front_num) + sorted(back_num)
num = [str(i).zfill(2) for i in num]
print(num)
hit_list = check_num(num)
for x in hit_list:
    print(x)