# Lesson 19: Advanced Git & The Power User's Toolkit

## Overview
Once you master the basics of branching and merging, you'll eventually encounter scenarios where the standard workflow isn't enough. This lesson covers "Power User" features that help you manage messy history, debug complex issues, and understand how Git works under the hood.

## 1. Managing Temporary Work: `git stash`
Sometimes you're in the middle of a change but need to switch branches immediately (e.g., to fix a production bug). You don't want to commit "half-finished" code.

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

*   **`git checkout <file>` / `git restore <file>`**: Discards local changes to a file and brings it back to its state in the last commit.
*   **`git revert <commit_id>`**: Creates a *new* commit that does the exact opposite of a previous commit. This is the safest way to undo changes on shared branches.
*   **`git reset --hard <commit_id>`**: Forcefully moves the branch back to a specific point in time, deleting all work after that point. **Use with extreme caution.**

## 4. Debugging & Inspection Tools

### `git blame`: Who changed this?
If you find a confusing line of code, `git blame <filename>` shows you exactly who wrote every line and in which commit. It's not for "blaming" people; it's for finding the context and the original ticket/PR.

### `git bisect`: Finding the Needle in the Haystack
If a bug appeared but you don't know which of the last 50 commits caused it, `git bisect` uses binary search to find the culprit:
1.  Tell Git a "good" commit (where the bug didn't exist).
2.  Tell Git a "bad" commit (the current one).
3.  Git will check out a commit in the middle. You test it and tell Git "good" or "bad."
4.  Git repeats until it finds the exact commit that introduced the bug.

### `git reflog`: The Ultimate Safety Net
If you accidentally delete a branch or perform a bad `reset`, Git keeps a log of every movement of the "HEAD" pointer for about 30 days. `git reflog` allows you to find the ID of a "lost" commit and recover it.

## 5. Picking Specific Changes: `git cherry-pick`
Imagine a teammate has a commit on their branch that fixes a bug you're experiencing, but you don't want to merge their *entire* branch. `git cherry-pick <commit_id>` lets you grab just that one specific commit and apply it to your current branch.

## 6. Git Internals: Content-Addressable Storage
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
[⬅️ Previous](03_collaboration.md) | [🏠 Table of Contents](../../README.md)
