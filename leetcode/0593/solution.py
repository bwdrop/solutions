#!/usr/bin/python3
"""
# Title
Valid Square

# URL
https://leetcode.com/problems/valid-square/

# Problem
Given the coordinates of four points in 2D space p1, p2, p3 and p4, return true if the four points construct a square.

The coordinate of a point pi is represented as [xi, yi]. The input is not given in any order.

A valid square has four equal sides with positive length and four equal angles (90-degree angles).

Example:
Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: true

# Solved by
Heliane Ly
November 2020

# Algorithm
To determine whether the set of points is a valid square,
we calculate the distance between every combination of points (6) and sort them.
If the two diagonals are the same length, and the four sides are as well, then we have a square.
"""
from math import sqrt

class Solution:
    def dist(self, p1: List[int], p2: List[int]) -> int:
        return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2
    
    def get_all_segments(self, points: List[List]) -> List[float]:
        segments = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                segments.append(self.dist(points[i], points[j]))
        return segments
    
    def all_equal(self, numbers: List[float]) -> bool:
        for i in range(len(numbers)):
            if i > 0 and numbers[i] != numbers[i - 1]:
                return False
        return True
    
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        segments = sorted(self.get_all_segments([p1, p2, p3, p4]))
        sides = segments[0:4]
        diagonals = segments[4:6]
        return sides[0] > 0 and self.all_equal(sides) and self.all_equal(diagonals)