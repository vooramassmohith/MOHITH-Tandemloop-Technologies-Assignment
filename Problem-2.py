Task: Given integer a, generate the first a odd numbers starting from 1 (exactly a numbers)

solution:

# Problem-2.py
# Generate first `a` odd numbers (starting from 1).
# Example: a=4 -> 1, 3, 5, 7

def generate_odds(a: int):
    if a <= 0:
        return []
    # We can compute k-th odd as 2*k+1 for k starting 0..a-1
    return [2*i + 1 for i in range(a)]

if __name__ == "__main__":
    # Example runs (prints comma separated)
    for a in [1, 2, 3, 4, 5]:
        seq = generate_odds(a)
        print(f"a = {a} -> {', '.join(map(str, seq))}")


Explanation:

Uses list comprehension: odd numbers are 1,3,5,... which are 2*i+1.
For a terms, i goes from 0 to a-1.

Complexity: O(a) time, O(a) space (to store list).
