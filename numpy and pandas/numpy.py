import numpy as np

"""

#Lesson 1:

array = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
                  [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
                  [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', '_']]])

word = array[2, 0, 0] + array[0, 1, 1] + array[2, 1, 2] + array[2, 2, 0]

print(word) #PRINTS SEXY


#Lesson 2:

array = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]])

print(array[2:, 2:]) #PRINTS [[11 12]

"""