import os, sys

from distutils.core import setup
from distutils.version import StrictVersion
from glob import glob

def get_files(path):
    files = []
    elements = glob(path + '/*')
    for elem in elements:
        if os.path.isdir(elem):
            files.extend(get_files(os.path.join(elem)))
        else:
            files.append(os.path.join(elem))
    return files

data_dirs = ('songs', 'themes')

data_files = []
for data_dir in data_dirs:
    data_files.extend(get_files(data_dir))

setup_data_files = []
for file in data_files:
    setup_data_files.append(('share/games/canta/media/'+os.path.dirname(file), [file]))


setup(	name = 'canta-media',
    description = "Canta is a 3D karaoke plattform for fun and education",
    url = "http://www.canta-game.org",
    author="Andreas Kattner, Felix R. Lopez, Stefan Huchler",
    author_email="andreas@canta-game.org, felix@canta-game.org, stefan@canta-game.org",
    data_files = setup_data_files,
)
