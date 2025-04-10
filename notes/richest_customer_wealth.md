# Richest Customer Wealth (LeetCode 1672)
**Problem Link:** https://leetcode.com/problems/richest-customer-wealth
**Date Completed:** 4/10/25

## Problem Statement
You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

## Thought Process
	1	Loop through accounts and append the sum of each list to a new one
	2	Return the max of the new list

## Time Complexity
O(m * n) because we are using the sum() function which uses O(n) time, but we are doing that m times where m is the number of customers (rows)

## Space Complexity
O(m) because we are creating a new list and appending one sum per customer 

## Challenges
This one was fairly easy and the only real problem I faced was that I tried to append accounts[i], which I quickly realized raises an error because i is a list and list indices can’t be lists.