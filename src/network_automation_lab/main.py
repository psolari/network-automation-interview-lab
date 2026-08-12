from genie.utils.diff import Diff
from pyats.topology import loader


def main() -> None:
    testbed = loader.load("testbed.yaml")
    device = testbed.devices["lon-rtr-01"]

    device.connect()

    before = device.learn("interface")
    before_state = before.info

    device.configure("""
        interface Loopback100
        description PYATS DIFF TEST
        ip address 10.100.100.1 255.255.255.255
        no shutdown
        """)

    after = device.learn("interface")
    after_state = after.info

    diff = Diff(before_state, after_state, exclude=before.exclude)

    diff.findDiff()
    print(diff)
    device.configure("""
        no interface Loopback100
        """)
    device.disconnect()


if __name__ == "__main__":
    main()
