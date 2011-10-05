#!/usr/bin/env python

__author__ = 'Mathias Lafeldt <mathias.lafeldt@gmail.com>'

import sys
import socket
import struct
import optparse

IP_IDENT = '$IP'


def dqn_to_int(ip):
    """Convert dotted quad string to long integer"""
    return struct.unpack('!L', socket.inet_aton(ip))[0]


def int_to_dqn(n):
    """Convert long integer to dotted quad string"""
    return socket.inet_ntoa(struct.pack('!L', n))


def cidr_to_int(cidr):
    """Convert CIDR to long integer"""
    return 0xffffffff ^ (1L << 32 - cidr) - 1


def ip_generator(ip, mask):
    """Generate IPs as dotted quad strings"""
    i = start = ip & mask
    end = start | (~mask & 0xffffffff)
    while i <= end:
        yield int_to_dqn(i)
        i += 1


def parse_subnet(subnet):
    """Parse subnet string to get IP and mask as integers"""
    if '/' in subnet:
        ip, mask = subnet.split('/', 1)
    else:
        ip, mask = subnet, str(32)

    ip_num = dqn_to_int(ip)

    if '.' in mask:
        mask_num = dqn_to_int(mask)
    else:
        mask_num = cidr_to_int(int(mask))

    return ip_num, mask_num


def main():
    parser = optparse.OptionParser()
    parser.add_option('-t', '--template', action='store')
    opts, args = parser.parse_args()

    if not len(args):
        sys.exit('error: subnet missing')

    if opts.template:
        try:
            f = open(opts.template, 'r')
            lines = [l.strip() for l in f if not l.startswith('#')]
        except IOError:
            sys.exit('error: failed to read template: %s' % opts.template)

    for subnet in args:
        try:
            ip_num, mask_num = parse_subnet(subnet)
        except (ValueError, socket.error):
            sys.exit('error: invalid subnet string: %s' % subnet)

        if opts.template:
            for ip in ip_generator(ip_num, mask_num):
                print '\n'.join((l.replace(IP_IDENT, ip) for l in lines))
        else:
            print '\n'.join(ip_generator(ip_num, mask_num))

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit('Aborting.')
