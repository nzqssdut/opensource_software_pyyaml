import re
from collections import Counter

# 手动定义一个简单的英语停用词集合
STOP_WORDS = {"a", "an", "the", "and", "or", "but", "is", "are", "was", "were", "in", "on", "at", "to", "of", "for",
              "with", "about", "as", "by", "it", "this", "that", "these", "those", "not", "no", "nor", "only", "just",
              "yet", "so", "such", "very", "too", "also", "any", "all", "each", "every", "some", "few", "many", "much",
              "several", "whom", "which", "who", "whose", "what", "when", "where", "why", "how"}

# 读取文件内容
file_path = r"D:\PyyamlIssue.txt"
with open(file_path, 'r', encoding='utf-8') as file:
    text_data = file.read()


# 使用正则表达式进行简单的分词处理
def simple_tokenize(text):
    words = re.findall(r'\b\w+\b', text)
    return words


# 预处理函数：分词、去除停用词、标注（这里简化处理，不进行词性标注）
def preprocess_text(text):
    # 分词
    words = simple_tokenize(text)
    # 移除停用词
    filtered_words = [word.lower() for word in words if word.isalpha() and word.lower() not in STOP_WORDS]
    return filtered_words


# 处理文本
processed_text = preprocess_text(text_data)

# 统计词频
word_counts = Counter(processed_text)

# 将结果写入文件
output_file_path = "result.txt"
with open(output_file_path, 'w', encoding='utf-8') as file:
    for word, count in word_counts.most_common():
        file.write(f"{word}: {count}\n")

print(f"词频统计完成，结果已保存至 {output_file_path}")
