import xml.etree.ElementTree as etree
import json


class JSONConnector:
    """
    类JSONConnector解析JSON文件，通过parsed_data()方法以一个字典（dict）的形式 返回数据。
    修饰器property使parsed_data()显得更像一个常规的变量，而不是一个方法
    """

    def __init__(self, filepath):
        print(444)
        self.data = None
        with open(filepath, mode='r', encoding='utf-8') as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data


class XMLConnector:
    """
    类XMLConnector解析XML文件，通过parsed_data()方法以xml.etree.Element列表的形式返回所有数据
    """

    def __init__(self, filepath):
        self.tree = etree.parse(filepath)

    @property
    def parsed_data(self):
        return self.tree


def connection_factory(filepath):
    """
    函数connection_factory是一个工厂方法，基于输入文件路径的扩展名返回一个 JSONConnector或XMLConnector的实例
    :param filepath:
    :return: 返回一个 JSONConnector或XMLConnector的实例
    """
    print(filepath)
    if filepath.endswith("json"):
        connector = JSONConnector
    elif filepath.endswith("xml"):
        connector = XMLConnector
    else:
        raise ValueError('Cannot connect to {}'.format(filepath))
    return connector(filepath)


def connect_to(filepath):
    """
    函数connect_to()对connection_factory()进行包装，添加了异常处理
    :param filepath:
    :return:返回一个JSONConnector或XMLConnector的实例对象
    """
    factory = None
    try:
        factory = connection_factory(filepath)
    except ValueError as ve:
        print(ve)
    return factory


def main(filepath):
    # 函数main()演示如何使用工厂方法设计模式。第一部分是确认异常处理是否有效
    data_factory = connect_to(filepath)
    # 第二部分是得到数据格式对应的处理
    new_data = data_factory.parsed_data
    # 第三部分是根据不同数据格式做特定的处理方法
    if type(data_factory) == XMLConnector:
        liars = new_data.findall(".//{}[{}='{}']".format('person', 'lastName', 'Liar'))
        print('found: {} persons'.format(len(liars)))
        for liar in liars:
            print('first name: {}'.format(liar.find('firstName').text))
            print('last name: {}'.format(liar.find('lastName').text))
            [print('phone number ({})'.format(p.attrib['type']), p.text)
             for p in liar.find('phoneNumbers')]
    if type(data_factory) == JSONConnector:
        for donut in new_data:
            print('name: {}'.format(donut['name']))
            print('price: ${}'.format(donut['ppu']))
            [print('topping: {} {}'.format(t['id'], t['type'])) for t in donut['topping']]


if __name__ == '__main__':
    main("person.xml")



"""
像现在这样，代码并未禁止直接实例化一个连接器。如果要禁止直接实例化，是否可以实现？ 试试看。 
 提示：Python中的函数可以内嵌类。 
"""