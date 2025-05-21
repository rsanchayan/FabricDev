# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "677a317f-0b5c-47a9-8401-42e4c5240d41",
# META       "default_lakehouse_name": "delta_lake",
# META       "default_lakehouse_workspace_id": "c0dd4888-5637-43a2-bac6-4508844202bb",
# META       "known_lakehouses": [
# META         {
# META           "id": "677a317f-0b5c-47a9-8401-42e4c5240d41"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

import com.microsoft.spark.fabric
from com.microsoft.spark.fabric.Constants import Constants  

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

limit_1 = 1000

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = spark.read.synapsesql("Input.dbo.fact_sale").limit(limit_1)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df.write.format("delta").mode("append").saveAsTable("New_table")



# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# PARAMETERS CELL ********************


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
