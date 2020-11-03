# Arenadata Hadoop 1.6.1

Arenadata Hadoop (Универсальная платформа данных) -  это интегрированный набор компонентов корпоративного уровня на базе решений с открытым исходным кодом. Платформа включает в себя все необходимые компоненты для управления данными, доступа к данным, анализа данных, интеграции, безопасности и администрирования.

ADH 1.6.1 Release Notes
Оффициальные версия продуктов Apache в ADH 1.6.1
Все компоненты ADH 1.6.1, представленные в данном документе, являются наиболее стабильными версиями официальных релизов продуктов Apache Software Foundation. Arenadata оставляет за собой лишь право добавления необхоимых изменений и патчей для обеспечения стабильного функционирования компонентов и их интеграции.

**Состав и версии компонентов ADH 1.6.1:**
- Apache Ambari 2.6.3
- Apache Ambari Log Search	0.5.0	
- Apache Ambari Infra	0.1.0	
- Apache HDFS	2.8.5
- Apache YARN	2.8.5
- Apache MapReduce2	2.8.5
- Apache Tez	0.9.1
- Apache Hive	2.3.3
- Apache HBase	1.3.5
- Apache Phoenix 4.14.0
- Apache Pig	0.17.0
- Apache Sqoop	1.4.7
- Apache Oozie	4.3.1
- Apache ZooKeeper	3.4.12
- Apache Flume	1.8.0
- Apache Atlas	0.8.2
- Apache Kafka	1.0.2
- Apache Knox	0.14.0
- Apache Ranger	0.7.1
- Apache Ranger KMS	0.7.1
- Apache Spark2	2.3.1
- Apache Zeppelin Notebook	0.8.0
- Apache Flink	1.6.1
- Apache Giraph	1.1.0
- Apache Mahout	0.13.0
- Apache NiFi	1.6.0
- Apache Slider	0.92.0
- Apache Solr	7.3.1
- Kafka Manager	1.1.2


**Дополнительные компоненты включенные в состав дистрибутива:**
- Bigtop-groovy 2.4.10
- Bigtop-jsvc   1.10.15
- Bigtop-tomcat 6.0.45
- Bigtop-utils  1.3.0
- extjs 2.2
- fping 3.10
- grafana 4.3.1
- libconfuse  2.7
- lzo 2.06
- lzo-devel 2.06
- lzo-minilzo 2.06
- mysql-connector-java  5.1.25
- net-tools 2.0
- numactl-libs  2.0.9
- pdsh 2.3.1
- perl-Crypt-DES 2.05
- perl-Net-SNMP 6.0.1
- rrdtool 1.4.8
- rrdtool-devel 1.4.8
- snappy 1.1.0
- snappy-devel 1.1.0

**Перечень новых функциональностей:**

+ `Apache HDFS, Apache YARN, Apache MR2` https://hadoop.apache.org/docs/r2.8.5/hadoop-project-dist/hadoop-common/release/2.8.5/RELEASENOTES.2.8.5.html

+ `Apache Zookeeper`https://zookeeper.apache.org/doc/r3.4.12/releasenotes.html

+ `Apache Tez` https://tez.apache.org/releases/0.9.1/release-notes.txt>

+ `Apache Hive` https://issues.apache.org/jira/secure/ReleaseNote.jspa?projectId=12310843&version=12342162

+ `Apache HBase` https://issues.apache.org/jira/secure/ReleaseNote.jspa?version=12343936&styleName=Html&projectId=12310753&Create=Create&atl_token=A5KQ-2QAV-T4JA-FDED%7C532fd2f5c68ef9cc47051e23daa7ec51514ea695%7Clin

+ `Apache Phoenix` https://issues.apache.org/jira/secure/ReleaseNote.jspa?version=12342145&styleName=&projectId=12315120&Create=Create&atl_token=A5KQ-2QAV-T4JA-FDED%7C532fd2f5c68ef9cc47051e23daa7ec51514ea695%7Clin

+ `Apache Pig` http://svn.apache.org/repos/asf/pig/branches/branch-0.17/RELEASE_NOTES.txt

+ `Apache Sqoop` https://sqoop.apache.org/docs/1.4.7/sqoop-1.4.7.releasenotes.html

+ `Apache Flume` https://flume.apache.org/releases/1.8.0.html

+ `Apache Oozie` https://oozie.apache.org/docs/4.3.1/release-log.txt

+ `Apache Atlas` https://git-wip-us.apache.org/repos/asf?p=atlas.git;a=blob;f=release-log.txt;hb=refs/tags/release-0.8.1-rc1

+ `Apache Flink` https://flink.apache.org/news/2018/09/20/release-1.6.1.html

+ `Apache Kafka` https://archive.apache.org/dist/kafka/1.0.2/RELEASE_NOTES.html

+ `Apache Mahout` http://mahout.apache.org/release-notes/Apache-Mahout-0.13.0-Release-Notes.pdf

+ `Apache Ranger` https://cwiki.apache.org/confluence/display/RANGER/Apache+Ranger+0.7.1+-+Release+Notes

+ `Apache Solr` https://lucene.apache.org/solr/7_3_0/changes/Changes.html

+ `Apache Spark` https://spark.apache.org/releases/spark-release-2-3-1.html

+ `Apache Zeppelin` https://zeppelin.apache.org/releases/zeppelin-release-0.8.0.html

+ `Apache Giraph` https://issues.apache.org/jira/secure/ReleaseNote.jspa?version=12324313&styleName=Html&projectId=12311820&Create=Create&atl_token=A5KQ-2QAV-T4JA-FDED%7Cf550d76dc7661f3664292f8b2cb901e6acc554dd%7Cli

**Известные проблемы:**

*Apache Oozie:*
- Возможно возникновение ошибки при проверке сервиса (Service Check) из-за недостатка ресурсов, возникает как правило при установке множества сервисов на одном узле;
