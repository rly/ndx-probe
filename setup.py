# -*- coding: utf-8 -*-

import os

from setuptools import setup, find_packages
from shutil import copy2

setup_args = {
    'name': 'ndx-probe',
    'version': '0.1.0',
    'description': 'An extension to hold metadata about a multi-electrode probe.',
    'author': 'Ryan Ly',
    'author_email': 'rly@lbl.gov',
    'url': '',
    'license': 'BSD 3-Clause',
    'install_requires': [
        'pynwb>=1.1.2'
    ],
    'packages': find_packages('src/pynwb'),
    'package_dir': {'': 'src/pynwb'},
    'package_data': {'ndx_probe': [
        'spec/ndx-probe.namespace.yaml',
        'spec/ndx-probe.extensions.yaml',
    ]},
    'classifiers': [
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
    ],
    'zip_safe': False
}


def _copy_spec_files(project_dir):
    ns_path = os.path.join(project_dir, 'spec', 'ndx-probe.namespace.yaml')
    ext_path = os.path.join(project_dir, 'spec', 'ndx-probe.extensions.yaml')

    dst_dir = os.path.join(project_dir, 'src', 'pynwb', 'ndx_probe', 'spec')
    if not os.path.exists(dst_dir):
        os.mkdir(dst_dir)

    copy2(ns_path, dst_dir)
    copy2(ext_path, dst_dir)


if __name__ == '__main__':
    _copy_spec_files(os.path.dirname(__file__))
    setup(**setup_args)
