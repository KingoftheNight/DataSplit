from setuptools import setup
from datasplit.__init__ import version

setup(name='datasplit',
    version=version,
    description='A tool for viewing and spliting data sets',
    url='https://github.com/KingoftheNight/DataSplit',
    author='Liang YC',
    author_email='1694822092@qq.com',
    license='BSD 2-Clause',
    packages=['datasplit'],
    install_requires=['PyQt5'],
    entry_points={
        'console_scripts': [
        'datasplit=datasplit.__main__:datasplit',
            ]
        },
    python_requires=">=3.6",
    include_package_data=True,
    zip_safe=True)
