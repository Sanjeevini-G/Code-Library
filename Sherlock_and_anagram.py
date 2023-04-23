#!/bin/python3

import math
import os
import random
import re
import sys

from collections import defaultdict

def sherlockAndAnagrams(s):
    # create a dictionary to store the frequency of each substring
    substr_freq = defaultdict(int)
    # loop over all substrings of the input string
    for i in range(len(s)):
        for j in range(i, len(s)):
            # sort the substring and use it as a key in the dictionary
            sorted_sub = ''.join(sorted(s[i:j+1]))
            substr_freq[sorted_sub] += 1
    # count the number of anagrammatic pairs of substrings
    anagram_count = 0
    for freq in substr_freq.values():
        anagram_count += freq * (freq - 1) // 2
    return anagram_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
