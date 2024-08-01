import sys
from operator import add

from pyspark.sql import SparkSession


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: characteroccurences <file>", file=sys.stderr)
        sys.exit(-1)

    spark = SparkSession\
        .builder\
        .appName("PythonWordCount")\
        .getOrCreate()

    lines = spark.read.text(sys.argv[1]).rdd.map(lambda r: r[0])
    counts = lines.flatMap(lambda s: [c for c in s]) \
                  .map(lambda c: (c, 1)) \
                  .reduceByKey(add)
    
    output = counts.collect()
    output.sort(key=lambda x: x[0])

    with open("results.txt", "w") as f:
        for (c, count) in output:
            f.write("Character: '{}', Count: {}\n".format(c, count))

    spark.stop()
