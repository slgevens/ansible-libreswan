Ansible role for libreswan
===========================

Context
========

Install, configure and start/stop libreswan tunnels

Playbook
==========
::

   ---
   - hosts: all
     gather_facts: True

     vars:
       nss_defined_password: True #defined to true only the first launch on a node
       nss_db_password: somepassword # should be encrypted obviously
   
       rsa_key_file: rsa_key
       ca_nickname: evens
       ca_subject: epiconcept
       ca_trusttargs: TC,C,T
       ca_issuer: evens
   
       cert: False #To set to true if you want to create required cert with the information set above
   
       secret_passwd:
         - { user: evens, password: solignac, connection: xauth }
	 - { user: evens, password: soligna2c, connection: xauth }
	 - { user: evens, password: soligna1c, connection: xauth }
	   #should be encryted obviously
     
       protostack: netkey
       plutostderrlog: /var/log/pluto.log

       setup_items: |- #to add some items on global configuration
         ikev2=insist

       tunnel_configuration: #to create your subnets, tunnels...
         - conn_name: evens
	   conn_items: |-
	     some more items

     tasks:
   
       - include_role: name=ansible-libreswan
         become: True
         environment: "{{ proxy_env }}"
	   
License
========

`MIT <./LICENSE>`_

Author
=======

Evens SOLIGNAC
