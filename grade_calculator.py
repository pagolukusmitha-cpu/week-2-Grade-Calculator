# ==========================================================
# Student Grade Calculator
# Week 2 Project - Control Flow & Data Structures
# Author: Kusmitha
# Description: A comprehensive grade calculator that processes multiple students' marks, calculates grades with personalized comments, and provides class statistics.
# ==========================================================

# ANSI Colors
GREEN = "\033[92m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"


# -----------------------------
# Grade Function
# -----------------------------
def calculate_grade(avg):
    if avg >= 90:
        return "A", "Excellent! Keep up the great work!"
    elif avg >= 80:
        return "B", "Very Good! You're doing well."
    elif avg >= 70:
        return "C", "Good. Room for improvement."
    elif avg >= 60:
        return "D", "Needs Improvement. Study harder."
    else:
        return "F", "Failed. Please seek help from teacher."


# -----------------------------
# Grade Color
# -----------------------------
def grade_color(grade):
    if grade == "A":
        return GREEN
    elif grade == "B":
        return BLUE
    elif grade == "C":
        return YELLOW
    else:
        return RED


# -----------------------------
# Input Validation
# -----------------------------
def get_valid_mark(subject):
    while True:
        try:
            mark = float(input(f"{subject}: "))
            if 0 <= mark <= 100:
                return mark
            else:
                print("Marks must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Enter a number.")


# -----------------------------
# Number of Students
# -----------------------------
def get_student_count():
    while True:
        try:
            count = int(input("Enter number of students: "))
            if count > 0:
                return count
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input.")


# -----------------------------
# Collect Student Data
# -----------------------------
def collect_students():

    students = []

    count = get_student_count()

    for i in range(count):

        print(f"\n===== Student {i+1} =====")

        while True:
            name = input("Student Name: ").strip()
            if name:
                break
            print("Name cannot be empty.")

        math = get_valid_mark("Math")
        science = get_valid_mark("Science")
        english = get_valid_mark("English")

        average = (math + science + english) / 3

        grade, comment = calculate_grade(average)

        students.append({
            "name": name,
            "math": math,
            "science": science,
            "english": english,
            "average": average,
            "grade": grade,
            "comment": comment
        })

    return students


# -----------------------------
# Display Results
# -----------------------------
def display_results(students):

    print("\n")
    print("=" * 90)
    print("RESULTS SUMMARY")
    print("=" * 90)

    print(
        f"{'Name':20}"
        f"{'Math':>8}"
        f"{'Science':>10}"
        f"{'English':>10}"
        f"{'Average':>10}"
        f"{'Grade':>8}"
    )

    print("-" * 90)

    for s in students:

        color = grade_color(s["grade"])

        print(
            f"{s['name']:20}"
            f"{s['math']:8.1f}"
            f"{s['science']:10.1f}"
            f"{s['english']:10.1f}"
            f"{s['average']:10.1f}"
            f"{color}{s['grade']:>8}{RESET}"
        )

        print(f"Comment: {s['comment']}")
        print("-" * 90)


# -----------------------------
# Statistics
# -----------------------------
def statistics(students):

    averages = [s["average"] for s in students]

    class_avg = sum(averages) / len(averages)

    highest = max(students, key=lambda x: x["average"])
    lowest = min(students, key=lambda x: x["average"])

    print("\nCLASS STATISTICS")
    print("=" * 40)

    print(f"Total Students : {len(students)}")
    print(f"Class Average  : {class_avg:.2f}")
    print(f"Highest Score  : {highest['average']:.2f} ({highest['name']})")
    print(f"Lowest Score   : {lowest['average']:.2f} ({lowest['name']})")


# -----------------------------
# Search Student
# -----------------------------
def search_student(students):

    name = input("\nEnter student name to search: ").lower()

    found = False

    for s in students:

        if s["name"].lower() == name:

            print("\nStudent Found")
            print("-" * 30)
            print(f"Name    : {s['name']}")
            print(f"Average : {s['average']:.2f}")
            print(f"Grade   : {s['grade']}")
            print(f"Comment : {s['comment']}")

            found = True
            break

    if not found:
        print("Student not found.")


# -----------------------------
# Save Results
# -----------------------------
def save_results(students):

    filename = "results_sample.txt"

    with open(filename, "w") as file:

        file.write("STUDENT RESULTS\n")
        file.write("=" * 60 + "\n")

        for s in students:

            file.write(
                f"{s['name']} | "
                f"Average: {s['average']:.2f} | "
                f"Grade: {s['grade']} | "
                f"{s['comment']}\n"
            )

    print(f"\nResults saved to '{filename}'")


# -----------------------------
# Main Menu
# -----------------------------
def menu():

    students = []

    while True:

        print("\n")
        print("=" * 40)
        print(" STUDENT GRADE CALCULATOR ")
        print("=" * 40)

        print("1. Enter Student Data")
        print("2. Display Results")
        print("3. Show Statistics")
        print("4. Search Student")
        print("5. Save Results")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            students = collect_students()

        elif choice == "2":
            if students:
                display_results(students)
            else:
                print("No student data.")

        elif choice == "3":
            if students:
                statistics(students)
            else:
                print("No student data.")

        elif choice == "4":
            if students:
                search_student(students)
            else:
                print("No student data.")

        elif choice == "5":
            if students:
                save_results(students)
            else:
                print("No student data.")

        elif choice == "6":
            print("Thank you for using the Grade Calculator.")
            break

        else:
            print("Invalid choice.")


# -----------------------------
# Program Starts Here
# -----------------------------
if __name__ == "__main__":
    menu()