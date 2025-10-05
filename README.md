# Find Me, The Biggest is the Winner

A program that identifies the largest of five user-entered numbers and then computes its factorial.

## 📝 Description

This program prompts a user to enter five numbers one by one. After all numbers are entered, it first identifies and displays the largest number among them. Then, it proceeds to calculate the factorial of this largest number, but only if it is a non-negative integer.

The core mathematical principle is the factorial, where the total is the result of n! (n being the number of times "RUN" was printed).

## 🎯 Problem Statement

**Input:** 
- Five numbers, entered sequentially by the user.

**Output:** 
- Line 1: The largest number found from the five inputs.
- Line 2: The result of the factorial calculation for the largest number. If the largest number is negative, it should display "NoProceed".

**Rules:**
- The program must find the maximum value from the five inputs.
- The factorial is only calculated for non-negative numbers.
- If the largest number is negative, the program outputs a specific error message instead of a factorial result.

## 💡 Examples

### Example 1
```
Input:
1
2
3
4
5

Output:
5
120
```
Explanation: The largest number is 5, and 5! is 120.

### Example 2
```
Input:
3
1
1
2
1

Output:
3
6
```
Explanation: The largest number is 3, and 3! is 6.

### Example 3
```
Input:
-1
-2
-3
-4
-5

Output:
-1
NoProceed
```
Explanation: The largest number is -1. Since it's negative, the factorial cannot be calculated.

## 🚀 How to Use

1. Clone this repository
```bash
git clone https://github.com/adiaryaz/Biggest-Number-Factorial.git
cd calculate-circle-area
```

2. Run the program (assuming the file is main.py):
```bash
python main.py
```

3. Enter five numbers, pressing Enter after each one.
