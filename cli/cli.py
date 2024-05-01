import os
import sys
import argparse

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(project_root)

parser = argparse.ArgumentParser(
                    prog='pt-vm-api',
                    description='Simply exports records based on PDQL filter',
                    epilog='Thanks to @avleonov')

parser.add_argument('hostaddress', help='HostAddress parameter from deploy (FQDN/IP)')
parser.add_argument('-u', '--user', required=True, help = 'PT MC User')
parser.add_argument('-p', '--password', required=True, help='PT MC User\'s Password')
parser.add_argument('-s', '--secret', required=True, help='ClientSecret parameter from /var/lib/deployer/role_instances/core*/params.yaml')
parser.add_argument('-f', '--filter', required=True, help='PDQL Filter to execute')
parser.add_argument('-a', '--assets', nargs='+', default=[], help='Assets\' Filter to execute')
parser.add_argument('-l', '--limit', default='50', help='Number of Records to get as response')
parser.add_argument('--csv', default=None, help='Filename to export response')

args = parser.parse_args()
