class Publisher:
    """
    Publisher类。观察者们保存在列表observers中。
    add()方法注册一个新的观察者，或者在该观察者已存在时引发一个错误。
    remove()方法注销一个已有观察者，或者在该观察者尚未存在时引发一个错误。
    notify()方法则在变化发生时通知所有观察者
    """
    def __init__(self):
        self.observers = []

    def add(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)
        else:
            print('Failed to add: {}'.format(observer))

    def remove(self, observer):
        try:
            self.observers.remove(observer)
        except ValueError:
            print('Failed to remove: {}'.format(observer))

    def notify(self):
        [o.notify(self) for o in self.observers]


class DefaultFormatter(Publisher):
    """
    __init__()做的第一件事情就是调用基类的__init__() 方法，因为这在Python中没法自动完成。
    DefaultFormatter实例有自己的名字，这样便于我们跟踪其状态。
    """
    def __init__(self, name):
        Publisher.__init__(self)
        self.name = name
        self._data = 0

    def __str__(self):
        """
        __str__()方法返回关于发布者名称和_data值的信息。
        type(self).__name是一种获取类名的方便技巧，避免硬编码类名。这降低了代码的可读性，却提高了可维护性
        """
        return "{}: '{}' has data = {}".format(type(self).__name__, self.name, self._data)

    @property
    def data(self):
        """
        对于_data变量，我们使用了property装饰器来将data方法变成属性来得到私有属性_data的值。
        """
        return self._data

    @data.setter
    def data(self, new_value):
        """
        data()更有意思。它使用了@setter修饰器，该修饰器会在每次使用赋值操作符（=）为_data变量赋新值时被调用。
        该方法也会尝试把新值强制类型转换为一个整数，并在类型转换失败时处理异常
        """
        try:
            self._data = int(new_value)
        except ValueError as e:
            print('Error: {}'.format(e))
        else:
            self.notify()


class HexFormatter:
    """观察者类1（十六进制）"""
    def notify(self, publisher):
        print("{}: '{}' has now hex data = {}".format(type(self).__name__, publisher.name, hex(publisher.data)))


class BinaryFormatter:
    """观察者类2（二进制）"""
    def notify(self, publisher):
        print("{}: '{}' has now bin data = {}".format(type(self).__name__, publisher.name, bin(publisher.data)))


def main():
    """
    main()函数一开始创建一个名为test1的Default- Formatter实例，并在之后关联了两个可用的观察者。
    也使用了异常处理来确保在用户输入问题数据时应用不会崩溃。此外，
    诸如两次添加相同的观察者或删除尚不存在的观察者之类的事情也不应该导致崩溃。
    """
    df = DefaultFormatter('test1')
    print(df)

    # 添加第一个观察者
    print()
    hf = HexFormatter()
    df.add(hf)
    df.data = 3
    print(df)

    #参加第二个观察者
    print()
    bf = BinaryFormatter()
    df.add(bf)
    df.data = 21
    print(df)

    # 删除一个观察者
    print()
    df.remove(hf)
    df.data = 40
    print(df)

    # 删除另一个观察者后再添加一个观察者
    print()
    df.remove(hf)
    df.add(bf)

    # 异常捕获
    df.data = 'hello'
    print(df)

    print()
    df.data = 15.8
    print(df)


if __name__ == '__main__':
    main()
