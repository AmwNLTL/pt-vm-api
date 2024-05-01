# pt-vm-api

This is a Python command-line interface (CLI) application that simply exports records based on PDQL filter from your MaxPatrol 10 (VM).

## Installation

1. Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/pdql-vm-cli.git
```

2. Navigate to the project directory:

```bash
cd pt-vm-cli
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the `main.py` file with appropriate command-line arguments to export records based on PDQL filters. 

```bash
usage: pt-vm-api [-h] -u USER -p PASSWORD -s SECRET -f FILTER [-a ASSETS [ASSETS ...]] [-l LIMIT] [--csv CSV] hostaddress

Simply exports records based on PDQL filter

positional arguments:
  hostaddress           HostAddress parameter from deploy (FQDN/IP)

options:
  -h, --help            show this help message and exit
  -u USER, --user USER  PT MC User
  -p PASSWORD, --password PASSWORD
                        PT MC User's Password
  -s SECRET, --secret SECRET
                        ClientSecret parameter from /var/lib/deployer/role_instances/core*/params.yaml
  -f FILTER, --filter FILTER
                        PDQL Filter to execute
  -a ASSETS [ASSETS ...], --assets ASSETS [ASSETS ...]
                        Assets' Filter to execute
  -l LIMIT, --limit LIMIT
                        Number of Records to get as response
  --csv CSV             Filename to export response

Thanks to @avleonov
```

Here's the basic usage:

```bash
# Exports CVEs of 2 specified by id hosts to example.csv limiting response to 10000 rows

python3 main.py 192.168.0.1 -u Administrator -p P@ssw0rd -s 00000000-0000-0000-0000-000000000000 -f 'select(@Host, Host.@Vulners.CVEs.Item) | sort(@Host ASC)' -l 10000 -a 00000000-0000-0001-0000-000000000001 00000000-0000-0001-0000-000000000002 --csv example.csv
```
... and one example: 

```bash
# Exports information about all Unix hosts like OS name and version 
# plus installed packages and its version to example.csv limited by 10000 records in response

python3 main.py mp10.ent.local -u Administrator -p P@ssw0rd -s 00000000-0000-0000-0000-000000000000 -f 'select(@UnixHost, UnixHost.OsName, UnixHost.OsVersion, UnixHost.Packages.Name, UnixHost.Packages.Version) | sort(@UnixHost ASC)' -a --csv sample.csv -l 10000
```
