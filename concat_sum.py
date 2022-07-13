"""
This problem is from CodeSignal
Observ: 
- Need to have function to concat two numbers

Brute force:
- Then iterate brute force through all the combinations
Time: O(n^2)
Space: O(1)

Add contribution of each item:
- Store the # of digits in each element of a
- Then sum the contribution of each item using the digit count
"""


def solution(a):
    """
    parameters:
    a: This is a list of integers to be concat-summed
    Time: O(n)
    Space: O(n)
    """
    sum, list_sum = 0, 0
    # create a var for the sum of all the nums in a (we are going to add this after iterating through each element in a)
    for num in a:
        list_sum += num

    # create the digit count map
    digit_count = [len(str(n)) for n in a]

    # scan through each element in a to count
    for num in a:
        for dc in digit_count:
            sum += num * (10 ** dc)
        sum += list_sum

    return sum


def main():
    a = [10, 2]  # expect 1344
    print(solution(a))
    b = [11, 22]  # expect 6666
    print(solution(b))


if __name__ == "__main__":
    main()
