import random
from enum import Enum

# 个Enum类型变量描述三种不同种类的水果树
Treetype = Enum('TreeType', 'apple_tree cherry_tree peach_tree')


class Tree:
    """
    pool变量是一个对象池（换句话说，是我们的缓存）。注意：pool是一个类属性（类的所有实例共享的一个变量。
    使用特殊方法__new__（这个方法在__init__之 前被调用），我们把Tree类变换成一个元类，元类支持自引用。
    这意味着cls引用的是Tree类。当客户端要创建Tree的一个实例时，会以tree_type参数传递树的种 类。树的种类用
    于检查是否创建过相同种类的树。如果是，则返回之前创建的对象；否则，将这个新的树种添加到池中，并返回相应的新对象
    """
    pool = dict()

    def __new__(cls, tree_type):
        obj = cls.pool.get(tree_type, None)
        if not obj:
            obj = object.__new__(cls)
            cls.pool[tree_type] = obj
            obj.tree_type = tree_type
        return obj

    def render(self, age, x, y):
        """
        方法render()用于在屏幕上渲染一棵树。
        """
        print('render a tree of type {} and age {} at ({}, {})'.format(self.tree_type, age, x, y))


def main():
    rnd = random.Random()
    # 一棵树的年龄是1到30年之间的一个随机值。
    age_min, age_max = 1, 30  # 单位为年

    # 坐标使用1到100之间的随机值
    min_point, max_point = 0, 100
    tree_counter = 0

    for _ in range(10):
        t1 = Tree(Treetype.apple_tree)
        t1.render(rnd.randint(age_min, age_max),
                  rnd.randint(min_point, max_point),
                  rnd.randint(min_point, max_point))
        tree_counter += 1

    for _ in range(3):
        t2 = Tree(Treetype.cherry_tree)
        t2.render(rnd.randint(age_min, age_max),
                  rnd.randint(min_point, max_point),
                  rnd.randint(min_point, max_point))
        tree_counter += 1

    for _ in range(5):
        t3 = Tree(Treetype.peach_tree)
        t3.render(rnd.randint(age_min, age_max),
                  rnd.randint(min_point, max_point),
                  rnd.randint(min_point, max_point))
        tree_counter += 1

    print('trees rendered: {}'.format(tree_counter))
    print('trees actually created: {}'.format(len(Tree.pool)))

    t4 = Tree(Treetype.cherry_tree)
    t5 = Tree(Treetype.cherry_tree)
    t6 = Tree(Treetype.apple_tree)
    print('{} == {}? {}'.format(id(t4), id(t5), id(t4) == id(t5)))
    print('{} == {}? {}'.format(id(t5), id(t6), id(t5) == id(t6)))


if __name__ == '__main__':
    main()
