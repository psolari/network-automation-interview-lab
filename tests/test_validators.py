from copy import deepcopy

from network_automation_lab.validators import (
    validate_duplicate_addresses,
    validate_intent,
    validate_interface_addresses,
    validate_required_fields,
    validate_vlan_ids,
)


def test_valid_interface_addresses(sample_data: dict) -> None:
    errors = validate_interface_addresses(sample_data)

    assert errors == []


def test_invalid_interface_address(sample_data: dict) -> None:
    data = deepcopy(sample_data)

    data["devices"]["lon-rtr-01"]["interfaces"]["GigabitEthernet1"][
        "ipv4"
    ] = "999.1.1.1/24"

    errors = validate_interface_addresses(data)

    assert len(errors) == 1
    assert any("999.1.1.1/24" in error for error in errors)


def test_no_duplicate_addresses(sample_data: dict) -> None:
    errors = validate_duplicate_addresses(sample_data)

    assert errors == []


def test_duplicate_interface_address(sample_data: dict) -> None:
    data = deepcopy(sample_data)

    data["devices"]["man-rtr-01"]["interfaces"]["GigabitEthernet2"][
        "ipv4"
    ] = "10.255.0.1/30"

    errors = validate_duplicate_addresses(data)

    assert len(errors) == 1
    assert any("10.255.0.1" in error for error in errors)


def test_valid_vlan_ids(sample_data: dict) -> None:
    errors = validate_vlan_ids(sample_data)

    assert errors == []


def test_invalid_vlan_id(sample_data: dict) -> None:
    data = deepcopy(sample_data)

    data["sites"]["london"]["vlans"][0]["id"] = 9999

    errors = validate_vlan_ids(data)

    assert len(errors) == 1
    assert any("9999" in error for error in errors)


def test_all_required_fields_present(sample_data: dict) -> None:
    errors = validate_required_fields(sample_data)

    assert errors == []


def test_missing_required_device_field(sample_data: dict) -> None:
    data = deepcopy(sample_data)

    del data["devices"]["lon-rtr-01"]["site"]

    errors = validate_required_fields(data)

    assert any("site" in error for error in errors)


def test_missing_required_interface_field(sample_data: dict) -> None:
    data = deepcopy(sample_data)

    del data["devices"]["lon-rtr-01"]["interfaces"]["GigabitEthernet1"]["description"]

    errors = validate_required_fields(data)

    assert any("description" in error for error in errors)


def test_missing_required_router_field(sample_data: dict) -> None:
    data = deepcopy(sample_data)

    del data["devices"]["lon-rtr-01"]["asn"]

    errors = validate_required_fields(data)

    assert any("asn" in error for error in errors)


def test_valid_intent(sample_data: dict) -> None:
    errors = validate_intent(sample_data)

    assert errors == []


def test_invalid_intent(sample_data: dict) -> None:
    data = deepcopy(sample_data)

    data["sites"]["london"]["vlans"][0]["id"] = 9999
    data["devices"]["lon-rtr-01"]["interfaces"]["GigabitEthernet1"][
        "ipv4"
    ] = "999.1.1.1/24"
    del data["devices"]["lon-rtr-01"]["site"]

    errors = validate_intent(data)

    assert len(errors) >= 3
    assert any("9999" in error for error in errors)
    assert any("999.1.1.1/24" in error for error in errors)
    assert any("site" in error for error in errors)
