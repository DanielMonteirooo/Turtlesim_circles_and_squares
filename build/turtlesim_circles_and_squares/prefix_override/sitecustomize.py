import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/dani/Estudos/codas/tac_robotica/my_workspace/install/turtlesim_circles_and_squares'
