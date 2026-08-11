import pytest
from copy import deepcopy
from jinja2 import UndefinedError

from network_automation_lab.renderer import (
    render_device_config,
    render_eos_interfaces,
    render_iosxe_interfaces,
    render_iosxe_bgp,
)


def test_render_iosxe_interfaces(sample_data: dict) -> None:
    device = sample_data["devices"]["lon-rtr-01"]
    config = render_iosxe_interfaces(device)
    assert "interface GigabitEthernet1" in config
    assert "description LAN uplink" in config
    assert "ip address 10.1.0.1 255.255.255.252" in config
    assert "no shutdown" in config


def test_render_eos_interfaces(sample_data: dict) -> None:
    device = sample_data["devices"]["lon-sw-02"]
    config = render_eos_interfaces(device)
    assert "interface Ethernet1" in config
    assert "description User access port" in config
    assert "switchport mode access" in config
    assert "switchport access vlan 10" in config
    assert "no shutdown" in config


def test_render_iosxe_bgp(sample_data: dict) -> None:
    device = sample_data["devices"]["lon-rtr-01"]
    config = render_iosxe_bgp(device)

    assert "router bgp 65001" in config
    assert "bgp router-id 10.1.255.1" in config
    assert "neighbor 10.255.0.2 remote-as 65002" in config
    assert "neighbor 10.255.0.2 description MAN-RTR-01" in config


def test_render_device_config_iosxe(sample_data: dict) -> None:
    device = sample_data["devices"]["lon-rtr-01"]

    config = render_device_config(device, "iosxe")

    assert "interface GigabitEthernet1" in config
    assert "router bgp 65001" in config


def test_render_device_config_eos(sample_data: dict) -> None:
    device = sample_data["devices"]["lon-sw-02"]

    config = render_device_config(device, "eos")

    assert "interface Ethernet1" in config
    assert "switchport access vlan 10" in config


def test_render_device_config_unsupported_platform(sample_data: dict) -> None:
    device = sample_data["devices"]["lon-rtr-01"]

    with pytest.raises(ValueError, match="Unsupported platform"):
        render_device_config(device, "junos")


def test_render_missing_interface_description(sample_data: dict) -> None:
    device = deepcopy(sample_data["devices"]["lon-rtr-01"])
    del device["interfaces"]["GigabitEthernet1"]["description"]

    with pytest.raises(UndefinedError):
        render_iosxe_interfaces(device)
