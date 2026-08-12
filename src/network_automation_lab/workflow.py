from getpass import getpass

from nornir_napalm.plugins.tasks import (
    napalm_configure,
    napalm_confirm_commit,
    napalm_validate,
)


def safe_change(nr, validation: list) -> None:
    lon_router = nr.filter(name="lon-rtr-01")
    nr.inventory.defaults.password = getpass("Lab password: ")

    results = lon_router.run(
        task=napalm_configure,
        configuration="""
        interface Loopback0
         description SAFE CHANGE TEST
        !
        """,
        dry_run=True,
    )
    diff_result = results["lon-rtr-01"][0]
    print(diff_result.diff)

    answer = ""
    acceptable_answers = ["y", "n"]

    while answer not in acceptable_answers:
        answer = (
            input("Are you happy with the diff and ready to continue? (y/n) ")
            .strip()
            .lower()
        )
        if answer in acceptable_answers:
            break
        else:
            print("Invalid response")

    if answer == "n":
        raise ValueError("Diff is unacceptable and script will not continue")

    commit_results = lon_router.run(
        task=napalm_configure,
        configuration="""
        interface Loopback0
         description SAFE CHANGE TEST
        !
        """,
        dry_run=False,
        revert_in=60,
    )
    commit_results.raise_on_error()

    validation_results = lon_router.run(
        task=napalm_validate,
        validation_source=validation,
    )

    complies = validation_results["lon-rtr-01"][0].result["complies"]

    if complies:
        commit_confirm_results = lon_router.run(task=napalm_confirm_commit)
        commit = commit_confirm_results["lon-rtr-01"][0]
        print(commit)
    else:
        raise ValueError("validation failure, rollback will occur")
