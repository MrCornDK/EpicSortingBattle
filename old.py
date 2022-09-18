def dMerge(items):
    if len(items) < len(items):

def mergeSort(items):
    if len(items) > 1:
        items = demerge(items)
        print(items)
        print(items[0])
        print(items[1])
        for i in items:
            i = mergeSort(i)
    return items
def bubbleSort(items):
    i = 0
    while i < len(items)-1:
        j = 0
        while j < len(items)-i-1:
            if items[j] > items[j+1]:
                current = items[j]
                items[j] = items[j+1]
                items[j+1] = current
            j += 1
        i += 1
    return items
def old_de_merge(items):
    t_items = []
    item_l = len(items)
    if item_l % 2 == 0 and item_l > 1:
        if item_l != 2:
            f_map = map(items.__getitem__, [0, int(item_l / 2 - 1)])
            s_map = map(items.__getitem__, [int(item_l / 2 - 1), item_l - 1])
        else:
            f_map = map(items.__getitem__, [0])
            s_map = map(items.__getitem__, [item_l - 1])
        t_items.append([list(f_map), list(s_map)])
    elif item_l % 2 == 1 and item_l > 1:
        f_map = map(items.__getitem__, [0, int((item_l + 1) / 2 - 1)])
        print("d")
        if item_l != 3:
            s_map = map(items.__getitem__, [int((item_l - 1) / 2 + 1), item_l - 1])
            print("e")
        else:
            s_map = map(items.__getitem__, [int((item_l - 1) / 2 + 1)])
            print("l")
        t_items.append(list(f_map))
        t_items.append(list(s_map))

    else:
        t_items = items
    return t_items

def old_merge(items):
    items = de_merge(items)
    if len(items) > 1:
        for r in range(len(items)):
            items[r] = mergeSort(items[r])
        if len(items[0]) == 1:
            print(items)
    return items


def demerge(items):
    global o_e
    length = len(items)
    t_arr = []
    t_arr2 = []
    i = 0
    if length % 2 == 0:
        while length / 2 > i:
            t_arr.append(items[i])
            t_arr2.append(items[i + int(length / 2)])
            i += 1
    elif length % 2 == 1:
        while (length - 1) / 2 > i:
            t_arr.append(items[i])
            t_arr2.append(items[i + int((length + 1) / 2)])
            i += 1
        t_arr.append(items[i])
    if len(t_arr) == 1:
        t_arr.append(t_arr2[0])
        res = t_arr
    else:
        res = [t_arr, t_arr2]
    return res


def OLDmergeSrt(items):
    global o_e
    if type(items) != int:
        if len(items) > 1:
            items = merge(items)
            items[0] = mergeSrt(items[0])
            items[1] = mergeSrt(items[1])

            if type(items[0]) == int:
                if len(items) == 2:
                    if items[0] < items[1]:
                        items = [items[0], items[1]]
                    else:
                        items = [items[1], items[0]]
            elif (len(items[0]) + len(items[1])) % 2 == 1:
                t_arr = []
                if len(items[0]) > len(items[1]):
                    it = items[0]
                    print("0")
                else:
                    it = items[1]
                    print("1")

                for i in range(len(it) - 1):
                    if items[0][i] < items[1][i]:
                        t_arr.append(items[0][i])
                        t_arr.append(items[1][i])

                    else:
                        t_arr.append(items[1][i])
                        t_arr.append(items[0][i])
                i = 0
                while it[-1] < t_arr[-i-1]:
                    i += 1

                x = slice(len(t_arr)-i)
                y = slice(len(t_arr)-i, len(t_arr))
                print("s",t_arr[x],t_arr[y])
                print(it)
                print("t1",t_arr)
                print("it0",items[0])
                print("it1",items[1])
                t_arr = t_arr[x]+[it[-1]]+t_arr[y]
                print("t2",t_arr)
                items = t_arr
            else:
                t_arr = []
                print(items[0])
                print(items[1])
                for i in range(len(items[0])):
                    if items[0][i] < items[1][i]:
                        t_arr.append(items[0][i])
                        t_arr.append(items[1][i])
                    else:
                        t_arr.append(items[1][i])
                        t_arr.append(items[0][i])

                items = t_arr

    return items