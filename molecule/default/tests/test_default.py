import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_ipsec_file(host):
    ipsec = host.file('/usr/local/sbin/ipsec')

    assert ipsec.exists


def test_ipsec_secrets_file(host):
    ipsec_conf = host.file('/etc/ipsec.conf')

    assert ipsec_conf.exists
    assert ipsec_conf.user == 'root'
    assert ipsec_conf.group == 'root'


def test_ipsec_conf_file(host):
    ipsec_secrets = host.file('/etc/ipsec.secrets')

    assert ipsec_secrets.exists
    assert ipsec_secrets.user == 'root'
    assert ipsec_secrets.group == 'root'
