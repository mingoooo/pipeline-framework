# pipeline-framework
[![Python3](https://img.shields.io/badge/python-3.6-green.svg?style=plastic)](https://www.python.org/)

pipeline framework for python.

input -> handle -> output

---

## 功能

编写输入、处理、输出模块，信息按管道顺序传递。


## 适用环境
- 消费队列
- 告警器
- 其他管道需求

## 使用

```
pip install -r requirements
python piper.py
```

## 自定义

添加自定义模块有以下约定：
- 需要继承包的BaseClass 

- 类名为包名的单数（如包名inputs，class就是Input）

- 实现run方法，管道将接收上一级run方法的return

- 配置文件（config/config.yml)增加相应workers配置

### Example:
#### 创建input
```
vim inputs/faker.py
```

```
from faker import Faker
from inputs import BaseInput


class Input(BaseInput):
    def __init__(self):
        self.fake = Faker()

    def run(self):
        return self.fake.name()

```

#### 创建handle
```
vim handles/pass.py
```

```
from handles import BaseHandle


class Handle(BaseHandle):
    def run(self, msg):
        return msg

```

#### 创建output
```
vim outputs/echo.py
```

```
from outputs import BaseOutput


class Output(BaseOutput):
    def __init__(self, prefix=''): # 参数可在实例化时传递
        self.prefix = prefix

    def run(self, msg):
        return self.prefix + msg

```

#### 修改配置文件
```
vim config/config.yml
```
```
log:
  log_path: test.log
  log_level: debug

workers:
  - input:
      name: faker
    handle:
      name: pass
    output:
      name: echo
      kwargs:
        prefix: Hello, # 要传递的参数
```

```
python piper.py
2018-04-20 17:37:42,037 [DEBUG] (worker): Create worker
2018-04-20 17:37:42,206 [DEBUG] (worker): Start worker
2018-04-20 17:37:42,206 [DEBUG] (worker): Input result: George Lane
2018-04-20 17:37:42,207 [DEBUG] (worker): Handle result: George Lane
2018-04-20 17:37:42,207 [DEBUG] (worker): Output result: Hello,George Lane
2018-04-20 17:37:42,407 [DEBUG] (worker): Input result: Bill Gonzalez
2018-04-20 17:37:42,407 [DEBUG] (worker): Handle result: Bill Gonzalez
2018-04-20 17:37:42,407 [DEBUG] (worker): Output result: Hello,Bill Gonzalez
2018-04-20 17:37:42,607 [DEBUG] (worker): Input result: Mark Walker
2018-04-20 17:37:42,607 [DEBUG] (worker): Handle result: Mark Walker
2018-04-20 17:37:42,607 [DEBUG] (worker): Output result: Hello,Mark Walker
```