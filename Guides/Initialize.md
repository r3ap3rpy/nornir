## Initialize project.

There are three ways to setup the project.

1. Pure config based
2. Inline your python script
3. Combination of the two above

### Pure

This type of initializatioon means you store everythink in your `config.yaml` file, and nornir is told where to look for this file, and the rest depends on the configs contents.

``` python
from nornir import InitNornir
nr = InitNornir(config_file="config.yaml")
```

### Inline

This type allows you to specify details for the core and the inventory configuration.

``` python
from nornir import InitNornir
nr = InitNornir(
    core={"num_workers": 100},
    inventory={
        "plugin": "nornir.plugins.inventory.simple.SimpleInventory",
        "options": {
            "host_file": "inventory/hosts.yaml",
            "group_file": "inventory/groups.yaml",
            "default_file": "inventory/defaults.yaml"
        }
    }
)
```

### Combination

Depending on your current situation it can come in handy when you combine the two concepts above.

``` python
from nornir import InitNornir
nr = InitNornir(core={"num_workers": 50}, config_file="config.yaml")
```

### hosts.yaml

An example for the hosts file, this file contains details as to how the connection is made agains the host, which group does the host belong to, etc...
THe data section comes in handy when you are filtering your hosts.

``` yaml
---
host1.dc1:
    hostname: 192.168.0.150
    port: 22
    username: nornir
    password: nornir
    platform: linux
    groups:
        - dc1
    data:
        site: cmh
        role: host
        type: host
```

### groups.yaml

Groups allow you to organize your hosts based on functionality and other criterias. You are able to specify `global` section to apply information globally to the groups.

``` yaml
---
global:
    data:
        company: r3ap3rpy
dc1:
    data:
        location: fransfurt
```

### defaults.yaml

This file allows you to have information applied to your groups, hosts etc... this is used when on other levels the referenced information cannotbe found.

``` yaml
---
data:
    market: devops
```

Now that we have laid the fundations we can go and practice some [commands](/Guides/Commands.md)