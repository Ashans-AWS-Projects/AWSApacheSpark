# Apache Spark Data Processing Project

## Overview

This project demonstrates the use of Apache Spark for large-scale data processing on an Amazon EMR cluster. We performed two primary tasks:
1. **Word Count**: Counting the number of words in "The Adventures of Sherlock Holmes" by Arthur Conan Doyle.
2. **Character Occurrences**: Counting the occurrences of each character in the same text.

## Table of Contents

- [Introduction](#introduction)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [Tasks Overview](#tasks-overview)
- [Results](#results)
- [Contributors](#contributors)
- [License](#license)

## Introduction

Apache Spark is a powerful framework designed for processing large datasets efficiently. This project utilizes Spark to handle text processing tasks, showcasing its capabilities in distributed computing and data analysis.

## Technologies Used

- **Apache Spark**: For distributed data processing.
- **Amazon EMR**: To create and manage a scalable Spark cluster.
- **Python**: Scripting language for the tasks.
- **AWS**: Infrastructure for running the Spark cluster.
- **Git**: Version control for managing project files.

## Setup and Installation

To run this project locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/spark-data-processing.git
    cd spark-data-processing
    ```

2. **Setup the EMR Cluster**:
   - Navigate to the AWS Console.
   - Create a new EMR cluster with Spark.
   - SSH into the cluster.

3. **Transfer Files to EMR**:
   - Copy the `book.txt` and `wordcount.py` files to the EMR cluster using SCP.
   - Place the dataset in HDFS as Spark reads data from there.

4. **Run the Spark Jobs**:
   - Execute the Python scripts via Spark-submit:
     ```bash
     spark-submit wordcount.py
     spark-submit characteroccurences.py
     ```

## Tasks Overview

### Task 1: Word Count
This task involves counting the number of words in the text. The Python script `wordcount.py` reads the text file and outputs the total word count.

### Task 2: Character Occurrences
In this task, the `characteroccurences.py` script counts the occurrences of each character in the text, providing insights into the frequency of different characters.

## Results

- **Word Count**: 15,212 words in "The Adventures of Sherlock Holmes".
- **Character Occurrences**: Detailed count of each character is provided in the `results.txt` file. For example:
  - Space (`' '`): 97,626 occurrences
  - Letter `e`: 54,581 occurrences

The complete results are available in the `results.txt` file.

## Contributors

- **Ryan Britton**
- **Ashan Deen**


