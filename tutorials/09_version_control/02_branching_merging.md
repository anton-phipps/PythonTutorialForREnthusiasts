# Lesson 17: Branching and Merging

## Overview
One of Git's most powerful features is **branching**. Branching allows you to step away from the "main" version of your code to try a new model, experiment with a different visualization, or fix a bug without affecting your stable analysis.

## 1. What is a Branch?
Think of a branch as a parallel universe. You can make changes in one universe without affecting the others. When you are happy with your changes, you can "merge" them back into the main universe.

### Key Commands
*   `git branch`: List available branches.
*   `git branch <name>`: Create a new branch.
*   `git checkout <name>` (or `git switch <name>`): Move to a branch.
*   `git checkout -b <name>`: Create and switch in one step.

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

Git will mark the file like this:
```python
<<<<<<< HEAD
print("Using Linear Regression")
=======
print("Using Bayesian Regression")
>>>>>>> experiment-bayesian-model
```

**To fix it:**
1.  Open the file and decide which version (or a mix) you want to keep.
2.  Remove the `<<<<<<<`, `=======`, and `>>>>>>>` markers.
3.  Save the file.
4.  `git add` the resolved file and `git commit` to finish the merge.

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
