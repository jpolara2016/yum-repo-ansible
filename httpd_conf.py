#!/usr/bin/python

old1 = "DocumentRoot \"/var/www/html\""
new1 = "DocumentRoot \"/mnt/localrepo\""

old2 = """<Directory />
    AllowOverride none
    Require all denied
</Directory>"""

new2 = """<Directory />
    Options All Indexes FollowSymLinks
    AllowOverride None
    Require all granted
</Directory>"""


def httpd_conf(file):

    with open(file) as f:
        newString1 = f.read().replace(old1, new1)
        f.close()

    with open(file, 'w') as f:
        f.write(newString1)
        f.close()

    with open(file) as f:
        newString2 = f.read().replace(old2, new2)
        f.close()

    with open(file, 'w') as f:
        f.write(newString2)
        f.close()


httpd_conf("/etc/httpd/conf/httpd.conf")