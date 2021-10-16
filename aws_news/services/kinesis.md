# kinesis_video_analytics
- stream video to Rekognition/Sagemaker

# kinesis_data_firehose
- perform etl with lambda and then send data to elasticsearch, splunk, redshift, AWS S3, http endpoints
- can batch/buffer data before sending to end destination

# kinesis_analytics
- sql queries over stream
- supports existing apps using apache flink (distributed streaming computation framework in python/java/sql without any built in data storage which is what kinesis provides)

# kinesis_data_streams
- shards data
- keeps data for a certain period of time
- you need to scale up/down ec2/lambda/other compute to process