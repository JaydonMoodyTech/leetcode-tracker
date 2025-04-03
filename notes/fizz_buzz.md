# Fizz Buzz (LeetCode #412)
**Problem Link:**  https://leetcode.com/problems/fizz-buzz/
**Date Completed:** 3/14/25

## Problem Statement
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.


## Thought Process
	1	Create an empty list to append each string because that is what must be returned 
	2	Loop through every number from 1 to ‘n’ using range(1 , n + 1) because we don’t want to include 0 in our list and range is exclusive, hence the ‘n + 1’
	3	Use if/else statements to check whether the current number ‘i’ is divisible by 3, 5, both, or none, and append the corresponding strings to the list (all elements of the list must be strings, so make sure to use str(i))

## Time Complexity
O(n) because we are looping through ‘n’ numbers

## Space Complexity
O(n) because we are creating a new list and appending ‘n’ elements to that list

## Challenges
This problem wasn’t very challenging due to the easy usage of if/else statements. The only real challenge I faced was forgetting to convert integer ‘i’ to a string, but that took me maybe 30 seconds to realize and fix. 
