def merge_sort(nums: list[int]):
    if len(nums) < 2:
        return nums
    nums_first_half = merge_sort(nums[:len(nums)//2])
    nums_last_half = merge_sort(nums[len(nums)//2:])
    return merge(nums_first_half, nums_last_half)

def merge(first, second):
    final = []
    i, j = 0, 0
    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            final.append(first[i])
            i += 1
        else:
            final.append(second[j])
            j += 1
    while i < len(first):
        final.append(first[i])
        i += 1
    while j < len(second):
        final.append(second[j])
        j += 1
    return final


if __name__ == "__main__":
    nums = [9, 1, 8, 2, 7, 3, 6, 5, 4]
    print(merge_sort(nums))