from collections import OrderedDict
import copy


class Book:
    """
    Book类展示了一种有趣的技术可避免可伸缩构造器问题。在__init__() 方法中，仅有三个形参是固定的：
    name、authors和price，但是使用rest变长列表，调用者 能以关键词的形式（名称=值）传入更多的参数。
    self.__dict__.update(rest)一行将rest 的内容添加到Book类的内部字典中，成为它的一部分。
    """

    def __init__(self, name, authors, price, **rest):
        '''rest的例子有: 出版商、长度、 标签、出版日期等等'''
        self.name = name
        self.authors = authors
        self.price = price  # 单位为美元
        self.__dict__.update(rest)

    def __str__(self):
        """
        我们并不知道所有被添加参数的名称，但又需要访问内部字典将这些参数 应用到__str__()中，并且字典的内容并不遵循
        任何特定的顺序，所以使用一个OrderedDict来强制元素有序，否则，每次程序执行都会产生不同的输出。
        :return: str
        """
        mylist = []
        ordered = OrderedDict(sorted(self.__dict__.items()))
        for i in ordered.keys():
            mylist.append('{}: {}'.format(i, ordered[i]))
            if i == 'price':
                mylist.append('$')
            mylist.append('\n')
        return ''.join(mylist)


class Prototype:
    """
    Prototype类实现了原型设计模式。Prototype类的核心是clone()方法，该方法使用我们 熟悉的copy.deepcopy()
    函数来完成真正的克隆工作。但Prototype类在支持克隆之外做了一 点更多的事情，它包含了方法register()和unregister()，
    这两个方法用于在一个字典中追 踪被克隆的对象。注意这仅是一个方便之举，并非必需。
    """

    def __init__(self):
        self.objects = dict()

    def register(self, identifier, obj):
        self.objects[identifier] = obj

    def unregister(self, identifier):
        del self.objects[identifier]

    def clone(self, identifier, **attr):
        """
        clone()方法和Book类中的__str__使用了相同的技巧，但这次是因为别的原因。使 用变长列表attr，
        我们可以仅传递那些在克隆一个对象时真正需要变更的属性变量
        :param identifier:版本号
        :param attr: 新添加的属性
        :return: obj
        """
        found = self.objects.get(identifier)

        if not found:
            raise ValueError('Incorrect object identifier: {}'.format(identifier))
        obj = copy.deepcopy(found)
        obj.__dict__.update(attr)
        return obj


def main():
    """
    main()函数以实践的方式展示了本节开头提到的《C程序设计语言》一书克隆的例子。克隆 该书的第一个版本来创建第二个版本，
    我们仅需要传递已有参数中被修改参数的值，但也可以传递额外的参数。在这个案例中，edition就是一个新参数，
    在书的第一个版本中并不需要，但对 于克隆版本却是很有用的信息。
    :return:
    """
    b1 = Book('The C Programming Language', ('Brian W. Kernighan', 'Dennis M.Ritchie'), price=118,
              publisher='Prentice Hall', length=228, publication_date='1978-02-22',
              tags=('C', 'programming', 'algorithms', 'data structures'))

    prototype = Prototype()
    cid = 'k&r-first'
    prototype.register(cid, b1)
    b2 = prototype.clone(cid, name='The C Programming Language(ANSI)', price=48.99, length=274,
                         publication_date='1988-04-01', edition=2)

    for i in (b1, b2):
        print(i)
    print("ID b1 : {} != ID b2 : {}".format(id(b1), id(b2)))


if __name__ == '__main__':
    main()
