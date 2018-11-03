# Задание по программированию. Линейная алгебра: сходство текстов 
from scipy.spatial import distance
import re
import numpy as np
import collections

wordsList = []
# Переменная, в которой будет хранится общее количество строк из текстового файла
lCount = 0
with open("sentences.txt") as file:
     for line in file:
         lCount += 1
         # Рзабиваем строку на слова
         # С помощью List comprehesion убираем из полученного списка слов пустые строки
         lineTokens =[token for token in re.split('[^a-z]' , line.lower()) if token !=""]
         wordsList = wordsList + lineTokens

# wCount - эта переменная в итоге буде хранить количество разных слов во всем тексте
# то есть размер словаря indexes
wCount = 1
# Инициализируем словарь индексов, сопоставленных разным словам из всего набора предложений
# создаем в словаре первый элемент {0 : wordslist[0], }
indexes = {0: wordsList[0]}
for word in wordsList:
    if word not in indexes.values():
        wCount = wCount + 1
        indexes[wCount-1] = word
print(indexes)

# Итоговая матрица, в которой будут хранится значения, равные
# количеству вхождений слова из списка wordsList в i-ом предложении
# инициализируем нулями
# indx - количество столбцов матрицы
matrx = np.zeros((lCount, wCount), dtype=int)

tmpCounter = 0 # количество вхождений слова из списка wordsList в текущем предложении
with open("sentences.txt") as file:
    for i, line in file:
        # То же, что и в строке реального кода
        # lineTokens =[token for token in re.split('[^a-z]' , line.lower()) if token !=""]
        lineTokens = [token for token in re.split('[^a-z]', line.lower()) if token]
        matrx[i] = collections.Counter(lineTokens)


cosDistList = []
for v in range(0, lCount):
    # находим для каждой строки
    # косинусные расстояния от нулевой строки (индексация с нуля)
    # spatial.distance.cosine computes the distance, and not the similarity.
    # So, you must subtract the value from 1 to get the similarity
    # https://stackoverflow.com/questions/18424228/cosine-similarity-between-2-number-lists
    cosDistList.append(1 - distance.cosine(matrx[0, :], matrx[v, :]))

print(matrx.shape) 
print(matrx)  
print(cosDistList)

for i in range(0, 21):
    print()
    for j in range(0,253):
        print(matrx[i, j], end="")


            