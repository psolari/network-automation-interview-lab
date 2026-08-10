from network_automation_lab.intent import load_intent
from network_automation_lab.queries import (
    get_bgp_neighbours,
    get_device,
    get_devices_by_role,
    get_interface_addresses,
    get_network_summary,
)
from network_automation_lab.validators import (
    validate_duplicate_addresses,
    validate_intent,
    validate_interface_addresses,
    validate_required_fields,
    validate_vlan_ids,
)


def main() -> None:
    data = load_intent("intent/network.yaml")

    device = get_device(data, "lon-rtr-01")

    devices_by_role = get_devices_by_role(data, "switch")

    interface_addresses = get_interface_addresses(data)

    bgp_neighbours = get_bgp_neighbours(data)

    network_summary = get_network_summary(data)

    validated_interface = validate_interface_addresses(data)

    validate_duplicates = validate_duplicate_addresses(data)

    validate_vlans = validate_vlan_ids(data)

    validate_fields = validate_required_fields(data)

    validated_intent = validate_intent(data)

    print(validated_intent)


if __name__ == "__main__":
    main()
