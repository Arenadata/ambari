#!/usr/bin/env python
from resource_management import *
from resource_management.libraries.script.script import Script
import sys, os, glob
from resource_management.libraries.functions.default import default

   
# server configurations
config = Script.get_config()

    
# params from flink-ambari-config
flink_install_dir = config['configurations']['flink-ambari-config']['flink_install_dir']
flink_appname = config['configurations']['flink-ambari-config']['flink_appname']

hadoop_conf_dir = config['configurations']['flink-ambari-config']['hadoop_conf_dir']
 
conf_dir = ''
bin_dir = flink_install_dir + '/bin'

java_home = config['hostLevelParams']['java_home']

# params from flink-conf.yaml
flink_yaml_content = config['configurations']['flink-env']['content']
flink_user = config['configurations']['flink-env']['flink_user']
flink_group = config['configurations']['flink-env']['flink_group']
flink_log_dir = config['configurations']['flink-env']['flink_log_dir']
flink_pid_dir = config['configurations']['flink-env']['flink_pid_dir']
flink_log_file = flink_log_dir + '/flink-start.log'

temp_file='/tmp/flink.tgz'
