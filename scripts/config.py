import yaml


def init_configurations():
    yaml_config = "./config.yml"
    with open(yaml_config, 'r') as y:
        configurations = yaml.safe_load(y)
    if not configurations:
        raise Exception("empty configuration in yaml file: {}".format(yaml_config))
    return configurations
