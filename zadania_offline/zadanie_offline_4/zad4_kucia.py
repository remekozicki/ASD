from zad4testy import runtests


def num_of_students(h, a, b):
    return h * (b - a)


def possible_building(T, Dorms, num):
    if Dorms[num] is not None:
        return Dorms[num]

    start = 0
    end = num
    while start <= end:
        mid = (start + end) // 2
        if T[mid][0][2] < T[num][0][1]:
            
            if T[mid + 1][0][2] < T[num][0][1]:
                start = mid + 1
            else:
                Dorms[num] = mid
                return Dorms[num]
        else:
            end = mid - 1

    Dorms[num] = -1
    return Dorms[num]


def maximum(T, Dorms, p):
    T.sort(key=lambda building: (building[0][2], building[0][1]))

    n = len(T)
    People = []
    for i in range(n):
        People.append(num_of_students(T[i][0][0], T[i][0][1], T[i][0][2]))

    F = [[0 for _ in range(p + 1)] for _ in range(n)]
    R = [[(0, 0) for _ in range(p + 1)] for _ in range(n)]

    for i in range(T[0][0][3], p + 1):
        F[0][i] = People[0]

    for k in range(p + 1):
        for j in range(1, n):
            F[j][k] = F[j - 1][k]
            R[j][k] = (j - 1, k)

            idx = possible_building(T, Dorms, j)

            if k >= T[j][0][3]:
                if idx == -1:
                    if People[j] > F[j][k]:
                        F[j][k] = People[j]
                        R[j][k] = (-1, -1)
                else:
                    if F[j][k] < F[idx][k - T[j][0][3]] + People[j]:
                        F[j][k] = F[idx][k - T[j][0][3]] + People[j]
                        R[j][k] = (idx, k - T[j][0][3])

    return (n - 1, p), R


def select_buildings(T, p):
    Buildings = []
    n = len(T)

    for i in range(n):
        Buildings.append([T[i], i])

    Dorms = [None for _ in range(n)]

    result, R = maximum(Buildings, Dorms, p)

    output = []
    max_cost = 0
    while result != (0, 0):
        if result == (-1, -1):
            break
        idx = Buildings[result[0]][1]
        if result[1] != R[result[0]][result[1]][1] and T[idx][3] + max_cost <= p:
            output.append(idx)
            max_cost += T[idx][3]

        result = R[result[0]][result[1]]

    return output


runtests(select_buildings)
