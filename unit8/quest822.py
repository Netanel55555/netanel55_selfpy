def sort_prices(list_of_tuples):

    list_of_tuples.sort(reverse=True, key=lambda x: x[1])
    print(list_of_tuples)


products = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]
sort_prices(products)