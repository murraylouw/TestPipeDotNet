from jinja2 import Template
import math
import numpy

# All Euler angles are in XYZ convention. X first, then Y, then Z axis rotations. Also called Tait-Bryan XYZ.

class Vector3:
    def __init__(self,X,Y,Z):
        self.X = X
        self.Y = Y
        self.Z = Z

base_data = { 
    'link_name'     : 'base',
    'x' : 0,
    'y' : 0,
    'z' : 0,
    'eulerX' : math.radians(0),
    'eulerY' : math.radians(0),
    'eulerZ' : math.radians(0),
    'mass' : 1000000,
    'mesh_filepath' : 'meshes/base.dae',   
    'enableCollision' : True,
    'colour' : 'Grey'
}
link_1_data = { 
    'link_name'     : 'link_1',
    'x' : 0,
    'y' : 0,
    'z' : 0,
    'eulerX' : math.radians(0),
    'eulerY' : math.radians(0),
    'eulerZ' : math.radians(0),
    'mass' : 10,
    'mesh_filepath' : 'meshes/link_1.dae', 
    'enableCollision' : False,
    'colour' : 'Blue'  
}
link_2_data = { 
    'link_name'     : 'link_2',
    'x' : 0,
    'y' : -0.20,
    'z' : -0.530,
    'eulerX' : math.radians(0),
    'eulerY' : math.radians(0),
    'eulerZ' : math.radians(0),
    'mass' : 10,
    'mesh_filepath' : 'meshes/link_2.dae', 
    'colour' : 'Orange'    
}
link_3_data = { 
    'link_name'     : 'link_3',
    'x' : 0,
    'y' : -0.20,
    'z' : -(0.53 + 1.16),
    'eulerX' : 0,
    'eulerY' : 0,
    'eulerZ' : 0,
    'mass' : 10,
    'mesh_filepath' : 'meshes/link_3.dae',  
    'colour' : 'Grey'   
}
link_4_data = { 
    'link_name'     : 'link_4',
    'x' : 0,
    'y' : -1.45,
    'z' : -(0.53 + 1.16 + 0.23),
    'eulerX' : 0,
    'eulerY' : 0,
    'eulerZ' : 0,
    'mass' : 10,
    'mesh_filepath' : 'meshes/link_4.dae', 
    'colour' : 'Blue'    
}
link_5_data = { 
    'link_name'     : 'link_5',
    'x' : 0,
    'y' : -1.45,
    'z' : -(0.53 + 1.16 + 0.23),
    'eulerX' : 0,
    'eulerY' : 0,
    'eulerZ' : 0,
    'mass' : 10,
    'mesh_filepath' : 'meshes/link_5.dae',   
    'colour' : 'Orange'  
}
link_6_data = { 
    'link_name'     : 'link_6',
    'x' : 0,
    'y' : -1.675,
    'z' : -1.92,
    'eulerX' : 0,
    'eulerY' : 0,
    'eulerZ' : 0,
    'mass' : 10,
    'mesh_filepath' : 'meshes/link_6.dae',   
    'colour' : 'Grey'  
}

joint_1_data = {
    'joint_name' : 'joint_1',
    'parent_link' : 'base',
    'child_link' : 'link_1',
    'x' : 0,
    'y' : 0,
    'z' : 0,
    'eulerX' : math.radians(0),
    'eulerY' : math.radians(0),
    'eulerZ' : math.radians(0),
    'joint_axis' : '0 0 1',    
    'limit_effort' : 300,
    'lower_limit' : -2.96705972839,
    'upper_limit' : 2.96705972839,
    'velocity_limit' : 10
}
joint_2_data = {
    'joint_name' : 'joint_2',
    'parent_link' : 'link_1',
    'child_link' : 'link_2',
    'x' : 0,
    'y' : 0.2,
    'z' : 0.53,
    'eulerX' : math.radians(0),
    'eulerY' : math.radians(0),
    'eulerZ' : math.radians(0),
    'joint_axis' : '1 0 0',    
    'limit_effort' : 300,
    'lower_limit' : -2.96705972839,
    'upper_limit' : 2.96705972839,
    'velocity_limit' : 10
}
joint_3_data = {
    'joint_name' : 'joint_3',
    'parent_link' : 'link_2',
    'child_link' : 'link_3',
    'x' : 0,
    'y' : 0,
    'z' : 1.16,
    'eulerX' : math.radians(0),
    'eulerY' : math.radians(0),
    'eulerZ' : math.radians(0),
    'joint_axis' : '1 0 0',    
    'limit_effort' : 300,
    'lower_limit' : -2.96705972839,
    'upper_limit' : 2.96705972839,
    'velocity_limit' : 10
}
joint_4_data = {
    'joint_name' : 'joint_4',
    'parent_link' : 'link_3',
    'child_link' : 'link_4',
    'x' : 0,
    'y' : 1.25,
    'z' : 0.23,
    'eulerX' : math.radians(0),
    'eulerY' : math.radians(0),
    'eulerZ' : math.radians(0),
    'joint_axis' : '0 1 0',    
    'limit_effort' : 300,
    'lower_limit' : -2.96705972839,
    'upper_limit' : 2.96705972839,
    'velocity_limit' : 10
}
joint_5_data = {
    'joint_name' : 'joint_5',
    'parent_link' : 'link_4',
    'child_link' : 'link_5',
    'x' : 0,
    'y' : 0,
    'z' : 0,
    'eulerX' : math.radians(0),
    'eulerY' : math.radians(0),
    'eulerZ' : math.radians(0),
    'joint_axis' : '1 0 0',    
    'limit_effort' : 300,
    'lower_limit' : -2.96705972839,
    'upper_limit' : 2.96705972839,
    'velocity_limit' : 10
}
joint_6_data = {
    'joint_name' : 'joint_6',
    'parent_link' : 'link_5',
    'child_link' : 'link_6',
    'x' : 0,
    'y' : 0.225,
    'z' : 0,
    'eulerX' : math.radians(0),
    'eulerY' : math.radians(0),
    'eulerZ' : math.radians(0),
    'joint_axis' : '0 1 0',    
    'limit_effort' : 300,
    'lower_limit' : -2.96705972839,
    'upper_limit' : 2.96705972839,
    'velocity_limit' : 10
}

