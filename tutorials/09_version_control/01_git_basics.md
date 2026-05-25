# Lesson 16: Git Fundamentals for Analysts

## Overview
As a researcher or analyst, your code is your laboratory notebook. Version control (Git) ensures that you can experiment freely without the fear of "breaking" a working analysis. If you've ever had files named `analysis_final.R`, `analysis_final_v2.R`, and `analysis_REAL_final.R`, Git is the solution.

## 1. What is Git?
Git is a distributed version control system. Unlike simple backups, Git tracks **changes** to files over time.

### 💡 Real-World Scenario: The "I Messed Up" Moment (Anton's Discovery)
Imagine **Anton** is assigned the task **"Clean 2024 Census Data"** in the Project Pipeline. He spends all morning writing a complex script. It works perfectly. After lunch, Anton decides to "optimize" the loop. Two hours later, the script is broken, and he can't remember exactly what he changed.

*   **Without Git:** Anton is hitting `Ctrl+Z` repeatedly, hoping he didn't save recently.
*   **With Git:** Since Anton committed his work before lunch, he simply tells Git to "discard changes" and his script is instantly back to the perfect version he had when he started.

### The Mental Model: R vs. Git
| Feature | R / usethis | Git (CLI) | Why it matters |
| --- | --- | --- | --- |
| **Setup** | `usethis::use_git()` | `git init` | Initializes a hidden `.git` folder to track history. |
| **Status** | RStudio Git Pane | `git status` | Shows which files are changed, new, or ready to save. |
| **Snapshot** | `usethis::use_git_protocol()` | `git commit` | Saves a permanent snapshot of your work. |
| **History** | RStudio History | `git log` | A searchable timeline of every change ever made. |

## 2. Configuration
Before you start, you need to tell Git who you are. This information is attached to every "commit" (snapshot) you make.

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

## 3. The Basic Workflow: Add and Commit
Git uses a "Three-Stage" system:
1.  **Working Directory:** Where you edit your files.
2.  **Staging Area (The Index):** Where you "prepare" files for a snapshot.
3.  **Repository:** Where the snapshots (commits) are permanently stored.

### 💡 Visualizing the Workflow
```text
 +----------------+       git add        +----------------+
 |                | -------------------> |                |
 | Working Direct.|                      |  Staging Area  |
 |  (Your Files)  | <------------------- |   (The Bag)    |
 |                |     git checkout     |                |
 +----------------+                      +----------------+
                                                 |
                                                 | git commit
                                                 v
                                         +----------------+
                                         |                |
                                         |   Repository   |
                                         |  (The Vault)   |
                                         |                |
                                         +----------------+
```

### ⚠️ Important: Git is NOT a Cloud Backup (Yet!)
One of the most common mistakes **Anton** might make is thinking that `git commit` sends his code to GitHub.
*   **Commit = Local:** When Anton commits, the snapshot is saved in the hidden `.git` folder **only on his computer**.
*   **Push = Remote:** If Anton's laptop breaks after a commit but *before* a "Push" (Lesson 18), his work is lost. 

**Rule of Thumb:** Commit often (for yourself), Push daily (for the team).

### 💡 Real-World Scenario: The Grocery Bag
Think of **Staging** like **Anton** preparing a task for review by **Alex**.
1.  **Anton** picks up items (edits files) for his "Census Data" task from the shelves (Working Directory).
2.  He puts specific files in his bag (Staging Area). He might leave out a temporary test file he doesn't want to show Alex yet.
3.  Once he's happy, he "checks out" (Commit). This snapshot is now a permanent part of the project's history.

### Step 1: Initialize
```bash
git init
```

### Step 2: Check Status
```bash
git status
```
*   **Red files:** Modified but not "staged" (not ready for the snapshot).
*   **Green files:** Staged and ready to be committed.

### Step 3: Stage Changes (The `add` command)
In RStudio, you click the "Staged" checkbox. In the terminal:
```bash
# Stage a specific file
git add analysis.py

# Stage everything in the current folder
git add .
```

### Step 4: Commit (The snapshot)
A commit should be a logical "chunk" of work.
```bash
git commit -m "Add initial data cleaning script"
```
*   **Pro-Tip:** Always write descriptive commit messages. "Fixed bug" is bad; "Fix division by zero in age calculation" is good.

## 4. Ignoring Files (`.gitignore`)
Analysts often have large data files (`.csv`, `.xlsx`) or secret API keys that shouldn't be in Git. We use a `.gitignore` file to tell Git what to ignore.

### 💡 Real-World Scenario: Preventing Data Leakage
**Anton** is working on the pipeline task **"Patient Outcome Analysis."** The task requires him to handle sensitive data in `data/patient_records.csv`. He wants to share his code with **Ashmita**, but he MUST NOT share the actual data. 

By adding `data/` to his `.gitignore`, **Anton** ensures that even if he runs `git add .`, the sensitive data file stays on his local machine and never accidentally ends up on the team's shared GitHub repository.

Example `.gitignore`:
```text
# Ignore data files
data/*.csv
data/*.parquet

# Ignore OS files
.DS_Store
Thumbs.db

# Ignore environment variables
.env
```

---

## 🏆 Challenge Exercise: Your First Repo
1.  Open your terminal in a new folder.
2.  Initialize a git repository.
3.  Create a file named `hello.py` and write `print("Hello Git")` inside.
4.  Stage and commit this file with the message "Initial commit".
5.  Modify `hello.py` to say `print("Hello Version Control")`.
6.  Use `git status` to see the change, then stage and commit it.
7.  Run `git log` to see your history!

---
[⬅️ Previous](../08_advanced_topics/04_local_ui.md) | [🏠 Table of Contents](../../README.md) | [Next ➡️](02_branching_merging.md)
