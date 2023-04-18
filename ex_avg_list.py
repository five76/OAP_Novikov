def square_trapec(a,b,h):
    """

    Вычисление площади трапеции

    :param a: нижнее основание трапеции
    :param b: верхнее основание трапеции
    :param h: высота трапеции
    :return s: площадь трапеции
    """
    s = (a+b)/2 * h
    return s


a = 10
b = 5
h = 3
sq = square_trapec()