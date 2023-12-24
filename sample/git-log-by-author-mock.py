from collections import defaultdict
import matplotlib.pyplot as plt

def plot_counts(counts):
    authors = list(counts.keys())
    line_counts = list(counts.values())

    plt.bar(authors, line_counts)
    plt.xlabel('Author')
    plt.ylabel('Line Count')
    plt.title('Line Counts by Author')
    plt.show()

if __name__ == "__main__":
    counts = defaultdict(int)
    counts['Alice'] = 1125
    counts['Bob'] = 2099
    counts['Charlie'] = 876

    plot_counts(counts)