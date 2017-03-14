'''
相関係数を求める

'''


def corr(x, y):
    '''

    :param x:list
    :param y: list
    :return:
    '''
    n = len(x)
    if len(x) != len(y):
        raise Exception("xとｙの長さが異なります")
    # 二乗の和を求める
    prod = []
    for xi, yi in zip(x, y):
        prod.append(xi * yi)

    sum_prod_x_y = sum(prod)
    sum_x = sum(x)
    sum_y = sum(y)

    squared_sum_x = sum_x ** 2
    squared_sum_y = sum_y ** 2

    x_square = []
    for xi in x:
        x_square.append(xi ** 2)
    x_square_sum = sum(x_square)
    y_square = []
    for yi in y:
        y_square.append(yi ** 2)

    y_square_sum = sum(y_square)

    # 相関係数の分子分母の計算
    numerator = n*sum_prod_x_y - sum_x * sum_y
    denominator_term1=n*x_square_sum-squared_sum_x
    denominator_term2=n*y_square_sum-squared_sum_y
    denominator=(denominator_term1*denominator_term2)**0.5
    if denominator ==0:
        raise Exception("分母が0なので相関係数は求められません")
    correl=numerator/denominator

    return correl


print(corr([1,2,3],[2,4,6]))
#print(corr([1,1,1],[2,2,2]))
