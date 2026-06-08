# Lesson 17: Branching and Merging

## Overview
One of Git's most powerful features is **branching**. Branching allows you to step away from the "main" version of your code to try a new model, experiment with a different visualization, or fix a bug without affecting your stable analysis.

## 1. What is a Branch?
Think of a branch as a parallel universe. You can make changes in one universe without affecting the others. When you are happy with your changes, you can "merge" them back into the main universe.

### 💡 Real-World Scenario: The "What-If" Analysis
**Anton** has a working task **"Linear Model for Crop Yield"** in the pipeline. He reads about a fancy new Random Forest approach and wants to see if it performs better. 

*   **The Risk:** If Anton modifies his existing script and the new approach doesn't work, he's spent the whole afternoon breaking a working model that **Alex** is expecting to see tomorrow.
*   **The Solution:** Anton creates a branch called `experiment-random-forest`. He does all his work there. If it's a failure, he just deletes the branch and goes back to `main` like nothing happened. If it's a success, he shows it to Alex and merges it!

### 💡 Real-World Scenario: The Emergency Bug Fix
**Ashmita** is halfway through a three-day pipeline task **"Refactor Visualization Code."** Suddenly, **Alex** finds a critical error in the data cleaning script on the `main` branch that needs to be fixed *now* for a client meeting.

*   **The Problem:** Ashmita's current files are a mess of half-finished visualization code. She can't just fix the bug and commit everything together.
*   **The Solution:** 
    1.  Ashmita saves her visualization work on its own branch (e.g., `feature-new-plots`).
    2.  She switches back to `main`.
    3.  She creates a tiny branch called `fix-cleaning-bug`.
    4.  She fixes the bug, merges it into `main`, and pushes it.
    5.  She switches back to `feature-new-plots` and continues her work exactly where she left off.

### Key Commands
*   `git branch`: List available branches.
*   `git branch <name>`: Create a new branch.
*   `git checkout <name>` (or `git switch <name>`): Move to a branch.
*   `git checkout -b <name>`: Create and switch in one step.

### 💡 Pro-Tip: Branch Naming Conventions
In a team with **Alex**, **Ashmita**, and **Anton**, it's helpful to name branches so everyone knows who is working on what. A common pattern is `initials/task-description`:
*   `aa/census-cleaning` (Anton)
*   `as/neural-net-fix` (Ashmita)
*   `aj/lead-review` (Alex)

## 2. The Branching Workflow
Imagine you want to try a new Bayesian model but don't want to break your current linear regression script.

```bash
# 1. Create a new branch for the experiment
git checkout -b experiment-bayesian-model

# 2. Work on your files...
# (Edit model.py)

# 3. Commit your experimental changes
git add model.py
git commit -m "Draft Bayesian model implementation"

# 4. Switch back to the main branch to do other work
git checkout main
```

## 3. Merging
Once your experiment is successful, you want to bring those changes back into your `main` branch.

```bash
# 1. Make sure you are on the 'main' branch
git checkout main

# 2. Merge the experiment branch
git merge experiment-bayesian-model
```

## 4. Handling Merge Conflicts
Sometimes, you change the same line of code in two different branches. Git won't know which one to keep and will create a **merge conflict**.

### 💡 Real-World Scenario: The Conflict
**Anton** and **Ashmita** both edit the "Year" column processing in `clean.py`.
*   **Anton's branch:** `year = int(row[0])`
*   **Ashmita's branch:** `year = pd.to_numeric(row[0])`

When **Alex** tries to merge them, Git stops and says: "I don't know which one is right!"

Git will mark the file like this:
```text
<<<<<<< HEAD
year = int(row[0])  # Anton's version
=======
year = pd.to_numeric(row[0])  # Ashmita's version
>>>>>>> as/neural-net-fix
```

**How to Fix It (Step-by-Step):**
1.  **Don't Panic:** A conflict is not a "bug"; it's Git asking for a human decision.
2.  **Talk to the Team:** Anton and Ashmita should decide which line is better. (In this case, Ashmita's `pd.to_numeric` is safer for analysts).
3.  **Edit the File:** Delete the markers (`<<<<`, `====`, `>>>>`) and the line you don't want.
    *   *Corrected file:* `year = pd.to_numeric(row[0])`
4.  **Save and Stage:** Run `git add clean.py`.
5.  **Finish the Merge:** Run `git commit`. Git will automatically suggest a "Merge branch..." message. Save and exit.

---

## 🏆 Challenge Exercise: Branching Out
1.  In your repo from Lesson 16, create a new branch called `feature-greeting`.
2.  Switch to that branch.
3.  Add a new file `greet.py` that asks for a user's name and prints it.
4.  Commit the new file.
5.  Switch back to `main`. Is `greet.py` still there? (It shouldn't be!)
6.  Merge `feature-greeting` into `main`.
7.  Verify that `greet.py` is now available on the `main` branch.

---
[⬅️ Previous](01_git_basics.md) | [🏠 Table of Contents](../../README.md) | [Next ➡️](03_collaboration.md)
