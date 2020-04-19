from nornir import InitNornir
from nornir.plugins.tasks import commands
from nornir.plugins.functions.text import print_result

nr = InitNornir(config_file = 'config.yaml')

host = nr.filter(site = "home", role = "host")

result = host.run(task = commands.remote_command,
                        command = "df -h",
                        name = "Available free space")

print_result(result, vars = ["stdout"])

