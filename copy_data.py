#!/usr/bin/env python

from __future__ import print_function

import pandas as pd
pd.set_option('max_rows', 10)
import click
import os
import glob

@click.command()
@click.argument('source')
@click.argument('package')
@click.argument('destination')
def main(source, package, destination):
    #print("Copy from '%s' to '%s'" % (source, destination))
    #print(glob.glob(os.path.join(source, 'csv', package, '*.csv')))
    #print(glob.glob(os.path.join(source, 'doc', package, 'rst', '*.rst')))
    df = pd.read_csv(os.path.join(source, 'datasets.csv'))
    df = df[df['Package'] == package]
    print(df)

if __name__ == '__main__':
    main()
