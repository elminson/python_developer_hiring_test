#!/usr/bin/env python

import re


def checkIPs(ip_arrays):
    # Identifies the type of IP addresses (IPv4, IPv6, or "Neither").
    ipv4_pattern = get_ipv4_pattern()
    ipv6_pattern = get_ipv6_pattern()

    for ip_array in ip_arrays:
        if ipv4_pattern.match(ip_array):
            print('IPv4')
        elif ipv6_pattern.match(ip_array):
            print('IPv6')
        else:
            print('Neither')


def get_ipv4_pattern():
    # Compiles a regex pattern that matches IPv4 addresses.
    byte = '([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])'
    regex = '^{0}(\.{0}){{3}}$'.format(byte)
    pattern = re.compile(regex)
    return pattern


def get_ipv6_pattern():
    # Compiles a regex pattern that matches IPv6 addresses.
    hex_group = '[0-9A-Fa-f]{1,4}'  # Four hex digits
    regex = '^({0})(:{0}){{7}}$'.format(hex_group)
    pattern = re.compile(regex)
    return pattern


if __name__ == '__main__':
    ip_array_count = int(input())
    ip_arrays = (raw_input() for _ in range(ip_array_count))
    checkIPs(ip_arrays)
