from pyspark.sql import SparkSession
from pyspark.sql.functions import col, explode

# Create Spark session
spark = SparkSession.builder.appName("Nobel").getOrCreate()

# Read the JSON file
df = spark.read.option("multiline", True).json("/Users/arun/Desktop/DEP/Data/Sourcedata/nobel.json")

# Print schema to verify structure
df.printSchema()

# Explode the top-level 'winners' array
df2 = df.select(
    col("year"),
    explode("winners").alias("category_data")
)

# Explode nested winners per category
df3 = df2.select(
    col("year"),
    col("category_data.category").alias("category"),
    explode(col("category_data.winners")).alias("winner")
)

# Flatten the final columns
flat_df = df3.select(
    col("year"),
    col("category"),
    col("winner.name").alias("name"),
    col("winner.country").alias("country"),
    col("winner.achievement").alias("achievement")
)

# Show the flattened DataFrame
flat_df.show(truncate=False)
