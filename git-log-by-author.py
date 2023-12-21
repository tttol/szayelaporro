import subprocess
import sys
from collections import defaultdict
import matplotlib.pyplot as plt

def count_lines_by_author(author_names):
    counts = defaultdict(int)
    for author_name in author_names:
        command = ['git', 'log', f'--author={author_name}', '--pretty=tformat:', '--numstat']
        result = subprocess.run(command, capture_output=True, text=True)
        lines = result.stdout.splitlines()

        for line in lines:
            additions, deletions, _ = line.split('\t', 2)
            if additions.isdigit():
                counts[author_name] += int(additions)
            if deletions.isdigit():
                counts[author_name] += int(deletions)

    return counts

def plot_counts(counts):
    authors = list(counts.keys())
    line_counts = list(counts.values())

    plt.bar(authors, line_counts)
    plt.xlabel('Author')
    plt.ylabel('Line Count')
    plt.title('Line Counts by Author')
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python git-log.py [Author Name 1] [Author Name 2] ...")
        sys.exit(1)

    counts = count_lines_by_author(sys.argv[1:])
    plot_counts(counts)