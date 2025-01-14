import json
import yaml
import time
import random
import string

# 生成测试数据
def generate_data(size):
    return {
        "name": "example",
        "data": ["".join(random.choices(string.ascii_letters, k=10)) for _ in range(size)],
        "nested": {f"key_{i}": random.randint(1, 100) for i in range(size // 10)},
    }

# 性能测试函数
def performance_test(output_file):
    results = []
    sizes = [10, 100, 1000, 10000,100000,1000000]
    for size in sizes:
        data = generate_data(size)

        # 测试序列化性能
        start_time = time.time()
        yaml_dump = yaml.dump(data)
        dump_time = time.time() - start_time

        # 测试反序列化性能
        start_time = time.time()
        yaml_load = yaml.load(yaml_dump, Loader=yaml.FullLoader)
        load_time = time.time() - start_time

        # 保存结果
        results.append({
            "data_size": size,
            "dump_time": f"{dump_time} s",
            "load_time": f"{load_time} s"
        })

    # 保存到文件
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4)
    print(f"Performance results saved to {output_file}")

# 运行性能测试并保存结果
performance_results_file = "./data/performance_results.json"
performance_test(performance_results_file)
