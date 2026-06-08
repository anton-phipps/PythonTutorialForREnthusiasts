# Block 1
import pandas as pd
import os

# Create a sample DataFrame
df = pd.DataFrame({'id': [1, 2, 3], 'value': [10.5, 20.3, 15.8]})

# Create dummy directories for the examples to work
os.makedirs("Files", exist_ok=True)
os.makedirs("Tables", exist_ok=True)

# Block 2
# Save as a standard file
df.to_csv("Files/transformed_data.csv", index=False)

# Save as a Delta Table (Native Lakehouse Format)
# Note: Requires 'deltalake' library locally, but built-in to Fabric
from deltalake import write_deltalake
write_deltalake("Tables/my_research_table", df, mode='overwrite')

# Block 3
# Note: This block assumes you are in a Spark environment (e.g., Fabric Notebook)
try:
    # Convert Pandas to Spark
    spark_df = spark.createDataFrame(df)

    # Write as a Managed Table (Best for PowerBI)
    spark_df.write.format("delta").mode("overwrite").saveAsTable("gold_research_data")
except NameError:
    print("Spark environment not found, skipping Spark example.")

# Block 4
try:
    import sempy.fabric as fabric
    # List all datasets in your workspace
    fabric.list_datasets()
except ImportError:
    print("sempy not installed, skipping Fabric Semantic Link example.")

