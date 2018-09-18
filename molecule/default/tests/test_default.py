import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')
    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_docker_package_installed(host):
    assert host.package('docker').is_installed


def test_docker_pip_package_installed(host):
    packages = host.pip_package.get_packages()
    assert 'docker' in packages


def test_docker_config_exists(host):
    f = host.file('/etc/sysconfig/docker')
    assert f.exists


def test_docker_config_written(host):
    options = (
        'OPTIONS="--log-driver=json-file '
        '--log-opt max-size=50m '
        '--log-opt max-file=1 '
        '--default-ulimit '
        'nofile=4096:65535 '
        '--bip=172.17.42.1/16 '
        '--mtu=9001"'
    )
    output = host.check_output('cat /etc/sysconfig/docker')
    assert options in output


def test_docker_cron_exists(host):
    f = host.file('/etc/cron.hourly/docker-gc-dangling-volumes.sh')
    assert f.exists
