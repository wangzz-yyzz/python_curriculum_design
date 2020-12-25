def quick_sort(data: list, left, right):
    if left < right:
        i = left
        j = right
        pivot = data[left]
        while i != j:
            while j > i and data[j].get_score() < pivot.get_score():
                j -= 1
            if j > i:
                data[i] = data[j]
                i += 1
            while i < j and data[i].get_score() > pivot.get_score():
                i += 1
            if i < j:
                data[j] = data[i]
                j -= 1
        data[i] = pivot
        quick_sort(data, left, i - 1)
        quick_sort(data, i + 1, right)
