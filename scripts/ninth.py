from nornir import InitNornir
from nornir.plugins.tasks.apis import http_method
from nornir.plugins.tasks.files import write_file, sftp
from nornir.plugins.tasks.commands import remote_command
from nornir.plugins.functions.text import print_result

nr = InitNornir(config_file = "config.yaml")

hosts = nr.filter(site= "home", role='host')

downloadpip = hosts.run(task = http_method, method = "get", url = "https://bootstrap.pypa.io/get-pip.py")

pip = downloadpip['host1.dc1'].result

createpip = hosts.run(task = write_file, filename='get-pip.py', content = pip)

copypip = hosts.run(task = sftp, action = "put", src = "get-pip.py",dst = "/tmp/get-pip.py")

execute = hosts.run(task = remote_command, command = "python /tmp/get-pip.py")

print_result(execute)

