import pytest

from network_automation_lab.queries import get_device, get_devices_by_role, get_platform


def test_get_device(sample_data: dict) -> None:
    result = get_device(sample_data, "lon-rtr-01")

    assert result["role"] == "router"
    assert result["site"] == "london"


def test_get_devices_by_role(sample_data: dict) -> None:
    result = get_devices_by_role(sample_data, "router")

    assert len(result) == 2
    for hostname, device in sample_data["devices"].items():
        if device["role"] == "router":
            assert hostname in result
        else:
            assert hostname not in result


@pytest.mark.parametrize(
    "hostname, expected_platform",
    [
        ("lon-rtr-01", "iosxe"),
        ("lon-sw-02", "eos"),
    ],
)
def test_get_platform(
    sample_inventory: dict,
    hostname: str,
    expected_platform: str,
) -> None:
    result = get_platform(sample_inventory, hostname)

    assert result == expected_platform
