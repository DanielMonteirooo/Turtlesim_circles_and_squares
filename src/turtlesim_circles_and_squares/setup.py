from setuptools import find_packages, setup

package_name = 'turtlesim_circles_and_squares'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    py_modules=['scripts.move_turtles'],
    data_files=[
        ('share/' + package_name + '/launch', ['launch/turtlesim_launch.py']),
        # Include package.xml and resource files
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='dani',
    maintainer_email='dmonteiro117@gmail.com',
    description='Pacote para mover tartarugas em círculos e quadrados no Turtlesim',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'move_turtles = scripts.move_turtles:main',
        ],
    },
)
