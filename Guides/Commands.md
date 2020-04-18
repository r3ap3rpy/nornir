## Commands

Official documentation should be [visited](https://nornir.readthedocs.io/en/latest/plugins/tasks/index.html) for further details.

Let's retrieve information about the available freespace on our remote host.

``` python
from nornir.plugins.tasks import commands
from nornir import InitNornir
from nornir.plugins.functions.text import print_result

nr = InitNornir(core={"num_workers": 50}, config_file="config.yaml")

hosts = nr.filter(site="home", role="host")

result = hosts.run(task=commands.remote_command,command="df -h", name = "Available space")

print_result(result, vars=["stdout"])
```

Let's upload a file.

``` python
from nornir.plugins.tasks import files
from nornir import InitNornir
from nornir.plugins.functions.text import print_result

nr = InitNornir(core={"num_workers": 50}, config_file="config.yaml")

hosts = nr.filter(site="home", role="host")

result = hosts.run(task=files.sftp, name = "Upload file", action="put",src="LICENSE.txt",dst="/tmp/LICENSE.txt")

print_result(result)
```

Let's write to a local file.

``` python
from nornir.plugins.tasks import files
from nornir import InitNornir
from nornir.plugins.functions.text import print_result

nr = InitNornir(core={"num_workers": 50}, config_file="config.yaml")

hosts = nr.filter(site="home", role="host")

result = hosts.run(task=files.write_file, name = "Upload file", filename="LICENSE.txt", content="Iamyournewcontent",)

print_result(result)
```

## Functions

Here is a list of supported tasks.

``` python
from nornir.plugins.tasks import commands
from nornir import InitNornir
from nornir.plugins.functions.text import print_result

def available_resources(task):
    task.run(task=commands.remote_command,
             name="Available disk",
             command="df -h")
    task.run(task=commands.remote_command,
             name="Available memory",
             command="free -m")

hosts = nr.filter(site="home", role="host")

result = hosts.run(task=available_resources)

print_result(result, vars=["stdout"])
```

Now we can will learn to make sense of the [filters](/Guides/Filtering.md) available.
