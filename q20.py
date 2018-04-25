#!/usr/bin/env python

import sys


def extract_host(line):
    return line.split()[0]


def increase_count(host_dict, host_addr):
    if host_addr in host_dict:
        host_dict[host_addr] += 1
    else:
        host_dict[host_addr] = 1


def read_hosts(infilename):
    res_dict = {}
    log_file = file(infilename)
    for line in log_file:
        if line.isspace():
            continue
        host_addr = extract_host(line)
        increase_count(res_dict, host_addr)
    return res_dict


def write_hosts(outfilename, host_dict):
    out_file = file(outfilename, "w")
    for host_addr, count in host_dict.iteritems():
        out_file.write("%s\t%d\n" % (host_addr, count))
    out_file.close()


def parse_cmd_line_args():
    if len(sys.argv) != 3:
        print("Usage: %s [infilename] [outfilename]" % sys.argv[0])
        sys.exit(1)
    return sys.argv[1], sys.argv[2]


def main():
    infilename = 'hosts_access_log_00.txt'
    outfilename = 'records_hosts_access_log_00.txt'

    host_dict = read_hosts(infilename)
    write_hosts(outfilename, host_dict)


if __name__ == "__main__":
    main()
