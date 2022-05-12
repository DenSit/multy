def solution(dic, word=''):
    """
    join digits in number = solving result
    :return:  number
    """
    for i in range(1, 5):
        word += dic.get(i, '0')
    return int(word)


def helping(str1, str2):
    """
    create useful examples from multiplication table
    :param str1: first factor
    :param str2: second factor
    :return: examples list
    """
    lst = []
    for i in str2[::-1]:
        for j in str1[::-1]:
            lst.append(f'{i} х {j} = {int(i) * int(j)}')
    return lst


def solve_time(t1, t2):
    """
    measure solving time
    :param t1: time in the beginning
    :param t2: time after successful solution
    :return: execution time
    """
    t = int(t1 - t2)
    minutes = str(t // 60) if len(str(t // 60)) == 2 else '0' + str(t // 60)
    seconds = str(t % 60) if len(str(t % 60)) == 2 else '0' + str(t % 60)
    return minutes + ':' + seconds
