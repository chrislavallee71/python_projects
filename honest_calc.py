msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

oper_set = ["+", "-", "*", "/"]
memory = 0


def is_one_digit(v):
    return -10 < v < 10 and v.is_integer()


def check(v1, v2, v3):
    msg = ""

    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6

    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg = msg + msg_7

    if (v1 == 0 or v2 == 0) and (v3 != '/' and v3 in oper_set):
        msg = msg + msg_8

    if msg != "":
        msg = msg_9 + msg
        print(msg)
        pass

    else:
        pass


while True:
    equation = input(msg_0)

    if 'M' in equation:
        equation = equation.replace('M', str(memory))

    x, oper, y = equation.split()

    try:
        x = float(x)
        y = float(y)

    except ValueError:
        print(msg_1)
        continue

    if oper not in oper_set:
        print(msg_2)
        continue

    if check(x, y, oper):
        continue

    if oper == "+":
        result = x + y

    elif oper == "-":
        result = x - y

    elif oper == "*":
        result = x * y

    elif oper == "/" and y == 0:
        print(msg_3)
        continue
    else:
        result = x / y

    print(float(result))

    if input(msg_4).lower() == "y":

        if not is_one_digit(result):
            memory = result

        elif is_one_digit(result):
            msg_index = 10

            while msg_index < 12:
                if input(locals()["msg_" + str(msg_index)]).lower() == "y" and msg_index < 12:
                    msg_index += 1
                else:
                    break

            if msg_index == 12 and input(msg_12).lower() == "y":
                memory = result
                pass

    if input(msg_5).lower() == "n":
        break
