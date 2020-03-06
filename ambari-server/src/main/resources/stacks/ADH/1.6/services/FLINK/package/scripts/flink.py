#!/usr/bin/env python

import sys, os, pwd, grp, signal, time, glob
from resource_management.libraries.functions.check_process_status import check_process_status
from resource_management.core.resources.system import Execute
from resource_management import *
from subprocess import call

class Master(Script):

  def get_component_name(self):
    return "flink"

  def get_env(self):
    import params
    return {'JAVA_HOME': params.java_home, 'FLINK_PID_DIR': params.flink_pid_dir}

  def install(self, env):
    import params
    import status_params

    env.set_params(params)
    env.set_params(status_params)
    self.install_packages(env)
    Execute(('ln','-sf', format('/usr/lib/hadoop-yarn/lib/jersey-client-1.9.jar'),'/usr/lib/flink/lib/jersey-client.jar'),
      not_if=format("ls /usr/lib/flink/lib/jersey-client.jar"),
      only_if=format("ls /usr/lib/hadoop-yarn/lib/jersey-client-1.9.jar"),
      sudo=True)
    Execute(('ln','-sf', format('/usr/lib/hadoop-yarn/lib/jersey-server-1.9.jar'),'/usr/lib/flink/lib/jersey-server.jar'),
      not_if=format("ls /usr/lib/flink/lib/jersey-server.jar"),
      only_if=format("ls /usr/lib/hadoop-yarn/lib/jersey-server-1.9.jar"),
      sudo=True)
    Execute(('ln','-sf', format(' /usr/lib/hadoop-yarn/lib/jersey-core-1.9.jar'),'/usr/lib/flink/lib/jersey-core.jar'),
      not_if=format("ls /usr/lib/flink/lib/jersey-core.jar"),
      only_if=format("ls  /usr/lib/hadoop-yarn/lib/jersey-core-1.9.jar"),
      sudo=True)
    Execute(('ln','-sf', format('/usr/lib/hadoop-yarn/lib/jersey-guice-1.9.jar'),'/usr/lib/flink/lib/jersey-guice.jar'),
      not_if=format("ls /usr/lib/flink/lib/jersey-guice.jar"),
      only_if=format("ls /usr/lib/hadoop-yarn/lib/jersey-guice-1.9.jar"),
      sudo=True)
    Execute(('ln','-sf', format('/usr/lib/hadoop-yarn/lib/jersey-json-1.9.jar'),'/usr/lib/flink/lib/jersey-json.jar'),
      not_if=format("ls /usr/lib/flink/lib/jersey-json.jar"),
      only_if=format("ls /usr/lib/hadoop-yarn/lib/jersey-json-1.9.jar"),
      sudo=True)


    Directory([status_params.flink_pid_dir, params.flink_log_dir],
            create_parents=True,
            mode=0755,
            owner=params.flink_user,
            group=params.flink_group
    )

    File(params.flink_log_file,
            mode=0644,
            owner=params.flink_user,
            group=params.flink_group,
            content=''
    )

  def configure(self, env, isInstall=False):
    import params
    import status_params
    env.set_params(params)
    env.set_params(status_params)

    self.create_hdfs_user(params.flink_user)
    self.config_ssh(params.flink_user)

    #write out config
    properties_content=InlineTemplate(params.flink_yaml_content)
    File(format("{conf_dir}/flink-conf.yaml"), content=properties_content, owner=params.flink_user)
    Execute(('ln','-sf', format('{flink_log_dir}'),format('{flink_install_dir}/log')),
      not_if=format("ls {flink_install_dir}"),
      only_if=format("ls {flink_log_dir}""),
      sudo=True)

  def config_ssh(self, flink_user):
    if not os.path.exists(format("{flink_home_dir}/.ssh/id_rsa")):
      cmd1 = format("ssh-keygen -f {flink_home_dir}/.ssh/id_rsa -t rsa -N \"\"")
      Execute(cmd1, user=flink_user)
      cmd2 = format("cat {flink_home_dir}/.ssh/id_rsa.pub >> {flink_home_dir}/.ssh/authorized_keys")
      Execute(cmd2, user=flink_user)
      cmd3 = format("echo -e \"Host localhost\n  StrictHostKeyChecking no\" > {flink_home_dir}/.ssh/config")
      Execute(cmd3, user=flink_user)

  def stop(self, env):
    import params
    import status_params
    cmd = format("{params.bin_dir}/jobmanager.sh stop")
    Execute (cmd, user=params.flink_user, environment=self.get_env())
    File(status_params.flink_pid_file,
      action = "delete",
      owner = params.flink_user
    )

  def start(self, env):
    import params
    import status_params

    env.set_params(params)
    env.set_params(status_params)

    self.configure(env, True)

    cmd = format("{params.bin_dir}/jobmanager.sh start >> {params.flink_log_file}")
    #cmd = "env >/tmp/1.log"
    Execute (cmd, user=params.flink_user, environment=self.get_env())

    if os.path.exists(params.temp_file):
      os.remove(params.temp_file)

  def status(self, env):
    import status_params
    check_process_status(status_params.flink_pid_file)

  def create_hdfs_user(self, user):
    Execute('hadoop fs -mkdir -p /user/'+user, user='hdfs', ignore_failures=True)
    Execute('hadoop fs -chown ' + user + ' /user/'+user, user='hdfs')
    Execute('hadoop fs -chgrp ' + user + ' /user/'+user, user='hdfs')

if __name__ == "__main__":
  Master().execute()
