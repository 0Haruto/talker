from setuptools import find_packages, setup

package_name = 'fifty_fifty'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Haruto Yamamoto',
    maintainer_email='s23c1146pp@s.chibakoudai.jp',
    description='a package for practice class',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'luck_clock = fifty_fifty.luck_clock:main' 
        ],
    },
)
