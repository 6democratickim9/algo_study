def solution():
    num_list = list(map(int, input().split(' ')))
    s = num_list[0]
    e = num_list[1]
    if exception_case(s, e) == "INPUT ERROR!":
        print("INPUT ERROR!")
        return "INPUT ERROR!"
    
    result = ""
    if s > e:
        o = -1
        e -= 1
    else:
        o = 1
        e += 1
        
    for j in range(s, e, o):
        for i in range(1, 10):
            if j * i >= 10:
                result = result + f"{j} * {i} = {i*j}   "
            else:
                result = result + f"{j} * {i} =  {i*j}   "
            if i % 3 == 0:
                result = result + "\n"
        result = result + "\n"

    print(result)

    
def exception_case(num1, num2):
    if num1 < 2 or num1 > 9:
        return "INPUT ERROR!"
    if num2 < 2 or num2 > 9:
        return "INPUT ERROR!"


while True:
    if solution() != "INPUT ERROR!":
        break