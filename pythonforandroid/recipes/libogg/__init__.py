from typing import TYPE_CHECKING

import sh

from pythonforandroid.archs import Arch
from pythonforandroid.recipe import Recipe
from pythonforandroid.toolchain import current_directory, shprint

if TYPE_CHECKING:
    from pythonforandroid.archs import Arch



class OggRecipe(Recipe):
    version = '1.3.3'
    url = 'http://downloads.xiph.org/releases/ogg/libogg-{version}.tar.gz'
    built_libraries = {'libogg.so': 'src/.libs'}

    def build_arch(self, arch: 'Arch'):
        with current_directory(self.get_build_dir(arch.arch)):
            env = self.get_recipe_env(arch)
            flags = [
                '--host=' + arch.command_prefix,
            ]
            configure = sh.Command('./configure')
            shprint(configure, *flags, _env=env)
            shprint(sh.make, _env=env)


recipe = OggRecipe()
