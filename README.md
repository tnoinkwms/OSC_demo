# OSC_demo
初年次ゼミで使用したpython-oscのデモコード
```sh
git clone https://github.com/tnoinkwms/OSC_demo.git
```

# RGB
### python requirements
```sh
pip install python-osc
pip install matplotlib
pip install threading
```

### 送信
送信と受信のtermnalは分けてください．
```sh
cd ./osc_demo/color
python osc_demo_color.py
```
### 受信
OSCで受信して，RGBを表示する．
```sh
cd ./osc_demo/color
python osc_demo_color_recieve.py
```

# logistic
### python requirements
```sh
pip install python-osc
```

### 送信
送信と受信のtermnalは分けてください．
```sh
cd ./osc_demo/logistic
python osc_demo_send.py
```
### 受信
OSCで受信して，送られてきたパラメーターをprintする．
```sh
cd ./osc_demo/logistic
python osc_demo_recieve.py
```
