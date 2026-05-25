# Lesson 19: Advanced Git & The Power User's Toolkit

## Overview
Once you master the basics of branching and merging, you'll eventually encounter scenarios where the standard workflow isn't enough. This lesson covers "Power User" features that help you manage messy history, debug complex issues, and understand how Git works under the hood.

## 1. Managing Temporary Work: `git stash`
Sometimes you're in the middle of a change but need to switch branches immediately (e.g., to fix a production bug). You don't want to commit "half-finished" code.

### 💡 Real-World Scenario: The Sudden Interruption
**Anton** is deep in the "zone," refactoring a messy data ingestion script for the **"API Integration"** task. He's changed 20 lines, and the code currently won't even run. Suddenly, **Alex** calls: "The production dashboard is down! We need you to check the `production` branch immediately."

*   **The Problem:** Anton can't commit his broken code, but Git won't let him switch branches with uncommitted changes that would be overwritten.
*   **The Solution:** Anton runs `git stash`. His changes are safely tucked away, and his working directory is clean. He switches to `production`, fixes the dashboard, then switches back and run `git stash pop`. His "half-finished" work is restored exactly as it was.

*   **`git stash`**: Takes your uncommitted changes and "hides" them in a temporary storage area.
*   **`git stash pop`**: Brings your changes back and removes them from the stash.
*   **`git stash list`**: Shows all your saved stashes.

## 2. Rewriting History: Rebase vs. Merge
While `git merge` combines branches by creating a "merge commit," `git rebase` takes your changes and "replays" them on top of another branch.

*   **Why Rebase?** It keeps a perfectly linear project history. Instead of having "spaghetti" lines in your history graph, it looks like a single straight line.
*   **The Golden Rule:** Never rebase branches that have been pushed to a shared repository. It changes the history of the branch, which can confuse your teammates.

### Amending the Last Commit
Made a typo in your last commit message or forgot to add a small file?
```bash
git commit --amend -m "Corrected message"
```

## 3. Undoing Changes: Reset, Revert, and Restore
Git provides several ways to "go back," depending on how much history you want to change.

| Command | What it does | Risk Level | When to use it |
| --- | --- | --- | --- |
| `git restore` | Discards uncommitted changes in a file. | Low | "I messed up my current edits and want to start over." |
| `git revert` | Creates a NEW commit that undoes a previous one. | Safe | "I pushed a bug to the team and need to fix it safely." |
| `git reset` | Moves the branch back in time, deleting history. | **DANGEROUS** | "I'm working alone and want to pretend those last 3 commits never happened." |

*   **`git checkout <file>` / `git restore <file>`**: Discards local changes to a file and brings it back to its state in the last commit.
*   **`git revert <commit_id>`**: Creates a *new* commit that does the exact opposite of a previous commit. This is the safest way to undo changes on shared branches.
*   **`git reset --hard <commit_id>`**: Forcefully moves the branch back to a specific point in time, deleting all work after that point. **Use with extreme caution.**

## 4. Debugging & Inspection Tools

### `git blame`: Who changed this?
If you find a confusing line of code, `git blame <filename>` shows you exactly who wrote every line and in which commit. It's not for "blaming" people; it's for finding the context and the original ticket/PR.

### `git bisect`: Finding the Needle in the Haystack
If a bug appeared but you don't know which of the last 50 commits caused it, `git bisect` uses binary search to find the culprit:

### 💡 Real-World Scenario: Finding the "Breaking" Change
**Anton** hasn't run the main analysis script for the **"Longitudinal Study"** in a week. Today, it fails with a strange `MemoryError`. He knows it worked fine last Monday, but he's made dozens of small commits since then.

*   **The Manual Way:** Anton could manually check out every 5th commit and try to run the script. That could take all afternoon.
*   **The `bisect` Way:** Anton tells Git "it worked at commit `ABC` and it's broken at commit `XYZ`." Git will automatically jump to the middle commit. Anton tests it. If it's "good," Git knows the bug is in the second half. If "bad," it's in the first half. He'll find the exact commit that introduced the bug in just a few steps!

1.  Tell Git a "good" commit (where the bug didn't exist).
2.  Tell Git a "bad" commit (the current one).
3.  Git will check out a commit in the middle. You test it and tell Git "good" or "bad."
4.  Git repeats until it finds the exact commit that introduced the bug.

### `git reflog`: The Ultimate Safety Net
If you accidentally delete a branch or perform a bad `reset`, Git keeps a log of every movement of the "HEAD" pointer for about 30 days. `git reflog` allows you to find the ID of a "lost" commit and recover it.

## 5. Picking Specific Changes: `git cherry-pick`
Imagine a teammate has a commit on their branch that fixes a bug you're experiencing, but you don't want to merge their *entire* branch. `git cherry-pick <commit_id>` lets you grab just that one specific commit and apply it to your current branch.

### 💡 Real-World Scenario: Borrowing a Fix
**Ashmita** is working on a massive new feature on the `ashmita-experimental` branch for the **"Neural Network Optimization"** task. While doing that, she found and fixed a bug in the shared `utils.py` file that is also causing **Anton** problems in his **"Data Prep"** task.

*   **The Problem:** Anton wants Ashmita's bug fix, but he definitely DON'T want all her experimental, half-finished neural network code.
*   **The Solution:** Anton finds the ID of Ashmita's specific bug-fix commit and run `git cherry-pick <commit_id>`. Now he has the fix, and none of the experiments.

## 6. Versioning for Reproducibility: `git tag`
For researchers like **Anton** and **Ashmita**, being able to say "this is the exact code used for the June 2024 Report" is vital for reproducibility.

*   **`git tag -a v1.0 -m "Final version for Lancet Submission"`**: Creates a permanent label for the current commit.
*   **`git push origin v1.0`**: Sends the tag to GitHub.

Even if you continue working and make 100 more commits, you can always jump back to `v1.0` to see exactly what you did for that specific report.

## 7. Git Internals: Content-Addressable Storage
Under the hood, Git is essentially a simple Key-Value database.
*   **Blobs:** Stores file content.
*   **Trees:** Stores directory structures (mapping filenames to Blobs).
*   **Commits:** Stores metadata (author, date, message) and a pointer to a Tree.
Everything is indexed by a **SHA-1 Hash**. If even one character in a file changes, its Hash changes, which is why Git is so good at ensuring data integrity.

---

## 🏆 Summary Checklist
To be truly competent in Git, you should be able to explain:
1.  The difference between **merging** (preserving history) and **rebasing** (linearizing history).
2.  How to use the **stash** to manage interruptions.
3.  When to use **revert** (safe) vs. **reset** (dangerous).
4.  How **bisect** can save hours of debugging time.
5.  What a **SHA-1 Hash** represents in the context of a commit.

---
[⬅️ Previous](03_collaboration.md) | [🏠 Table of Contents](../../README.md) | [Next ➡️](../10_sharing/01_quarto.md)
