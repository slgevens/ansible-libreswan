# ansible-libreswan

## Context

Install, configure and start/stop libreswan tunnels

## Usage

```yaml       
tasks:
  - include_role: name=ansible-libreswan
```

These extra vars should be used once with the required vars defined:
```console
ansible-playbook libreswan.yml -e create_ca_cert=True -e set_nssdb_secret=True -D
```

- `set_nssdb_secret` indicate that you want to create and set the secret for the DB

- `create_ca_cert=True` indicate that you want to create your own CA certificate

Otherwise, play it like that:
```console
ansible-playbook libreswan.yml -D
```

To start all the tunnel set in your playbook : 
```
ansible-playbook libreswan.yml -D -e libreswan_manage_start=True
```

## License

[MIT](./LICENSE)

## Author

[Evens SOLIGNAC](mailto:evenssolignac@live.fr)