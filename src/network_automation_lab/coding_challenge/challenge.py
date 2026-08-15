from ipaddress import IPv4Interface
import pprint

devices = [
    {
        "hostname": "lon-rtr-01",
        "site": "london",
        "role": "router",
        "platform": "iosxe",
        "management_ip": "192.168.1.15",
        "status": "active",
    },
    {
        "hostname": "lon-sw-01",
        "site": "london",
        "role": "switch",
        "platform": "iosxe",
        "management_ip": "192.168.1.20",
        "status": "active",
    },
    {
        "hostname": "man-rtr-01",
        "site": "manchester",
        "role": "router",
        "platform": "iosxe",
        "management_ip": "192.168.1.15/24",
        "status": "active",
    },
    {
        "hostname": "man-rtr-02",
        "site": "manchester",
        "role": "router",
        "platform": "iosxe",
        "management_ip": "not-an-ip",
        "status": "active",
    },
    {
        "hostname": "old-rtr-01",
        "site": "london",
        "role": "router",
        "platform": "iosxe",
        "management_ip": "192.168.1.99",
        "status": "decommissioned",
    },
]


def get_active_routers_by_site(devices: list[dict]) -> dict[str, list[dict]]:
    routers_by_site = {}
    for device in devices:
        if device.get("status") == "active" and device.get("role") == "router":
            try:
                ip = IPv4Interface(device["management_ip"]).ip
                if device["site"] in routers_by_site.keys():
                    routers_by_site[device["site"]].append(
                        {
                            "hostname": device["hostname"],
                            "platform": device["platform"],
                            "management_ip": ip.compressed,
                        }
                    )
                else:
                    routers_by_site[device["site"]] = (
                        {
                            "hostname": device["hostname"],
                            "platform": device["platform"],
                            "management_ip": ip.compressed,
                        },
                    )
            except (ValueError, KeyError):
                pass
    return routers_by_site


if __name__ == "__main__":
    routers_by_site = get_active_routers_by_site(devices)
    print(routers_by_site)
