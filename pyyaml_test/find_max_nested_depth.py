import yaml
import json
import time

def find_max_nested_depth(output_file):
    max_depth = 0
    results = []

    try:
        # 从浅层开始递增深度
        for depth in range(1, 10000):  # 设置一个足够大的上限
            nested_data = {}
            current = nested_data
            for _ in range(depth):
                current["key"] = {}
                current = current["key"]

            # 测试序列化和反序列化
            start_time = time.time()
            yaml_dump = yaml.dump(nested_data)
            yaml_load = yaml.load(yaml_dump, Loader=yaml.FullLoader)
            end_time = time.time()

            # 记录深度和耗时
            results.append({"depth": depth, "time_taken": end_time - start_time})
            max_depth = depth
    except RecursionError:
        print(f"RecursionError encountered at depth: {max_depth + 1}")
    except yaml.YAMLError:
        print(f"YAMLError encountered at depth: {max_depth + 1}")
    finally:
        # 保存测试结果到文件
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=4)
        print(f"Maximum nested depth: {max_depth}")
        print(f"Results saved to {output_file}")
        return max_depth, results

# 运行测试并保存结果
output_file = "data/max_nested_depth.json"
max_depth, depth_results = find_max_nested_depth(output_file)
