# Network Automation Interview Lab

Practical network automation lab built for Senior Network Automation Engineer interview preparation.

## Goals

The project will demonstrate:

- Python network automation
- structured network inventory and intent
- Jinja2 configuration generation
- pytest automated testing
- Nornir orchestration
- Netmiko and NAPALM
- NETCONF, RESTCONF and gNMI
- pyATS / Genie validation
- Docker
- GitHub Actions CI/CD
- Terraform
- Source of Truth integration
- GitOps
- model-driven telemetry

## Lab Network

The lab represents two UK sites:

- London
- Manchester

Initial device inventory:

| Device | Site | Platform | Role |
|---|---|---|---|
| lon-rtr-01 | London | Cisco IOS-XE | Router |
| lon-sw-01 | London | Cisco IOS-XE | Switch |
| lon-sw-02 | London | Arista EOS | Switch |
| man-rtr-01 | Manchester | Cisco IOS-XE | Router |
| man-sw-01 | Manchester | Cisco IOS-XE | Switch |
| man-sw-02 | Manchester | Arista EOS | Switch |

The inventory currently represents logical lab devices. Management addresses will later be updated to match actual virtual devices where required.
