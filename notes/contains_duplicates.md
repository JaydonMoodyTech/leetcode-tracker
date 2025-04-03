# Contains Duplicates (LeetCode #217)
**Problem Link:**  https://leetcode.com/problems/contains-duplicate
**Date Completed:** 3/27/25

## Problem Statement
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

## Thought Process
	1	Sort ‘nums’ because if there is a duplicate their indexes would be next to each other
	2	Loop through the length of ‘nums’ - 1 so we don’t get an index out of bounds error
	3	If the number at the current index is equal to the number at the next index (because we sorted ‘nums’), return ‘True’
	4	If there are no instances where the number at the current index is equal to the number at the next index, return ‘False’

## Time Complexity
O(n log n) because we are using Python’s built-in sort() function. While looping through the list list has O(n) time complexity, as the input size grows, sorting becomes the primary contributor to the overall runtime.

## Space Complexity
O(n) because Python’s sort() function creates temporary arrays in memory during the sorting process


## Challenges
At first, I looped through ‘nums’ and appended each number to a new list and checked if the current number had already been appended to ‘nums’ previously.  This works for smaller data sets, but one of the test cases had a million inputs and I encountered a runtime error. So, I came up with sorting ‘nums’ so that duplicates would be indexed next to each other and I could just loop through to see if the current number I was at, is the same as the next number in ‘nums’
