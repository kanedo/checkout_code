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

