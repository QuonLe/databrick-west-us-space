# Databricks notebook source
# MAGIC %pip install dbdemos

# COMMAND ----------

import dbdemos
dbdemos.list_demos()

# COMMAND ----------

def func(a,b):
    print(a+b)

# COMMAND ----------

func(5,10)
