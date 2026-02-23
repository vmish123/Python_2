def main():
    print("Задание 1")
    first_task()
    print("Задание 2")
    second_task()
    print("Задание 3")
    third_task()
    print("Задание 4")
    fourth_task()
    print("Задание 5")
    fifth_task()
    print("Задание 6")
    sixth_task()
    print("Задание 7")
    seventh_task()
    print("Задание 8")
    eighth_task()
    print("Задание 9")
    ninth_task()
    print("Задание 10")
    tenth_task()
    print("Задание 11")
    eleventh_task()
    print("Задание 12")
    twelfth_task()
    print("Задание 13")
    thirteenth_task()
    print("Задание 14")
    fourteenth_task()
    print("Задание 15")
    fifteenth_task()


# Задание 1
def first_task():
    first_string = input()

    print(first_string[2])
    print(first_string[-2])
    print(first_string[:5])
    print(first_string[:-2])
    print(first_string[::2])
    print(first_string[1::2])
    print(first_string[::-1])
    print(first_string[::-2])
    print(len(first_string))


# Задание 2
def second_task():
    second_string = input()

    first_part = second_string[(len(second_string) + 1) // 2:]
    second_part = second_string[:(len(second_string) + 1) // 2]

    new_string = first_part + second_part
    print(new_string)


# Задание 3
def third_task():
    third_string = input()
    first_h = third_string.index("h")
    last_h = len(third_string) - third_string[::-1].index("h")

    third_string = (
            third_string[:first_h + 1] +
            third_string[last_h - 2:first_h:-1] +
            third_string[last_h - 1:]
    )

    print(third_string)


# Задание 4
def fourth_task():
    fourth_string = input()

    if fourth_string.count("f") > 0:
        first_f = fourth_string.index("f")
        print(first_f)

    if fourth_string.count("f") > 1:
        last_f = len(fourth_string) - fourth_string[::-1].index("f") - 1
        print(last_f)


# Задание 5
def fifth_task():
    current_word = input()
    while True:
        next_word = input()

        if next_word[0].lower() == current_word[-1].lower():
            current_word = next_word
            continue

        else:
            print(next_word)
            break


# Задание 6
def sixth_task():
    entered_word = input()
    k = 1

    for i in entered_word:
        print(i * k, end="")
        k += 1


# Задание 7
def seventh_task():
    entered_trace = input()
    symb = entered_trace[0]
    entered_trace = entered_trace[1:]

    current_length = 0

    while True:
        if "V" in entered_trace:
            current_segment = entered_trace[:entered_trace.index("V")]
            entered_trace = entered_trace[entered_trace.index("V") + 1:]
            is_end = False
        else:
            current_segment = entered_trace
            entered_trace = ""
            is_end = True

        segment_length = len(current_segment)

        if segment_length == 0:
            print(" " * current_length + symb)

        elif current_segment[0] == ">":
            print(" " * current_length + symb * (segment_length + 1))
            current_length += segment_length

        elif current_segment[0] == "<":
            current_length -= segment_length
            print(" " * current_length + symb * (segment_length + 1))

        if is_end:
            break


# Задание 8
def eighth_task():
    entered_word = input()
    word_length = len(entered_word)
    middle_index = word_length // 2

    if word_length % 2 == 0:
        for i in range(middle_index):
            empty_left = " " * (middle_index - 1 - i)
            empty_between = " " * (2 * i)

            left_letter = entered_word[middle_index - 1 - i]
            right_letter = entered_word[middle_index + i]

            print(empty_left + left_letter + empty_between + right_letter)

    else:
        for i in range(middle_index + 1):
            empty_left = " " * (middle_index - i)

            if i == 0:
                print(empty_left + entered_word[middle_index])

            else:
                empty_between = " " * (2 * i - 1)

                left_letter = entered_word[middle_index - i]
                right_letter = entered_word[middle_index + i]

                print(empty_left + left_letter + empty_between + right_letter)


# Задание 9
def ninth_task():
    number_list = []

    while True:
        entered_number = input("Введите число (! для отмены): ")

        if entered_number == "!":
            break

        number_list.append(int(entered_number))

    if len(number_list) > 1:
        for i in range(len(number_list) - 1):
            if number_list[i + 1] > number_list[i]:
                print(number_list[i + 1], end=" ")


# Задание 10
def tenth_task():
    number_list = []

    while True:
        entered_number = input("Введите число (! для отмены): ")

        if entered_number == "!":
            break

        number_list.append(int(entered_number))

    if len(number_list) > 1:
        for i in range(len(number_list) - 1):
            if number_list[i + 1] * number_list[i] > 0:
                print(number_list[i], number_list[i + 1])
                break


# Задание 11
def eleventh_task():
    some_list = []

    while True:
        entered_element = input("Введите элемент (! для отмены): ")

        if entered_element == "!":
            break

        some_list.append(entered_element)

    if len(some_list) > 1:
        for i in range(0, len(some_list) - 1, 2):
            some_list[i], some_list[i + 1] = some_list[i + 1], some_list[i]

    print(some_list)


# Задание 12
def twelfth_task():
    some_list = []

    while True:
        entered_element = input("Введите элемент (! для отмены): ")

        if entered_element == "!":
            break

        some_list.append(entered_element)

    for i in some_list:
        if some_list.count(i) == 1:
            print(i, end=" ")


# Задание 13
def thirteenth_task():
    indexes = list(map(int, input().split()))
    source_string = input().split()
    new_string = []

    for i in indexes:
        new_string.append(source_string[i - 1])

    new_string = " ".join(new_string).capitalize()
    print(new_string)


# Задание 14
def fourteenth_task():
    x = []
    y = []

    for i in range(8):
        input_x, input_y = map(int, input().split())
        x.append(input_x)
        y.append(input_y)

    beats = False

    for i in range(8):
        for j in range(i + 1, 8):
            if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                beats = True
                break

        if beats:
            break

    if beats:
        print("YES")
    else:
        print("NO")


# Задание 15
def fifteenth_task():
    events_number = int(input())
    current_queue = []

    for i in range(events_number):
        entered_string = input()

        if "Кто последний?" in entered_string:
            last_name = entered_string.split()[-1].rstrip(".")
            current_queue.append(last_name)

        elif "Я только спросить!" in entered_string:
            last_name = entered_string.split()[-1].rstrip(".")
            current_queue.insert(0, last_name)

        elif entered_string == "Следующий!":

            if current_queue:
                print(f"Заходит {current_queue[0]}!")
                current_queue.remove(current_queue[0])
            else:
                print("В очереди никого нет.")


main()
