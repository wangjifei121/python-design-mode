from cowpy import cow

"""
我们将实现一个横幅生成器。想法很简单，将一段文本发送给一个函数，该函数要 生成一个包含该文本的横幅。
横幅有多种风格，比如点或虚线围绕文本。横幅生成器有一个默认风格，但应该能够使用我们自己提供的风格。 
"""
def dots_style(msg):
    """
    dots_style()简单地将msg首字母大写，并在其之前和之后输出10个点
    """
    msg = msg.capitalize()
    msg = '.' * 10 + msg + '.' * 10
    return msg


def admire_style(msg):
    msg = msg.upper()
    return '!'.join(msg)


def generate_banner(msg, style=dots_style):
    """
    数generate_banner()是我们的模板函数。它接受一个输入参数（msg，希望横幅包含的文本）和一个可选参数（style，希望使用的风格）。
    默认风格是dots_style，我们马上就能 看到。generate_banner()以一个简单的头部和尾部来包装带样式的文本。
    实际上，这个头部和尾部可以复杂得多，但在这里调用可以生成头部和尾部的函数来替代仅仅输出简单字符串也无不可。
    """
    print('-- start of banner --')
    print(style(msg))
    print('-- end of banner --\n\n')


def cow_style(msg):
    """
    cow_style()风格使用cowpy模块生成随机ASCII码艺 术字符，夸张地表现文本
    """
    msg1 = cow.milk_random_cow(msg)
    msg2 = cow.milk_random_cow(msg1)
    return msg2


def main():
    """
    main()函数向横幅发送文本“关关之舟，在河之洲！”，并使用所有可用风格将横幅输出到标准输出。
    """
    msg = '关关之舟，在河之洲！'
    [generate_banner(msg, style) for style in (dots_style, admire_style, cow_style)]


if __name__ == '__main__':
    main()

