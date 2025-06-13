[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/XeMTL_Yx)
# 🐍 Python Assignment: Loops, Ranges, and String Manipulation

#### ✨ Instructions:

Complete each of the tasks below. Each question is meant to help you practice working with `for`/`while` loops, the `range()` function, and controlling flow with `continue` and `break`, along with string operations like slicing and modification.

---

### 🚀 Task 1: Looping with `range()`

**Print all numbers from 1 to 20** (inclusive) using a `for` loop and the `range()` function.

**Bonus:** Print only even numbers.


---

### 🧪 Task 2: Skipping Items with `continue`

Loop through the numbers 1 to 10.
**Skip** (do not print) the number 5 using `continue`.


---

### ⛔ Task 3: Exiting a Loop with `break`

Loop through the numbers 1 to 10.
**Stop** the loop when the number 7 is reached using `break`.

---

### 🔄 **Task 4: Capitalize Every Other Letter**

Write a loop that takes a string and **capitalizes every other letter**, starting with the first.

**Example:**
Input: `"hello world"`
Output: `"HeLlO WoRlD"`


---

### 🔡 Task 5: Vowel Remover

Given a string, use a loop to remove all vowels (`a`, `e`, `i`, `o`, `u`) and print the result.

**Example:** `"hello world"` → `"hll wrld"`

---

### ✂️ Task 6: Stop at Special Character

Given a string, stop reading characters as soon as you hit a `!`.
Use a loop and `break`.

**Example:** `"hello! world"` → `"hello"`

---

Sure! Here's the updated **Bonus Challenge** — now a **Guessing Game** using loops and `break`:

---

### 🎯 **Bonus Challenge: Number Guessing Game**

Write a program that:

* Chooses a secret number between 1 and 10 (you can set it manually for now, e.g., `secret = 7`)
* Asks the user to guess the number in a loop
* Tells the user if they guessed wrong
* Ends the loop when the correct number is guessed (use `break`)
* After a correct guess, prints `"You got it!"`

```python
secret = 7  # You can change this or later use random.randint
while True:
    guess = int(input("Guess the number (1–10): "))
    
    # Your code here
```

---

use `random.randint()` to generate secret number
