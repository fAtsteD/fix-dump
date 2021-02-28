# Fix dump mysql

Fix dump .sql file for wp with some bad dumping and further using in mysql, for example locally.

## Run script

Use python and run

```bash
python src/app.py [path to file for changing] [old domain] [new domain]
```

## Filters

-   Percentage filter - find percentage corresponding text and change its to '%'
-   Domain filter - need old and new domain for changing. It also change serialized php object right.
