import pprint

from ncclient import manager


def main() -> None:

    with manager.connect(
        host="192.168.1.15",
        port=830,
        username="automation",
        password="cisco123",
        hostkey_verify=False,
        device_params={"name": "iosxe"},
    ) as connection:

        filter_xml = """
        <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
            <interface/>
        </native>
        """

        response = connection.get(
            filter=("subtree", filter_xml),
        )

        print(response.data_xml)


if __name__ == "__main__":
    main()
