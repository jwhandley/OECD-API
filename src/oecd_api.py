import requests
from lxml import etree
import pandas as pd
import argparse


def get_data(dataset: str, filter=None):
    url = f"http://stats.oecd.org/restsdmx/sdmx.ashx/GetData/{dataset}"

    if filter is not None:
        url += f"/{filter}"

    url += "/all?format=compact_v2"
    response = requests.get(url)
    response.raise_for_status()

    return etree.fromstring(response.content, parser=None)


def parse_data(data) -> pd.DataFrame:
    dataset = data[1]
    observations: list[dict] = []
    for series in dataset:
        metadata: dict = dict(series.attrib)
        for obs in series:
            observation: dict = dict(obs.attrib)

            observations.append(metadata | observation)

    return pd.DataFrame(observations)


# not implemented
def query_builder(countries: list[str], series: list[str]) -> str:
    # TODO: build filter query from country and series list
    return ""


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='OECD API Utility',
        description='Simple CLI tool to download data from the OECD API and output it as a CSV',
    )

    parser.add_argument('-d', '--dataset')
    parser.add_argument('-f', '--filter')
    parser.add_argument('-o', '--output')

    args = parser.parse_args()

    print(args)

    xml = get_data(args.dataset, args.filter)
    df = parse_data(xml)

    df.to_csv(args.output)
