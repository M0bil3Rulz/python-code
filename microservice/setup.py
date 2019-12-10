from os import path
from setuptools import setup

here = path.abspath(path.dirname(__file__))

setup(
        name='integration_testing',
        version='0.0.1',

        description='Integration Tests',

        author='Some User Name',
        author_email='some.user.email@invalid.com',

        packages=["scripts", "integration", "integration.utils"],

        install_requires=['coloredlogs', 'requests', 'urlparse2'],

        tests_require=['pytest', 'mock', 'testfixtures', 'coverage'],

        entry_points={
            'console_scripts': [
                'integration_testing = scripts.integration_testing:integration_testing',
            ],
        },
)
