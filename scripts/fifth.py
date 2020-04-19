from nornir import InitNornir
from nornir.plugins.tasks import networking
from nornir.plugins.functions.text import print_result

nr = InitNornir(config_file = 'config.yaml')

host = nr.filter(site = "home", role = "cisco")

fact_result = host.run(task = networking.napalm_get,
        getters = ["config"],
        retrieve = "all")

print_result(fact_result)

