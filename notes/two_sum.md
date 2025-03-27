# Two Sum (LeetCode #1)
**Problem Link:**   https://leetcode.com/problems/two-sum/
**Date Completed:** 3/26/25

## Problem Statement
Given an array of integers ‘nums’ and an integer target, return indices of the two numbers such that they add up to ‘target’. You may assume that each input would have exactly one solution, and you may not use the same element twice.

## Thought Process
	1	Use a hashmap to store previously seen numbers with their corresponding index
	2	Iterate through ‘nums’ to check for ‘target  - number’ (where ‘number’ is the current number as you are iterating through) 
	3	If ‘target - number’ is found in the hashmap, we can return the index of that number and the index of the current number
	4	If ‘target - number’ is not found, add that number and its index to the hashmap and loop back through until it is found

## Time Complexity
O(n) because you are looping through ‘nums’ and worst case would be checking every single number in ‘nums’ once

## Space Complexity
O(n) because we are creating a dictionary and potentially storing up to n values in that dictionary


## Challenges
At first, I tried a brute force approach with nested for loops, but this has a time complexity of O(n^2), so I tried to come up with a more efficient solution. I looked at a few hints and found that using a hashmap was more efficient When I first implemented a hashmap into my solution, I used a counter variable, which worked just fine. Later, though, I learned about ‘enumerate()’ , which would make my code cleaner and easier to read.
