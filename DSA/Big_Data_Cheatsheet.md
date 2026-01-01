# Big Data Cheatsheet - Complete Guide with Technologies & Best Practices

## Table of Contents
- [Big Data Fundamentals](#big-data-fundamentals)
- [Hadoop Ecosystem](#hadoop-ecosystem)
- [Apache Spark](#apache-spark)
- [Data Storage](#data-storage)
- [Data Processing](#data-processing)
- [Stream Processing](#stream-processing)
- [Data Warehousing](#data-warehousing)
- [NoSQL Databases](#nosql-databases)
- [Cloud Platforms](#cloud-platforms)
- [Data Pipeline Tools](#data-pipeline-tools)
- [Monitoring & Management](#monitoring--management)
- [Best Practices](#best-practices)

## Big Data Fundamentals

### The 5 V's of Big Data
```
Volume    - Scale of data (Terabytes to Petabytes)
Velocity  - Speed of data generation and processing
Variety   - Different types of data (structured, semi-structured, unstructured)
Veracity  - Quality and accuracy of data
Value     - Business value derived from data
```

### Big Data Architecture Patterns
```
Lambda Architecture:
┌─────────────────┐    ┌──────────────┐    ┌─────────────┐
│   Data Sources  │───▶│ Batch Layer  │───▶│ Serving     │
└─────────────────┘    └──────────────┘    │ Layer       │
         │              ┌──────────────┐    │             │
         └─────────────▶│ Speed Layer  │───▶│             │
                        └──────────────┘    └─────────────┘

Kappa Architecture:
┌─────────────────┐    ┌──────────────┐    ┌─────────────┐
│   Data Sources  │───▶│ Stream Layer │───▶│ Serving     │
└─────────────────┘    └──────────────┘    │ Layer       │
                                           └─────────────┘
```

### Data Types and Formats
```bash
# Structured Data
- CSV, TSV
- JSON, XML
- Parquet, ORC
- Avro

# Semi-structured Data
- JSON, XML
- Log files
- Email

# Unstructured Data
- Text documents
- Images, Videos
- Audio files
- Social media posts
```

## Hadoop Ecosystem

### Hadoop Core Components
```bash
# HDFS (Hadoop Distributed File System)
# Check HDFS status
hdfs dfsadmin -report

# List files in HDFS
hdfs dfs -ls /path/to/directory

# Copy file to HDFS
hdfs dfs -put local_file.txt /hdfs/path/

# Copy file from HDFS
hdfs dfs -get /hdfs/path/file.txt local_file.txt

# Create directory in HDFS
hdfs dfs -mkdir /hdfs/new_directory

# Remove file from HDFS
hdfs dfs -rm /hdfs/path/file.txt

# Check file size
hdfs dfs -du -h /hdfs/path/

# Set replication factor
hdfs dfs -setrep 3 /hdfs/path/file.txt
```

### MapReduce Programming
```java
// Mapper Class
public class WordCountMapper extends Mapper<LongWritable, Text, Text, IntWritable> {
    private final static IntWritable one = new IntWritable(1);
    private Text word = new Text();
    
    @Override
    public void map(LongWritable key, Text value, Context context) 
            throws IOException, InterruptedException {
        
        String line = value.toString().toLowerCase();
        StringTokenizer tokenizer = new StringTokenizer(line);
        
        while (tokenizer.hasMoreTokens()) {
            word.set(tokenizer.nextToken());
            context.write(word, one);
        }
    }
}

// Reducer Class
public class WordCountReducer extends Reducer<Text, IntWritable, Text, IntWritable> {
    private IntWritable result = new IntWritable();
    
    @Override
    public void reduce(Text key, Iterable<IntWritable> values, Context context)
            throws IOException, InterruptedException {
        
        int sum = 0;
        for (IntWritable value : values) {
            sum += value.get();
        }
        
        result.set(sum);
        context.write(key, result);
    }
}

// Driver Class
public class WordCount {
    public static void main(String[] args) throws Exception {
        Configuration conf = new Configuration();
        Job job = Job.getInstance(conf, "word count");
        
        job.setJarByClass(WordCount.class);
        job.setMapperClass(WordCountMapper.class);
        job.setCombinerClass(WordCountReducer.class);
        job.setReducerClass(WordCountReducer.class);
        
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);
        
        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));
        
        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}
```

### YARN (Yet Another Resource Negotiator)
```bash
# YARN commands
yarn application -list                    # List running applications
yarn application -kill application_id    # Kill application
yarn logs -applicationId application_id  # View application logs
yarn node -list                         # List cluster nodes
yarn queue -status queue_name            # Check queue status

# Resource management
yarn rmadmin -refreshQueues              # Refresh queue configuration
yarn rmadmin -refreshNodes               # Refresh node configuration
```

### Hive Data Warehousing
```sql
-- Create database
CREATE DATABASE IF NOT EXISTS sales_db;
USE sales_db;

-- Create external table
CREATE EXTERNAL TABLE sales_data (
    transaction_id STRING,
    customer_id STRING,
    product_id STRING,
    quantity INT,
    price DOUBLE,
    transaction_date STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION '/hdfs/path/to/sales/data/';

-- Partitioned table
CREATE TABLE sales_partitioned (
    transaction_id STRING,
    customer_id STRING,
    product_id STRING,
    quantity INT,
    price DOUBLE
)
PARTITIONED BY (year INT, month INT)
STORED AS PARQUET;

-- Insert data with dynamic partitioning
SET hive.exec.dynamic.partition = true;
SET hive.exec.dynamic.partition.mode = nonstrict;

INSERT INTO TABLE sales_partitioned PARTITION(year, month)
SELECT 
    transaction_id,
    customer_id,
    product_id,
    quantity,
    price,
    YEAR(transaction_date) as year,
    MONTH(transaction_date) as month
FROM sales_data;

-- Bucketed table for better performance
CREATE TABLE customer_bucketed (
    customer_id STRING,
    name STRING,
    email STRING,
    age INT
)
CLUSTERED BY (customer_id) INTO 10 BUCKETS
STORED AS ORC;

-- Optimized queries
-- Use partitioning
SELECT * FROM sales_partitioned 
WHERE year = 2023 AND month = 12;

-- Use bucketing for joins
SELECT /*+ MAPJOIN(c) */ s.*, c.name
FROM sales_partitioned s
JOIN customer_bucketed c ON s.customer_id = c.customer_id;

-- Window functions
SELECT 
    customer_id,
    transaction_date,
    price,
    SUM(price) OVER (PARTITION BY customer_id ORDER BY transaction_date) as running_total,
    ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY price DESC) as price_rank
FROM sales_data;
```

### HBase NoSQL Database
```java
// HBase Java API
Configuration config = HBaseConfiguration.create();
Connection connection = ConnectionFactory.createConnection(config);

// Create table
Admin admin = connection.getAdmin();
TableName tableName = TableName.valueOf("user_profiles");
HTableDescriptor tableDescriptor = new HTableDescriptor(tableName);
HColumnDescriptor columnDescriptor = new HColumnDescriptor("personal_info");
tableDescriptor.addFamily(columnDescriptor);
admin.createTable(tableDescriptor);

// Insert data
Table table = connection.getTable(tableName);
Put put = new Put(Bytes.toBytes("user123"));
put.addColumn(Bytes.toBytes("personal_info"), Bytes.toBytes("name"), Bytes.toBytes("John Doe"));
put.addColumn(Bytes.toBytes("personal_info"), Bytes.toBytes("age"), Bytes.toBytes("30"));
table.put(put);

// Retrieve data
Get get = new Get(Bytes.toBytes("user123"));
Result result = table.get(get);
String name = Bytes.toString(result.getValue(Bytes.toBytes("personal_info"), Bytes.toBytes("name")));

// Scan data
Scan scan = new Scan();
scan.addFamily(Bytes.toBytes("personal_info"));
ResultScanner scanner = table.getScanner(scan);
for (Result res : scanner) {
    // Process results
}

// Close connections
scanner.close();
table.close();
connection.close();
```

## Apache Spark

### Spark Core Concepts
```python
# PySpark - Spark with Python
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

# Create Spark session
spark = SparkSession.builder \
    .appName("BigDataProcessing") \
    .config("spark.sql.adaptive.enabled", "true") \
    .config("spark.sql.adaptive.coalescePartitions.enabled", "true") \
    .getOrCreate()

# Set log level
spark.sparkContext.setLogLevel("WARN")
```

### RDD Operations
```python
# Create RDD
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
rdd = spark.sparkContext.parallelize(data)

# Transformations (lazy evaluation)
filtered_rdd = rdd.filter(lambda x: x % 2 == 0)
mapped_rdd = rdd.map(lambda x: x * 2)
flat_mapped_rdd = rdd.flatMap(lambda x: [x, x * 2])

# Actions (trigger computation)
result = filtered_rdd.collect()
count = rdd.count()
first_element = rdd.first()
sum_result = rdd.reduce(lambda a, b: a + b)

# Key-value operations
pairs_rdd = rdd.map(lambda x: (x % 3, x))
grouped_rdd = pairs_rdd.groupByKey()
reduced_rdd = pairs_rdd.reduceByKey(lambda a, b: a + b)

# Join operations
rdd1 = spark.sparkContext.parallelize([(1, "a"), (2, "b"), (3, "c")])
rdd2 = spark.sparkContext.parallelize([(1, "x"), (2, "y"), (4, "z")])
joined_rdd = rdd1.join(rdd2)  # Inner join
left_joined_rdd = rdd1.leftOuterJoin(rdd2)
```

### DataFrame Operations
```python
# Create DataFrame
schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True),
    StructField("salary", DoubleType(), True)
])

data = [(1, "John", 25, 50000.0), (2, "Jane", 30, 60000.0), (3, "Bob", 35, 70000.0)]
df = spark.createDataFrame(data, schema)

# Read from files
df_csv = spark.read.option("header", "true").csv("path/to/file.csv")
df_json = spark.read.json("path/to/file.json")
df_parquet = spark.read.parquet("path/to/file.parquet")

# DataFrame operations
df.show()                           # Display data
df.printSchema()                    # Show schema
df.describe().show()                # Summary statistics
df.count()                          # Count rows
df.columns                          # Column names

# Selecting and filtering
df.select("name", "age").show()
df.filter(df.age > 25).show()
df.where(col("salary") > 55000).show()

# Aggregations
df.groupBy("age").agg(
    avg("salary").alias("avg_salary"),
    count("*").alias("count")
).show()

# Window functions
from pyspark.sql.window import Window

window_spec = Window.partitionBy("department").orderBy("salary")
df.withColumn("rank", row_number().over(window_spec)).show()

# Joins
df1 = spark.createDataFrame([(1, "John"), (2, "Jane")], ["id", "name"])
df2 = spark.createDataFrame([(1, "Engineering"), (2, "Marketing")], ["id", "dept"])
joined_df = df1.join(df2, "id", "inner")
```

### Spark SQL
```python
# Register DataFrame as temporary view
df.createOrReplaceTempView("employees")

# SQL queries
result = spark.sql("""
    SELECT 
        department,
        AVG(salary) as avg_salary,
        COUNT(*) as employee_count
    FROM employees
    WHERE age > 25
    GROUP BY department
    ORDER BY avg_salary DESC
""")

# Complex SQL operations
spark.sql("""
    WITH ranked_employees AS (
        SELECT 
            *,
            ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) as rank
        FROM employees
    )
    SELECT * FROM ranked_employees WHERE rank <= 3
""").show()

# User-defined functions (UDF)
from pyspark.sql.functions import udf

def categorize_age(age):
    if age < 30:
        return "Young"
    elif age < 50:
        return "Middle"
    else:
        return "Senior"

age_category_udf = udf(categorize_age, StringType())
df.withColumn("age_category", age_category_udf(col("age"))).show()
```

### Spark Streaming
```python
from pyspark.streaming import StreamingContext
from pyspark.sql.functions import *

# Structured Streaming
df_stream = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "user_events") \
    .load()

# Process streaming data
processed_stream = df_stream \
    .select(from_json(col("value").cast("string"), schema).alias("data")) \
    .select("data.*") \
    .groupBy(window(col("timestamp"), "1 minute"), col("event_type")) \
    .count()

# Output stream
query = processed_stream \
    .writeStream \
    .outputMode("update") \
    .format("console") \
    .trigger(processingTime='30 seconds') \
    .start()

query.awaitTermination()

# DStream (legacy streaming)
ssc = StreamingContext(spark.sparkContext, 10)  # 10 second batches

# Create DStream from Kafka
from pyspark.streaming.kafka import KafkaUtils
kafka_stream = KafkaUtils.createDirectStream(
    ssc, 
    ["topic_name"], 
    {"metadata.broker.list": "localhost:9092"}
)

# Process DStream
word_counts = kafka_stream \
    .map(lambda x: x[1]) \
    .flatMap(lambda line: line.split(" ")) \
    .map(lambda word: (word, 1)) \
    .reduceByKey(lambda a, b: a + b)

word_counts.pprint()
ssc.start()
ssc.awaitTermination()
```

### Spark Performance Optimization
```python
# Caching and persistence
df.cache()                          # Cache in memory
df.persist(StorageLevel.MEMORY_AND_DISK)  # Custom storage level

# Partitioning
df.repartition(10)                  # Repartition to 10 partitions
df.coalesce(5)                      # Reduce partitions to 5
df.repartition("column_name")       # Partition by column

# Broadcast variables
broadcast_var = spark.sparkContext.broadcast(large_dict)
# Use broadcast_var.value in transformations

# Accumulators
accumulator = spark.sparkContext.accumulator(0)
def process_record(record):
    accumulator.add(1)
    return record

rdd.map(process_record).collect()
print(f"Processed {accumulator.value} records")

# Configuration tuning
spark.conf.set("spark.sql.adaptive.enabled", "true")
spark.conf.set("spark.sql.adaptive.coalescePartitions.enabled", "true")
spark.conf.set("spark.sql.adaptive.skewJoin.enabled", "true")
spark.conf.set("spark.serializer", "org.apache.spark.serializer.KryoSerializer")
```

## Data Storage

### HDFS Best Practices
```bash
# Optimal block size (default 128MB)
hdfs dfsadmin -setDefaultBlockSize 268435456  # 256MB

# Replication factor
hdfs dfs -setrep 3 /path/to/important/data
hdfs dfs -setrep 1 /path/to/temp/data

# Compression
# Enable compression in Hadoop
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
    -D mapreduce.output.fileoutputformat.compress=true \
    -D mapreduce.output.fileoutputformat.compress.codec=org.apache.hadoop.io.compress.GzipCodec

# File formats comparison
# Parquet - Columnar, good for analytics
# ORC - Optimized Row Columnar, good for Hive
# Avro - Schema evolution, good for streaming
```

### Data Lake Architecture
```
Data Lake Zones:
┌─────────────────┐
│   Raw Zone      │  ← Ingested data (original format)
├─────────────────┤
│ Processed Zone  │  ← Cleaned and transformed data
├─────────────────┤
│ Curated Zone    │  ← Business-ready data
└─────────────────┘

Storage Formats:
- Bronze Layer: Raw data (JSON, CSV, logs)
- Silver Layer: Cleaned data (Parquet, Delta)
- Gold Layer: Aggregated data (Parquet, Delta)
```

### Delta Lake
```python
# Delta Lake with Spark
from delta.tables import *

# Create Delta table
df.write.format("delta").save("/path/to/delta-table")

# Read Delta table
delta_df = spark.read.format("delta").load("/path/to/delta-table")

# Update data
deltaTable = DeltaTable.forPath(spark, "/path/to/delta-table")
deltaTable.update(
    condition = col("id") == 123,
    set = { "status": lit("inactive") }
)

# Merge (upsert) operation
deltaTable.alias("target").merge(
    source_df.alias("source"),
    "target.id = source.id"
).whenMatchedUpdate(set = {
    "name": "source.name",
    "updated_at": "source.updated_at"
}).whenNotMatchedInsert(values = {
    "id": "source.id",
    "name": "source.name",
    "created_at": "source.created_at"
}).execute()

# Time travel
df_yesterday = spark.read.format("delta").option("timestampAsOf", "2023-12-01").load("/path/to/delta-table")
df_version_5 = spark.read.format("delta").option("versionAsOf", 5).load("/path/to/delta-table")

# Vacuum old files
deltaTable.vacuum(168)  # Retain 7 days of history
```

## Data Processing

### Apache Kafka
```bash
# Kafka commands
# Create topic
kafka-topics.sh --create --topic user-events --bootstrap-server localhost:9092 --partitions 3 --replication-factor 1

# List topics
kafka-topics.sh --list --bootstrap-server localhost:9092

# Describe topic
kafka-topics.sh --describe --topic user-events --bootstrap-server localhost:9092

# Produce messages
kafka-console-producer.sh --topic user-events --bootstrap-server localhost:9092

# Consume messages
kafka-console-consumer.sh --topic user-events --from-beginning --bootstrap-server localhost:9092

# Consumer groups
kafka-consumer-groups.sh --bootstrap-server localhost:9092 --list
kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group my-group
```

### Kafka Streams
```java
// Kafka Streams application
Properties props = new Properties();
props.put(StreamsConfig.APPLICATION_ID_CONFIG, "word-count-app");
props.put(StreamsConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
props.put(StreamsConfig.DEFAULT_KEY_SERDE_CLASS_CONFIG, Serdes.String().getClass());
props.put(StreamsConfig.DEFAULT_VALUE_SERDE_CLASS_CONFIG, Serdes.String().getClass());

StreamsBuilder builder = new StreamsBuilder();

// Create stream from topic
KStream<String, String> textLines = builder.stream("text-input");

// Process stream
KTable<String, Long> wordCounts = textLines
    .flatMapValues(textLine -> Arrays.asList(textLine.toLowerCase().split("\\W+")))
    .groupBy((key, word) -> word)
    .count(Materialized.as("counts-store"));

// Output to topic
wordCounts.toStream().to("word-count-output", Produced.with(Serdes.String(), Serdes.Long()));

// Start application
KafkaStreams streams = new KafkaStreams(builder.build(), props);
streams.start();
```

### Apache Flink
```java
// Flink streaming application
StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();

// Configure checkpointing
env.enableCheckpointing(5000);
env.getCheckpointConfig().setCheckpointingMode(CheckpointingMode.EXACTLY_ONCE);

// Create data stream
DataStream<String> text = env.socketTextStream("localhost", 9999);

// Process stream
DataStream<Tuple2<String, Integer>> wordCounts = text
    .flatMap(new FlatMapFunction<String, Tuple2<String, Integer>>() {
        @Override
        public void flatMap(String sentence, Collector<Tuple2<String, Integer>> out) {
            for (String word : sentence.split(" ")) {
                out.collect(new Tuple2<>(word, 1));
            }
        }
    })
    .keyBy(value -> value.f0)
    .window(TumblingProcessingTimeWindows.of(Time.seconds(5)))
    .sum(1);

// Output results
wordCounts.print();

// Execute
env.execute("Word Count Example");
```

### Apache Airflow
```python
# Airflow DAG
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'data-team',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'data_pipeline',
    default_args=default_args,
    description='Daily data processing pipeline',
    schedule_interval='0 2 * * *',  # Daily at 2 AM
    catchup=False
)

def extract_data(**context):
    # Extract data logic
    print("Extracting data...")
    return "data_extracted"

def transform_data(**context):
    # Transform data logic
    print("Transforming data...")
    return "data_transformed"

def load_data(**context):
    # Load data logic
    print("Loading data...")
    return "data_loaded"

# Define tasks
extract_task = PythonOperator(
    task_id='extract_data',
    python_callable=extract_data,
    dag=dag
)

transform_task = PythonOperator(
    task_id='transform_data',
    python_callable=transform_data,
    dag=dag
)

load_task = PythonOperator(
    task_id='load_data',
    python_callable=load_data,
    dag=dag
)

# Set dependencies
extract_task >> transform_task >> load_task
```

## Stream Processing

### Apache Storm
```java
// Storm topology
public class WordCountTopology {
    public static void main(String[] args) throws Exception {
        TopologyBuilder builder = new TopologyBuilder();
        
        // Spout (data source)
        builder.setSpout("sentence-spout", new SentenceSpout(), 1);
        
        // Bolt (processing unit)
        builder.setBolt("split-bolt", new SplitSentenceBolt(), 2)
               .shuffleGrouping("sentence-spout");
               
        builder.setBolt("count-bolt", new WordCountBolt(), 2)
               .fieldsGrouping("split-bolt", new Fields("word"));
        
        Config config = new Config();
        config.setDebug(true);
        
        if (args != null && args.length > 0) {
            // Submit to cluster
            config.setNumWorkers(3);
            StormSubmitter.submitTopology(args[0], config, builder.createTopology());
        } else {
            // Local mode
            LocalCluster cluster = new LocalCluster();
            cluster.submitTopology("word-count", config, builder.createTopology());
            Thread.sleep(10000);
            cluster.shutdown();
        }
    }
}
```

### Real-time Analytics Patterns
```python
# Sliding window aggregation
def sliding_window_aggregation(stream, window_size, slide_interval):
    """
    Implement sliding window aggregation
    """
    from collections import deque
    import time
    
    window = deque()
    last_slide = time.time()
    
    for event in stream:
        current_time = time.time()
        
        # Add new event
        window.append((event, current_time))
        
        # Remove old events
        while window and window[0][1] < current_time - window_size:
            window.popleft()
        
        # Slide window if needed
        if current_time - last_slide >= slide_interval:
            yield aggregate_window(window)
            last_slide = current_time

# Event time processing
def process_event_time(events):
    """
    Process events based on event time rather than processing time
    """
    # Sort events by event time
    sorted_events = sorted(events, key=lambda x: x['event_time'])
    
    # Handle late arrivals with watermarks
    watermark = max(event['event_time'] for event in sorted_events) - timedelta(minutes=5)
    
    # Process events within watermark
    for event in sorted_events:
        if event['event_time'] <= watermark:
            process_event(event)
        else:
            # Handle late event
            handle_late_event(event)
```

## Data Warehousing

### Dimensional Modeling
```sql
-- Star Schema Example

-- Fact table
CREATE TABLE sales_fact (
    sale_id BIGINT PRIMARY KEY,
    date_key INT,
    customer_key INT,
    product_key INT,
    store_key INT,
    quantity INT,
    unit_price DECIMAL(10,2),
    total_amount DECIMAL(10,2),
    discount_amount DECIMAL(10,2)
);

-- Dimension tables
CREATE TABLE date_dim (
    date_key INT PRIMARY KEY,
    date_value DATE,
    year INT,
    quarter INT,
    month INT,
    day INT,
    day_of_week INT,
    is_weekend BOOLEAN,
    is_holiday BOOLEAN
);

CREATE TABLE customer_dim (
    customer_key INT PRIMARY KEY,
    customer_id STRING,
    customer_name STRING,
    customer_segment STRING,
    customer_city STRING,
    customer_state STRING,
    customer_country STRING,
    effective_date DATE,
    expiry_date DATE,
    is_current BOOLEAN
);

CREATE TABLE product_dim (
    product_key INT PRIMARY KEY,
    product_id STRING,
    product_name STRING,
    category STRING,
    subcategory STRING,
    brand STRING,
    supplier STRING
);

-- Slowly Changing Dimension (SCD Type 2)
CREATE TABLE customer_dim_scd2 (
    customer_key INT PRIMARY KEY,
    customer_id STRING,
    customer_name STRING,
    customer_segment STRING,
    effective_date DATE,
    expiry_date DATE,
    is_current BOOLEAN,
    version INT
);

-- SCD Type 2 Update Process
INSERT INTO customer_dim_scd2 (
    customer_key,
    customer_id,
    customer_name,
    customer_segment,
    effective_date,
    expiry_date,
    is_current,
    version
)
SELECT 
    ROW_NUMBER() OVER (ORDER BY customer_id) + (SELECT MAX(customer_key) FROM customer_dim_scd2),
    customer_id,
    customer_name,
    customer_segment,
    CURRENT_DATE,
    '9999-12-31',
    TRUE,
    COALESCE((SELECT MAX(version) FROM customer_dim_scd2 WHERE customer_id = new.customer_id), 0) + 1
FROM new_customer_data new;

-- Update existing records
UPDATE customer_dim_scd2 
SET expiry_date = CURRENT_DATE - 1, is_current = FALSE
WHERE customer_id IN (SELECT customer_id FROM new_customer_data)
  AND is_current = TRUE;
```

### Apache Druid
```json
// Druid ingestion spec
{
  "type": "index_parallel",
  "spec": {
    "dataSchema": {
      "dataSource": "user_events",
      "timestampSpec": {
        "column": "timestamp",
        "format": "iso"
      },
      "dimensionsSpec": {
        "dimensions": [
          "user_id",
          "event_type",
          "platform",
          "country"
        ]
      },
      "metricsSpec": [
        {
          "type": "count",
          "name": "count"
        },
        {
          "type": "longSum",
          "name": "session_duration",
          "fieldName": "duration"
        }
      ],
      "granularitySpec": {
        "type": "uniform",
        "segmentGranularity": "DAY",
        "queryGranularity": "HOUR"
      }
    },
    "ioConfig": {
      "type": "index_parallel",
      "inputSource": {
        "type": "s3",
        "uris": ["s3://bucket/path/to/data/"]
      },
      "inputFormat": {
        "type": "json"
      }
    },
    "tuningConfig": {
      "type": "index_parallel",
      "maxRowsPerSegment": 5000000,
      "maxRowsInMemory": 1000000
    }
  }
}
```

## NoSQL Databases

### MongoDB
```javascript
// MongoDB operations
// Insert documents
db.users.insertOne({
    name: "John Doe",
    email: "john@example.com",
    age: 30,
    tags: ["developer", "mongodb"]
});

db.users.insertMany([
    {name: "Jane Smith", email: "jane@example.com", age: 25},
    {name: "Bob Johnson", email: "bob@example.com", age: 35}
]);

// Query documents
db.users.find({age: {$gte: 25}});
db.users.find({tags: "developer"});
db.users.find({}, {name: 1, email: 1, _id: 0});

// Aggregation pipeline
db.users.aggregate([
    {$match: {age: {$gte: 25}}},
    {$group: {
        _id: "$department",
        avgAge: {$avg: "$age"},
        count: {$sum: 1}
    }},
    {$sort: {avgAge: -1}}
]);

// Index creation
db.users.createIndex({email: 1}, {unique: true});
db.users.createIndex({name: "text", description: "text"});
db.users.createIndex({location: "2dsphere"});

// Update documents
db.users.updateOne(
    {email: "john@example.com"},
    {$set: {age: 31}, $push: {tags: "senior"}}
);

db.users.updateMany(
    {age: {$lt: 30}},
    {$set: {category: "junior"}}
);
```

### Cassandra
```sql
-- Cassandra CQL
-- Create keyspace
CREATE KEYSPACE user_data 
WITH REPLICATION = {
    'class': 'SimpleStrategy',
    'replication_factor': 3
};

USE user_data;

-- Create table
CREATE TABLE user_events (
    user_id UUID,
    event_time TIMESTAMP,
    event_type TEXT,
    event_data MAP<TEXT, TEXT>,
    PRIMARY KEY (user_id, event_time)
) WITH CLUSTERING ORDER BY (event_time DESC);

-- Insert data
INSERT INTO user_events (user_id, event_time, event_type, event_data)
VALUES (uuid(), '2023-12-01 10:30:00', 'login', {'ip': '192.168.1.1', 'device': 'mobile'});

-- Query data
SELECT * FROM user_events 
WHERE user_id = 123e4567-e89b-12d3-a456-426614174000
  AND event_time >= '2023-12-01'
  AND event_time < '2023-12-02';

-- Create secondary index
CREATE INDEX ON user_events (event_type);

-- Materialized view
CREATE MATERIALIZED VIEW events_by_type AS
SELECT user_id, event_time, event_type, event_data
FROM user_events
WHERE event_type IS NOT NULL AND user_id IS NOT NULL AND event_time IS NOT NULL
PRIMARY KEY (event_type, event_time, user_id);
```

### Elasticsearch
```json
// Elasticsearch operations
// Create index with mapping
PUT /user_logs
{
  "mappings": {
    "properties": {
      "timestamp": {"type": "date"},
      "user_id": {"type": "keyword"},
      "message": {"type": "text"},
      "level": {"type": "keyword"},
      "source": {"type": "keyword"},
      "location": {"type": "geo_point"}
    }
  }
}

// Index document
POST /user_logs/_doc
{
  "timestamp": "2023-12-01T10:30:00Z",
  "user_id": "user123",
  "message": "User logged in successfully",
  "level": "INFO",
  "source": "auth-service",
  "location": {"lat": 40.7128, "lon": -74.0060}
}

// Search queries
GET /user_logs/_search
{
  "query": {
    "bool": {
      "must": [
        {"term": {"level": "ERROR"}},
        {"range": {"timestamp": {"gte": "2023-12-01", "lte": "2023-12-02"}}}
      ]
    }
  },
  "aggs": {
    "errors_by_source": {
      "terms": {"field": "source"}
    }
  }
}

// Full-text search
GET /user_logs/_search
{
  "query": {
    "match": {
      "message": "login failed"
    }
  },
  "highlight": {
    "fields": {
      "message": {}
    }
  }
}
```

## Cloud Platforms

### AWS Big Data Services
```bash
# AWS CLI commands for big data services

# S3 operations
aws s3 cp local_file.csv s3://my-bucket/data/
aws s3 sync ./local_folder s3://my-bucket/data/ --delete
aws s3 ls s3://my-bucket/data/ --recursive --human-readable

# EMR (Elastic MapReduce)
aws emr create-cluster \
    --name "MyCluster" \
    --release-label emr-6.4.0 \
    --instance-type m5.xlarge \
    --instance-count 3 \
    --applications Name=Spark Name=Hadoop \
    --ec2-attributes KeyName=my-key-pair \
    --use-default-roles

# Kinesis Data Streams
aws kinesis create-stream --stream-name my-stream --shard-count 2
aws kinesis put-record --stream-name my-stream --data "test data" --partition-key "key1"

# Glue (ETL service)
aws glue start-job-run --job-name my-etl-job

# Athena (Query service)
aws athena start-query-execution \
    --query-string "SELECT * FROM my_table LIMIT 10" \
    --result-configuration OutputLocation=s3://my-results-bucket/
```

### Google Cloud Platform
```bash
# GCP commands for big data

# BigQuery
bq query --use_legacy_sql=false '
SELECT 
    country,
    COUNT(*) as user_count
FROM `project.dataset.users`
GROUP BY country
ORDER BY user_count DESC
LIMIT 10'

# Dataflow (Apache Beam)
python -m apache_beam.examples.wordcount \
    --input gs://dataflow-samples/shakespeare/kinglear.txt \
    --output gs://my-bucket/results/outputs \
    --runner DataflowRunner \
    --project my-project \
    --region us-central1

# Cloud Storage
gsutil cp local_file.csv gs://my-bucket/data/
gsutil -m rsync -r ./local_folder gs://my-bucket/data/

# Pub/Sub
gcloud pubsub topics create my-topic
gcloud pubsub subscriptions create my-subscription --topic=my-topic
gcloud pubsub topics publish my-topic --message="Hello World"
```

### Azure Big Data Services
```bash
# Azure CLI commands

# Data Lake Storage
az storage blob upload --file local_file.csv --container-name data --name file.csv

# HDInsight
az hdinsight create \
    --name mycluster \
    --resource-group myresourcegroup \
    --type spark \
    --component-version Spark=2.4 \
    --http-user admin \
    --http-password mypassword \
    --ssh-user sshuser \
    --ssh-password mypassword

# Event Hubs
az eventhubs eventhub create --name my-eventhub --namespace-name my-namespace --resource-group myresourcegroup

# Stream Analytics
az stream-analytics job create \
    --resource-group myresourcegroup \
    --name my-stream-job \
    --location "West US 2"
```

## Data Pipeline Tools

### Apache NiFi
```xml
<!-- NiFi flow configuration -->
<template>
    <description>Data ingestion flow</description>
    <processors>
        <processor>
            <name>GetFile</name>
            <type>org.apache.nifi.processors.standard.GetFile</type>
            <properties>
                <property>
                    <name>Input Directory</name>
                    <value>/data/input</value>
                </property>
                <property>
                    <name>File Filter</name>
                    <value>.*\.csv</value>
                </property>
            </properties>
        </processor>
        
        <processor>
            <name>ConvertRecord</name>
            <type>org.apache.nifi.processors.standard.ConvertRecord</type>
            <properties>
                <property>
                    <name>Record Reader</name>
                    <value>CSVReader</value>
                </property>
                <property>
                    <name>Record Writer</name>
                    <value>JsonRecordSetWriter</value>
                </property>
            </properties>
        </processor>
        
        <processor>
            <name>PutHDFS</name>
            <type>org.apache.nifi.processors.hadoop.PutHDFS</type>
            <properties>
                <property>
                    <name>Hadoop Configuration Resources</name>
                    <value>/etc/hadoop/conf/core-site.xml,/etc/hadoop/conf/hdfs-site.xml</value>
                </property>
                <property>
                    <name>Directory</name>
                    <value>/data/processed</value>
                </property>
            </properties>
        </processor>
    </processors>
</template>
```

### Luigi Pipeline
```python
# Luigi data pipeline
import luigi
from luigi.contrib.hdfs import HdfsTarget
from luigi.contrib.spark import SparkSubmitTask

class DataIngestion(luigi.Task):
    date = luigi.DateParameter()
    
    def output(self):
        return HdfsTarget(f"/data/raw/{self.date}/data.csv")
    
    def run(self):
        # Data ingestion logic
        with self.output().open('w') as output_file:
            # Write data to HDFS
            pass

class DataTransformation(SparkSubmitTask):
    date = luigi.DateParameter()
    
    def requires(self):
        return DataIngestion(self.date)
    
    def output(self):
        return HdfsTarget(f"/data/processed/{self.date}/")
    
    @property
    def app(self):
        return "transform_data.py"
    
    @property
    def app_options(self):
        return [
            "--input", self.input().path,
            "--output", self.output().path
        ]

class DataAggregation(luigi.Task):
    date = luigi.DateParameter()
    
    def requires(self):
        return DataTransformation(self.date)
    
    def output(self):
        return HdfsTarget(f"/data/aggregated/{self.date}/")
    
    def run(self):
        # Aggregation logic
        pass

if __name__ == '__main__':
    luigi.run()
```

## Monitoring & Management

### Cluster Monitoring
```bash
# Hadoop cluster monitoring
# YARN Resource Manager UI: http://resourcemanager:8088
# HDFS NameNode UI: http://namenode:9870
# Spark History Server: http://sparkhistory:18080

# Command line monitoring
yarn top                           # Top applications
hdfs dfsadmin -report             # HDFS status
mapred job -list                  # MapReduce jobs

# Spark monitoring
spark-submit \
    --conf spark.eventLog.enabled=true \
    --conf spark.eventLog.dir=hdfs://namenode:9000/spark-logs \
    --conf spark.sql.adaptive.enabled=true \
    my_app.py
```

### Performance Tuning
```python
# Spark performance tuning
spark.conf.set("spark.sql.adaptive.enabled", "true")
spark.conf.set("spark.sql.adaptive.coalescePartitions.enabled", "true")
spark.conf.set("spark.sql.adaptive.skewJoin.enabled", "true")
spark.conf.set("spark.sql.adaptive.localShuffleReader.enabled", "true")

# Memory tuning
spark.conf.set("spark.executor.memory", "4g")
spark.conf.set("spark.executor.memoryFraction", "0.8")
spark.conf.set("spark.sql.shuffle.partitions", "200")

# Serialization
spark.conf.set("spark.serializer", "org.apache.spark.serializer.KryoSerializer")
spark.conf.set("spark.kryo.registrationRequired", "false")

# Caching strategies
# Cache frequently accessed data
df.cache()
df.persist(StorageLevel.MEMORY_AND_DISK_SER)

# Unpersist when no longer needed
df.unpersist()
```

### Data Quality Monitoring
```python
# Great Expectations for data quality
import great_expectations as ge

# Create expectation suite
df_ge = ge.from_pandas(df)

# Define expectations
df_ge.expect_column_to_exist("user_id")
df_ge.expect_column_values_to_not_be_null("user_id")
df_ge.expect_column_values_to_be_unique("user_id")
df_ge.expect_column_values_to_be_between("age", min_value=0, max_value=120)
df_ge.expect_column_values_to_match_regex("email", r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")

# Validate data
validation_result = df_ge.validate()

# Custom data quality checks
def check_data_quality(df):
    """Custom data quality checks"""
    issues = []
    
    # Check for duplicates
    duplicate_count = df.count() - df.dropDuplicates().count()
    if duplicate_count > 0:
        issues.append(f"Found {duplicate_count} duplicate records")
    
    # Check for null values in critical columns
    critical_columns = ["user_id", "timestamp", "event_type"]
    for col in critical_columns:
        null_count = df.filter(df[col].isNull()).count()
        if null_count > 0:
            issues.append(f"Found {null_count} null values in {col}")
    
    # Check data freshness
    from pyspark.sql.functions import max as spark_max, current_timestamp, datediff
    max_timestamp = df.select(spark_max("timestamp")).collect()[0][0]
    days_old = df.select(datediff(current_timestamp(), lit(max_timestamp))).collect()[0][0]
    if days_old > 1:
        issues.append(f"Data is {days_old} days old")
    
    return issues
```

## Best Practices

### Data Architecture Principles
```
1. Scalability
   - Design for horizontal scaling
   - Use distributed systems
   - Plan for data growth

2. Reliability
   - Implement fault tolerance
   - Use replication
   - Plan for disaster recovery

3. Performance
   - Optimize data formats
   - Use appropriate partitioning
   - Implement caching strategies

4. Security
   - Encrypt data at rest and in transit
   - Implement access controls
   - Audit data access

5. Cost Optimization
   - Use appropriate storage tiers
   - Optimize compute resources
   - Monitor and control costs
```

### Data Pipeline Best Practices
```python
# 1. Idempotent operations
def process_data_idempotent(input_path, output_path, date):
    """Ensure operations can be safely retried"""
    temp_path = f"{output_path}_temp_{date}"
    
    try:
        # Process data to temporary location
        df = spark.read.parquet(input_path)
        processed_df = transform_data(df)
        processed_df.write.mode("overwrite").parquet(temp_path)
        
        # Atomic move to final location
        spark.sql(f"DROP TABLE IF EXISTS temp_table")
        spark.sql(f"CREATE TABLE temp_table USING PARQUET LOCATION '{temp_path}'")
        spark.sql(f"CREATE OR REPLACE TABLE final_table USING PARQUET LOCATION '{output_path}' AS SELECT * FROM temp_table")
        
    except Exception as e:
        # Cleanup on failure
        spark.sql(f"DROP TABLE IF EXISTS temp_table")
        raise e

# 2. Data validation
def validate_data_schema(df, expected_schema):
    """Validate data schema before processing"""
    actual_schema = df.schema
    
    if actual_schema != expected_schema:
        raise ValueError(f"Schema mismatch. Expected: {expected_schema}, Actual: {actual_schema}")
    
    return True

# 3. Error handling and logging
import logging

def robust_data_processing(input_path, output_path):
    """Robust data processing with error handling"""
    logger = logging.getLogger(__name__)
    
    try:
        logger.info(f"Starting data processing: {input_path} -> {output_path}")
        
        # Validate input
        if not spark.catalog.tableExists(input_path):
            raise FileNotFoundError(f"Input table not found: {input_path}")
        
        # Process data
        df = spark.read.table(input_path)
        validate_data_schema(df, expected_schema)
        
        processed_df = transform_data(df)
        
        # Validate output
        if processed_df.count() == 0:
            raise ValueError("Processed data is empty")
        
        # Write output
        processed_df.write.mode("overwrite").saveAsTable(output_path)
        
        logger.info(f"Successfully processed {processed_df.count()} records")
        
    except Exception as e:
        logger.error(f"Data processing failed: {str(e)}")
        # Send alert
        send_alert(f"Data pipeline failed: {str(e)}")
        raise

# 4. Configuration management
import configparser

def load_config(config_file):
    """Load configuration from file"""
    config = configparser.ConfigParser()
    config.read(config_file)
    
    return {
        'input_path': config.get('paths', 'input'),
        'output_path': config.get('paths', 'output'),
        'batch_size': config.getint('processing', 'batch_size'),
        'max_retries': config.getint('processing', 'max_retries')
    }

# 5. Testing data pipelines
import unittest
from pyspark.sql import SparkSession

class TestDataPipeline(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.spark = SparkSession.builder.appName("test").getOrCreate()
    
    def test_data_transformation(self):
        # Create test data
        test_data = [("user1", 25), ("user2", 30)]
        test_df = self.spark.createDataFrame(test_data, ["user_id", "age"])
        
        # Apply transformation
        result_df = transform_data(test_df)
        
        # Assert results
        self.assertEqual(result_df.count(), 2)
        self.assertIn("age_category", result_df.columns)
    
    @classmethod
    def tearDownClass(cls):
        cls.spark.stop()
```

### Security Best Practices
```bash
# 1. Kerberos authentication
kinit -kt /path/to/keytab user@REALM

# 2. HDFS permissions
hdfs dfs -chmod 750 /secure/data
hdfs dfs -chown user:group /secure/data

# 3. Encryption
# Enable HDFS encryption
hadoop key create mykey -size 256
hdfs crypto -createZone -keyName mykey -path /encrypted

# 4. Network security
# Configure SSL/TLS for Hadoop services
# Use VPNs for remote access
# Implement firewall rules

# 5. Data masking
def mask_sensitive_data(df):
    """Mask sensitive columns"""
    from pyspark.sql.functions import regexp_replace, sha2
    
    return df.withColumn(
        "email_masked",
        regexp_replace("email", r"(.{2}).*(@.*)", r"$1***$2")
    ).withColumn(
        "ssn_hashed",
        sha2("ssn", 256)
    ).drop("email", "ssn")
```

This comprehensive Big Data cheatsheet covers all major technologies, frameworks, and best practices used in modern big data environments. Each section includes practical examples and real-world implementation patterns that you can use in production systems.