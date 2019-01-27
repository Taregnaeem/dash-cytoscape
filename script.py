import os
import requests


def request_and_update(url, filename):
    r = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(r.content)


github_url = 'https://raw.githubusercontent.com/plotly/dash-cytoscape/master/'

update_directory_list = [
    'demos/data',
    'demos/editor',
]

update_list = [
    'usage.py',
    'usage-advanced.py',
    'usage-elements.py',
    'usage-events.py',
    'usage-stylesheet.py',

    'demos/dash_reusable_components.py',
    'demos/usage-phylogeny.py',

    'demos/editor/__init__.py',
    'demos/editor/callbacks.py',
    'demos/editor/constants.py',
    'demos/editor/layout.py',

    'demos/data/sample_network.txt',
    'demos/data/apaf.xml'
]


if __name__ == '__main__':
    # Create new directories if needed
    for dir in update_directory_list:
        os.makedirs(dir)

    # Create new files, or update the files with the current master version
    for file in update_list:
        request_and_update(github_url + file, file)
