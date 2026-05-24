# 🐘 Big Data Engineering — NTI Internship (HCIA Track)

> Hands-on labs and projects completed during the **National Telecommunication Institute (NTI)** Big Data internship program, following the **Huawei HCIA Big Data** curriculum.

---

## 🧰 Tech Stack & Tools

### Core Ecosystem
![Hadoop](https://img.shields.io/badge/Apache%20Hadoop-66CCFF?style=for-the-badge&logo=apachehadoop&logoColor=black)
![HDFS](https://img.shields.io/badge/HDFS-005C84?style=for-the-badge&logo=apache&logoColor=white)
![YARN](https://img.shields.io/badge/Apache%20YARN-F5A623?style=for-the-badge&logo=apache&logoColor=white)
![MapReduce](https://img.shields.io/badge/MapReduce-FF6B35?style=for-the-badge&logo=apache&logoColor=white)

### Data Processing & Analytics
![Apache Spark](https://img.shields.io/badge/Apache%20Spark-E25A1C?style=for-the-badge&logo=apachespark&logoColor=white)
![Apache Hive](https://img.shields.io/badge/Apache%20Hive-FDEE21?style=for-the-badge&logo=apachehive&logoColor=black)
![HBase](https://img.shields.io/badge/Apache%20HBase-D22128?style=for-the-badge&logo=apache&logoColor=white)

### Data Ingestion & Streaming
![Apache Kafka](https://img.shields.io/badge/Apache%20Kafka-231F20?style=for-the-badge&logo=apachekafka&logoColor=white)
![Apache Flume](https://img.shields.io/badge/Apache%20Flume-5B4E94?style=for-the-badge&logo=apache&logoColor=white)

### Infrastructure & Containers
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)

### Languages & Tools
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)
![Bash](https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)

### GUI Tools
![HDFS GUI](https://img.shields.io/badge/HDFSExplorer%20GUI-005C84?style=for-the-badge&logo=apachehadoop&logoColor=white)

---

## 📁 Repository Structure

```
big-data-nti-internship/
│
├── map_reduce_labs/
│   ├── shakespeare/              # Shakespeare word frequency
│   │   ├── mapper.py
│   │   └── reducer.py
│   ├── apache_log/     # IP address frequency from Apache logs
│   │   ├── mapper.py
│   │   └── reducer.py
│   └── china_city_scores/       # Mean & Std Dev of city scores
│       ├── mapper.py
│       └── reducer.py
│
├── hbase_labs/                       # HBase labs (coming soon)
│
├── spark/                       # (Coming soon)
├── hive/                        # (Coming soon)
├── kafka/                       # (Coming soon)
├── flume/                       # (Coming soon)
├── docker/                      # (Coming soon)
│
└── README.md
```

---

## ✅ Completed Labs

### 📦 1. MapReduce

MapReduce jobs written in Python using Hadoop Streaming, running on HDFS via YARN.

---

#### 🏙️ China City Score Analysis

**Goal:** Parse a dataset of Chinese cities and their scores, then compute the **count, mean, and standard deviation** per city — ranked by mean score descending.

**Input format:** `score***city_name` (delimiter: `***`)

**Pipeline:**
- **Mapper** → emits `city \t score`
- **Reducer** → aggregates per-city scores, computes statistics, ranks results

**Sample Output:**
```
1    Beijing    COUNT=120    MEAN=88.45    STD_DEV=4.21
2    Shanghai   COUNT=98     MEAN=85.10    STD_DEV=5.67
...
```

📂 [`mapreduce/china_city_scores/`](./mapreduce/china_city_scores/)

---

#### 🌐 Apache Log IP Frequency

**Goal:** Parse Apache access logs and count the **frequency of each IP address** to identify traffic patterns.

**Input format:** Standard Apache Combined Log Format

**Pipeline:**
- **Mapper** → extracts the IP field and emits `ip \t 1`
- **Reducer** → sums counts per IP using streaming aggregation

**Sample Output:**
```
192.168.1.1    342
10.0.0.5       215
...
```

📂 [`mapreduce/apache_log_analysis/`](./mapreduce/apache_log_analysis/)

---

#### 📖 Shakespeare Word Count

**Goal:** Classic word frequency count across Shakespeare's novels — a foundational MapReduce benchmark.

**Pipeline:**
- **Mapper** → tokenizes each line and emits `word \t 1`
- **Reducer** → aggregates counts and outputs results sorted lexicographically

**Sample Output:**
```
and      27534
the      22538
to       19667
...
```

📂 [`mapreduce/word_count/`](./mapreduce/word_count/)

---

### 🗄️ 2. HBase

HBase NoSQL database labs — schema design, shell commands, Java/Python API operations.

📂 [`hbase/`](./hbase/) *(more details coming soon)*

---

## 🖥️ GUI Tools Used

### HDFS Explorer + YARN Manager (GUI App)

A graphical interface used throughout the labs for:
- **Browsing and managing HDFS** — uploading input files, viewing output directories, downloading results
- **Starting and monitoring YARN** — launching ResourceManager and NodeManager, tracking job progress via the YARN Web UI
- Inspecting job logs and application history without needing to use the CLI for every operation

This tool significantly speeds up the file management workflow when running iterative MapReduce jobs.

---

## 🚀 How to Run a MapReduce Job

> Prerequisites: Hadoop installed and configured, YARN running, Python 3 available.

```bash
# 1. Upload input file to HDFS
hdfs dfs -put input.txt /user/hadoop/input/

# 2. Run the job using Hadoop Streaming
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  -input /user/hadoop/input/ \
  -output /user/hadoop/output/ \
  -mapper mapper.py \
  -reducer reducer.py \
  -file mapper.py \
  -file reducer.py

# 3. View the results
hdfs dfs -cat /user/hadoop/output/part-00000
```

---

## 🗺️ Roadmap

| Tool | Status |
|---|---|
| MapReduce | ✅ Complete |
| HBase | ✅ Complete |
| Apache Spark | 🔄 Coming Soon |
| Apache Hive | 🔄 Coming Soon |
| Apache Kafka | 🔄 Coming Soon |
| Apache Flume | 🔄 Coming Soon |
| Docker (Hadoop Cluster) | 🔄 Coming Soon |

---

## 🎓 About

**Program:** Huawei HCIA Big Data — NTI (National Telecommunication Institute) Internship  
**Focus:** Distributed storage, batch processing, real-time streaming, and NoSQL databases on the Hadoop ecosystem  
**Language:** Python (Hadoop Streaming), with Java and SQL used in upcoming modules