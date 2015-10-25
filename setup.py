from setuptools import setup, find_packages

setup(
    name='SesameContract',
    version='0.1',
    description='Conditional decryption service',
    classifiers=[
      'Development Status :: 1 - Planning',
      'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
      'Programming Language :: Python :: 3.4',
    ],
    url='https://github.com/EaterOA/sesamecontract',
    author='Vincent Wong',
    author_email='duperduper@ucla.edu',
    license='GPL2',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'cryptography',
        'secretsharing',
    ],
    entry_points={
        'console_scripts': [
            'sesame-server = sesamecontract.sesameserver:main',
            'sesame = sesamecontract.sesame:main',
        ],
    },
)
