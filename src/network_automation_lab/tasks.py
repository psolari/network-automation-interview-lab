import time

from nornir.core.task import Result, Task

from network_automation_lab.queries import get_device
from network_automation_lab.renderer import render_device_config


def get_host_summary(task: Task) -> Result:
    summary = (
        f"name={task.host.name}, "
        f"hostname={task.host.hostname}, "
        f"platform={task.host.platform}"
    )

    return Result(
        host=task.host,
        result=summary,
    )


def get_hostname(task: Task) -> Result:
    return Result(
        host=task.host,
        result=f"Hostname: {task.host.hostname}",
    )


def get_platform(task: Task) -> Result:
    return Result(
        host=task.host,
        result=f"Platform: {task.host.platform}",
    )


def get_device_details(task: Task) -> Result:
    task.run(task=get_hostname)
    task.run(task=get_platform)

    return Result(
        host=task.host,
        result="Device details collected",
    )


def slow_task(task: Task) -> Result:
    time.sleep(2)

    return Result(host=task.host, result=f"Finished {task.host.name}")


def failure_test(task: Task) -> Result:
    if task.host.name == "lon-rtr-01":
        raise ValueError("Deliberate Failure")

    return Result(
        host=task.host,
        result=f"{task.host.name} completed successfully",
    )


def generate_config_task(task: Task, intent: dict) -> Result:
    hostname = task.host.name
    platform = task.host.platform
    device = get_device(
        data=intent,
        hostname=hostname,
    )
    config = render_device_config(device=device, platform=platform)

    return Result(host=task.host, result=config)
