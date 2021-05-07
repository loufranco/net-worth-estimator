This script shows how to implement the spreadsheet desribed here:

https://loufranco.com/blog/very-simple-net-worth-estimator

As of May 2021, here is how I installed matplotlib on an M1 Mac:

I use pyenv and pip to install python, so these instructions require that.

Use at least Python 3.9.4:

```bash
pyenv install 3.9.4
```

Here's what I did to install matplotlib

```bash
python -m pip install cython
python -m pip install --no-cache-dir --no-binary :all: --no-use-pep517 numpy
python -m pip install -U matplotlib
```