# OSC_demo
初年次ゼミで使用したpython-oscのデモコード

## RGB
### python requirements
```sh
pip install python-osc
pip install matplotlib
pip install threading
```

### 送信
送信と受信のtermnalは分けてください．
```sh
cd color
python osc_demo_color.py
```
### 受信
OSCで受信して，RGBを表示する．
```sh
cd color
python osc_demo_color_recieve.py
```

### logistic
### 送信
送信と受信のtermnalは分けてください．
```sh
cd logistic
python osc_demo_color.py
```
### 受信
OSCで受信して，送られてきたパラメーターをprintする．
```sh
cd logistic
python osc_demo_color_recieve.py
```
