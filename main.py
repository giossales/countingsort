def main() -> None:
    lst = eval(input())
    #input1: list = [5, 18, 11, 11, 15, 19, 12, 18]
    #input2: list = [12, 5, 1, 7, 11, 50, 9, 14, 15, 12]
    print(f"{counting_sort(lst)} (Sorted: {is_sorted(lst)})")

def maior(x: list) -> int:
    m: int = x[0]
    for i in range(1, len(x)):
        if x[i] > m:
            m = x[i]
    return m

def counting_sort(arr: list) -> list:
    m: int = maior(arr)
    aux: list = [0] * (m + 1)
    for num in arr:
        aux[num] += 1
    j: int = 0
    for i in range(len(aux)):
        while aux[i] > 0:
            arr[j] = i
            aux[i] -= 1
            j += 1
    return arr

def is_sorted(arr: list) -> bool:
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            return False
    return True

if __name__ == "__main__":
    main()