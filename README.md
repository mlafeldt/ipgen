ipgen
=====

Simple command-line tool to generate IP addresses.


Usage
-----

Generate all IP addresses of a Class C network:

    $ ipgen 192.168.0.0/255.255.255.0
    192.168.0.0
    192.168.0.1
    192.168.0.2
    ...
    192.168.0.253
    192.168.0.254
    192.168.0.255

Lazy people can use the CIDR notation:

    $ ipgen 10.0.0.0/16
    10.0.0.0
    10.0.0.1
    10.0.0.2
    ...
    10.0.255.253
    10.0.255.254
    10.0.255.255

You can pass it as many subnets as you want:

    $ ipgen 192.168.0.0/30 1.2.3.4/32 10.0.0.0/255.255.255.128
    192.168.0.0
    192.168.0.1
    192.168.0.2
    192.168.0.3
    1.2.3.4
    10.0.0.0
    10.0.0.1
    10.0.0.2
    ...
    10.0.0.125
    10.0.0.126
    10.0.0.127

TODO: show templating example


License
-------

See LICENSE file.


Contact
-------

* Web: <https://github.com/misfire/ipgen>
* Mail: <mathias.lafeldt@gmail.com>
