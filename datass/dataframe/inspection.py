import pandas as pd


def df_value_counts(df):
    """
    Generalizes pd.value_counts() to all columns

    param pandas.DataFrame df: dataframe
    """
    print('>> Value counts:\n')
    for c in df.columns:
        print(f'# {c}:\n{df[c].value_counts()}\n\n')


def df_describe(df):
    """
    Generalizes pd.describe() to all columns

    param pandas.DataFrame df: dataframe
    """
    print('>> Describe columns:\n')
    for c in df.columns:
        print(f'# {c}:\n{df[c].describe()}\n\n')


def df_isnull(df):
    """
    Generalizes pd.isnull() to all columns

    param pandas.DataFrame df: dataframe
    """
    print('>> Null registers:\n')
    for c in df.columns:
        cnt = df[pd.isnull(df[c])].shape[0]
        if cnt == 0:
            print(f'# {c}: 0 null rows')
        else:
            print(f'# {c}: {cnt} rows')


def df_total_amazing_inspection(df):
    """
    Runs an amazing inspection

    :param pandas.DataFrame df: dataframe
    :returns:
    :rtype:
    :raises:
    """
    pass
