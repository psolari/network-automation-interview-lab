from ipaddress import IPv4Interface


def validate_interface_addresses(data: dict) -> list[str]:
    errors = []

    for hostname, device in data["devices"].items():
        for interface, details in device.get("interfaces", {}).items():
            if "ipv4" in details:
                try:
                    IPv4Interface(details["ipv4"])
                except ValueError:
                    errors.append(
                        f"{hostname} {interface} has invalid IPv4 address: "
                        f'{details["ipv4"]}'
                    )

    return errors


def validate_duplicate_addresses(data: dict) -> list[str]:
    found_addresses = set()
    duplicates = []

    for hostname, device in data["devices"].items():
        for interface, details in device.get("interfaces", {}).items():
            if "ipv4" in details:
                try:
                    address = IPv4Interface(details["ipv4"]).ip
                except ValueError:
                    continue

                if address in found_addresses:
                    duplicates.append(f"Duplicate IPv4 address found: {address}")
                else:
                    found_addresses.add(address)

    return duplicates


def validate_vlan_ids(data: dict) -> list[str]:
    errors = []

    for site, details in data["sites"].items():
        for vlan in details.get("vlans", []):
            if not 1 <= vlan["id"] <= 4094:
                errors.append(f'Site {site} has invalid VLAN ID: {vlan["id"]}')

    return errors


def validate_required_fields(data: dict) -> list[str]:
    required_device_fields = ["site", "role", "interfaces"]
    required_interface_fields = ["description", "enabled"]
    required_router_fields = ["asn", "bgp"]
    errors = []

    for hostname, device in data["devices"].items():
        for field in required_device_fields:
            if field not in device:
                errors.append(f"Device {hostname} is missing required field: {field}")

        for interface, details in device.get("interfaces", {}).items():
            for field in required_interface_fields:
                if field not in details:
                    errors.append(
                        f"Device {hostname} interface {interface} "
                        f"is missing required field: {field}"
                    )

        if device.get("role") == "router":
            for field in required_router_fields:
                if field not in device:
                    errors.append(
                        f"Device {hostname} is missing required field: {field}"
                    )

    return errors


def validate_intent(data: dict) -> list[str]:
    errors = []

    errors.extend(validate_required_fields(data))
    errors.extend(validate_interface_addresses(data))
    errors.extend(validate_duplicate_addresses(data))
    errors.extend(validate_vlan_ids(data))

    return errors
