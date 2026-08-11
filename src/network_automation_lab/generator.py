from network_automation_lab.queries import (
    get_device,
    get_platform,
)
from network_automation_lab.renderer import render_device_config


def generate_device_config(data: dict, inventory: dict, hostname: str) -> str:
    device = get_device(data, hostname)
    platform = get_platform(inventory, hostname)
    return render_device_config(device, platform)


def generate_all_config(data: dict, inventory: dict) -> dict:
    generated_configs = {}
    for hostname, details in inventory.items():
        generated_configs[hostname] = generate_device_config(data, inventory, hostname)
    return generated_configs
