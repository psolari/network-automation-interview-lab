from pathlib import Path
from ipaddress import IPv4Interface

from jinja2 import Environment, FileSystemLoader, StrictUndefined

TEMPLATE_DIR = Path("templates")

environment = Environment(
    loader=FileSystemLoader(TEMPLATE_DIR),
    trim_blocks=True,
    lstrip_blocks=True,
    undefined=StrictUndefined,
)


def prepare_interfaces(interfaces: dict) -> dict:
    prepared_interfaces = {}

    for interface, details in interfaces.items():
        prepared_details = details.copy()

        if "ipv4" in prepared_details:
            interface_address = IPv4Interface(prepared_details["ipv4"])

            prepared_details["ipv4"] = {
                "address": str(interface_address.ip),
                "netmask": str(interface_address.netmask),
            }

        prepared_interfaces[interface] = prepared_details

    return prepared_interfaces


def render_iosxe_interfaces(device: dict) -> str:
    prepared_interfaces = prepare_interfaces(device["interfaces"])
    template = environment.get_template("iosxe_interfaces.j2")
    return template.render(interfaces=prepared_interfaces)


def render_eos_interfaces(device: dict) -> str:
    template = environment.get_template("eos_interfaces.j2")
    return template.render(interfaces=device["interfaces"])


def render_interfaces(device: dict, platform: str) -> str:
    if platform == "iosxe":
        return render_iosxe_interfaces(device)
    if platform == "eos":
        return render_eos_interfaces(device)
    raise ValueError(f"Unsupported platform: {platform}")


def render_iosxe_bgp(device: dict) -> str:
    template = environment.get_template("iosxe_bgp.j2")
    return template.render(device=device)


def render_iosxe_config(device: dict) -> str:
    config_parts = []

    config_parts.append(render_iosxe_interfaces(device))

    if "bgp" in device:
        config_parts.append(render_iosxe_bgp(device))

    return "\n".join(config_parts)


def render_eos_config(device: dict) -> str:
    config_parts = []

    config_parts.append(render_eos_interfaces(device))

    return "\n".join(config_parts)


def render_device_config(device: dict, platform: str) -> str:
    if platform == "iosxe":
        return render_iosxe_config(device)
    if platform == "eos":
        return render_eos_config(device)
    raise ValueError(f"Unsupported platform: {platform}")
