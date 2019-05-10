import numpy as np
def countingSort(array):
    count_dict = {}
    for i in array:
        if i not in count_dict.keys():
            count_dict[i] = 1
        else:
            count_dict[i] += 1
    count_key = [k for k in count_dict.keys()]
    count_key.sort()
    new_dict = {}

    for kidx in range(len(count_key)):
        if kidx == 0:
            new_dict[count_key[kidx]] = count_dict[count_key[kidx]]
        else:
            new_dict[count_key[kidx]] = count_dict[count_key[kidx]]
            for idx in range(kidx):
                new_dict[count_key[kidx]] += count_dict[count_key[idx]]
    ARRAY = np.empty_like(array)
    for i in array:
        count = new_dict[i]
        ARRAY[count-1] = i
        new_dict[i] -= 1

    return ARRAY.tolist()


if __name__ == "__main__":
    array = [8,5,8,6,3,5,1,3,5,7,8,9,2,4,6,4,4,10,2,6,8,4]
    sorted_array = countingSort(array)
