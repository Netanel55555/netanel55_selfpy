def chocolate_maker(small, big, x):
    print(int(x/5) <= big and int(x % 5) <= small)

chocolate_maker(3, 1, 8)
chocolate_maker(3, 1, 9)
chocolate_maker(3, 2, 10)