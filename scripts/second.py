from nornir import InitNornir
from nornir.plugins.tasks import files
from nornir.plugins.functions.text import print_result

nr = InitNornir(config_file = 'config.yaml')

host = nr.filter(site = "home", role = "host")

result = host.run(task = files.sftp,
                        action = "put",
                        src = 'config.yaml',
                        dst = '/tmp/config.yaml',
                        name = "Upload config.yaml to /tmp")

print_result(result)

