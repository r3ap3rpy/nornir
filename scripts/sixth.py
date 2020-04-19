from nornir import InitNornir
from nornir.plugins.tasks import networking
from nornir.plugins.functions.text import print_result

nr = InitNornir(config_file = 'config.yaml')

host = nr.filter(site = "home", role = "cisco")

fact_result = host.run(task = networking.napalm_ping,
        source='192.168.56.100',
        dest = '192.168.56.1')

print_result(fact_result)

