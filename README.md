# create-playbook

A cli tool for creating Ansible playbook skeletons.  Installing create-playbook
in a virtual environment will give you access to the cli command `create-playbook`.

    create-playbook --help

    create-playbook <playbook-name> <role-1> <role-2> ... <role-n>

NOTE: <playbook-name> must be a path that doesn't reference a current file or
      directory.  A new directory and it's parent directories will be made for
      the playbook skeleton.