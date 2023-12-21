import matplotlib.pyplot as plt
import pandas as pd

# Gitログファイルを解析する関数
def parse_git_log(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) == 3:
                additions, deletions, author = parts
                try:
                    additions = int(additions)
                    deletions = int(deletions)
                    data.append((author, additions, deletions))
                except ValueError:
                    continue
    return data

# ログデータを解析
git_log_data = parse_git_log('git_log.txt')

# データをDataFrameに変換
df = pd.DataFrame(git_log_data, columns=['Author', 'Additions', 'Deletions'])
grouped_df = df.groupby('Author').sum()

# 棒グラフを作成
grouped_df.plot(kind='bar', stacked=True)
plt.title('Git Contributions by Author')
plt.xlabel('Author')
plt.ylabel('Lines of Code')
plt.show()
