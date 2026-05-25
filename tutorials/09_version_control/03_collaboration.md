# Lesson 18: Collaboration & Best Practices

## Overview
Git is the foundation for collaborative research. While you can use it alone, its true power shines when working with a team on platforms like GitHub, GitLab, or Azure DevOps.

## 1. Remotes: Connecting to the Cloud
A "remote" is a version of your project hosted on the internet or a network.

### 💡 Visualizing the Sync
```text
      ANTON'S LAPTOP                     GITHUB (REMOTE)                 ASHMITA'S LAPTOP
   +------------------+                +------------------+            +------------------+
   |  Local Commits   | -- git push -> |  Shared History  | <- git pull|  Local Commits   |
   |                  | <- git pull -- |                  | -- git push|                  |
   +------------------+                +------------------+            +------------------+
```

### 💡 Real-World Scenario: Working Across Two Computers
**Anton** does his heavy data processing on a powerful workstation in the office for the **"Genomic Sequencing"** task, but he wants to tweak his plots on his laptop at home.

*   **Without Git:** Anton is emailing himself `.zip` files, or carrying a USB stick. He inevitably ends up with different versions of the code on each machine, causing a headache the next morning.
*   **With Git:** Anton `git push`es his changes from the workstation to GitHub before leaving the office. When he gets home, he simply `git pull`s on his laptop. Everything is perfectly in sync.

### 💡 Real-World Scenario: The "Rejected" Push
**Anton** finishes his code for "Genomic Sequencing" and tries to `git push`. But **Ashmita** just pushed her "Data Cleaning" fix five minutes ago. Git blocks Anton with a scary error: `[rejected] main -> main (fetch first)`.

*   **The Problem:** The remote (GitHub) has history that Anton doesn't have. Git won't let him push because he might accidentally overwrite Ashmita's work.
*   **The Solution:** Anton must `git pull` first. This brings Ashmita's changes into his local machine. If there are no conflicts, he can then `git push` successfully.

*   `git clone <url>`: Download an existing repository.
*   `git remote add origin <url>`: Connect your local repo to a new online repo.
*   `git push origin <branch>`: Send your local commits to the remote.
*   `git pull origin <branch>`: Fetch changes from the remote and merge them into your local work.

## 2. The Pull Request (PR) Workflow
In professional data science teams, you don't merge your own code directly into `main`. Instead, you use a **Pull Request**.

### 💡 Real-World Scenario: The Peer Review
**Anton** has finished a complex analysis for the pipeline task **"Historical Weather Patterns."** He's confident, but everyone makes mistakes. 

*   **The Workflow:** Anton opens a Pull Request (PR) on GitHub. **Ashmita** reviews his code. She notices that Anton used a slightly outdated population estimate in his denominator for a per-capita calculation. 
*   **The Benefit:** Because the team uses PRs, the error is caught by Ashmita *before* **Alex** sees the final report. Anton updates the code, Ashmita approves it, and the final analysis is robust.

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
