class SensitiveInfo:
    """
    SensitiveInfo类包含我们希望保护的信息。
    users变量是已有用户的列表。
    read()方法 输出用户列表。
    add()方法将一个新用户添加到列表中。
    """
    def __init__(self):
        self.users = ['nick', 'tom', 'ben', 'mike']

    def read(self):
        print('There are {} users: {}'.format(len(self.users), ' '.join(self.users)))

    def add(self, user):
        self.users.append(user)
        print('Added user {}'.format(user))


class Info:
    """
    Info类是SensitiveInfo的一个保护代理。secret变量值是客户端代码在添加新用户时被要求告知/提供的密码。
    注意，这只是一个例子。现实中，永远不要执行以下操作:
         在源代码中存储密码
         以明文形式存储密码
         使用一种弱（例如，MD5）或自定义加密形式

    read()方法是SensetiveInfo.read()的一个包装。
    add()方法确保仅当客户端代码知道 密码时才能添加新用户
    """

    def __init__(self):
        self.protected = SensitiveInfo()
        self.secret = '111111'

    def read(self):
        self.protected.read()

    def add(self, user):
        sec = input('what is the secret? ')
        self.protected.add(user) if sec == self.secret else print("That's wrong!")


def main():
    """
    main()函数展示了客户端代码可以如何使用代理模式。客户端代码创建一个Info类的实例，
    并使用菜单让用户选择来读取列表、添加新用户或退出应用。
    """
    info = Info()
    while True:
        print('1. read list |==| 2. add user |==| 3. quit')
        key = input('choose option: ')
        if key == '1':
            info.read()
        elif key == '2':
            name = input('choose username: ')
            info.add(name)
        elif key == '3':
            exit()
        else:
            print('unknown option: {}'.format(key))


if __name__ == '__main__':
    main()
