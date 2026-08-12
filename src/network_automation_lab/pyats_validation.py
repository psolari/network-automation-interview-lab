from genie.utils.diff import Diff
from pyats import aetest
from pyats.topology import loader


class CommonSetup(aetest.CommonSetup):

    @aetest.subsection
    def connect(self, testbed):
        device = testbed.devices["lon-rtr-01"]
        device.connect()

        self.parent.parameters["device"] = device


class ValidateChange(aetest.Testcase):

    @aetest.setup
    def take_baseline(self, device):
        self.bgp_before = device.learn("bgp")
        self.interfaces_before = device.learn("interface")

    @aetest.test
    def make_change(self, device):
        device.configure("""
            interface Loopback100
             description PYATS VALIDATION TEST
             ip address 10.100.100.1 255.255.255.255
             no shutdown
            """)

    @aetest.test
    def validate_expected_change(self, device):
        parsed = device.parse("show ip interface brief")

        loopback = parsed["interface"]["Loopback100"]

        if loopback["ip_address"] != "10.100.100.1":
            self.failed("Loopback100 does not have the expected IP address")

    @aetest.test
    def validate_bgp_unchanged(self, device):
        bgp_after = device.learn("bgp")

        diff = Diff(
            self.bgp_before.info,
            bgp_after.info,
            exclude=self.bgp_before.exclude,
        )

        diff.findDiff()

        if str(diff):
            self.failed(f"Unexpected BGP changes:\n{diff}")

    @aetest.cleanup
    def cleanup(self, device):
        device.configure("no interface Loopback100")


class CommonCleanup(aetest.CommonCleanup):

    @aetest.subsection
    def disconnect(self, device):
        device.disconnect()


if __name__ == "__main__":
    testbed = loader.load("testbed.yaml")

    aetest.main(testbed=testbed)
