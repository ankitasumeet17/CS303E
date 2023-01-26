
#  File: Boxes.py

#  Description: --

#  Student Name: Ankita Sumeet 

#  Student UT EID: as96977

#  Partner Name: Jingwen (Ivy) Lou

#  Partner UT EID: -- 

#  Course Name: CS 313E

#  Unique Number: A11

#  Date Created: 10/14/21

#  Date Last Modified: 10/15/21

import sys

"""# Input: 2-D list of boxes. Each box of three dimensions is sorted
#        box_list is sorted
# Output: function returns two numbers, the maximum number of boxes
#         that fit inside each other and the number of such nesting
#         sets of boxes
def nesting_boxes (box_list):
  ...
"""
# stores subsets of box in box_subsets
# stores sorted boxes in box_list 
# stores current subset of boxes in sub_set
# indexes box_list using idx
# box_subsets is a 3-D list that has all the subset of boxes
def sub_sets_boxes (box_list, sub_set, idx, box_subsets):
  hi = len(box_list)
  if (idx == hi):
    box_subsets.append(sorted(sub_set))
    return
  else:
    sub_copy = sub_set[:]
    sub_set.append(box_list[idx])
    sub_sets_boxes(box_list, sub_set, idx + 1, box_subsets)
    sub_sets_boxes(box_list, sub_copy, idx + 1, box_subsets)

# stores largest subsets that nest in the 3-D list nesting_boxes
def largest_nesting_subsets (box_subsets, largest_size, nesting_boxes):
  if len(nesting_boxes) != 0:
    return
  else:
    i = 0
    while(len(box_subsets[i]) == largest_size):
      if check_boxes(box_subsets[i]):
        nesting_boxes.append(box_subsets[i])
      i += 1
    return largest_nesting_subsets(box_subsets[i:], largest_size - 1, nesting_boxes)

# returns boolean t/f if all boxes in the subset fits
def check_boxes(sub):
  box = 0
  while box + 1 < len(sub):
    if does_fit(sub[box], sub[box +1]):
      box += 1
    else:
      return False
  return True

# returns True if box1 fits inside box2
def does_fit (box1, box2):
  return (box1[0] < box2[0] and box1[1] < box2[1] and box1[2] < box2[2])

def main():
  # read the number of boxes 
  line = sys.stdin.readline()
  line = line.strip()
  num_boxes = int (line)

  # create an empty list for the boxes
  box_list = []

  # read the boxes from the file
  for i in range (num_boxes):
    line = sys.stdin.readline()
    line = line.strip()
    box = line.split()
    for j in range (len(box)):
      box[j] = int (box[j])
    box.sort()
    box_list.append (box)

  # print to make sure that the input was read in correctly

  # sort the box list
  box_list.sort()

  # print the box_list to see if it has been sorted.
  
  # create an empty list to hold all subset of boxes
  box_subsets = []

  # create a list to hold a single subset of boxes
  sub_set = []

  # generate all subsets of boxes and store them in box_subsets
  sub_sets_boxes (box_list, sub_set, 0, box_subsets)

  #sorts subsets by length of subset in reverse
  # i.e gives largest subsets at the front of the list till smallest subsets
  box_subsets.sort(key = lambda x: len(x), reverse = True)

  # initialize the size of the largest sub-set of nesting boxes
  largest_size = len(box_list)

  # create a list to hold the largest subsets of nesting boxes
  nesting_boxes = []

  # go through all the subset of boxes and only store the
  # largest subsets that nest in nesting_boxes
  largest_nesting_subsets (box_subsets, largest_size, nesting_boxes)

  # print the largest number of boxes that fit
  print(len(nesting_boxes[0]))

  # print the number of sets of such boxes
  print(len(nesting_boxes))

if __name__ == "__main__":
  main()

