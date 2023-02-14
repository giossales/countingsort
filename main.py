def maior(x):
    m = x[0]
    for i in range(1, len(x)):
        if x[i] > m:
            m = x[i]
    return m


def counting_sort(arr):
    m = maior(arr)
    aux = [0] * (m + 1)
    for num in arr:
        aux[num] += 1
    
    j = 0
    for i in range(len(aux)):
        while aux[i] > 0:
            arr[j] = i
            aux[i] -= 1
            j += 1
    return arr


def main():
    print(counting_sort([5, 18, 11, 11, 15, 19, 12, 18]))


if __name__ == "__main__":
    main()