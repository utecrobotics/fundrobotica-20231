#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import JointState

if __name__ == "__main__":
  
  rospy.init_node("jointsNode") 
  pub = rospy.Publisher('joint_states', JointState, queue_size=1)
  
  # Nombres de las articulaciones
  jnames = ("head_pan", "right_j0", "right_j1", "right_j2", "right_j3","right_j4", "right_j5", "right_j6")
  # Configuracion articular deseada (en radianes)
  jvalues = [0, 0, -0.78, 0, 1.57, 0, 0.78, 0]

  # Objeto (mensaje) de tipo JointState
  jstate = JointState()
  # Asignar valores al mensaje
  jstate.header.stamp = rospy.Time.now()
  jstate.name = jnames
  jstate.position = jvalues
  
  # Frecuencia del envio (en Hz)
  rate = rospy.Rate(100)

  # Bucle de ejecucion continua
  while not rospy.is_shutdown():

    # Tiempo actual (necesario como indicador para ROS)
    jstate.header.stamp = rospy.Time.now()
    # Publicar mensaje
    pub.publish(jstate)
    # Esperar hasta la siguiente iteracion
    rate.sleep()
