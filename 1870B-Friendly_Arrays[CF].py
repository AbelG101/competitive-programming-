num_test_cases = int(input())

for _ in range(num_test_cases):
    size_a, size_b = list(map(int, input().split()))
    array_a = list(map(int, input().split()))
    array_b = list(map(int, input().split()))

    # Calculate the bitwise OR of elements in array_b
    b_or_result = 0
    for b_element in array_b:
        b_or_result |= b_element

    # Initialize variables to store XOR results
    min_xor_result, max_xor_result = 0, 0

    # Iterate through array_a to calculate XOR results
    for a_element in array_a:
        # Calculate XOR result with original array_a
        min_xor_result ^= a_element
        # Calculate XOR result with modified array_a after OR operations with array_b
        max_xor_result ^= (a_element | b_or_result)

    # Determine and print minimum and maximum possible XOR results
    if size_a % 2 == 0:
        print(max_xor_result, min_xor_result)
    else:
        print(min_xor_result, max_xor_result)
