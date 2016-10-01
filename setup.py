from setuptools import setup

setup(
    name='Anonymous Voter',
    version='0.1',
    long_description=__doc__,
    packages=['annon_voter',
              'annon_voter_site'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask']
)
