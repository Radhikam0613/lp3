def fractional_knapsack(values, weights, capacity): #tc = O(n log n), sc = O(n)
# Sort items by value-to-weight ratio in (reverse=True)descending order
      items = sorted(  
            range(len(values)),
            key=lambda i: values[i] / weights[i],
            reverse=True)
      total = 0
      print("\nItem\tValue\tWeight\tRatio\tFraction Taken")
      # Iterate through the sorted items and take as much of each item as possible
      for i in items:
            # If the knapsack is full, break out of the loop
            if capacity == 0: # tc = O(n), sc = O(1)
                  break
            # Take the minimum of the item's weight and the remaining capacity of the knapsack
            take = min(weights[i], capacity)
            fraction = take / weights[i]
            total += fraction * values[i]
            capacity -= take
      print(i + 1, "\t", values[i], "\t", weights[i],"\t", round(values[i] / weights[i], 2),"\t", round(fraction, 4))
      return total
n = int(input("Enter number of items: "))
values = []
weights = []
for i in range(n):
      #str(i + 1) converts the result of i + 1 into a string (text) 
      # so that it can be concatenated with the rest of the string in the input prompt.
      values.append(float(input("Enter value of item " + str(i + 1) + ": ")))
      weights.append(float(input("Enter weight of item " + str(i + 1) + ": ")))
capacity = float(input("Enter knapsack capacity: "))
print("Maximum value obtained:", fractional_knapsack(values, weights, capacity))