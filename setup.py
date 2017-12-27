from setuptools import setup, find_packages


NAME = 'create_playbook'
VERSION = '0.1.0'
AUTHOR = 'James Hibbard'

setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    description='Create Ansible playbook skeletons',
    install_requires=[
        'Click'
    ],
    exta_requires={

    },
    packages=find_packages(),
    entry_points='''
        [console_scripts]
        create-playbook=scripts.playbook:make_skeleton
    ''',
)
