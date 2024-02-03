def filter_even_nums(nums):
    def is_odd(n):
        return n & 1

    return list(filter(is_odd, nums))


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filter_even_nums(nums))
