import json
import matplotlib.pyplot as plt

from pyyaml_test.find_max_nested_depth import max_depth

output_file = "data/max_nested_depth.json"
# 加载测试结果
with open(output_file, "r", encoding="utf-8") as f:
    depth_results = json.load(f)

# 提取数据
depths = [item["depth"] for item in depth_results]
times = [item["time_taken"] for item in depth_results]

# 可视化
plt.figure(figsize=(10, 6))
plt.plot(depths, times, marker="o", color="blue", label="Time Taken")
plt.axvline(x=max_depth, color="red", linestyle="--", label=f"Max Depth = {max_depth}")
plt.xlabel("Nested Depth", fontsize=12)
plt.ylabel("Time Taken (seconds)", fontsize=12)
plt.title("Maximum Nested Depth Performance", fontsize=14)
plt.legend()
plt.grid()
plt.tight_layout()

# 保存图表
visualization_file = "data/max_nested_depth_visualization.png"
plt.savefig(visualization_file)
plt.show()

print(f"Visualization saved to {visualization_file}")
