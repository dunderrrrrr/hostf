![hostf](/img/hostf.png?raw=true)  

Sometimes you need to manage your hosts file `/etc/hosts`.  
Some do it on a daily basis.  

This Python script will do it for you faster than lightning :zap: :sparkles:

## Installing
Clone and cd into dir.
```sh
$ git clone git@github.com:dunderrrrrr/hostf.git && cd hostf/
```  

Add to `~/.bashrc`.
```shell
alias hostf='sudo /usr/bin/python3 /home/user/path/hostf/hostf.py'
```

Reload shell or restart terminal.
```
$ source ~/.bashrc
```

## Usage
### Add / delete / show records
```sh
$ hostf -a 10.1.1.50 example.com
```
```sh
$ hostf -d 10.1.1.50
```
```sh
$ hostf
127.0.0.1   localhost
10.1.1.5    test-serv
10.10.1.7   example.com
```

## Help
```sh
$ hostf -h
usage:
[ADD] hostf -a <ip> <hostname>
[DEL] hostf -d <ip>

hostf will manage /etc/hosts faster than lightning.

optional arguments:
  -h, --help            show this help message and exit
  -a 10.1.1.5 test.com  Add to hosts.
  -d 10.1.1.5           Delete from hosts.
```
