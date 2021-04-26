#!/usr/bin/env python

from resource_management import *

class HttpFS(Script):
    def install(self, env):
        Logger.info("Installing HttpFS packages")
        self.install_packages(env)
        #if any other install steps were needed they can be added here

    def configure(self, env):
        import params
        Logger.info("Enabling HttpFS service")
        env.set_params(params)
        Execute(('systemctl enable hadoop-httpfs'), user='root')

    #To stop the service, use the linux service stop command and pipe output to log file
    def stop(self, env):
        Logger.info("Stopping HttpFS service")
        Execute(('service hadoop-httpfs stop'), user='root')

    #To start the service, use the linux service start command and pipe output to log file
    def start(self, env):
        Logger.info("Starting HttpFS service")
        self.configure(env)
        Execute(('service hadoop-httpfs start'), user='root')

    #To get status of the, use the linux service status command
    def status(self, env):
        Logger.info("Getting status of HttpFS service")
        try:
            Execute(('service hadoop-httpfs status'), user='root')
        except Fail:
            raise ComponentIsNotRunning()

if __name__ == "__main__":
    HttpFS().execute()
