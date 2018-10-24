from enum import Enum
from abc import ABCMeta, abstractmethod

State = Enum('State', ('new','running','sleeping','restart','zombie'))


class User:
    pass


class Process:
    pass


class File:
    pass


class Server(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass

    def __str__(self):
        return self.name

    @abstractmethod
    def boot(self):
        pass

    @abstractmethod
    def kill(self, restart=True):
        pass


class FileServer(Server):
    """
    服务进程FileServer除了Server接口要求实现的方法之外,还有一个create_file()方法用于创建文件。
    """
    def __init__(self):
        '''初始化文件服务进程要求的操作'''
        self.name = 'FileServer'
        self.state = State.new

    def boot(self):
        print('booting the {}'.format(self))
        '''启动文件服务进程要求的操作'''
        self.state = State.running

    def kill(self, restart=True):
        print('Killing {}'.format(self))
        '''终止文件服务进程要求的操作'''
        self.state = State.restart if restart else State.zombie

    def create_file(self, user, name, permissions):
        '''检查访问权限的有效性、用户权限等'''
        print("trying to create the file '{}' for user '{}' with permissions {}".format(name, user, permissions))


class ProcessServer(Server):
    """
    服务进程ProcessServer除了Server接口要求实现的方法之外,还有一个create_process()方法用于创建进程。
    """

    def __init__(self):
        '''初始化进程服务进程要求的操作'''
        self.name = 'ProcessServer'
        self.state = State.new

    def boot(self):
        print('booting the {}'.format(self))
        '''启动进程服务进程要求的操作'''
        self.state = State.running

    def kill(self, restart=True):
        print('Killing {}'.format(self))
        '''终止进程服务进程要求的操作'''
        self.state = State.restart if restart else State.zombie

    def create_process(self, user, name):
        '''检查用户权限和生成PID等'''
        print("trying to create the process '{}' for user '{}'".format(name, user))

#
# class WindowServer:
#     pass
#
#
# class NetworkServer:
#     pass


class OperatingSystem:
    """
    OperatingSystem类是一个外观。__init__()中创建所有需要的服务进程实例。
    start()方法是系统的入口点，供客户端代码使用。如果需要，可以添加更多的包装方法作为服务的访问点，
    比如包装方法create_file()和create_process()。从客户端的角度来看，
    所有服务都是由OperatingSystem类提供的。客户端并不应该被不必要的细节所干扰，
    比如，服务进程的存在和每个服务进程的责任。
    """

    def __init__(self):
        self.fs = FileServer()
        self.ps = ProcessServer()

    def start(self):
        [i.boot() for i in (self.fs, self.ps)]

    def create_file(self, user, name, permissions):
        return self.fs.create_file(user, name, permissions)

    def create_process(self, user, name):
        return self.ps.create_process(user, name)


def main():
    os = OperatingSystem()
    os.start()
    os.create_file('foo', 'hello', '-rw-r-r')
    os.create_process('bar', 'ls /tmp')


if __name__ == '__main__':
    main()
