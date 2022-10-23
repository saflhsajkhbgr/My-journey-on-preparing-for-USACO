

def check(d1, d2):
    d1greater = 0
    d2greater = 0
    for i in d1:
        for j in d2:
            if i > j:
                d1greater += 1
            elif j > i:
                d2greater += 1

    if d1greater > d2greater:
        return 1
    elif d1greater < d2greater:
        return -1
    else:
        return 0


def main(A, B):
    res = check(A, B)
    if res == 0:
        return 'no'
    elif res == 1:
        # A>B
        for j in range(1, 11):
            for k in range(1, 11):
                for m in range(1, 11):
                    for n in range(1, 11):
                        if check([j, k, m, n], A) == 1 and check([j, k, m, n], B) == -1:
                            return 'yes'
        return 'no'
    elif res == -1:
        # A<B
        for j in range(1, 11):
            for k in range(1, 11):
                for m in range(1, 11):
                    for n in range(1, 11):
                        if check([j, k, m, n], A) == -1 and check([j, k, m, n], B) == 1:
                            return 'yes'
        return 'no'


if __name__ == '__main__':
    # with open('prob2_bronze_jan22/3.in') as file:
    #     n = int(file.readline())
    #     for i in range(n):
    #         line = [int(i) for i in file.readline().split()]
    #         A = line[0:4]
    #         B = line[4:8]
    #         ans = main(A, B)
    #         print(ans)
    n = int(input())
    for i in range(n):
        line = [int(i) for i in input().split()]
        A = line[0:4]
        B = line[4:8]
        ans = main(A, B)
        print(ans)