# Ansible example based on Vagrant

Getting started
---------------

1. Install `vagrant` from https://www.vagrantup.com.
2. Install `ansible`, [instructions](http://docs.ansible.com/ansible/intro_installation.html#installing-the-control-machine).
3. Get the source code of this repo.
4. Copy `Vagrantfile.dist` to `Vagrantfile` and run `vagrant up`

Uncomment `#ansible.verbose  = true` to increase verbosity.

Handcrafted module usage example
--------------------------------

This repo contains simplest example modules, which is written in different languages.

### `Python`:

    $ ansible                                                                \
        -i .vagrant/provisioners/ansible/inventory/vagrant_ansible_inventory \
        -m example_python_module.py                                          \
        nginx                                                                \

### `Bash`:

    $ ansible                                                                \
        -i .vagrant/provisioners/ansible/inventory/vagrant_ansible_inventory \
        -m example_bash_module.bash                                          \
        nginx                                                                \

### `PHP`:

    $ ansible                                                                \
        -i .vagrant/provisioners/ansible/inventory/vagrant_ansible_inventory \
        -m example_php_module.php                                            \
        nginx                                                                \
