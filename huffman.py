import heapq 
from collections import Counter
text = input("Enter text: ")
freq = Counter(text)
heap = [[f, [[ch, ""]]] for ch, f in freq.items()] #tc = O(n), sc = O(n)
heapq.heapify(heap) # tc = O(n), sc = O(n)

if len(heap) == 1:
      ch = heap[0][1][0][0]
      print("Character\tFrequency\tHuffman Code")
      print(ch, "\t\t", freq[ch], "\t\t", 0)
else: # tc = O(n log n), sc = O(n)
      while len(heap) > 1: 
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)
            for item in left[1]:
                  item[1] = "0" + item[1]
            for item in right[1]:
                  item[1] = "1" + item[1]
            heapq.heappush(heap, [
            left[0] + right[0],
            left[1] + right[1]
                  ])
      print("Character\tFrequency\tHuffman Code")
      for ch, code in sorted(heap[0][1]):
            print(ch, "\t\t", freq[ch], "\t\t", code)


# #tc = O(n log n), sc = O(n) nlogn because we are using a heap data structure to build
# # the Huffman tree, and the time complexity of inserting and removing elements from a 
# # heap is O(log n). Since we are performing these operations for each character in the 
# # input text, the overall time complexity is O(n log n). The space complexity is O(n) 
# # because we are storing the frequency of each character in a dictionary and the Huffman 
# # codes in a list.
# #implements a min-heap, where the element with the smallest priority is removed first
# import heapq 
# # Counter counts how many times each character occurs in the input
# from collections import Counter

# text = input("Enter text: ")
# freq = Counter(text)
# # defining heap as a list of lists, where each inner list contains the 
# # frequency and a list of [character, code] pairs
# heap = [[f, [[ch, ""]]] for ch, f in freq.items()] #tc = O(n), sc = O(n)
# # Converts the list into a min-heap in linear time, in-place, in O(n) time complexity
# heapq.heapify(heap) # tc = O(n), sc = O(n)

# # If the heap has only one element, it means there is only one unique character
# # in the input text. In this case, we can directly assign a Huffman code of 0 to 
# # that character. 
# if len(heap) == 1:
#       ch = heap[0][1][0][0]
#       print("Character\tFrequency\tHuffman Code")
#       print(ch, "\t\t", freq[ch], "\t\t", 0)
# # Otherwise, we repeatedly pop the two elements with the smallest frequencies from 
# # the heap, combine them into a new node, and push it back into the heap 
# # until only one element remains. This final element contains the complete Huffman tree, 
# # from which we can extract the Huffman codes for each character.
# else: # tc = O(n log n), sc = O(n)
#       while len(heap) > 1: 
#             left = heapq.heappop(heap)
#             right = heapq.heappop(heap)
#             for item in left[1]:
#                   #item[0] is the character in the left node
#                   #item[1] is the code for the character in the left node, 
#                   # and we prepend "0" to it to indicate that it is on the left side of the tree.
#                   item[1] = "0" + item[1]
#             for item in right[1]:
#                   #item[0] is the character in the right node
#                   #item[1] is the code for the character in the right node, 
#                   # and we prepend "1" to it to indicate that it is on the right side of the tree.
#                   item[1] = "1" + item[1]
#             # The new node's frequency is the sum of the frequencies of the two nodes
#             # (left[0] is the frequency of the left node and left[1] is the list of 
#             # character-code pairs for the left node, and similarly for the right node). 
#             # and its character-code pairs are the concatenation of the character-code
#             # pairs from the two nodes.
#             heapq.heappush(heap, [
#             left[0] + right[0],
#             left[1] + right[1]
#                   ])

#       print("Character\tFrequency\tHuffman Code")
#       # sorted() sorts the character-code pairs alphabetically.
#       for ch, code in sorted(heap[0][1]):
#             print(ch, "\t\t", freq[ch], "\t\t", code)