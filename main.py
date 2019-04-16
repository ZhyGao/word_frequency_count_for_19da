from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import jieba

from wordcloud import WordCloud, ImageColorGenerator


def save_cloud_img(wordlist):

    wl = " ".join(wordlist)

    coloring = np.array(Image.open(path.join(d, "background.jpg")))


    # 设置停用词
    # stopwords = set(STOPWORDS)
    # stopwords.add("said")

    # 你可以通过 mask 参数 来设置词云形状
    wc = WordCloud(background_color="white", max_words=2000, mask=coloring,
                    max_font_size=50, random_state=42,font_path='simsun.ttf')

    wc.generate(wl)

    # create coloring from image
    image_colors = ImageColorGenerator(coloring)
    wc.recolor(color_func=image_colors)
    # show
    # 在只设置mask的情况下,你将会得到一个拥有图片形状的词云
    plt.imshow(wc)
    plt.axis("off")
    plt.savefig("./save_img.png")
    plt.show()



d = path.dirname(__file__)

# Read the whole text.
text = open(path.join(d, '19da.txt'), encoding='gb18030').read()

# 结巴分词
words = jieba.lcut(text)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word,0) + 1
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)
for i in range(30):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))
save_cloud_img(words)
