from multiprocessing import cpu_count
from typing import TYPE_CHECKING

import sh

from pythonforandroid.archs import Arch
from pythonforandroid.logger import shprint
from pythonforandroid.recipe import Recipe
from pythonforandroid.util import current_directory

if TYPE_CHECKING:
    from pythonforandroid.archs import Arch



class PngRecipe(Recipe):
    name = 'png'
    version = '1.6.37'
    url = 'https://github.com/glennrp/libpng/archive/v{version}.zip'
    built_libraries = {'libpng16.so': '.libs'}

    def build_arch(self, arch: 'Arch'):
        build_dir = self.get_build_dir(arch.arch)
        with current_directory(build_dir):
            env = self.get_recipe_env(arch)
            shprint(
                sh.Command('./configure'),
                '--host=' + arch.command_prefix,
                '--target=' + arch.command_prefix,
                '--disable-static',
                '--enable-shared',
                '--prefix={}/install'.format(self.get_build_dir(arch.arch)),
                _env=env,
            )
            shprint(sh.make, '-j', str(cpu_count()), _env=env)


recipe = PngRecipe()
