# python3
# 221RDB128 Bernhards Arnitis 11

def build_heap(data):
    n = len(data)
    swaps = []
    for i in range(n//2 - 1, -1, -1): 
        mazakais = i
        kreis = 2 * i + 1
        labs = 2 * i + 2

        if kreis < n and data[kreis] < data[mazakais]:
            mazakais = kreis
        if labs < n and data[labs] < data[mazakais]:
            mazakais = labs
        if mazakais != i:
            data[i], data[mazakais] = data[mazakais], data[i]
            swaps.append((i, mazakais)) 
            k = mazakais
            while k * 2 + 1 < n:
                j = k * 2 + 1
                if j + 1 < n and data[j + 1] < data[j]:
                    j += 1
                if data[k] <= data[j]:
                    break
                data[k], data[j] = data[j], data[k]
                swaps.append((k, j))
                k = j
    return swaps
# TODO: Creat heap and heap sort
# try to achieve  O(n) and not O(n2)
    


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    text = input()
    if "I" in text:
        n = int(input())
        data = list(map(int, input().split()))
        swaps = build_heap(data)
        m = len(swaps)
        print(m)
        for i, j in swaps:
            print(i, j)
    if "F" in text:
        files = input()
        if "a" not in files:
            with open("/test + files") as fl:
                n = int(input())
                data = list(map(int, input().split()))
                swaps = build_heap(data)
                m = len(swaps)
                print(m)
                for i, j in swaps:
                    print(i, j)

    # checks if lenght of data is the same as the said lenght
    #assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps


if __name__ == "__main__":
    main()
