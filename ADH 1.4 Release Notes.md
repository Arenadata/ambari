# Arenadata Hadoop 1.4

Arenadata Hadoop (Универсальная платформа данных) -  это интегрированный набор компонентов корпоративного уровня на базе решений с открытым исходным кодом. Платформа включает в себя все необходимые компоненты для управления данными, доступа к данным, анализа данных, интеграции, безопасности и администрирования.

ADH 1.4 Release Notes
Оффициальные версия продуктов Apache в ADH 1.4
Все компоненты ADH 1.4, представленные в данном документе, являются наиболее стабильными версиями официальных релизов продуктов Apache Software Foundation. Arenadata оставляет за собой лишь право добавления необхоимых изменений и патчей для обеспечения стабильного функционирования компонентов и их интеграции.

**Состав и версии компонентов ADH 1.4:**
- Apache Ambari 2.2.1
- Apache HDFS	2.7.3
- Apache YARN	2.7.3
- Apache MapReduce	2.7.3
- Apache Zookeeper	3.4.6
- Apache Tez	0.7.1
- Apache Hive	1.2.1
- Apache HBase	1.1.3
- Apache Phoenix	4.9.0
- Apache Pig	0.15.0
- Apache Sqoop	1.4.6
- Apache Flume	1.7.0
- Apache Oozie	4.3.0
- Apache Atlas	0.7.1
- Apache NiFi   1.1.2
- Apache Apex 	3.5.0
- Apache Flink	1.1.3
- Apache Kafka	0.10.1
- Apache Knox	0.12.0
- Apache Mahout	0.12.2
- Apache Ranger	0.7.0
- Apache Ranger KMS	0.7.0
- Apache Solr	6.6.0
- Apache Spark	2.1.0
- Apache Zeppelin 	0.7.0
- Apache Giraph	1.1.0
- Apache Kite	1.1.0

**Дополнительные компоненты включенные в состав дистрибутива:**
- Hue	3.11.0
- Bigtop-groovy 2.4.10
- Bigtop-jsvc   1.10.15
- Bigtop-tomcat 6.0.45
- Bigtop-utils  1.2.0
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

**Перечень новых функциональностей и известных проблем:**

- Apache HDFS, Apache YARN, Apache MR2: https://hadoop.apache.org/docs/r2.7.3/hadoop-project-dist/hadoop-common/releasenotes.html
- Apache Zookeeper: https://zookeeper.apache.org/doc/r3.4.6/releasenotes.html
- Apache Tez: https://tez.apache.org/releases/0.7.1/release-notes.txt
- Apache Hive: https://issues.apache.org/jira/secure/ReleaseNote.jspa?version=12332384&styleName=Html&projectId=12310843&Create=Create&atl_token=A5KQ-2QAV-T4JA-FDED%7C548094b8f7501729191fb1f6879ba84afc0b1241%7Clout
- Apache HBase: https://issues.apache.org/jira/secure/ReleaseNote.jspa?projectId=12310753&version=12333152
- Apache Phoenix: https://phoenix.apache.org/release_notes.html
- Apache Pig: http://svn.apache.org/repos/asf/pig/branches/branch-0.15/RELEASE_NOTES.txt
- Apache Sqoop: https://sqoop.apache.org/docs/1.4.6/sqoop-1.4.6.releasenotes.html
- Apache Flume: https://flume.apache.org/releases/1.7.0.html
- Apache Oozie: https://oozie.apache.org/docs/4.3.0/release-log.txt
- Apache Atlas: https://git-wip-us.apache.org/repos/asf?p=incubator-atlas.git;a=blob;f=release-log.txt;hb=refs/tags/release-0.7.1-rc3
- Apache Flink: https://flink.apache.org/news/2016/10/12/release-1.1.3.html
- Apache Kafka: https://archive.apache.org/dist/kafka/0.10.1.0/RELEASE_NOTES.html
- Apache Mahout: http://mahout.apache.org/release-notes/Apache-Mahout-0.13.0-Release-Notes.pdf
- Apache Ranger: https://cwiki.apache.org/confluence/display/RANGER/Apache+Ranger+0.7.0+-+Release+Notes
- Apache Solr: https://lucene.apache.org/solr/6_6_0/changes/Changes.html
- Apache Spark: https://spark.apache.org/releases/spark-release-2-1-0.html
- Apache Zeppelin: https://zeppelin.apache.org/releases/zeppelin-release-0.7.0.html
- Apache Giraph: https://issues.apache.org/jira/secure/ReleaseNote.jspa?version=12324313&styleName=Html&projectId=12311820&Create=Create&atl_token=A5KQ-2QAV-T4JA-FDED%7Cf550d76dc7661f3664292f8b2cb901e6acc554dd%7Clin
- Apache Kite: http://kitesdk.org/docs/1.1.0/release-notes.html
- Hue: https://github.com/cloudera/hue/blob/master/docs/release-notes/release-notes-3.11.0.txt

**Известные проблемы:**
- Apache Oozie: В некоторых случаях возможно возникновение ошибки при проверке сервиса (Service Check) Oozie в Ambari. https://jira.arenadata.io/browse/ADH-76

- Apache Atlas: Некорректно осуществляется запуск сервиса при комманде Start All Services, требуется запуск сервиса после старта всех остальных процессов. https://jira.arenadata.io/browse/ADH-82
