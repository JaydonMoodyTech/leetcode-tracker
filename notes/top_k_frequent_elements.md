# Top K Frequent Elements (LeetCode 347)
**Problem Link:** https://leetcode.com/problems/top-k-frequent-elements
**Date Completed:** 4/4/25

## Problem Statement
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

## Thought Process
	1	Store each value and its number of occurrences in a hashmap
	2	Sort through the dictionary by using sorted() to create a list with each value in descending order based on the number of occurrences
	3	Loop through that list in range(len(list) - k) because that will leave us with the number of values we need to delete
	4	For every loop we delete the first element and we will be left with k most frequent elements

## Time Complexity
O(n log(n)) because sorting dominates time complexity and our sort is O(n log(n))

## Space Complexity
O(n) because we are creating a hashmap and adding potentially every element in nums, and creating a list with every element of that hashmap

## Challenges
This one was pretty challenging for me until I found that I could use a hashmap and how to use the sorted() method. I used outside resources, specifically w3schools because I find they have the best explanations and examples, to figure out this solution after spending around 30 minutes of trial and error.
