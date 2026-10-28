# My AI Study Planner

A beginner-friendly Python project that creates a personalized weekly study plan for a student working toward an AI learning goal.

> **Important:** This is a simple rule-based planner. It does not use an AI model, AI API, database, GUI, or external Python package.

## Features

- Asks for the student's name.
- Asks for their AI learning goal.
- Asks how many days per week they can study.
- Asks how many hours they can study on each study day.
- Calculates total weekly study hours.
- Prints a personalized study plan.
- Saves the plan to `study_plan.txt`.
- Validates numeric inputs.

## Requirements

- Python 3.8 or newer recommended
- No external packages required

## How to run

1. Download or clone this project.
2. Open a terminal or command prompt in the project folder.
3. Run:

   ```bash
   python main.py
   ```

   On some systems, use `python3 main.py` instead.

4. Answer the questions. Your plan will be displayed and saved as `study_plan.txt` in the current folder.

## Example calculation

If you study 3 days per week for 2 hours per study day:

`3 days × 2 hours = 6 total study hours per week`

## Project files

- `main.py` — the Python program.
- `README.md` — project instructions.
- `study_plan.txt` — created automatically when the program runs.
- `.gitignore` — ignores Python cache files and the generated personal study plan.

## Publish on GitHub

1. Sign in to [GitHub](https://github.com/).
2. Create a new repository named `my-ai-study-planner`.
3. Keep it public if you want everyone to see it. You can skip adding a README on GitHub because this project already has one.
4. Download and extract this project, then open a terminal inside its folder.
5. Run these commands, replacing the placeholder with your repository URL:

   ```bash
   git init
   git add main.py README.md .gitignore
   git commit -m "Add My AI Study Planner"
   git branch -M main
   git remote add origin https://github.com/YOUR-USERNAME/my-ai-study-planner.git
   git push -u origin main
   ```

If Git asks you to authenticate, follow GitHub's sign-in instructions. Do not share your password or access token with anyone.

### Optional: run before publishing

Run `python main.py`, enter sample details, and check that the plan appears and `study_plan.txt` is created. The `.gitignore` keeps that generated file out of the initial Git commit so you do not accidentally publish personal study details.
