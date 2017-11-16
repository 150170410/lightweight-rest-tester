import unittest

import click
import sys

from rest_tester.main import generate_test_functions, run_test_functions
from rest_tester.options import Options


class TestsContainer(unittest.TestCase):
    pass


@click.command()
@click.argument('test_suites_dir', type=click.Path(exists=True))
@click.option('--base_url', default=None, type=str, help='Base URL of API.')
@click.option('--auth_user', default=None, type=str, help='Authentication user information.')
@click.option('--auth_pass_file', default=None, type=str, help='Authentication password file.')
def main(test_suites_dir, base_url, auth_user, auth_pass_file):
    options = Options(base_url=base_url, auth_user=auth_user, auth_pass_file=auth_pass_file)

    generate_test_functions(TestsContainer, test_suites_dir, options)
    was_successful = run_test_functions(TestsContainer)
    if not was_successful:
        print('Testing was NOT successful!')
        sys.exit(1)
