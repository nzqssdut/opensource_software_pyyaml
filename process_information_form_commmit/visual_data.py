import matplotlib.pyplot as plt
from collections import defaultdict


# 处理commit_author.txt
def read_commit_author(file_path):
    author_data = {}
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            author, count = line.strip().split(": ")
            author_data[author] = int(count)
    return author_data


# 处理commit_date.txt
def read_commit_date(file_path):
    date_data = defaultdict(set)
    with open(file_path, "r", encoding="utf-8") as f:
        current_date = None
        for line in f:
            if line.startswith("Date:"):
                current_date = line.strip().split(": ")[1]
            elif current_date and not line.startswith("  Total"):
                author = line.strip().split(": ")[0]
                date_data[current_date].add(author)
    return date_data


# 对commit_author.txt进行可视化
def visualize_author_data(author_data, output_file):
    authors = list(author_data.keys())
    commit_counts = list(author_data.values())

    plt.figure(figsize=(10, 6))
    plt.bar(authors, commit_counts, color='skyblue',align='center')
    plt.xlabel('Author', fontsize=12)
    plt.ylabel('Number of Commits', fontsize=12)
    plt.title('Commits by Author', fontsize=14)
    plt.xticks(rotation=60, ha='right')
    plt.tight_layout()
    plt.savefig(output_file)
    plt.show()


# 对commit_date.txt进行可视化
def visualize_date_data(date_data, output_file):
    dates = []
    author_counts = []
    for date, authors in sorted(date_data.items()):
        dates.append(date)
        author_counts.append(len(authors))

    plt.figure(figsize=(30, 6))
    plt.scatter(dates, author_counts, color='red', label='Authors per Day')
    plt.xlabel('Date', fontsize=5)
    plt.ylabel('Number of Authors', fontsize=12)
    plt.title('Number of Authors by Date', fontsize=14)
    plt.xticks(rotation=90, ha='right')
    plt.tight_layout()
    plt.legend()
    plt.savefig(output_file)
    plt.show()


# 文件路径和输出文件
commit_author_file = "data/commit_author.txt"
commit_date_file = "data/commit_date.txt"
author_output_image = "data/commit_author_bar_chart.png"
date_output_image = "data/commit_date_scatter_plot.png"

# 执行方法
author_data = read_commit_author(commit_author_file)
date_data = read_commit_date(commit_date_file)

visualize_author_data(author_data, author_output_image)
visualize_date_data(date_data, date_output_image)
