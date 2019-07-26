"""
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Ambari Agent

"""

from resource_management import *

class GiraphServiceCheck(Script):
  def service_check(self, env):
    import params
    env.set_params(params)

    giraph_command = format("/usr/lib/giraph/bin/giraph /usr/lib/giraph/giraph-gora.jar -la")
    

    Execute( giraph_command,
             tries = 3,
             try_sleep = 5,
             environment={'HADOOP_HOME': params.hadoop_home,'HADOOP_CONF_DIR': params.hadoop_conf_dir,'JAVA_HOME': params.java64_home},
             path = format('/usr/sbin:/sbin:/usr/local/bin:/bin:/usr/bin'),
             user = params.smokeuser
    )

if __name__ == "__main__":
  GiraphServiceCheck().execute()


