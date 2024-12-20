def missingnumber(arr):
    n = len(arr) + 1
    NowSum = sum(arr)
    ExpectedSum = (n * (n + 1)) / 2
    return ExpectedSum - NowSum

arr=[1,2,3,4,6,7,8]
print(missingnumber(arr))