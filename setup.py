from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from setuptools import setup

setup(
    name='CompetSMAC',
    version='0.1',
    description='Competitive SMAC - Competitive StarCraft Multi-Agent Challenge.',
    long_description="""CompetSMAC - Competitive StarCraft Multi-Agent Challenge - https://github.com/paleroy/competSmac""",
    author='Pascal Leroy',
    author_email='pleroy@uliege.be',
    license='MIT License',
    url='https://github.com/paleroy/competSmac',
    packages=[
        'smac',
        'smac.env',
        'smac.env.starcraft2',
        'smac.env.starcraft2.maps',
        'smac.bin',
        'smac.examples',
    ],
    install_requires=[
        'pysc2==3.0.0',
        's2protocol==5.0.8.86383.1',
        'protobuf == 3.6.1',
        'absl-py>=0.1.0',
        'numpy>=1.10',
    ],
)
