def knapsack(values, weights, capacity):# tc = O(n * capacity), sc = O(n * capacity)
      n = len(values)
      dp = [[0] * (capacity + 1) for _ in range(n + 1)]
      for i in range(1, n + 1):
            for w in range(1, capacity + 1):
                  if weights[i - 1] <= w:
                        dp[i][w] = max(
                              values[i - 1] + dp[i - 1][w - weights[i - 1]],
                              dp[i - 1][w]
                        )
                  else:
                        dp[i][w] = dp[i - 1][w]
      selected, w = [], capacity
      for i in range(n, 0, -1):
            if dp[i][w] != dp[i - 1][w]:
                  selected.append(i - 1)
            w -= weights[i - 1]
      selected.reverse()
      print("\nSelected Items:")
      print("Item\tWeight\tValue")
      for i in selected:
            print(i + 1, "\t", weights[i], "\t", values[i])
      print("Maximum Value:", dp[n][capacity])
n = int(input("Enter number of items: "))
values , weights = [], []
for i in range(n):
      print("\nItem", i + 1)
      values.append(int(input("Enter value: ")))
      weights.append(int(input("Enter weight: ")))
capacity = int(input("\nEnter knapsack capacity: "))
knapsack(values, weights, capacity)


# def knapsack(values, weights, capacity):# tc = O(n * capacity), sc = O(n * capacity)
#       n = len(values)
#       # Initialize a 2D array to store the maximum value that can be obtained for each 
#       subproblem. The array has for _ in range(n + 1) rows (for each item) and 
#       # [0] * (capacity + 1) columns (for each weight from 0 to capacity).
      # We need four rows, representing: for n = 3 items
      # - Row 0: using zero items
      # - Row 1: using the first item
      # - Row 2: using the first two items
      # - Row 3: using all three items
      # The underscore _ is a variable name 
      # conventionally used when we do not need the loop variable itself.
#       dp = [[0] * (capacity + 1) for _ in range(n + 1)]

#       # Fill the dp array using a bottom-up approach
#       i selects how many items are available.
#       range not form 0 as row and col 00 will be 0 as base case
#       for i in range(1, n + 1):
#             # For each item, we iterate through all possible weights from 1 to capacity
#             w selects the current weight capacity.
#             for w in range(1, capacity + 1):
#                   # If the weight of the current item is less than or equal to the current weight w,
#                   # we have two options: either include the item in the knapsack or exclude it.
#                  i - 1 to accesss zero indexing  and w for curr capacity 
#                 if weights[i - 1] <= w:
#                         # We take the maximum of the two options: including the item (which adds 
#                         # its value to the maximum value obtainable with the remaining weight) 
#                         # or excluding it (which keeps the maximum value obtainable with the same weight).
#                         # dp[i - 1][w - weights[i - 1]] What is the maximum value we can 
#                         # obtain from the previous items with capacity 2?                        
#                           dp[i][w] = max(
#                               values[i - 1] + dp[i - 1][w - weights[i - 1]],
#                               dp[i - 1][w]
#                         )
#                   else:
#                         # If the weight of the current item is greater than the current weight w,
#                         # we cannot include it in the knapsack, so we simply carry forward the 
#                         # maximum value obtainable with the same weight from the previous item.
#                         dp[i][w] = dp[i - 1][w]

#       selected = []
#       w = capacity

#       # range(n, 0, -1) iterates from n down to 1 (inclusive), 
#       # which allows us to backtrack through the dp array to find 
#       # which items were included in the optimal solution.
#       for i in range(n, 0, -1):
#             # If the value in the dp array for the current item and weight is 
#             # different from the value for the previous item and the same weight,
#             # it means that the current item was included in the optimal solution,
#             # so we add it
#             if dp[i][w] != dp[i - 1][w]:
#                   selected.append(i - 1)
#             # We subtract the weight of the included item from the remaining capacity
#             w -= weights[i - 1]

#       # The selected items are reversed to maintain the original order of the 
#       # items as they were added to the knapsack.
#       selected.reverse()

#       print("\nSelected Items:")
#       print("Item\tWeight\tValue\tFraction Taken")

#       total_weight = 0
#       for i in selected:
#             print(i + 1, "\t", weights[i], "\t", values[i], "\t", 1.0)
#             # The total weight of the selected items is calculated by summing the 
#             # weights of the selected items.
#             total_weight += weights[i]

#       print("\nTotal Weight:", total_weight)
#       print("Maximum Value:", dp[n][capacity])
      
# n = int(input("Enter number of items: "))
# values = []
# weights = []
# for i in range(n):
#       print("\nItem", i + 1)
#       values.append(int(input("Enter value: ")))
#       weights.append(int(input("Enter weight: ")))
# capacity = int(input("\nEnter knapsack capacity: "))
# knapsack(values, weights, capacity)