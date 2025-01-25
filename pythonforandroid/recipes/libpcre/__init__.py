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


class LibpcreRecipe(Recipe):
    version = '8.44'
    url = 'https://ftp.pcre.org/pub/pcre/pcre-{version}.tar.bz2'

    built_libraries = {'libpcre.so': '.libs'}

    def build_arch(self, arch: 'Arch'):
        env = self.get_recipe_env(arch)

        with current_directory(self.get_build_dir(arch.arch)):
            shprint(
                sh.Command('./configure'),
                *'''--host=arm-linux-androideabi
                    --disable-cpp --enable-jit --enable-utf8
                    --enable-unicode-properties'''.split(),
                _env=env)
            shprint(sh.make, '-j', str(cpu_count()), _env=env)

    def get_lib_dir(self, arch: 'Arch'):
        return join(self.get_build_dir(arch), '.libs')


recipe = LibpcreRecipe()
