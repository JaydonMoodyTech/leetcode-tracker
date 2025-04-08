# Valid Palindrome (LeetCode 123)
**Problem Link:** https://leetcode.com/problems/valid-palindrome
**Date Completed:** 4/8/25

## Problem Statement
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

## Thought Process
	1	Loop through every element in s to check if the element is alphanumeric
	2	If the element is alphanumeric, then we convert that element to lowercase and add it to a new string
	3	Check if the new string is equal it itself reversed (string == string[::-1])

## Time Complexity
O(n) because we are using a loop to check every element in s 

## Space Complexity
O(n) because we are creating a new variable and potentially adding n elements

## Challenges
This was pretty straight forward and I didn’t really have many problems. The only thing I needed a refresher on was how to reverse a string by slicing.
