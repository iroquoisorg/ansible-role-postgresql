import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_postgresql_is_installed(host):
    assert host.package("postgresql-11").is_installed
    assert host.package("postgresql-client-11").is_installed
    assert host.package("postgresql-common").is_installed


def test_postgresql_is_running(host):
    postgresql = host.process.filter(user="postgres", comm="postgres")

    assert len(postgresql) >= 5

def test_if_postgresql_listens_on_tcp_port(host):
    assert host.socket('tcp://127.0.0.1:5432').is_listening
