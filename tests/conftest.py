import pytest


@pytest.fixture
def sample_data() -> dict:
    return {
        "sites": {
            "london": {
                "name": "London",
                "vlans": [
                    {
                        "id": 10,
                        "name": "USERS",
                        "subnet": "10.1.10.0/24",
                    },
                    {
                        "id": 20,
                        "name": "SERVERS",
                        "subnet": "10.1.20.0/24",
                    },
                ],
            },
            "manchester": {
                "name": "Manchester",
                "vlans": [
                    {
                        "id": 10,
                        "name": "USERS",
                        "subnet": "10.2.10.0/24",
                    },
                    {
                        "id": 20,
                        "name": "SERVERS",
                        "subnet": "10.2.20.0/24",
                    },
                ],
            },
        },
        "devices": {
            "lon-rtr-01": {
                "site": "london",
                "role": "router",
                "asn": 65001,
                "interfaces": {
                    "GigabitEthernet1": {
                        "description": "LAN uplink",
                        "ipv4": "10.1.0.1/30",
                        "enabled": True,
                    },
                    "GigabitEthernet2": {
                        "description": "WAN to MAN-RTR-01",
                        "ipv4": "10.255.0.1/30",
                        "enabled": True,
                    },
                },
                "bgp": {
                    "router_id": "10.1.255.1",
                    "neighbours": [
                        {
                            "address": "10.255.0.2",
                            "remote_as": 65002,
                            "description": "MAN-RTR-01",
                        }
                    ],
                },
            },
            "man-rtr-01": {
                "site": "manchester",
                "role": "router",
                "asn": 65002,
                "interfaces": {
                    "GigabitEthernet1": {
                        "description": "LAN uplink",
                        "ipv4": "10.2.0.1/30",
                        "enabled": True,
                    },
                    "GigabitEthernet2": {
                        "description": "WAN to LON-RTR-01",
                        "ipv4": "10.255.0.2/30",
                        "enabled": True,
                    },
                },
                "bgp": {
                    "router_id": "10.2.255.1",
                    "neighbours": [
                        {
                            "address": "10.255.0.1",
                            "remote_as": 65001,
                            "description": "LON-RTR-01",
                        }
                    ],
                },
            },
            "lon-sw-01": {
                "site": "london",
                "role": "switch",
                "interfaces": {
                    "GigabitEthernet1/0/1": {
                        "description": "User access port",
                        "enabled": True,
                        "mode": "access",
                        "vlan": 10,
                    },
                    "GigabitEthernet1/0/2": {
                        "description": "Server access port",
                        "enabled": True,
                        "mode": "access",
                        "vlan": 20,
                    },
                },
            },
            "lon-sw-02": {
                "site": "london",
                "role": "switch",
                "interfaces": {
                    "Ethernet1": {
                        "description": "User access port",
                        "enabled": True,
                        "mode": "access",
                        "vlan": 10,
                    },
                },
            },
        },
    }


@pytest.fixture
def sample_inventory() -> dict:
    return {
        "lon-rtr-01": {
            "hostname": "192.0.2.11",
            "platform": "iosxe",
        },
        "lon-sw-02": {
            "hostname": "192.0.2.22",
            "platform": "eos",
        },
        "man-rtr-01": {
            "hostname": "192.0.2.31",
            "platform": "iosxe",
        },
        "lon-sw-01": {
            "hostname": "192.0.2.21",
            "platform": "iosxe",
        },
    }
