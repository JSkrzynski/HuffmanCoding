from heapFunctions import *
from pathlib import Path


def count(sequence):
    array = []
    sequence = sorted(sequence)
    sequence = list(sequence)
    for i in sequence:
        if i not in array:
            array.append(i)
    dictionary = []
    list1, list2 = [], []
    for a in array:
        n = 0
        for letter in sequence:
            if letter == a:
                n += 1
        list1.append(a)
        list2.append(n)
    dictionary.append(list1)
    dictionary.append(list2)
    return dictionary


def findingMin(list):
    key = list[0][0]
    value = list[1][0]
    i = 0
    index = 0
    for element in list[1]:
        if element <= value:
            key = list[0][i]
            value = element
            index = i
        i += 1
    del list[0][index]
    del list[1][index]
    buildHeap(list)
    return key, value


def insert(list, key, value):
    list[0].append(key)
    list[1].append(value)
    buildHeap(list)


def encodeSign(letter, list):
    result = ""
    for key in list:
        if key != letter:
            if key.startswith(letter):
                letter = key
                result += "0"
            elif key.endswith(letter):
                letter = key
                result += "1"
    return result[::-1]


def dictionaryMaker(list):
    dictionary = {}
    for letter in list:
        if len(letter) == 1:
            dictionary[letter] = encodeSign(letter, list)
    return dictionary


def results(strInput):
    dictionary = count(strInput)
    listTwo = {}
    while len(dictionary[0]) != 1:
        key1, value1 = findingMin(dictionary)
        key2, value2 = findingMin(dictionary)
        if value1 < value2:
            name = key1 + key2
            listTwo[key1] = value1
            listTwo[key2] = value2
            listTwo[name] = value1 + value2
        else:
            name = key2 + key1
            listTwo[key2] = value2
            listTwo[key1] = value1
            listTwo[name] = value1 + value2
        insert(dictionary, name, value1 + value2)
    return dictionaryMaker(list(listTwo.keys()))


def encode(filename):
    txt = Path(filename).read_text(encoding="utf-8")
    dictionary = results(txt)
    txt = list(txt)
    for item in txt:
        txt[txt.index(item)] = dictionary[item]
    arr = ''
    for char in txt:
        arr += char
    i = 9
    while i < len(arr):
        arr = arr[0:i] + " " + arr[i:]
        i += 9
    arr = arr.split(" ")

    file = open("encoded" + filename, "w+")
    for item in arr:
        file.write(item)
    file.close()
