def maior(x):
    m = x[0]
    for i in range(1, len(x)):
        if x[i] > m:
            m = x[i]
    return m

def main():
    ...

if __name__ == "__main__":
    main()