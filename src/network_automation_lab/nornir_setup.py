from nornir import InitNornir


def initialise_nornir():
    nr = InitNornir(config_file="config.yaml")
    return nr
