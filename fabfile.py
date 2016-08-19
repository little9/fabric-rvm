from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm

def vagrant(port): 
    env.user = 'vagrant'
    # Give the port as an arugment -- this changes depending on the VM
    env.hosts = ['127.0.0.1:%s' % port]
    # use vagrant ssh key // via http://sysadminpy.com/sysadmin/2011/04/30/use-fabric-on-vagrant-instances/ updated to vagrant-ssh
    result = local('vagrant ssh-config | grep IdentityFile', capture=True)
    env.key_filename = result.split()[1]

def install_basics():
    # Install basics for installing rvm and downloading other software
    run('sudo yum groupinstall "Development Tools"')
    run('sudo yum install curl git libxml2 libxml2-dev libxslt-devel libxslt-devel')

def firewall_config():
    with settings(warn_only=True):
        run('sudo service iptables stop')

def install_rvm():
    # Install the Ruby Version Manager, along with the current stable version of Ruby
    # Install the bundler gem
    run('curl -sSL https://rvm.io/mpapis.asc | gpg2 --import -')
    run('\curl -sSL https://get.rvm.io | bash -s stable')
    run('rvm install 2.3.1')
    run('rvm use 2.3.1 && gem install bundler')
