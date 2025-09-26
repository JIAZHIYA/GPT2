import json
import os

# 定义TXT文件路径和输出的JSON文件路径
txt_folder_path = '../data/'
json_file_path = './input.json'


# 函数：将txt文件中的每篇文章提取出来并转换为json格式
def convert_txt_to_json(txt_folder_path, json_file_path):
    articles = []

    # 遍历文件夹中的所有txt文件
    for filename in os.listdir(txt_folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(txt_folder_path, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                # 读取文件内容并加入到文章列表中
                article = file.read().strip()  # 去掉首尾空格
                articles.append(article)

    # 将文章列表写入JSON文件
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(articles, json_file, ensure_ascii=False, indent=4)


# 执行转换
convert_txt_to_json(txt_folder_path, json_file_path)

print("转换完成！")
