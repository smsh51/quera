def find_house_number(x, y):
    layer = max(abs(x), abs(y)) + (1 if abs(x)==abs(y) else 0)
    if layer == 0:
        return 1  # مبدا

    start_number = ((layer - 1) * 4 * (layer - 1) + 1) + 1

    if y == layer:  # بالای مربع
        return start_number + (x - (-layer))
    elif x == layer:  # سمت راست مربع
        return start_number + (2 * layer - 1) + (layer - y)
    elif y == -layer:  # پایین مربع
        return start_number + (4 * layer - 3) + (layer - x)
    else:  # سمت چپ مربع
        return start_number + (6 * layer - 5) - (layer + y)

ts = int(input())
for t in range(ts):
    # x, y = list(map(int, input().split(' ')))
    print(find_house_number(*list(map(int, input().split(' ')))))


def calculate_house_number(x, y):
    # پیدا کردن لایه یا "دور" که خانه در آن قرار دارد
    layer = max(abs(x), abs(y))

    # تعداد کل خانه‌ها در لایه‌های قبل
    total_before_layer = 4 * ((layer - 1) * layer)  # سری حسابی

    # محاسبه پلاک در لایه فعلی
    if layer == x and y > -layer:
        # حرکت به بالا
        number = total_before_layer + (y + layer)
    elif layer == -y:
        # حرکت به چپ
        number = total_before_layer + (layer * 3 - x)
    elif -layer == x:
        # حرکت به پایین
        number = total_before_layer + (layer * 5 + y)
    else:
        # حرکت به راست
        number = total_before_layer + (layer * 7 + x)

    # اضافه کردن تصحیح برای شروع صحیح شمارش از 1
    return number - (4 * (layer - 1)) + 1


# مثال
x, y = 2, 3
print(calculate_house_number(x, y))