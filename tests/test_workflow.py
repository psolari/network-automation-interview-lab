from network_automation_lab.generator import generate_all_config
from network_automation_lab.output import write_configs


def test_generate_and_write_configs(
    sample_data: dict,
    sample_inventory: dict,
    tmp_path,
) -> None:
    configs = generate_all_config(sample_data, sample_inventory)
    write_configs(configs, tmp_path)
    assert (tmp_path / "lon-rtr-01.cfg").exists()
    config = (tmp_path / "lon-rtr-01.cfg").read_text(encoding="utf-8")
    files = list(tmp_path.glob("*.cfg"))
    assert len(files) == len(configs)
    assert (tmp_path / "lon-sw-02.cfg").exists()
    assert "router bgp 65001" in config
    eos_int_config = (tmp_path / "lon-sw-02.cfg").read_text(encoding="utf-8")
    assert "interface Ethernet1" in eos_int_config
    assert "description User access port" in eos_int_config
    assert "switchport mode access" in eos_int_config
    assert "switchport access vlan 10" in eos_int_config
    assert "no shutdown" in eos_int_config
