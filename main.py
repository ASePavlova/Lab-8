# Лаботрная работа 8
# Написать функцию, которая находит n-ый по порядку убывания элемент с списке без сортировки
def kbig(nums, u):
    if u==1:
        return max(nums)
    z = nums[0]
    r1=max(nums)
    nums.remove(r1)

    for y in range(0, len(nums)):

        for w in range(0, len(nums)):

            if abs(r1 - nums[w]) < z:
                z = abs(r1 - nums[w])
                ql = nums[w]

        z=nums[0]

        r1 = ql
        nums.remove(r1)

        if y+2 == u:
            return r1
