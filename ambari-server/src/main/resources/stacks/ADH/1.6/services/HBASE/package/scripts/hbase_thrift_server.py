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
"""

from resource_management.libraries.functions import conf_select, check_process_status, format
from resource_management.libraries.script import Script
from hbase_thrift import hbase_thrift_server
from hbase import hbase

class HBaseThriftServer(Script):

  def configure(self, env):
    import params
    env.set_params(params)
    hbase(name='hbasethriftserver')


  def start(self, env, upgrade_type=None):
    import params
    env.set_params(params)
    self.configure(env)
    hbase_thrift_server('start')


  def stop(self, env, upgrade_type=None):
    import params
    env.set_params(params)
    hbase_thrift_server('stop')


  def pre_upgrade_restart(self, env, upgrade_type=None):
    import params
    env.set_params(params)


  def status(self, env):
    import status_params
    env.set_params(status_params)
    pid_file = format("{pid_dir}/hbase-{hbase_user}-thrift.pid")
    check_process_status(pid_file)

  def security_status(self, env):
    check_process_status(status_params.spark_thrift_server_pid_file)
    self.put_structured_out({"securityState": "UNSECURED"})

if __name__ == "__main__":
  HBaseThriftServer().execute()
