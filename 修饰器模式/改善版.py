known = {0: 0, 1: 1}

def fibonacci(n):
    assert (n >= 0), 'n must be >= 0'
    if n in known:
        return known[n]
    res = fibonacci(n - 1) + fibonacci(n - 2)
    known[n] = res
    return res


if __name__ == '__main__':
    from timeit import Timer

    t = Timer('fibonacci(8)', 'from __main__ import fibonacci')
    print(t.timeit())
    print(fibonacci(8))


"""
执行基于memoization的代码实现，可以看到性能得到了极大的提升，甚至对于计算大的数 值性能也是可接受的
"""