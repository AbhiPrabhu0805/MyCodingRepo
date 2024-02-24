from pyspark.sql import SparkSession
spark = (SparkSession.builder.appName("TestingRDDS").getOrCreate())
words_list="Spark made my life very very easy by distributing data".split(" ")
type(words_list)
print(words_list)
words_rdd=spark.sparkContext.parallelize(words_list)
words_data=words_rdd.collect()
for word in words_data:
    print(word)

print(words_rdd.count())
print(words_rdd.distinct().count())

words_unique_rdd=words_rdd.distinct()

words_unique_data=words_unique_rdd.collect()

for word in words_unique_data:
    print(word)

print(words_rdd.filter(lambda word: word.startswith('S')).collect())

num_list=[*range(1,21)]
print(num_list)

nums_rdd=spark.sparkContext.parallelize(num_list)
nums_data=nums_rdd.collect()
print(nums_data)


nums_sqr_rdd=nums_rdd.map(lambda num: (num, num*num))
print(nums_sqr_rdd.collect())

words_flat_rdd=words_rdd.flatMap(lambda word:(word, word[0],word.startswith("S")))

print(words_flat_rdd.collect())

countries_list=[('India',3),('USA',1),('England',2)]

countries_rdd=spark.sparkContext.parallelize(countries_list)

countries_sorted=countries_rdd.sortByKey().collect()

print(countries_sorted)

countries_sorted_2=countries_rdd.map(lambda c:(c[1],c[0])).sortByKey(False).map(lambda c:(c[1],c[0])).collect()

print(countries_sorted_2)

def word_length_check(leftw, rightw):
    if len(leftw)>len(rightw):
        return leftw
    else:
        return rightw

word_len_check_rdd=spark.sparkContext.parallelize(words_list)

result=word_len_check_rdd.reduce(lambda leftwrd, rightwrd: word_length_check(leftwrd,rightwrd))
#or
result=word_len_check_rdd.reduce(word_length_check)
print(result)

print(words_rdd.first())

print(words_rdd.max())

print(words_rdd.min())
