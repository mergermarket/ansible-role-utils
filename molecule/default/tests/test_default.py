import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')
    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_bind_utils_package_installed(host):
    assert host.package('bind-utils').is_installed


def test_telnet_package_installed(host):
    assert host.package('telnet').is_installed


def test_nmap_package_installed(host):
    assert host.package('nmap').is_installed
