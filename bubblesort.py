print("Ця програма визначає найбільший добуток двох сусідніх чисел у масиві")
number_list = []
h = input("Введіть перший елемент списку числом.")
try_status = True

while try_status:
    if h == "#":
        try_status = False
        if len(number_list) < 3:
            try_status = True
            print("Список замалий. Додайте принаймні 3 числа")
            h = input("Введіть наступний елемент списку. Якщо список закінчився, введіть символ '#'")
            continue
        else:
            break

    try:
        x = int(h)
        number_list.append(x)
        print(f"Елемент {x} додано.")
        h = input("Введіть наступний елемент списку. Якщо список закінчився, введіть символ '#'")

    except ValueError:
        print("помилка у вводі. Введіть число")
        h = input("Введіть наступний елемент списку. Якщо список закінчився, введіть символ '#'")
        if h == "#":
            try_status = False
            if len(number_list) < 3:
                try_status = True
                print("Список замалий. Додайте принаймні 3 числа")
                h = input("Введіть наступний елемент списку. Якщо список закінчився, введіть символ '#'")
                continue
            else:
                break
        continue
print(f"Наразі список виглядає так: {number_list}. Вираховую найбільший добуток.")
# 5, 4, 8, 12, 1
highest_multi = 0
n_counter = 1
for number in number_list[1:-1]:
    prev_number = number_list[n_counter-1]
    next_number = number_list[n_counter+1]
    multi1 = number * prev_number
    multi2 = number * next_number
    if multi1 > multi2 and multi1 > highest_multi:
        highest_multi = multi1
    elif multi2 > highest_multi:
        highest_multi = multi2
    n_counter += 1
print("Найбільший добуток вийшов", highest_multi)
# i hate everything in the world i am da monsta....