# checkout_code
Tool to checkout a specific commit to a unique location

## installation

```
pip install .
```

## usage

```
checkout_code 
  --repository /path/to/git/repo
  --checkout-dir /path/to/version/location 
  -c commit_hash 
  --use-prefix
```

`--use-prefix` prefixes the directories in `checkout_dir` with the repository name

To get the final path use an additional `--get-path`, i.e.

```
checkout_code 
  --repository /path/to/git/repo
  --checkout-dir /path/to/version/location 
  -c commit_hash 
  --use-prefix
  --get-path
```
this will only print the path but **not** checkout the code. Its intendented to be used in a variable.


## example usage in scripts


```
source env/bin/activate
COMMIT="b59616685000ddb5583186bcb7fd4b3e3d481f19"
checkout_code --repository ~/src/sockeye --checkout-dir ~/work/sockeye/ -c $COMMIT --use-prefix
path=$(checkout_code --repository ~/src/sockeye --checkout-dir ~/work/sockeye/ -c $COMMIT --use-prefix --get-path)
export PYTHONPATH="$path:$PYTHONPATH"
```

## environment files

To make it easier to use you can also use [`.env`](https://github.com/theskumar/python-dotenv) files instead or in addition to CLI-options. You can specify the file by using `--env /path/to/.env/file` or it will [automatically search for files](https://github.com/theskumar/python-dotenv#getting-started). In the environment file just use
```
repository=/path/to/repo
checkout_dir=/path/to/checkout_dir
use_prefix=True
```
to specify your settings. 

**Note** command line arguments will always override environment settings


## version history

### 0.1 2018-03-08

* initial version

### 0.2 2018-03-08

* added file lock
* added requirements

### 0.3 2018-03-20

* added loading of env files