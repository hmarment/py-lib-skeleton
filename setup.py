try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()


config = {
    'name': 'py-lib-skeleton',
    'description': 'Skeleton project structure for Python Libraries (intended'
    'to be installed elsewhere, for use in other projects)',
    'long_description': open('README.md').read(),
    'author': 'Henry Marment',
    'url': '',
    'download_url': '',
    'author_email': 'henrymarment@gmail.com',
    'version': '0.0.1',
    'install_requires': requirements,
    'packages': find_packages(),
    'scripts': [],
    'include_package_data': True
}

setup(**config)
