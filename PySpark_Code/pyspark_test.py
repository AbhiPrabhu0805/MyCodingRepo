from pyspark import SparkContext
sc = SparkContext('local[*]') 
big_list=range(1000)
rdd=sc.parallelize(big_list,2)
odds=rdd.filter(lambda x:x%2!=0)
print(odds.take(5))
