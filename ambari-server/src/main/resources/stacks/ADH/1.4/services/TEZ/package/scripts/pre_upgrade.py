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

from resource_management.libraries.script import Script
from resource_management.libraries.functions.version import compare_versions
from resource_management.libraries.functions.copy_tarball import copy_to_hdfs
from resource_management.core.exceptions import Fail

from resource_management.core.logger import Logger

class TezPreUpgrade(Script):

  def prepare(self, env):
    """
    During the "Upgrade" direction of a Stack Upgrade, it is necessary to ensure that the older tez tarball
    has been copied to HDFS. This is an additional check for added robustness.
    """
    import params
    env.set_params(params)


if __name__ == "__main__":
  TezPreUpgrade().execute()

