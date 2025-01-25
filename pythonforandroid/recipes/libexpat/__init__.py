
from multiprocessing import cpu_count
from os.path import join
from typing import TYPE_CHECKING

import sh

from pythonforandroid.archs import Arch
from pythonforandroid.logger import shprint
from pythonforandroid.recipe import Recipe
from pythonforandroid.util import current_directory

if TYPE_CHECKING:
    from pythonforandroid.archs import Arch


class LibexpatRecipe(Recipe):
    version = 'master'
    url = 'https://github.com/libexpat/libexpat/archive/{version}.zip'
    built_libraries = {'libexpat.so': 'dist/lib'}
    depends = []

    def build_arch(self, arch: 'Arch'):
        env = self.get_recipe_env(arch)
        with current_directory(join(self.get_build_dir(arch.arch), 'expat')):
            dst_dir = join(self.get_build_dir(arch.arch), 'dist')
            shprint(sh.Command('./buildconf.sh'), _env=env)
            shprint(
                sh.Command('./configure'),
                '--host={}'.format(arch.command_prefix),
                '--enable-shared',
                '--without-xmlwf',
                '--prefix={}'.format(dst_dir),
                _env=env)
            shprint(sh.make, '-j', str(cpu_count()), _env=env)
            shprint(sh.make, 'install', _env=env)


recipe = LibexpatRecipe()
