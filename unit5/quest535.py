def distance(num1, num2, num3):
    answer = 0

    if abs(num1 - num2) == 1 or abs(num1 - num3):

        if (abs(num1 - num2) >= 2 and abs(num2 - num3) >= 2) or (abs(num3 - num2) >= 2 and abs(num3 - num1) >= 2):
            answer = 1

    print(answer > 0)


distance(1, 2, 10)
distance(4, 5, 3)
