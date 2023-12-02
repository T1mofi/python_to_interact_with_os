import os

# create file
open('novel.txt', 'w')

os.rename('novel.txt', 'tsimafeis_novel.txt')

os.remove('tsimafeis_novel.txt')
