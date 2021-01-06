# robosys_mypkg

ロボットシステム学演習課題2のROSパッケージです。

## 動作環境

以下の環境にて動作確認を行っています。

- ROS Noetic
  - OS: Ubuntu 20.04.1 LTS
  - Device: Raspberry Pi 4 Model B

## インストール方法

- [ros_setup_scripts_Ubuntu20.04_server](http://github.com/ryuichiueda/ros_setup_scripts_Ubuntu20.04_server)を参照しROSをインストールします。

- [ロボットシステム学第10回](https://ryuichiueda.github.io/robosys2020/lesson10_ros.html#/)を参照しワークスペースを準備します。

- `git`を使用して本パッケージをダウンロードします。

  ```bash
  cd ~/catkin_ws/src
  git clone https://zjzj-zz/robosys_mypkg.git
  ```

- `catkin_make`を使用して本パッケージをビルドします。

  ```bash
  cd ~/catkin_ws && catkin_make
  ```

## パッケージ概要

c++とpythonのコードのトピック間通信を行います。
簡単な四則演算を行います。

### [cpp_greeting.launch](https://github.com/zjzj-zz/robosys_mypkg/blob/main/launch/cpp_greeting.launch)

[greeting_talker.cpp](https://github.com/zjzj-zz/robosys_mypkg/blob/main/src/greeting_talker.cpp)のノードから送られた挨拶を[greeting_listener.cpp](https://github.com/zjzj-zz/robosys_mypkg/blob/main/src/greeting_listener.cpp)で受信して表示するlaunchファイルです。

次のコマンドで起動します。

```bash
roslaunch robosys_mypkg cpp_greeting.git
```
