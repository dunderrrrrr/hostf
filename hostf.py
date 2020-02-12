import sys
import socket
import argparse
from _defs import read_hosts
from _defs import add_host
from _defs import del_host
from _defs import clear_lines


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        usage="\n[ADD] hostf -a <ip> <hostname>\n[DEL] hostf -d <ip>",
        description='hostf will manage /etc/hosts faster than lightning.'
    )
    parser.add_argument(
        '-a',
        action='store',
        metavar=('10.1.1.5', 'test.com'),
        nargs=2,
        help='Add to hosts.'
    )
    parser.add_argument(
        '-d',
        action='store',
        metavar=('10.1.1.5'),
        nargs=1,
        help='Delete from hosts.'
    )
    args = parser.parse_args()
    if len(sys.argv)==1:
        read_hosts()
        sys.exit(1)
    if args.a:
        try:
            ip = socket.inet_aton(args.a[0])
            valid_ip = True
        except Exception as E:
            valid_ip = False
        if valid_ip:
            add_host(args.a[0], args.a[1])
            read_hosts()
        else:
            print("{} is not a valid IPv4 or IPv6 address.".format(args.a[0]))
    if args.d:
        del_host(args.d[0])
        read_hosts()
