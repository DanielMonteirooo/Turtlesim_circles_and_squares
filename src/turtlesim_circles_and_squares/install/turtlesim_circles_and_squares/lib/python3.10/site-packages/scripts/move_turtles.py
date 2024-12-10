import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math

class TurtleMover(Node):
    def __init__(self):
        super().__init__('turtle_mover')
        
        # Publishers para ambas as tartarugas
        self.publisher_turtle1 = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.publisher_turtle2 = self.create_publisher(Twist, '/turtle2/cmd_vel', 10)

        # Timer para controle das tartarugas
        self.create_timer(0.1, self.move_turtles)

        self.t = 0  # Controlador de tempo para movimento em quadrado

    def move_turtles(self):
        # Movimento da tartaruga 1 (círculo)
        twist_circle = Twist()
        twist_circle.linear.x = 5.0  # Velocidade linear
        twist_circle.angular.z = 2.0  # Velocidade angular (círculo)
        self.publisher_turtle1.publish(twist_circle)

        # Movimento da tartaruga 2 (quadrado)
        twist_square = Twist()
        side_duration = 2.0  # Tempo para cada lado do quadrado
        if self.t < side_duration:
            twist_square.linear.x = 2.0  # Move em linha reta
            twist_square.angular.z = 0.0
        elif self.t < side_duration + 1.0:
            twist_square.linear.x = 5.0  # Velocidade linear maior
            twist_square.angular.z = math.pi
        else:
            self.t = 0  # Reinicia o contador após completar o lado

        self.publisher_turtle2.publish(twist_square)
        self.t += 0.1


def main(args=None):
    rclpy.init(args=args)
    node = TurtleMover()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
