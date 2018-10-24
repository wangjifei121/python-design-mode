import os

verbose = True


class RenameFile:
    """
    重命名工具，使用RenameFile类来实现。__init__()方法接受源文件路径（path_src）和目标文件路径（path_dest）作为参数。
    如果文件路径未使用路径分隔符，则在当前目录下创建文件。使用路径分隔符的一个例子是传递字符串/tmp/file1作为path_src，
    字符串/home/user/file2作为path_dest。不使用路径的例子则是传递file1作为path_src， file2作为path_dest。
    """

    def __init__(self, path_src, path_dest):
        self.src, self.dest = path_src, path_dest

    def execute(self):
        """
        execute()方法使用os.rename()完成实际的重命名。verbose是一个全局标记，被激活时（默认是激活的），能向用户反馈执行的操作。
        如果你倾向于静默地执行命令，则可以取消激活状态。注意，虽然对于示例来说print()足够好了，
        但通常会使用更成熟更强大的方式，例如,日志模块
        """
        if verbose:
            print("[renaming '{}' to '{}']".format(self.src, self.dest))
        os.rename(self.src, self.dest)

    def undo(self):
        """
        我们的重命名工具通过undo()方法支持撤销操作。在这里，撤销操作再次使用os.rename() 将文件名恢复为原始值。
        :return:
        """
        if verbose:
            print("[renaming '{}' back to '{}']".format(self.dest, self.src))
        os.rename(self.dest, self.src)


class CreateFile:
    """
    再次回到使用类的方式。CreateFile类用于创建一个文件。__init__()函数接受熟悉的path参数和一个txt字符串，
    默认向文件写入hello world文本。通常来说，合理的默认行为是创建一个空文件，但因这个例子的需要，
    我决定向文件写个一个默认字符串。可以根据需要更改它
    """

    def __init__(self, path, txt='hello world\n'):
        self.path, self.txt = path, txt

    def execute(self):
        """
        execute()方法使用with语句和open()来打开文件（mode='w'意味着写模式），并使用 write()来写入txt字符串。
        :return:
        """
        if verbose:
            print("[creating file '{}']".format(self.path))
        with open(self.path, mode='w', encoding='utf-8') as out_file:
            out_file.write(self.txt)

    def undo(self):
        """
        创建一个文件的撤销操作是删除它。因此，undo()简单地使用delete_file()来实现目的。
        :return:
        """
        delete_file(self.path)


class ReadFile:
    """
    ReadFile类的execute()方法再次使用with() 语句配合open()，这次是读模式，并且只是使用print()来输出文件内容。
    """

    def __init__(self, path):
        self.path = path

    def execute(self):
        if verbose:
            print("[reading file '{}']".format(self.path))
        with open(self.path, mode='r', encoding='utf-8') as in_file:
            print(in_file.read(), end='')


def delete_file(path):
    """
    文件删除功能实现为单个函数，而不是一个类。我想让你明白并不一定要为想要添加的每个命令（之后会涉及更多）都创建一个新类。
    delete_file()函数接受一个字符串类型的文件路 径，并使用os.remove()来删除它。
    """
    if verbose:
        print("deleting file '{}'".format(path))
    os.remove(path)


def main():
    # main()函数使用这些工具类/方法。参数orig_name和new_name是待创建文件的原始名称以及重命名后的新名称。
    orig_name, new_name = 'file1', 'file2'

    # commands列表用于添加（并配置）所有我们之后想要执行的命令。注意，命令不会被执行，除非我们显式地调用每个命令的execute()。
    commands = []
    for cmd in CreateFile(orig_name), ReadFile(orig_name), RenameFile(orig_name, new_name):
        commands.append(cmd)

    # 循环执行命令
    [c.execute() for c in commands]

    # 下一步是询问用户是否需要撤销执行过的命令。用户选择撤销命令或不撤销。
    answer = input('reverse the executed commands? [y/n] ')

    # 如果选择不撤销，则输出结果
    if answer not in 'yY':
        print("the result is {}".format(new_name))
        exit()

    # 如果选择撤销，则执行commands列表中所有命令的undo()。由于并不是所有命令都支持撤销，
    # 因此在undo()方法不存在时产生的AttributeError异常要使用异常处理来捕获。如果你不喜欢对这种情况使用
    # 异常处理，可以通过添加一个布尔方法（例如，supports_undo() 或 can_be_undone()）来显式地检测命令是否支持撤销操作。
    for c in reversed(commands):
        try:
            c.undo()
        except AttributeError as e:
            pass


if __name__ == "__main__":
    main()
