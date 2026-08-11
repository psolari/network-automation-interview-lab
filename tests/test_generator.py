from unittest.mock import patch

from network_automation_lab.generator import generate_device_config


def test_generate_device_config(sample_data: dict, sample_inventory: dict) -> None:
    device = sample_data["devices"]["lon-rtr-01"]

    with patch(
        "network_automation_lab.generator.render_device_config"
    ) as mock_renderer:
        mock_renderer.return_value = "FAKE CONFIG"
        result = generate_device_config(
            data=sample_data,
            inventory=sample_inventory,
            hostname="lon-rtr-01",
        )
        assert result == "FAKE CONFIG"
        mock_renderer.assert_called_once_with(
            device,
            "iosxe",
        )
