import json
import yaml
import time
import random
import string

def exception_test(output_file):
    results = []

    # 测试无效格式
    invalid_yaml = "key1: value1\nkey2 value2"
    try:
        yaml.load(invalid_yaml, Loader=yaml.FullLoader)
    except yaml.YAMLError as e:
        results.append({"test": "Invalid YAML Format", "result": "Passed", "error": str(e)})

    # 测试深度嵌套
    deep_nested_data = {"key": {}}
    current = deep_nested_data["key"]
    for _ in range(1000):
        current["key"] = {}
        current = current["key"]

    try:
        yaml.dump(deep_nested_data)
        results.append({"test": "Deeply Nested Structure", "result": "Passed"})
    except RecursionError as e:
        results.append({"test": "Deeply Nested Structure", "result": "Failed", "error": str(e)})

    # 测试特殊字符
    special_char_yaml = """key: "value with \\x00 null byte" """
    try:
        yaml.load(special_char_yaml, Loader=yaml.FullLoader)
        results.append({"test": "Special Character", "result": "Passed"})
    except yaml.YAMLError as e:
        results.append({"test": "Special Character", "result": "Failed", "error": str(e)})

    # 保存结果到文件
    with open(output_file, "w", encoding="utf-8") as f:
        for result in results:
            f.write(json.dumps(result, indent=4) + "\n")
    print(f"Exception results saved to {output_file}")

# 运行异常测试并保存结果
exception_results_file = "data/exception_results.txt"
exception_test(exception_results_file)
