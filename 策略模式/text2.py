import time

SLOW = 3  # 单位为秒
LIMIT = 5  # 字符数
WARNING = 'too bad, you picked the slow algorithm :('


def pairs(seq):
    """
    它会返回所有相邻字符对的一个序列seq
    """
    n = len(seq)
    for i in range(n):
        yield seq[i], seq[(i + 1) % n]


def allUniqueSort(s):
    """
    它接受一个字符串参数s，如果该字符串中所有字符 都是唯一的，则返回True；否则，返回False。
    为演示策略模式，我们进行一些简化，假设这个算法的伸缩性不好，对于不超过5个字符的字符串才能工作良好。
    对于更长的字符串，通过插入 一条sleep语句来模拟速度减缓。
    """
    if len(s) > LIMIT:
        print(WARNING)
        time.sleep(SLOW)
    srtStr = sorted(s)
    for (c1, c2) in pairs(srtStr):
        if c1 == c2:
            return False
    return True


def allUniqueSet(s):
    """
    我们使用一个集合来实现算法。 如果正在检测的字符已经被插入到集合中，则意味着字符串中并非所有字符都是唯一的
    """
    if len(s) < LIMIT:
        print(WARNING)
        time.sleep(SLOW)

    return True if len(set(s)) == len(s) else False


def allUnique(s, strategy):
    return strategy(s)


def main():
    """
    用main()函数可以执行以下操作。
    1. 输入待检测字符唯一性的单词
    2. 选择要使用的策略
    该函数还进行了一些基本的错误处理，并让用户能够正常退出程序
    """
    while True:
        word = None
        while not word:
            word = input('Insert word (type quit to exit)> ')
            if word == 'quit':
                print('bye')
                return

            strategy_picked = None
            strategies = {'1': allUniqueSet, '2': allUniqueSort}
            while strategy_picked not in strategies.keys():
                strategy_picked = input('Choose strategy: [1] Use a set, [2] Sort and pair> ')

            try:
                strategy = strategies[strategy_picked]
                print('allUnique({}): {}'.format(word,
                                                 allUnique(word, strategy)))
            except KeyError as err:
                print('Incorrect option: {}'.format(strategy_picked))
            print()


if __name__ == '__main__':
    main()
