## Filtering

Filtering is about finding the hosts against which your scripts run.

The most important thing to remember is that filtering is cumulative.

In order to filter hosts in our home site you could call the following section.

``` python
nr.filter(site="home")
```

In order to get our routers at home site you could call the.

``` python
nr.filter(site="home").filter(role="router")
```

## Logging


In order to allow capturing the output of the actions into a file the following section needs to be passed to `InitNornir` either from via a file or in script.

``` python
nr = InitNornir(core={"num_workers": 50}, config_file="config.yaml",,logging={"file": "mylogs", "level": "debug"})
```

After this we can take a look at how [Network](/Guides/Network.md) automation can be done with nornir.
