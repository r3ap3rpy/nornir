## Setting up nornir

You can pick Windows, Linux or MacOS host to setup your nornir instance.
This guide assumes a version 3.7 installation of [Python](https://www.python.org/downloads/release/python-370/) and at least 1 virtual machine that will be managed.
One virtual machine should be a Linux. I am going to use in the course a [CentOS7](https://www.centos.org/download/).

The machines can have as low as 2vCPU and 2GB of ram.

### Installing nornir

On the host machine I install the *virtualenv* module in python with the following command.

``` python
python -m pip install virtualenv
```

If you have multiple versions of python make sure your default `python` is the version 3.7, otherwise you need to give the full path for the command to work.

After this you can create your little environment where the setup will live.

Mine lives on the Desktop\NornirProject folder of my user, so after navigating there the following command is issued.

``` python
virtualenv nornirproject
```

Once this is done we will need 2 more folders, one is `scripts` the other is `inventory`.

You can now activate your project and install nornir.

``` bash
# This is for windows
nornirproject\Scripts\activate.bat
# This is for linux
source nornir/bin/activate
# install nornir
pip install nornir
```

Now nornir is installed, the next section will give you a quick tour about basic layout of the project and how you can [Initialize](/Guides/Initialize.md) your project files.


