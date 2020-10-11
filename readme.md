### Getting started

![spiral](spiral.png)

create python virtual environment named `venv`

```shell
python3 -m venv './venv'
```

activate virtual environment with `source './venv/bin/activate'`

update pip

```shell
pip install --upgrade pip setuptools wheel
```

install library `pystdlib`

```shell
pip install git+ssh://git@github.com/ibqn/pystdlib.git
```

test that the library was installed correctly by executing the following command

```shell
python -c 'import pystdlib; print("ok")'
```

to deactivate venv run `deactivate`

## Git

create new repository by running `git init` and check its status with `git status`
