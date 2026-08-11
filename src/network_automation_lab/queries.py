def get_device(data: dict, hostname: str) -> dict:
    return data["devices"][hostname]


def get_platform(inventory: dict, hostname: str) -> str:
    return inventory[hostname]["platform"]


def get_devices_by_role(data: dict, role: str) -> dict:
    devices_by_role = {}

    for hostname, device in data["devices"].items():
        if device["role"] == role:
            devices_by_role[hostname] = device

    return devices_by_role


def get_interface_addresses(data: dict) -> dict:
    interface_addresses = {}

    for hostname, device in data["devices"].items():
        for interface, details in device["interfaces"].items():
            interface_address = details.get("ipv4")
            if interface_address != None:
                if hostname in interface_addresses:
                    interface_addresses[hostname][interface] = interface_address
                else:
                    interface_addresses[hostname] = {interface: interface_address}

    return interface_addresses


def get_bgp_neighbours(data: dict) -> list:
    bgp_neighbours = []

    for hostname, device in data["devices"].items():
        if "bgp" in device:
            for neighbour in device["bgp"]["neighbours"]:
                bgp_neighbours.append(
                    {
                        "hostname": hostname,
                        "address": neighbour["address"],
                        "remote_as": neighbour["remote_as"],
                        "description": neighbour["description"],
                    }
                )

    return bgp_neighbours


def get_network_summary(data: dict) -> dict:
    device_count = len(data["devices"])
    router_count = len(get_devices_by_role(data, "router"))
    switch_count = len(get_devices_by_role(data, "switch"))
    site_count = len(data["sites"])
    bgp_neighbour_count = len(get_bgp_neighbours(data))
    network_summary = {
        "device_count": device_count,
        "router_count": router_count,
        "switch_count": switch_count,
        "site_count": site_count,
        "bgp_neighbour_count": bgp_neighbour_count,
    }
    return network_summary
