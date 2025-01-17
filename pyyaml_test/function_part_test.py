import yaml
import unittest


class TestPyYAML(unittest.TestCase):
    def test_simple_dict_load_and_dump(self):
        # 测试简单字典的加载和转储
        # 定义一个简单的 Python 字典，包含人的基本信息
        data = {'name': 'John', 'age': 30}
        print(f"Original simple dictionary: {data}")

        try:
            # 将字典转储为 YAML 格式的字符串，使用 yaml.dump 函数
            # dump 函数将 Python 对象序列化为 YAML 格式的字符串
            yaml_str = yaml.dump(data)
            print(f"YAML string of simple dictionary: {yaml_str}")
        except yaml.YAMLError as e:
            self.fail(f"Failed to dump simple dictionary to YAML: {e}")

        try:
            # 从 YAML 字符串加载数据，使用 yaml.load 函数并指定 Loader 为 yaml.FullLoader
            # FullLoader 是一种安全的加载器，避免潜在的安全问题，例如反序列化恶意代码
            loaded_data = yaml.load(yaml_str, Loader=yaml.FullLoader)
            print(f"Loaded data from YAML string: {loaded_data}")
        except yaml.YAMLError as e:
            self.fail(f"Failed to load simple dictionary from YAML: {e}")

        # 验证加载的数据是否与原始数据相同，使用 unittest 的 assertEqual 方法
        # 如果两者不相等，测试将失败并输出相应的错误信息
        self.assertEqual(data, loaded_data, "The loaded data from the simple dictionary should match the original data.")

        # 将输出结果存储到文件中
        with open('./data/simple_dict_test_output.txt', 'a') as f:
            f.write(f"Original simple dictionary: {data}\n")
            f.write(f"YAML string of simple dictionary: {yaml_str}\n")
            f.write(f"Loaded data from YAML string: {loaded_data}\n")
            f.write("---------------------------\n")

    def test_nested_dict_load_and_dump(self):
        # 测试嵌套字典的加载和转储
        # 定义一个更复杂的嵌套字典，包含人的信息和地址信息
        data = {
            'person': {
                'name': 'John',
                'age': 30,
                'address': {
                    'city': 'New York',
                    'zipcode': '10001'
                }
            }
        }
        print(f"Original nested dictionary: {data}")

        try:
            # 将嵌套字典转储为 YAML 格式的字符串
            yaml_str = yaml.dump(data)
            print(f"YAML string of nested dictionary: {yaml_str}")
        except yaml.YAMLError as e:
            self.fail(f"Failed to dump nested dictionary to YAML: {e}")

        try:
            # 从 YAML 字符串加载数据
            loaded_data = yaml.load(yaml_str, Loader=yaml.FullLoader)
            print(f"Loaded data from YAML string: {loaded_data}")
        except yaml.YAMLError as e:
            self.fail(f"Failed to load nested dictionary from YAML: {e}")

        # 验证加载的数据是否与原始数据相同
        self.assertEqual(data, loaded_data, "The loaded data from the nested dictionary should match the original data.")

        # 将输出结果存储到文件中
        with open('./data/nested_dict_test_output.txt', 'a') as f:
            f.write(f"Original nested dictionary: {data}\n")
            f.write(f"YAML string of nested dictionary: {yaml_str}\n")
            f.write(f"Loaded data from YAML string: {loaded_data}\n")
            f.write("---------------------------\n")

    def test_list_load_and_dump(self):
        # 测试列表的加载和转储
        # 定义一个包含不同数据类型的列表，包含字符串、整数和字典
        data = ['apple', 123, {'key': 'value'}]
        print(f"Original list: {data}")

        try:
            # 将列表转储为 YAML 格式的字符串
            yaml_str = yaml.dump(data)
            print(f"YAML string of list: {yaml_str}")
        except yaml.YAMLError as e:
            self.fail(f"Failed to dump list to YAML: {e}")

        try:
            # 从 YAML 字符串加载数据
            loaded_data = yaml.load(yaml_str, Loader=yaml.FullLoader)
            print(f"Loaded data from YAML string: {loaded_data}")
        except yaml.YAMLError as e:
            self.fail(f"Failed to load list from YAML: {e}")

        # 验证加载的数据是否与原始数据相同
        self.assertEqual(data, loaded_data, "The loaded data from the list should match the original data.")

        # 将输出结果存储到文件中
        with open('./data/list_test_output.txt', 'a') as f:
            f.write(f"Original list: {data}\n")
            f.write(f"YAML string of list: {yaml_str}\n")
            f.write(f"Loaded data from YAML string: {loaded_data}\n")
            f.write("---------------------------\n")

    def test_nested_list_load_and_dump(self):
        # 测试嵌套列表的加载和转储
        # 定义一个嵌套的列表，包含多个子列表，子列表中包含不同的数据类型
        data = [['apple', 'banana'], [1, 2, 3], [{'key1': 'value1'}, {'key2': 'value2'}]]
        print(f"Original nested list: {data}")

        try:
            # 将嵌套列表转储为 YAML 格式的字符串
            yaml_str = yaml.dump(data)
            print(f"YAML string of nested list: {yaml_str}")
        except yaml.YAMLError as e:
            self.fail(f"Failed to dump nested list to YAML: {e}")

        try:
            # 从 YAML 字符串加载数据
            loaded_data = yaml.load(yaml_str, Loader=yaml.FullLoader)
            print(f"Loaded data from YAML string: {loaded_data}")
        except yaml.YAMLError as e:
            self.fail(f"Failed to load nested list from YAML: {e}")

        # 验证加载的数据是否与原始数据相同
        self.assertEqual(data, loaded_data, "The loaded data from the nested list should match the original data.")

        # 将输出结果存储到文件中
        with open('./data/nested_list_test_output.txt', 'a') as f:
            f.write(f"Original nested list: {data}\n")
            f.write(f"YAML string of nested list: {yaml_str}\n")
            f.write(f"Loaded data from YAML string: {loaded_data}\n")
            f.write("---------------------------\n")


if __name__ == '__main__':
    unittest.main()