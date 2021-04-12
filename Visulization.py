import sweetviz as sv
import pandas as pd
from pywebio import *
import csv
import re


def create_profile(df):
    with output.put_loading(shape='grow'):
        report = sv.analyze(df)
        report.show_html()

    with open('SWEETVIZ_REPORT.html', 'r') as f:
        html = f.read()
        output.put_html(html)


def content_to_pandas(content):
    with open('tmp.csv', 'w') as f:
        writer = csv.writer(f, delimiter='\t')
        for line in content:
            writer.writerow(re.split('\s+', line))

    return pd.read_csv("tmp.csv")


def app():
    file = input.file_upload("Upload your csv file.", accept='.csv')
    content = file['content'].decode('utf-8').splitlines()

    df = content_to_pandas(content)
    create_profile(df)


if __name__ == '__main__':
    start_server(app, port=8080, debug=True)
