# Lesson 21: PowerBI & Microsoft Fabric Integration

## Overview
In the modern enterprise, your Python code is rarely the "final product." It is usually a component in a larger data story told through **PowerBI** and managed within **Microsoft Fabric**. This lesson provides a deep dive into why these technologies are used and how to integrate your Python workflows into them.

---

## 1. Why use the Microsoft Data Stack?
For an R user, the transition to PowerBI and Fabric can be summarized as moving from **"Local Scripting"** to **"Enterprise Data Orchestration."**

*   **PowerBI:** The "UI of the organization." It provides a governed, secure, and interactive way to share insights without sending around static PDF reports.
*   **Microsoft Fabric:** A unified platform that replaces the "fragmented" stack (SQL Server + Spark + Data Factory + PowerBI). Everything is stored in **OneLake** (the "OneDrive for data").

---

## 2. Deep Dive: Python in PowerBI
You don't have to choose between PowerBI and Python; you can use Python to "supercharge" PowerBI where its native tools (DAX and M) fall short.

### A. Power Query (The "Extract & Transform" Layer)
**When to use:** When you need complex data cleaning (e.g., fuzzy matching, regex, or specialized scientific libraries) that is difficult to write in Power Query's "M" language.
*   **Feature:** `Get Data` -> `Python Script`.
*   **The "Why":** You can use `Pandas` or `Polars` to perform transformations that would take hundreds of lines of "M" code in just 5 lines of Python.

### B. Python Visuals (The "Visual" Layer)
**When to use:** When PowerBI's built-in charts aren't enough (e.g., complex statistical plots, ridgeline plots, or specific `plotnine` customizations).
*   **Feature:** The "Python Visual" icon in the visualizations pane.
*   **The "Why":** You get the full power of `Matplotlib`, `Seaborn`, and `Plotly` (static) inside a PowerBI report.

---

## 3. Deep Dive: Microsoft Fabric
Fabric is the "SaaS" evolution of data engineering. For a research analyst, it simplifies everything about the data lifecycle.

### A. OneLake: The Single Source of Truth
In the past, you had data in CSVs, SQL Servers, and S3 buckets. Fabric introduces **OneLake**.
*   **The "Why":** No more "where is the latest version of this file?" Every notebook, every PowerBI report, and every SQL query points to the same underlying file in OneLake.

### B. Fabric Notebooks: Jupyter with "Enterprise Extras"
While Fabric Notebooks look like Jupyter, there are key differences in how you access data and manage the environment.

| Feature | Local Jupyter | Microsoft Fabric Notebook |
| --- | --- | --- |
| **File Paths** | `C:/data/file.csv` | `Files/data/file.csv` or `abfss://...` |
| **Libraries** | `pip install` in terminal | `%pip install` or Environment Settings |
| **Data Engine** | Local CPU (Pandas/Polars) | Spark Cluster (PySpark) + Local CPU |
| **Secrets** | `.env` files | `mssparkutils.credentials.getSecret()` |

---

## 4. Natively Storing Data in a Lakehouse
In Fabric, you don't just "save a file." You write to the **Lakehouse**. The best practice is to store data as **Delta Tables**, which are Parquet files with a transaction log (making them "SQL-like").

### A. Writing with Pandas (Small/Medium Data)
If your data fits in memory, you can write directly to the `Tables` or `Files` section of your Lakehouse.

```python
# Save as a standard file
df.to_csv("Files/transformed_data.csv", index=False)

# Save as a Delta Table (Native Lakehouse Format)
# Note: Requires 'deltalake' library locally, but built-in to Fabric
import deltalake
df.to_delta("Tables/my_research_table")
```

### B. Writing with PySpark (Big Data)
In Fabric, Spark is the "native" language. It handles massive datasets by spreading the work across a cluster.

```python
# Convert Pandas to Spark
spark_df = spark.createDataFrame(df)

# Write as a Managed Table (Best for PowerBI)
spark_df.write.format("delta").mode("overwrite").saveAsTable("gold_research_data")
```

## 5. The "Semantic Link" (SemPy)
Fabric has a unique library called `sempy`. It allows your Python code to "talk" to PowerBI datasets.
*   **Feature:** You can run DAX queries directly from your Python notebook.
*   **Why use it?** You can pull in calculated measures from a PowerBI model to use in your Python statistical models, ensuring you're using the "official" business logic.

```python
import sempy.fabric as fabric
# List all datasets in your workspace
fabric.list_datasets()
```

## 6. Feature Walkthrough: Decision Matrix

| Need | Native Tool | Python "Superpower" |
| --- | --- | --- |
| **Data Cleaning** | Power Query (M) | `Pandas` / `Polars` (for regex & complex logic) |
| **Calculations** | DAX | `SciPy` / `Statsmodels` (for advanced stats) |
| **Standard Charts** | PowerBI Visuals | `Seaborn` (for publication-quality aesthetics) |
| **Big Data** | PowerBI Aggregations | `PySpark` in Fabric Notebooks |
| **Scheduling** | PowerBI Gateway | Fabric Pipelines (automated Python runs) |

---

## 5. Walkthrough: From Python Script to PowerBI Dashboard
1.  **Develop Locally:** Write your cleaning logic in a Jupyter Notebook using Lesson 03 (Wrangling) skills.
2.  **Move to Fabric:** Copy that code into a **Fabric Notebook**.
3.  **Write to Lakehouse:** Use `df.write_delta("Files/my_clean_data")`.
4.  **Connect PowerBI:** Open PowerBI, connect to the **Fabric Lakehouse**, and use **Direct Lake** mode.
5.  **Schedule:** Set the Fabric Notebook to run every Monday at 8 AM. Your dashboard is now fully automated!

---

## 🏆 Challenge Exercise: Enterprise Strategy
1.  **Analyze your Workflow:** Take a current R-based project. Where does the data come from? Where does the final chart go?
2.  **The "Fabric" Map:** 
    *   Could the raw data move to **OneLake**?
    *   Could your `dplyr` logic move to a **Fabric Notebook**?
    *   Could your final `ggplot` move to a **PowerBI Python Visual**?
3.  **Discussion:** Why is "Direct Lake" safer for data integrity than emailing around Excel files or CSVs?

---
[⬅️ Previous](01_quarto.md) | [🏠 Table of Contents](../../README.md)
