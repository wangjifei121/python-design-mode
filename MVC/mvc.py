quotes = ('A man is not complete until he is married. Then he is finished.', 'As I said before, I never repeat myself.',
          'Behind a successful man is an exhausted woman.', 'Black holes really suck...', 'Facts are stubborn things.')


class QuoteModel:
    """
    模型极为简约，只有一个get_quote()方法，基于索引n从quotes元组中返回对应的名人名言（字符串）。
    """
    def get_quote(self, n):
        try:
            value = quotes[n]
        except IndexError as err:
            value = 'Not found!'
        return value


class QuoteTerminalView:
    """
    视图有三个方法，分别是show()、error()和select_quote()。
    """
    def show(self, quote):
        """
        show()用于在屏幕上输 出一句名人名言（或者输出提示信息Not found!）；
        """
        print('And the quote is: "{}"'.format(quote))

    def error(self, msg):
        """
        error()用于在屏幕上输出一条错误消息；
        """
        print('Error: {}'.format(msg))

    def select_quote(self):
        """
        select_quote()用于读取用户的选择
        """
        return input('Which quote number would you like to see? ')


class QuoteTerminalController:
    """
    控制器负责协调
    """
    def __init__(self):
        """
        __init__()方法初始化模型和视图
        """
        self.model = QuoteModel()
        self.view = QuoteTerminalView()

    def run(self):
        """
        run()方法校验用户提供的名言索 引，然后从模型中获取名言，并返回给视图展示
        """
        valid_input = False
        while not valid_input:
            try:
                n = self.view.select_quote()
                n = int(n)
                vaild_input = True
            except ValueError as err:
                self.view.error("Incorrect index '{}'".format(n))
            quote = self.model.get_quote(n)
            self.view.show(quote)


def main():
    controller = QuoteTerminalController()
    while True:
        controller.run()


if __name__ == '__main__':
    main()
