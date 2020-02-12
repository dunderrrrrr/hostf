hosts_file = "/etc/hosts"


def read_hosts():
    f = open(hosts_file, 'r')
    for line in f:
        print(line.rstrip())


def add_host(ip, hostname):
    try:
        file_object = open(hosts_file, 'a')
        file_object.write('\n{}\t{}'.format(ip, hostname))
        file_object.close()
    except Exception as E:
        print(E)
        sys.exit(0)


def del_host(ip):
    try:
        with open(hosts_file,"r+") as f:
            new_f = f.readlines()
            f.seek(0)
            for line in new_f:
                if ip not in line:
                    f.write(line)
            f.truncate()
        clear_lines()
    except Exception as E:
        print(E)
        sys.exit(0)


def clear_lines():
    with open(hosts_file) as in_file, open(hosts_file, 'r+') as out_file:
        out_file.writelines(line for line in in_file if line.strip())
        out_file.truncate()
