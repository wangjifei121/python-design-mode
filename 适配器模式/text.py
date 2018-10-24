class Synthesizer:
    """
    在Synthesizer类 中，主要动作由play()方法执行。
    """

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'the {} synthesizer'.format(self.name)

    def play(self):
        return 'is playing an electronic song'


class Human:
    """
    在Human类中，主要动作由speak()方法执行
    """

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return '{} the human'.format(self.name)

    def speak(self):
        return 'says hello'


class Computer:
    """
    用来显示一台计算机的基本信息
    """

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'the {} computer'.format(self.name)

    def execute(self):
        """
        execute方法是计算机可以执行的主要动作。这一方法由客户端代码调用。
        :return: str
        """
        return 'executes a program'


class Adapter:
    """
    客户端仅知道如何调用execute()方法，并不知道play()和speak()。在不改变Synthesizer和Human类的前提下，我们该如何做才能
    让代码有效？适配器是救星！我们创建一个通用的Adapter类，将一些带不同接口的对象适配到一个统一接口中。__init__()方法的obj参数
    是我们想要适配的对象，adapted_methods是一个字典，键值对中的键是客户端要调用的方法，值是应该被调用的方法。
    """

    def __init__(self, obj, execute=None, **kwargs):
        self.obj = obj
        self.execute = execute
        self.__dict__.update(kwargs)

    def __str__(self):
        return str(self.obj)


def main():
    objects = [Computer('Asus')]
    synth = Synthesizer('moog')
    objects.append(Adapter(synth, execute=synth.play, **synth.__dict__))
    human = Human('Bob')
    objects.append(Adapter(human, execute=human.speak, **human.__dict__))

    for i in objects:
        print('{} {}'.format(str(i), i.execute()))
    for i in objects:
        print(i.name)


if __name__ == "__main__":
    main()
