from state_machine import State, Event, acts_as_state_machine, after, before, InvalidStateTransition


# 每个创建好的进程都有自己的状态机。使用state_machine模块
# 创建状态机的第一个步骤是使用@acts_as_state_machine修饰器。
@acts_as_state_machine
class Process:
    """
    定义状态机的状态。这是我们在状态图中看到的节点的映射。
    唯一的区别是应指定 状态机的初始状态。这可通过设置inital=True来指定。
    """
    created = State(initial=True)
    waiting = State()
    running = State()
    terminated = State()
    blocked = State()
    swapped_out_waiting = State()
    swapped_out_blocked = State()

    # 接着定义状态转换。在state_machine模块中，一个状态转换就是一个Event。
    # 我们使用参数from_states和to_state来定义一个可能的转换。from_states可以是单个状态或一组状态（元组）。
    wait = Event(from_states=(created, running, blocked, swapped_out_waiting), to_state=waiting)
    run = Event(from_states=waiting, to_state=running)
    terminate = Event(from_states=running, to_state=terminated)
    block = Event(from_states=(running, swapped_out_blocked), to_state=blocked)
    swap_wait = Event(from_states=waiting, to_state=swapped_out_waiting)
    swap_block = Event(from_states=blocked, to_state=swapped_out_blocked)

    # 每个进程都有一个名称。正式的应用场景中，一个进程需要多得多的信息才能发挥其作用（例 如，ID、优先级和状态等），
    # 但为了专注于模式本身，我们进行一些简化,只初始化对应的name
    def __init__(self, name):
        self.name = name

    # 在发生状态转换时，如果什么影响都没有，那转换就没什么用了。state_machine模块提 供@before和@after修饰器，
    # 用于在状态转换之前或之后执行动作。为了达到示例的目的，这 里的动作限于输出进程状态转换的信息。
    @after('wait')
    def wait_info(self):
        print('{} entered waiting mode'.format(self.name))

    @after('run')
    def run_info(self):
        print('{} is running'.format(self.name))

    @after('terminate')
    def terminate_info(self):
        print('{} terminated'.format(self.name))

    @after('block')
    def block_info(self):
        print('{} is blocked'.format(self.name))

    @after('swap_wait')
    def swap_wait_info(self):
        print('{} is swapped out and waiting'.format(self.name))

    @after('swap_block')
    def swap_block_info(self):
        print('{} is swapped out and blocked'.format(self.name))


def transition(process, event, event_name):
    """
    transition()函数接受三个参数：process、event和event_name。在尝试执行event时，如果发生错误，则会输出事件的名称。
    :param process:是一个Process类实例，
    :param event: event是一个Event类（wait、run和terminate等）实例，
    :param event_name: 而event_name 是事件的名称。
    """
    try:
        event()
    except InvalidStateTransition as err:
        print('Error: transition of {} from {} to {} failed'.format(process.name, process.current_state, event_name))


def state_info(process):
    """
    state_info()函数展示进程当前（激活）状态的一些基本信息。
    """
    print('state of {}: {}'.format(process.name, process.current_state))


def main():
    # 在main()函数的开始，我们定义了一些字符串常量，作为event_name参数值传递。
    RUNNING = 'running'
    WAITING = 'waiting'
    BLOCKED = 'blocked'
    TERMINATED = 'terminated'

    # 我们创建两个Process实例，并输出它们的初始状态信息。
    p1, p2 = Process('process1'), Process('process2')
    [state_info(p) for p in (p1, p2)]

    # 其余部分将尝试不同的状态转换。回忆一下本章之前提到的状态图。允许的状态转换应与状态图一致。
    # 例如，从状态“运行”转换到状态“阻塞”是可能的，但从状态“阻塞”转换 到状态“运行”则是不可能的。
    print()
    transition(p1, p1.wait, WAITING)
    transition(p2, p2.terminate, TERMINATED)
    [state_info(p) for p in (p1, p2)]

    print()
    transition(p1, p1.run, RUNNING)
    transition(p2, p2.wait, WAITING)
    [state_info(p) for p in (p1, p2)]

    print()
    transition(p2, p2.run, RUNNING)
    [state_info(p) for p in (p1, p2)]

    print()
    [transition(p, p.block, BLOCKED) for p in (p1, p2)]
    [state_info(p) for p in (p1, p2)]

    print()
    [transition(p, p.terminate, TERMINATED) for p in (p1, p2)]
    [state_info(p) for p in (p1, p2)]


if __name__ == '__main__':
    main()
