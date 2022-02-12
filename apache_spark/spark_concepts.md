- resilient distributed dataset (RDD's) = collection of elements partitioned across the nodes of a cluster
- RDD's are either from HDFS or the client driver program
- broadcast variables = cache a value in memory across all nodes
- accumlators = values that are only added to such as sums and counters

- SparkContext = client driver main entry point to direct Spark how to access the cluster

- executors = processes that run computations and store data for your application
- SparkSession = entry point for programming spark using the built in Dataset or DataFrame API