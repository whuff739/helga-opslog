from setuptools import setup, find_packages


version = '0.0.1'


setup(name="helga-opslog",
    version=version,
    description=('Helga plugin to record & recall opslog entries'),
    author='William Huff',
    author_email='whuff@pindrop.com',
    url='https://github.atl.pdrop.net/whuff/helga-opslog',
    packages=find_packages(),
    py_modules=['helga_opslog'],
    include_package_data=True,
    zip_safe=True,
    entry_points = dict(
        helga_plugins=[
            'opslog = helga_opslog:opslog'
        ],
    ),
)
