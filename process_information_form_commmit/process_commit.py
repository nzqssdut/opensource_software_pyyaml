import re
from collections import defaultdict
import json


def process_commit_file(input_file, author_output_file, date_output_file):
    """
    处理 commit 数据，统计作者及日期信息，并保存到文件。
    :param input_file: 包含 commit 数据的输入文件名
    :param author_output_file: 保存作者统计数据的输出文件名
    :param date_output_file: 保存日期统计数据的输出文件名
    """
    # 用于统计作者的提交数量
    author_count = defaultdict(int)
    # 用于统计日期的提交数量和作者
    date_count = defaultdict(lambda: defaultdict(int))

    # 读取文件内容
    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()

    # 使用正则表达式匹配每条 commit 信息
    pattern = r"Commit SHA: ([a-f0-9]{40})\nMessage: (.*?)\nAuthor: (.*?)\nDate: (.*?)\n"
    matches = re.findall(pattern, content, re.DOTALL)

    for _, _, author, date in matches:
        # 按作者统计提交数量
        author_count[author] += 1

        # 按日期统计提交数量及作者
        date_only = date.split("T")[0]  # 提取日期部分
        date_count[date_only][author] += 1

    # 保存作者统计数据到文件
    with open(author_output_file, "w", encoding="utf-8") as f:
        for author, count in sorted(author_count.items(), key=lambda x: x[1], reverse=True):
            f.write(f"{author}: {count}\n")

    # 保存日期统计数据到文件
    with open(date_output_file, "w", encoding="utf-8") as f:
        for date, authors in sorted(date_count.items()):
            f.write(f"Date: {date}\n")
            total_commits = sum(authors.values())
            f.write(f"  Total Commits: {total_commits}\n")
            for author, count in sorted(authors.items(), key=lambda x: x[1], reverse=True):
                f.write(f"    {author}: {count}\n")


# 配置文件名
input_file = "./data/PyyamlCommit.txt"
author_output_file = "./data/commit_author.txt"
date_output_file = "./data/commit_date.txt"

# 调用处理函数
process_commit_file(input_file, author_output_file, date_output_file)
print("统计完成，结果已保存到 ./data/commit_author.txt 和 ./data/commit_date.txt")
