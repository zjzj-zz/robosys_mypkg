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

- [greeting_talker.cpp](https://github.com/zjzj-zz/robosys_mypkg/blob/main/src/greeting_talker.cpp)のノードから送られた挨拶を[greeting_listener.cpp](https://github.com/zjzj-zz/robosys_mypkg/blob/main/src/greeting_listener.cpp)で受信して表示するlaunchファイルです。 
- c++同士の通信を行います。

- 次のコマンドで起動します。

  ```bash
  roslaunch robosys_mypkg cpp_greeting.launch
  ```

- 個別で実行を確認する場合には以下のコマンドを別々の端末で実行します。

  ```bash
  roscore 
  rosrun robosys_mypkg greeting_talker 
  rosrun robosys_mypkg greeting_listener
  ```

### [py_greeting.launch](https://github.com/zjzj-zz/robosys_mypkg/blob/main/launch/py_greeting.launch)

- [greeting_talker.cpp](https://github.com/zjzj-zz/robosys_mypkg/blob/main/src/greeting_talker.cpp)のノードから送られた挨拶を[greeting_listener_py.py](https://github.com/zjzj-zz/robosys_mypkg/blob/main/scripts/greeting_listener_py.py)で受信して表示するlaunchファイルです。 
- c++とpythonのノード間で通信を行います。

- 次のコマンドで起動します。

  ```bash
  roslaunch robosys_mypkg py_greeting.launch
  ```

- 個別で実行を確認する場合には以下のコマンドを別々の端末で実行します。

  ```bash
  roscore
  rosrun robosys_mypkg greeting_talker
  rosrun robosys_mypkg greeting_listener_py.py
  ```
### [calculator.launch](https://github.com/zjzj-zz/robosys_mypkg/blob/main/launch/calculator.launch)

- 簡単な四則演算を行うlaunchファイルです。
- 1 + 1 のように＜数値＞spece＜演算子＞spece＜数値＞の入力から答えを出力します。

- 次のコマンドで起動します。

  ```bash
  roslaunch robosys_mypkg calculator.launch
  ```

- 個別で実行を確認する場合には以下のコマンドを別々の端末で実行します。

  ```bash
  roscore
  rosrun robosys_mypkg input.py
  rosrun robosys_mypkg calculate.py
  rosrun robosys_mypkg output.py
  ```

- 実行方法は[input.py](https://github.com/zjzj-zz/robosys_mypkg/blob/main/scripts/input.py)を起動した端末に、`1 + 1`のように入力します。[calculate.py](https://github.com/zjzj-zz/robosys_mypkg/blob/main/scripts/calculate.py)で計算した結果が[output.py](https://github.com/zjzj-zz/robosys_mypkg/blob/main/scripts/output.py)を起動した端末に`data: 2.0`のように表示されます。

- このlaunchファイルで扱える演算は`+ - * /`です。

## デモ動画

- 実際に実行したときの動画はこちらです。

[![](https://img.youtube.com/vi/qLvJ595EBtI/0.jpg)](https://www.youtube.com/watch?v=qLvJ595EBtI)

## 著者

[Hikaru Jitsukawa](https://github.com/zjzj-zz)

ROSセットアップに関して：
[Ryuichi Ueda](https://github.com/ryuichiueda)

## ライセンス

[BSD 3-Clause "New" or "Revised" License](https://github.com/zjzj-zz/robosys_mypkg/blob/main/LICENSE)
