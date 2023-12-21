import matplotlib.pyplot as plt
import pandas as pd
import subprocess
import sys

def save_git_log(author_name):
    command = ['git', 'log', f'--author={author_name}', '--pretty=tformat:', '--numstat']
    with open('git_log.txt', 'w') as f:
        subprocess.run(command, stdout=f)

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

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python git-log.py [Author Name]")
        sys.exit(1)

    save_git_log(sys.argv[1])
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