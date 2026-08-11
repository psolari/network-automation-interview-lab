from pathlib import Path


def write_configs(configs: dict, output_dir: str | Path) -> None:
    output_path = Path(output_dir)

    output_path.mkdir(parents=True, exist_ok=True)
    for hostname, config in configs.items():
        file_path = output_path / f"{hostname}.cfg"
        file_path.write_text(config, encoding="utf-8")
