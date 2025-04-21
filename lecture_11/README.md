Notes
-----

* Install python3.8+ in order to run given examples.
* Shell scripts `(*.sh)` work with POSIX shell and won't work with Windows (maybe WSL might help)

Install dependencies
--------------------

Install python dependencies for scipts:

```sh
pip install -r requirements.txt
```

or

```sh
python3 -m pip install -r requirements.txt
```

Install python dependencies for tests:

```sh
pip install -r test_requirements.txt
```

or

```sh
python3 -m pip install -r test_requirements.txt
```

Run scripts
-----------

python3 quadratic.py 1 -5 6
python3 nbu_xchange.py USD UAH 1000

Run tests
---------

pytest .
