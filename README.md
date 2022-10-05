
![](etc/img/apple-touch-icon.png)

## [**Data** **S**cience **S**hortcutS - DataSS](https://htbrandao.github.io/datass/)

# About

I got tired of rewriting the same old data analysis functions again. For now on I'll write them in this package.

MIT License.

<br>

# Installation ([PyPI](https://pypi.org/project/datass/))

Download and install:

```bash
$ git clone https://gitlab.com/cqd-lab/datass.git
$ cd datass/
$ pip3 install -e .
```

or, install from PyPI:

```bash
$ pip3 install datass
```

or, install a specific version:

```bash
$ pip3 install datass==0.0.1
```

Create/update the live docs:
```bash
$ cd docs
$ make html
```

<br>

# Usage:

Example:

```python
>> import datass
>> import pandas as pd
>> df = pd.read_csv('some-file.csv')
# find null values
>> datass.dataframe.inspection.df_isnull(df)
# run value counts
>> datass.dataframe.inspection.df_value_counts(df)
# run describe
>> datass.dataframe.inspection.df_describe(df)
```

<br>

___
- Documentation created using [Sphinx](https://www.sphinx-doc.org/en/master/)
- Packaged using this [guide](https://packaging.python.org/tutorials/packaging-projects/)
- Bootstrap [theme](https://startbootstrap.com/theme/freelancer)

<br>

___
TODOs

\#  | ???
----|------
1   | keep on coding the actual module
2   | tests
3   | improve readme
