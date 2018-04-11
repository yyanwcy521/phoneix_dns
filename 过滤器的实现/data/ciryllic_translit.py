import codecs
from transliterate.utils import slugify

out = open('ru_translit.txt', 'w')

with codecs.open('ru__.txt.txt', 'r', 'utf-8') as f:
    for line in f:
        out.write(slugify(line) + '\n')
