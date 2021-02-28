#
# Complete the 'maximumLearning' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY iv
#  2. INTEGER_ARRAY articles
#  3. INTEGER p
#
import os
from sys import setrecursionlimit
from typing import Dict

"""
The question is very similar to the 0-1 knap-sack problem
"""

memo: Dict[tuple, int] = {}  # memoizing  mapping of  ( page_count) ==> the max_value at that time


def get_max_iv(iv, article_pages, max_pages, article_idx=0) -> int:
    n = len(article_pages)
    if article_idx >= n:
        return 0

    if memo.get((max_pages, article_idx)) is not None:
        return memo.get((max_pages, article_idx))

    # two options for each of the article
    # choose this article
    max_iv__including_article = 0
    if max_pages >= article_pages[article_idx]:
        max_iv__including_article = iv[article_idx] + \
                                    get_max_iv(iv, article_pages, max_pages - article_pages[article_idx],
                                               article_idx + 1)

    # do not choose this article
    max_iv__excluding_article = get_max_iv(iv, article_pages, max_pages, article_idx + 1)

    # maximum_intellectual_value i can get
    max_i_value = max(max_iv__including_article, max_iv__excluding_article)
    memo[(max_pages, article_idx)] = max_i_value

    return max_i_value


def maximumLearning(i_value, pages_per_articles, max_pages_per_day) -> int:
    setrecursionlimit(11000)
    pages_after_reading_twice = [2 * page_size for page_size in pages_per_articles]
    # print(articles)
    # print(pages_after_reading_twice)

    return get_max_iv(i_value, pages_after_reading_twice, max_pages_per_day)


if __name__ == '__main__':
    # iv = [2, 4, 4, 5]
    # articles = [2, 2, 3, 4]
    # p = 15
    iv = [3, 2, 2]
    articles = [3, 2, 2]
    p = 9
    print(maximumLearning(iv, articles, p))

""" 
iv = [2, 4, 4, 5]
articles = [2, 2, 3, 4]
p = 15
"""
