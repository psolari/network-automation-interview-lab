from network_automation_lab.coding_challenge.challenge import get_active_routers_by_site


def test_get_active_routers_by_site(sample_data: list[dict]) -> None:
    result = get_active_routers_by_site(sample_data)

    assert result == {
        "london": [
            {
                "hostname": "lon-rtr-01",
                "platform": "iosxe",
                "management_ip": "192.168.1.15",
            }
        ],
        "manchester": [
            {
                "hostname": "man-rtr-01",
                "platform": "iosxe",
                "management_ip": "192.168.1.15",
            }
        ],
    }
