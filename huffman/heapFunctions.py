def heapify(i, list):
    l = 2 * i + 1
    r = 2 * i + 2
    if l < len(list[0]) and list[1][l] > list[1][i]:
        largest = l
    else:
        largest = i
    if r < len(list[0]) and list[1][r] > list[1][largest]:
        largest = r
    if largest != i:
        list[0][i], list[0][largest] = list[0][largest], list[0][i]
        list[1][i], list[1][largest] = list[1][largest], list[1][i]
        heapify(largest, list)


def buildHeap(list):
    i = len(list[0]) // 2
    while i >= 0:
        heapify(i, list)
        i -= 1