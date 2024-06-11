def bubble_sort(nums):
    sorted = False
    while not sorted:
        to_swap = None
        for idx in range(len(nums) - 1):
            if nums[idx] > nums[idx + 1]:
                to_swap = nums[idx]
                nums[idx] = nums[idx + 1]
                nums[idx + 1] = to_swap
        if to_swap is None:
            sorted = True
    return nums


if __name__ == "__main__":
    nums = [9, 1, 8, 2, 7, 3, 6, 5, 4]
    print(bubble_sort(nums))