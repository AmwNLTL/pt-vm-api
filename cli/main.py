import cli
from api.api import get_response_from_pdql
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings
disable_warnings(InsecureRequestWarning)
import json
import csv
import export.export

response = get_response_from_pdql(cli.args.hostaddress, cli.args.user, cli.args.password, cli.args.secret, cli.args.filter, cli.args.assets, cli.args.limit)

# JSON not pretty
# print(response.json()['records'])

# JSON pretty
records = json.dumps(response.json()['records'],indent=4)
print(records)

if cli.args.csv is not None:
    export.export_to_csv(json.loads(records), cli.args.csv)
