# Plus One (LeetCode #66)*
**Problem Link:** https://leetcode.com/problems/plus-one
**Date Completed:** 4/2/25

## Problem Statement
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

## Thought Process
	1	Loop through each number in digits and concatenate that to an empty string variable to maintain the order of the numbers
	2	Add one to that number by converting that string variable to an integer and adding 1
	3	Convert it back to a string so we can loop through every character in that string
	4	Append each character (as an int) to a new list and return that list

## Time Complexity
O(n) because we are looping through every number in digits and every character in our empty string variable (not nested)

## Space Complexity
O(n) because we are creating a variable and appending every element in digits to that variable, then we create a new list to append each character in that variable

## Challenges
This problem was actually pretty easy and only took me 5 minutes to code. My solution has a pretty efficient runtime but I am going to try and optimize my code later for a more efficient space complexity. The one mistake I did run into was not converting the characters in the string to an int before appending it to the list
