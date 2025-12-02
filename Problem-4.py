Task: For the given list of integers, return counts of how many numbers are divisible by each integer in [1,2,3,4,5,6,7,8,9]. Output a dictionary or printed mapping.

Given example:
Input: [1,2,8,9,12,46,76,82,15,20,30]
Output: {1:11, 2:8, 3:4, 4:4, 5:3, 6:2, 7:0, 8:1, 9:1}

# Problem-4.py


def count_multiples(numbers, divisors=range(1, 10)):
    # initialize counts to zero
    counts = {d: 0 for d in divisors}
    for n in numbers:
        for d in divisors:
            if n % d == 0:
                counts[d] += 1
    return counts

if __name__ == "__main__":
    sample = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
    result = count_multiples(sample)
    # Print in the exact format from example (sorted by divisor)
    print(result)  # e.g. {1:11, 2:8, 3:4, ...}

Explanation:
For each number, check divisibility against 1..9 and increment counters.
This is straightforward and correct for the example.
Complexity: O(n * 9) = O(n) where n = len(numbers). Space O(1) extra (counts size fixed 9), O(n) if storing input list.
