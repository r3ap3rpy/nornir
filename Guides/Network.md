## Configurae Devices

SSH needs to be enabled and an appropriate username and password present.
We are going to use [GNS3](https://www.gns3.com/) to emulate cisco IOS routers.

``` bash
conf ter
line vty 0 4
transport input ssh
login local

username nornir password nornir
enable secret nornir

hostname c2681/c3745
ip domain-name r3ap3rpy.com


crypto key generate rsa
2048

ip ssh version 2


int fa0/0
ip address 192.168.220.10/11 255.255.255.0
no shut
```

Now you should be able to test the ssh connnection. You may have a situation that you need to add extra arguments for the ssh connection to work.

``` bash
ssh -oKexAlgorithms=+diffie-hellman-group1-sha1 -c aes256-cbc nornir@192.168.220.10
```

### Add them to hosts file

Let's add the routers into our hosts file.

``` yaml
host2.home:
    hostname: 192.168.220.10
    port: 22
    username: nornir
    password: nornir
    platform: ios
    groups:
        - dc1
    data:
        site: home
        role: cisco
        type: router
    connection_options:
        napalm:
            extras:
                optional_args:
                    secret: nornir
        netmiko:
          extras:
              secret: nornir

host2.home:
    hostname: 192.168.220.11
    port: 22
    username: nornir
    password: nornir
    platform: ios
    groups:
        - dc1
    data:
        site: home
        role: cisco
        type: router
    connection_options:
        napalm:
            extras:
                optional_args:
                    secret: nornir
        netmiko:
          extras:
              secret: nornir
```

As you can see this is a bit different from the host before, and we have an extra connection option which is the `secret` password.

### Run stuff against them

Now we can query some `facts` form our device.

``` python
from nornir import InitNornir
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks import networking

nr = InitNornir(core={"num_workers": 50}, config_file="config.yaml")

routers = nr.filter(site="home", role="cisco")
result = routers.run(task=networking.napalm_get,getters=["facts"])

print_result(result)
```

We can retrieve the running configuration aswell.

``` python
from nornir import InitNornir
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks import networking

nr = InitNornir(core={"num_workers": 50}, config_file="config.yaml")

routers = nr.filter(site="home", role="cisco")

result = routers.run(task=networking.napalm_get,getters=["config"],retrieve="all")
print_result(result)
```

We can perform remote pings aswell.

``` python
from nornir import InitNornir
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks import networking

nr = InitNornir(core={"num_workers": 50}, config_file="config.yaml")

routers = nr.filter(site="home", role="cisco")


result = routers.run(task=networking.napalm_ping,source='192.168.220.10',dest='192.168.220.1')
print_result(result)
```

We can modify the configuration aswell.

``` python
from nornir import InitNornir
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks import networking

nr = InitNornir(core={"num_workers": 50}, config_file="config.yaml")

routers = nr.filter(site="home", role="cisco")


result = routers.run(task=networking.netmiko_send_config,config_commands=['ip ssh version 2'])
print_result(result)
```