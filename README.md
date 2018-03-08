# checkout_code
Tool to checkout a specific commit to a unique location

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
