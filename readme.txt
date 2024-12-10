Como executar o Script:

1= Abra o terminal no my_workspace
2= Execute o codigo:

colcon build
source /opt/ros/humble/setup.bash
source install/setup.bash

3:Depois execute:

source /opt/ros/humble/setup.bash
source install/setup.bash
ros2 launch turtlesim_circles_and_squares turtlesim_launch.py

4:Abra um outro terminal, e execute:

source /opt/ros/humble/setup.bash
source install/setup.bash
ros2 run turtlesim_circles_and_squares move_turtles

Assim abrirá 2 janelas com tartarugas andando formando circulos e quadrados.(turtlesim_circles_and_squares)