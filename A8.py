import time
from queue import PriorityQueue

# -------------------------------
# BRUTE FORCE
# -------------------------------
def knapsack_bruteforce(W, wt, val, n):
    if n == 0 or W == 0:
        return 0
    if wt[n-1] > W:
        return knapsack_bruteforce(W, wt, val, n-1)
    return max(
        val[n-1] + knapsack_bruteforce(W - wt[n-1], wt, val, n-1),
        knapsack_bruteforce(W, wt, val, n-1)
    )

# DYNAMIC PROGRAMMING

def knapsack_dp(W, wt, val, n):
    dp = [[0]*(W+1) for _ in range(n+1)]

    for i in range(n+1):
        for w in range(W+1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif wt[i-1] <= w:
                dp[i][w] = max(val[i-1] + dp[i-1][w-wt[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][W]

# -------------------------------
# BRANCH AND BOUND
# -------------------------------
class Node:
    def __init__(self, level, profit, weight, bound):
        self.level = level
        self.profit = profit
        self.weight = weight
        self.bound = bound

    def __lt__(self, other):
        return self.bound > other.bound  # Max heap behavior

def bound(node, n, W, wt, val):
    if node.weight >= W:
        return 0

    profit_bound = node.profit
    j = node.level + 1
    total_weight = node.weight

    while j < n and total_weight + wt[j] <= W:
        total_weight += wt[j]
        profit_bound += val[j]
        j += 1

    if j < n:
        profit_bound += (W - total_weight) * val[j] / wt[j]

    return profit_bound

def knapsack_bnb(W, wt, val, n):
    pq = PriorityQueue()

    u = Node(-1, 0, 0, 0)
    max_profit = 0

    u.bound = bound(u, n, W, wt, val)
    pq.put(u)

    while not pq.empty():
        u = pq.get()

        if u.bound <= max_profit:
            continue

        level = u.level + 1
        if level >= n:
            continue

        # Include item
        weight = u.weight + wt[level]
        profit = u.profit + val[level]

        if weight <= W and profit > max_profit:
            max_profit = profit

        new_node = Node(level, profit, weight, 0)
        new_node.bound = bound(new_node, n, W, wt, val)

        if new_node.bound > max_profit:
            pq.put(new_node)

        # Exclude item
        new_node = Node(level, u.profit, u.weight, 0)
        new_node.bound = bound(new_node, n, W, wt, val)

        if new_node.bound > max_profit:
            pq.put(new_node)

    return max_profit

n = int(input("Enter number of items: "))

wt = []
val = []

print("\nEnter weights:")
for i in range(n):
    wt.append(int(input(f"Weight {i+1}: ")))

print("\nEnter values:")
for i in range(n):
    val.append(int(input(f"Value {i+1}: ")))

W = int(input("\nEnter knapsack capacity: "))

# -------------------------------
# EXECUTION & TIMING
# -------------------------------
# Brute Force
start = time.time()
res1 = knapsack_bruteforce(W, wt, val, n)
end = time.time()
time_bf = end - start

# Dynamic Programming
start = time.time()
res2 = knapsack_dp(W, wt, val, n)
end = time.time()
time_dp = end - start

# Branch and Bound
start = time.time()
res3 = knapsack_bnb(W, wt, val, n)
end = time.time()
time_bnb = end - start


print("\n" + "="*70)
print("{:<25} {:<10} {:<15} {:<15}".format("Algorithm", "Result", "Time (sec)", "Space Complexity"))
print("="*70)

print("{:<25} {:<10} {:<15.6f} {:<15}".format(
    "Brute Force", res1, time_bf, "O(n)"
))

print("{:<25} {:<10} {:<15.6f} {:<15}".format(
    "Dynamic Programming", res2, time_dp, "O(nW)"
))

print("{:<25} {:<10} {:<15.6f} {:<15}".format(
    "Branch & Bound", res3, time_bnb, "O(n)"
))

print("="*70)