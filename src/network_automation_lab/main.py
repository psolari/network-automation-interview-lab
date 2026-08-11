import time

from network_automation_lab.intent import load_intent
from network_automation_lab.nornir_setup import initialise_nornir
from network_automation_lab.tasks import generate_config_task


def main() -> None:

    data = load_intent("intent/network.yaml")
    nr = initialise_nornir()

    results = nr.run(
        task=generate_config_task,
        intent=data,
    )

    print(results)


if __name__ == "__main__":
    main()
