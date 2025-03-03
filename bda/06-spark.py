""""
gedit big.txt
start-all.sh
jps 
    [localhost:9870, utilities, upload]
spark-shell

var linesRDD = sc.textFile("hdfs://localhost:54310/big.txt")

var wordsRDD = linesRDD.flatMap(_.split(" ")) 

var wordskvrdd = wordsRDD.map((_, 1))

var wordCount = wordskvrdd.reduceByKey(_ + _)   

wordCount.saveAsTextFile("hdfs://localhost:54310/output")

"""