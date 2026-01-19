from pyspark.sql import SparkSession

# Create Spark session
spark = SparkSession.builder \
    .appName("SimpleSparkExample") \
    .master("local[*]") \
    .getOrCreate()

# Sample data
data = [
    ("Alice", 30),
    ("Bob", 25),
    ("Charlie", 35)
]

# Create DataFrame
df = spark.createDataFrame(data, ["name", "age"])

# Simple transformation
filtered_df = df.filter(df.age > 30)

# Action
filtered_df.show()

# Stop Spark
spark.stop()

