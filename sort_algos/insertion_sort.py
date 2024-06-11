def insertion_sort(nums):
    for idx in range(1, len(nums)):
        j = idx
        while j > 0 and nums[j-1] > nums[j]:
            nums[j-1], nums[j] = nums[j], nums[j-1]
            j = j - 1
    return nums


if __name__ == "__main__":
    nums = [9, 1, 8, 2, 7, 3, 6, 5, 4]
    print(insertion_sort(nums))
