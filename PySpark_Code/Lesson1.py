from pyspark import SparkContext
sc = SparkContext('local[*]') 

from pyspark.sql import SparkSession
from pyspark.sql.functions import count


spark=(SparkSession.builder.appName("TotalOrdersPerRegionCountry").getOrCreate())

print(type(spark))

sales_file="sales_records.csv"

sales_df=(spark.read.format("csv").option("header","true").option("infer_schema","true").load(sales_file))

sales_df.select("Region","Country","Order ID").show(n=10, truncate=False)

print(type(sales_df))

count_sales_df= sales_df.select("Region","Country","Order ID").groupBy("Region","Country").agg(count("Order ID").alias("Total Orders")).orderBy("Total Orders", ascending=False)

count_sales_df.show(n=10, truncate=False)

print("Total Rows =",count_sales_df.count())

