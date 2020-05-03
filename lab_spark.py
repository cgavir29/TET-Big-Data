#!/usr/bin/env python
# coding: utf-8

# # Data Processing using Pyspark

#import SparkSession
from pyspark.sql.types import StringType, DoubleType, IntegerType
from pyspark.sql.functions import pandas_udf, PandasUDFType
from pyspark.sql.functions import udf
from pyspark.sql import SparkSession


# create spar session object
spark = SparkSession.builder.appName('data_processing').getOrCreate()

# Load csv Dataset
df = spark.read.csv('s3://tet-bd/datasets/spark/Casos_positivos_de_COVID-19_en_Colombia.csv',
                    inferSchema=True, header=True)


# In[ ]:


# columns of dataframe
df.columns


# In[ ]:


# check number of columns
len(df.columns)


# In[ ]:


# number of records in dataframe
df.count()


# In[ ]:


# shape of dataset
print((df.count(), len(df.columns)))


# In[ ]:


# printSchema
df.printSchema()


# In[ ]:


# fisrt few rows of dataframe
df.show(5)


# In[ ]:


# select only 2 columns
df.select('age', 'mobile').show(5)


# In[ ]:


# info about dataframe
df.describe().show()


# In[ ]:


# In[ ]:


# with column
df.withColumn("age_after_10_yrs", (df["age"]+10)).show(10, False)


# In[ ]:


df.withColumn('age_double', df['age'].cast(DoubleType())).show(10, False)


# In[ ]:


# with column
df.withColumn("age_after_10_yrs", (df["age"]+10)).show(10, False)


# In[ ]:


# filter the records
df.filter(df['mobile'] == 'Vivo').show()


# In[ ]:


# filter the records
df.filter(df['mobile'] == 'Vivo').select('age', 'ratings', 'mobile').show()


# In[ ]:


# filter the multiple conditions
df.filter(df['mobile'] == 'Vivo').filter(df['experience'] > 10).show()


# In[ ]:


# filter the multiple conditions
df.filter((df['mobile'] == 'Vivo') & (df['experience'] > 10)).show()


# In[ ]:


# Distinct Values in a column
df.select('mobile').distinct().show()


# In[ ]:


# distinct value count
df.select('mobile').distinct().count()


# In[ ]:


df.groupBy('mobile').count().show(5, False)


# In[ ]:


# Value counts
df.groupBy('mobile').count().orderBy('count', ascending=False).show(5, False)


# In[ ]:


# Value counts
df.groupBy('mobile').mean().show(5, False)


# In[ ]:


df.groupBy('mobile').sum().show(5, False)


# In[ ]:


# Value counts
df.groupBy('mobile').max().show(5, False)


# In[ ]:


# Value counts
df.groupBy('mobile').min().show(5, False)


# In[ ]:


# Aggregation
df.groupBy('mobile').agg({'experience': 'sum'}).show(5, False)


# In[ ]:


# UDF


# In[ ]:


# normal function
def price_range(brand):
    if brand in ['Samsung', 'Apple']:
        return 'High Price'
    elif brand == 'MI':
        return 'Mid Price'
    else:
        return 'Low Price'


# In[ ]:


# create udf using python function
brand_udf = udf(price_range, StringType())
# apply udf on dataframe
df.withColumn('price_range', brand_udf(df['mobile'])).show(10, False)


# In[ ]:


# using lambda function
age_udf = udf(lambda age: "young" if age <= 30 else "senior", StringType())
# apply udf on dataframe
df.withColumn("age_group", age_udf(df.age)).show(10, False)


# In[ ]:


# pandas udf


# In[ ]:


# create python function
def remaining_yrs(age):
    yrs_left = 100-age

    return yrs_left


# In[ ]:


# create udf using python function
length_udf = pandas_udf(remaining_yrs, IntegerType())
# apply pandas udf on dataframe
df.withColumn("yrs_left", length_udf(df['age'])).show(10, False)


# In[ ]:


# udf using two columns
def prod(rating, exp):
    x = rating*exp
    return x


# In[ ]:


# create udf using python function
prod_udf = pandas_udf(prod, DoubleType())
# apply pandas udf on multiple columns of dataframe
df.withColumn("product", prod_udf(
    df['ratings'], df['experience'])).show(10, False)


# In[ ]:


# duplicate values
df.count()


# In[ ]:


# drop duplicate values
df = df.dropDuplicates()


# In[ ]:


# validate new count
df.count()


# In[ ]:


# drop column of dataframe
df_new = df.drop('mobile')


# In[ ]:


df_new.show(10)


# In[ ]:


# saving file (csv)


# In[ ]:


# current working directory
pwd


# In[ ]:


# target directory
write_uri = 's3://<bucket/dir>/df_csv'


# In[ ]:


# save the dataframe as single csv
df.coalesce(1).write.format("csv").option("header", "true").save(write_uri)


# In[ ]:


# parquet


# In[ ]:


# target location
parquet_uri = 's3://<bucket/dir>/df_parquet'


# In[ ]:


# save the data into parquet format
df.write.format('parquet').save(parquet_uri)


# In[ ]:

