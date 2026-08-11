from network_automation_lab.generator import (
    generate_all_config,
)
from network_automation_lab.intent import load_intent
from network_automation_lab.inventory import load_inventory
from network_automation_lab.output import write_configs
from network_automation_lab.queries import get_devices_by_role


def main() -> None:

    data = load_intent("intent/network.yaml")
    result = get_devices_by_role(data, "router")
    print(result)

    # inventory = load_inventory("inventory/hosts.yaml")

    # configs = generate_all_config(data=data, inventory=inventory)
    # write_configs(configs, "generated")


if __name__ == "__main__":
    main()
