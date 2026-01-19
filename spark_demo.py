from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg

# 1️⃣ Create Spark session
spark = SparkSession.builder.appName("SparkDemo").master("local[*]").getOrCreate()

# 2️⃣ Read CSV file into DataFrame
df = spark.read.csv("people.csv", header=True, inferSchema=True)

# 3️⃣ Show the data
print("Original Data:")
df.show()

# 4️⃣ Filter people older than 30
df_filtered = df.filter(col("age") > 30)
print("People older than 30:")
df_filtered.show()

# 5️⃣ Group by country and calculate average salary
df_grouped = df.groupBy("country").agg(avg("salary").alias("avg_salary"))
print("Average salary by country:")
df_grouped.show()

# 6️⃣ Stop Spark session
spark.stop()

