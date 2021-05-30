# Patika Robotik Görevi
Bu görevde amaç başlangıç noktasından bir hedefe gidip geri gelmektir.  
AMCL paketinde "initial_pose=(10,10)" verilmiş ve (3,8) noktasında gidip geri gelmesi amaçlanmıştır.

## Kurulum ve Ayarlama

```bash
cd ~/
git clone https://github.com/Mky07/test_ws.git
cd ~/test_ws/
rosdep install --from-paths src --ignore-src -r -y # install needed dependency
source /opt/ros/melodic/setup.bash
cd src/
catkin_init_workspace
cd ..
catkin_make
```

```bash
gedit ~/.bashrc
```
bashrc dosyasının içine aşağıdaki satırı kopyala:
```
source ~/test_ws/devel/setup.bash
```

## Çalıştırma

```bash
### gazebo:
roslaunch mir_gazebo mir_maze_world.launch
rosservice call /gazebo/unpause_physics   # or click the "start" button in the Gazebo GUI

### localization:
roslaunch mir_navigation amcl.launch initial_pose_x:=10.0 initial_pose_y:=10.0

# navigation:
roslaunch mir_navigation start_planner.launch \
    map_file:=$(rospack find mir_gazebo)/maps/maze.yaml \
    virtual_walls_map_file:=$(rospack find mir_gazebo)/maps/maze_virtual_walls.yaml
rviz -d $(rospack find mir_navigation)/rviz/navigation.rviz
```
