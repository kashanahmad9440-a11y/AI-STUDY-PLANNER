"""
My AI Study Planner
A beginner-friendly study planner built with basic Python only.
Note: The "AI" in the project name describes the learning goal; this
program does not connect to an AI service or use an AI API.
"""

from datetime import datetime


def ask_student_details():
    """Ask for the student's details and validate numeric answers."""
    name = input("What is your name? ").strip()
    while not name:
        name = input("Please enter your name: ").strip()

    goal = input("What is your AI learning goal? ").strip()
    while not goal:
        goal = input("Please describe your AI learning goal: ").strip()

    while True:
        try:
            study_days = int(input("How many days per week can you study (1-7)? "))
            if 1 <= study_days <= 7:
                break
            print("Please enter a number from 1 to 7.")
        except ValueError:
            print("Please enter a whole number, such as 3.")

    while True:
        try:
            daily_hours = float(input("How many hours can you study each study day? "))
            if 0 < daily_hours <= 24:
                break
            print("Please enter a number greater than 0 and no more than 24.")
        except ValueError:
            print("Please enter a number, such as 1 or 1.5.")

    return name, goal, study_days, daily_hours


def build_study_plan(name, goal, study_days, daily_hours):
    """Create a personalized plan as a string."""
    weekly_hours = study_days * daily_hours
    hours_text = f"{weekly_hours:g}"

    plan_lines = [
        "=" * 48,
        "MY AI STUDY PLAN",
        "=" * 48,
        f"Student name: {name}",
        f"AI learning goal: {goal}",
        f"Study days per week: {study_days}",
        f"Study hours per study day: {daily_hours:g}",
        f"Total weekly study hours: {hours_text}",
        "",
        "PERSONALIZED WEEKLY PLAN",
        "-" * 48,
        "Use this simple routine on each of your study days:",
        "1. Review your previous notes (10% of your session).",
        "2. Learn one new concept or follow a tutorial (40%).",
        "3. Practise with a small exercise or coding task (40%).",
        "4. Write down what you learned and what to review (10%).",
        "",
        f"Your focus: make steady progress toward '{goal}'.",
        "Beginner tip: split big goals into small weekly milestones.",
        "",
        "SUGGESTED STUDY DAYS",
    ]

    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday",
                "Friday", "Saturday", "Sunday"]
    for day in weekdays[:study_days]:
        plan_lines.append(f"- {day}: {daily_hours:g} hour(s) — learn, practise, and review.")

    plan_lines.extend([
        "",
        "WEEKLY CHECK-IN",
        "- What did I learn this week?",
        "- What was difficult?",
        "- What will I practise next week?",
        "",
        f"Created on: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        "This planner uses basic Python. It does not call an AI API.",
        "=" * 48,
    ])
    return "\n".join(plan_lines), weekly_hours


def main():
    print("\nWelcome to My AI Study Planner!\n")
    name, goal, study_days, daily_hours = ask_student_details()
    plan, weekly_hours = build_study_plan(name, goal, study_days, daily_hours)

    print("\n" + plan)
    try:
        with open("study_plan.txt", "w", encoding="utf-8") as file:
            file.write(plan)
        print("\nYour study plan has been saved to study_plan.txt")
    except OSError as error:
        print(f"\nCould not save the plan: {error}")


if __name__ == "__main__":
    main()
