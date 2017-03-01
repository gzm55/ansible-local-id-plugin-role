local_id_plugin
===============

A lookup plugin for getting the user id or name of the current ansible process.

Requirements
------------

Ansible >= 2.0

Role Variables
--------------

N/A

Dependencies
------------

N/A

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: gzm55.local_id_plugin }
      tasks:
         - debug: msg="current effective user is {{ lookup('id', 'euname') }}"

License
-------

BSD
