## Setting up nornir

You can pick Windows, Linux or MacOS host to setup your nornir instance.
This guide assumes a version 3.7 installation of [Python](https://www.python.org/downloads/release/python-370/) and at least 2 virtual machine that will be managed.
One virtual machine should be a Windows machine, the other a Linux. I am going to use in the course a [CentOS7](https://www.centos.org/download/), a [Windows Server 2019](https://www.microsoft.com/en-us/cloud-platform/windows-server) and a [Catalina](https://www.apple.com/hu/macos/catalina/) setup. 

The machines can have as low as 2vCPU and 4GB of ram.

### Installing nornir

On the host machine I install the *virtualenv* module in python with the following command.

``` python
python -m pip install virtualenv
```

