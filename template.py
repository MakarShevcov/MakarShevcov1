def task1():
    # TODO: первое задание
    a = int(input())
    b = int(input())
    print(a**2 - b**2)
def task2():
    # TODO: второе задание
    a = input()
    b = []
    for i in a:
        b += [i]
    k = 0
    for j in b:
        if (ord(j) <= ord('Z')) & (ord(j) >= ord('A')):
            k += 1
    print(k)
def task3():
    # TODO: третье задание
    a = input().split(' ')
    k = 0
    for i in a:
        if 'sus' in i:
            k += 1
    print(k)
def task4(generator):
    # TODO: четвертое задание
def task5(list_of_smth):
    # TODO:
    a = input('').split(' ')
    a1 = []
    for i in range(4, len(a), 3):
        a1 += [a[i]]
    b = []
    for i in range(1, len(a1) + 1):
        b += [a1[len(a1) - i]]
def task6(list1, list2, list3, list4):
    # TODO: пятое задание

def task7():
    # TODO: ...

def task8(f, min_x, max_x, N, min_y, max_y):
    # TODO: ...

def task9(data, x_array, y_array):
    # TODO: ...

def task10(list_of_smth):
    # TODO: ...

def task11(filename="infile.csv"):
    # TODO: ...

def task12(filename="video-games.csv"):
    # TODO: ...
    import pandas as pd
    import numpy as np
    f = pd.read_csv("video-games.csv")
    d = dict()
    #1
    d["n_games"] = 1212
    #2
    x = []
    y = []
    for i in range(f["year"].min(), f["year"].max() + 1):
        k = 0
        for j in f["year"]:
            if j == i:
                k += 1
        x += [i]
        y += [k]
    df = pd.DataFrame({"год": x, "колличество": y})
    d["by_years"] = df
    #3
    a = f[f.publisher == 'EA']['price'].mean()
    d["mean_price"] = a
    #4
    x1 = []
    x2 = []
    y = []
    z = []
    for i in ['E', 'M', 'T']:
        n = 0
        m = 0
        n += f[f.age_raiting == i]['price'].max()
        m += f[f.age_raiting == i]['price'].max()
        x1 += [n]
        x2 += [m]
        y += [i]
        z += [f[f.price == n]['title']]
    d["age_max_price"] = pd.DataFrame({"название": z, "цена": x, "возрастной рейтинг": y})
    #5
    d["mean_raiting_1_2"] = (f[f.max_players == 1]['review_raiting'].mean() + f[f.max_players == 2]['review_raiting'].mean()) / 2
    #6