linkTemplate = '''
    <link name="{{ link_name }}">
        <inertial>
            <mass value="{{ mass }}"/>
            <inertia ixx="100"  ixy="0"  ixz="0" iyy="100" iyz="0" izz="100" />
	    </inertial>
        <visual>
            <origin xyz="{{ x }} {{ y }} {{ z }}" rpy="{{ eulerX }} {{ eulerY }} {{ eulerZ }}"/>
            <geometry>
                <mesh filename="{{ mesh_filepath }}"/>
            </geometry>
            <material name="{{ colour }}"/>
        </visual>
        {% if enableCollision %}
        <collision>
            <geometry>
                <mesh filename="{{ mesh_filepath }}"/>
            </geometry>
        </collision>
        {% endif %}
    </link>  
    '''


jointTemplate = '''
    <joint name="{{ joint_name }}" type="revolute">
        <parent link="{{ parent_link }}"/>
        <child link="{{ child_link }}"/>
        <origin xyz="{{ x }} {{ y }} {{ z }}" rpy="{{ eulerX }} {{ eulerY }} {{ eulerZ }}"/>
        <axis xyz="{{ joint_axis }}"/>
        <limit effort="{{ limit_effort }}" lower="{{ lower_limit }}" upper="{{ upper_limit }}" velocity="{{ velocity_limit }}"/>
        <dynamics damping="0.5"/>
    </joint>
'''

fileTemplate = '''
<?xml version="1.0" ?>

<robot name="kawasaki">
    
    <!-- Import Rviz colors -->
    <material name="Grey">
        <color rgba="0.2 0.2 0.2 1.0"/>
    </material>
    <material name="Orange">
        <color rgba="1.0 0.423529411765 0.0392156862745 1.0"/>
    </material>
    <material name="Blue">
        <color rgba="0.5 0.7 1.0 1.0"/>      
    </material>
    
    {{ base }}
    {{ link_1 }}
    {{ link_2 }}
    {{ link_3 }}
    {{ link_4 }}
    {{ link_5 }}
    {{ link_6 }}
      

    {{ joint_1 }} 
	{{ joint_2 }} 
	{{ joint_3 }} 
	{{ joint_4 }} 
	{{ joint_5 }} 
	{{ joint_6 }} 
	
	
</robot>
'''

# {{ link_3 }}
#     {{ link_4 }}
#     {{ link_5 }}
#     {{ link_6 }} 
# {{ joint_3 }} 
# 	{{ joint_4 }} 
# 	{{ joint_5 }} 
# 	{{ joint_6 }} 

 
file_template_data = {
    'base' : Template(linkTemplate).render(base_data),
    'link_1' : Template(linkTemplate).render(link_1_data),
    'link_2' : Template(linkTemplate).render(link_2_data),
    'link_3' : Template(linkTemplate).render(link_3_data),
    'link_4' : Template(linkTemplate).render(link_4_data),
    'link_5' : Template(linkTemplate).render(link_5_data),
    'link_6' : Template(linkTemplate).render(link_6_data),
    
    'joint_1' : Template(jointTemplate).render(joint_1_data),
    'joint_2' : Template(jointTemplate).render(joint_2_data),
    'joint_3' : Template(jointTemplate).render(joint_3_data),
    'joint_4' : Template(jointTemplate).render(joint_4_data),
    'joint_5' : Template(jointTemplate).render(joint_5_data),
    'joint_6' : Template(jointTemplate).render(joint_6_data)
    
}

fileString = Template(fileTemplate).render(file_template_data)

# Write to file
filename = "kawasaki_BX200L/kawasaki_BX200L.urdf"
f = open(filename, "w")
f.write(fileString)
f.close()

print("Generated file: " + filename)