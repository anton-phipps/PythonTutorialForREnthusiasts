# Lesson 18: Collaboration & Best Practices

## Overview
Git is the foundation for collaborative research. While you can use it alone, its true power shines when working with a team on platforms like GitHub, GitLab, or Azure DevOps.

## 1. Remotes: Connecting to the Cloud
A "remote" is a version of your project hosted on the internet or a network.

*   `git clone <url>`: Download an existing repository.
*   `git remote add origin <url>`: Connect your local repo to a new online repo.
*   `git push origin <branch>`: Send your local commits to the remote.
*   `git pull origin <branch>`: Fetch changes from the remote and merge them into your local work.

## 2. The Pull Request (PR) Workflow
In professional data science teams, you don't merge your own code directly into `main`. Instead, you use a **Pull Request**.

1.  **Branch:** Create a branch for your specific task.
2.  **Push:** Push your branch to the remote (GitHub).
3.  **Open PR:** On GitHub, you open a request to merge your branch into `main`.
4.  **Review:** Teammates review your code, suggest changes, and ensure the analysis is sound.
5.  **Merge:** Once approved, the PR is merged.

## 3. Best Practices for Analysts

### Atomic Commits
A commit should do **one thing**. Don't fix a bug, update a plot, and change the README in one commit. If you make a mistake, it's much easier to revert one small change than one giant one.

### Descriptive Messages
*   **Bad:** `updates`, `fix`, `work`
*   **Good:** `Update cleaning script to handle missing dates`, `Refactor scatter plot to use Plotnine`, `Add documentation for API endpoints`

### Keep `main` Stable
Always treat your `main` branch as "production-ready." If someone clones your repo and runs `main`, it should work without errors. Do all your "messy" work on branches.

### The `.gitignore` is Sacred
Never commit:
*   Credentials (API keys, passwords).
*   Large datasets (use a data lake or SQL database instead).
*   Temporary files or local environment settings.

---

## 🏆 Challenge Exercise: The Team Simulation
Since you might be working alone right now, simulate a collaboration:
1.  Create a branch `readme-update`.
2.  Update the `README.md` (or create a dummy one) with a "Contributors" section.
3.  Commit and imagine you are pushing this for review.
4.  Switch to `main` and make a *different* change to the same file (to simulate a teammate's work).
5.  Try to merge `readme-update` into `main`.
6.  Resolve the resulting conflict and commit.

---
[⬅️ Previous](02_branching_merging.md) | [🏠 Table of Contents](../../README.md) | [Next ➡️](04_advanced_git.md)
