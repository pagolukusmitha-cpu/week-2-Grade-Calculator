# week-2-Grade-Calculator
# Student Grade Calculator

## Project Description

The Student Grade Calculator is a Python application that allows users to enter marks for multiple students, calculate their average marks, assign grades, provide personalized comments, and display class statistics. It also supports searching for students and saving results to a file.

---

## Features

- Process multiple students
- Input validation using while loops
- Error handling using try-except
- Grade calculation using if/elif/else
- Personalized comments
- Store data using lists and dictionaries
- Search for a student by name
- Save results to a text file
- Display class statistics
- Color-coded grades in the terminal
- Menu-driven interface

---

## Technologies Used

- Python 3
- Functions
- Lists
- Dictionaries
- Loops
- Conditional Statements
- Exception Handling
- File Handling

---

## Grading System

| Average Marks | Grade | Comment |
|--------------|-------|---------------------------------------|
| 90–100 | A | Excellent! Keep up the great work! |
| 80–89 | B | Very Good! You're doing well. |
| 70–79 | C | Good. Room for improvement. |
| 60–69 | D | Needs Improvement. Study harder. |
| 0–59 | F | Failed. Please seek help from teacher. |

---

## Project Structure

```
week2-grade-calculator/
│
├── grade_calculator.py
├── test_students.txt
├── results_sample.txt
├── README.md
└── .gitignore
```

---

## How to Run

1. Open a terminal.
2. Navigate to the project folder.

```bash
cd week2-grade-calculator
```

3. Run the program.

```bash
python grade_calculator.py
```

4. To test using sample input:

```bash
python grade_calculator.py < test_students.txt
```

---

## Sample Output

```
============================================================
      STUDENT GRADE CALCULATOR
============================================================

Enter number of students: 2

===== Student 1 =====
Student Name: John Smith
Math: 85
Science: 92
English: 88

===== Student 2 =====
Student Name: Sarah Johnson
Math: 78
Science: 81
English: 85

RESULTS SUMMARY

John Smith      88.3   B   Very Good! You're doing well.
Sarah Johnson   81.3   B   Very Good! You're doing well.

CLASS STATISTICS

Total Students : 2
Class Average  : 84.8
Highest Average: 88.3 (John Smith)
Lowest Average : 81.3 (Sarah Johnson)
```

---

## What I Learned

- Using functions to organize code
- Using if/elif/else statements
- Working with lists and dictionaries
- Using for and while loops
- Handling invalid input using try-except
- Reading and writing text files
- Formatting output using Python string formatting

---

## Screenshots
sample input: input.png

sample output: sample_output.png

## Challenges Faced

### Challenge
Handling invalid user input.

### Solution
Used while loops with try-except blocks to repeatedly ask for valid input.

### Challenge
Formatting the results table.

### Solution
Used formatted strings with alignment specifiers for neat output.

### Challenge
Calculating class statistics.

### Solution
Used Python built-in functions like `sum()`, `max()`, `min()`, and list comprehensions.

---

## Author

**Kusmitha**
