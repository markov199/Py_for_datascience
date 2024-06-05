import sys
import time
import os

def ft_tqdm(lst: range):
    total = len(lst)
    progress = 0
    for x in lst:
        progress += 1
        percent = (progress / total * 100)
        # calcutale bar length using terminal size
        total_bar = int(2 / 3 * os.get_terminal_size().columns)
        progress_bar = int(percent * total_bar / 100)
        print(f"{int(percent)}%|{"=" * (progress_bar- 1)}>{"-" * (total_bar - progress_bar)}|{ progress}/{total}", end="\r")
        yield (x)

""" ref
    https://github.com/tqdm/tqdm#iterable-based#user-content-usage
"""
