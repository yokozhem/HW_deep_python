""" 3. В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. 
Не учитывать знаки препинания и регистр символов. 
За основу возьмите любую статью из википедии или из документации к языку.
"""

import re
from collections import Counter

def count_words(text):
    # Приведение текста к нижнему регистру и удаление знаков препинания
    cleaned_text = re.sub(r'[^\w\s]', '', text.lower())
    # Разделение текста на слова и подсчет их количества
    word_counts = Counter(cleaned_text.split())
    # Возвращение 10 самых частых слов
    most_common_words = word_counts.most_common(10)
    return most_common_words

# Пример использования функции
text = """
Vladimir Vladimirovich Putin[c][d] (born 7 October 1952) is a Russian politician and former intelligence 
officer who is the president of Russia. Putin has held continuous positions as president or prime minister 
since 1999:[e] as prime minister from 1999 to 2000 and from 2008 to 2012, and as president from 2000 to 2008 and 
since 2012.[f][7] He is the longest-serving Russian or Soviet leader since Joseph Stalin.
"""
most_common_words = count_words(text)
print("10 самых часто встречающихся слов:")
for word, count in most_common_words:
    print(word, "-", count)

