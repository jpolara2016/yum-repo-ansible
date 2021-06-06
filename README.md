# Create YUM repo server using Ansible

This is to show how you can create YUM repo server with Apache(httpd) on Linux using Ansible.

### Requirements
1. At least 2 Linux VMs, CentOS or AmazonLinux (1 YUM repo server & 1 client machine).
2. You need to assign public IP to YUM server if you will be accessing this repo over the Internet and make sure to change the ip/hostname in the plabook for `hosts: yum-client` block.
3. Assure you have SSH access to the servers you run this playbook to.

### Commands
```json
git clone https://github.com/jpolara2016/yum-repo-ansible.git
cd yum-repo-ansible
ansible-playbook -i inventory yum_repo.yml
```

### Validation
1. http://18.234.132.162/
2. Install tree on the client machine
    ```yum install tree --disablerepo="*" --enablerepo=localrepo```
