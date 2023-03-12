import random


def number_create(a, b):
    a = random.randint(a, b)
    return a


def phoneNo(operator, chooseType):
    phone_number = ["1"]
    number = {2: [3, 5, 7, 8, 9],
              3: {3: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                  8: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                  5: [0, 1, 2, 3, 5, 6, 7, 8, 9],
                  7: [0, 1, 2, 3, 5, 6, 7, 8],
                  9: [8, 9]},
              4: {"四川移洞": [5, 7, 8, 9],
                  "四川连通": [0, 2, 5, 6, 9],
                  "四川电兴": [3, 7, 9]},
              5: {"选取靓号": [6666666, 8888888, 9999999],
                  "普通选号": []}}

    for i in number:
        a = random.randint(0, 10)
        if i == 2:
            while number[i].count(a) != 1:
                a = random.randint(0, 10)
            phone_number.append(str(a))
        elif i == 3:
            while number[i][int(phone_number[1])].count(a) != 1:
                a = random.randint(0, 10)
            phone_number.append(str(a))
        elif i == 4:
            if number[i].get(operator):
                while number[i][operator].count(a) != 1:
                    a = random.randint(0, 10)
                phone_number.append(str(a))
            else:
                print("没有该种营运商类型")
                break
        else:
            if number[i].get(chooseType):
                if number[i] == "选取靓号":
                    a = random.randint(0, 3)
                    phone_number.append(str(number[i][chooseType][a]))
                else:
                    a = random.randint(1000000, 10000000)
                    phone_number.append(str(a))
            else:
                print("没有该种营运商类型")
                break
    return phone_number


phoneNumber = phoneNo("四川连通", "选取靓号")
if len(phoneNumber) > 4:
    print("".join(phoneNumber))
    if "".join(phoneNumber) == 19999999999:
        print("".join(phoneNumber))
    else:
        print("该号码不是我想要的号码，我不办理")
