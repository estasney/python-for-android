from multiprocessing import cpu_count
from typing import TYPE_CHECKING

import sh

from pythonforandroid.archs import Arch
from pythonforandroid.logger import shprint
from pythonforandroid.recipe import Recipe
from pythonforandroid.util import current_directory

if TYPE_CHECKING:
    from pythonforandroid.archs import Arch



class LibIconvRecipe(Recipe):

    version = '1.16'

    url = 'https://ftp.gnu.org/pub/gnu/libiconv/libiconv-{version}.tar.gz'

    built_libraries = {'libiconv.so': 'lib/.libs'}

    def build_arch(self, arch: 'Arch'):
        env = self.get_recipe_env(arch)
        with current_directory(self.get_build_dir(arch.arch)):
            shprint(
                sh.Command('./configure'),
                '--host=' + arch.command_prefix,
                '--prefix=' + self.ctx.get_python_install_dir(arch.arch),
                _env=env)
            shprint(sh.make, '-j' + str(cpu_count()), _env=env)


recipe = LibIconvRecipe()
