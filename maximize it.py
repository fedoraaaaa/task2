import itertools

def maximize_it():
    # Read input
    K, M = map(int, input().split())
    lists = []
    for _ in range(K):
        parts = list(map(int, input().split()))
        Ni = parts[0]
        elements = parts[1:]
        lists.append(elements)
    
    max_s = 0
    # Generate all possible combinations of elements from each list
    for combination in itertools.product(*lists):
        current_sum = sum(x*x for x in combination) % M
        if current_sum > max_s:
            max_s = current_sum
            # Early exit if maximum possible is found
            if max_s == M - 1:
                break
    print(max_s)

maximize_it()