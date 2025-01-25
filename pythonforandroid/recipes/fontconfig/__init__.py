from os.path import join
from typing import TYPE_CHECKING

import sh

from pythonforandroid.archs import Arch
from pythonforandroid.recipe import BootstrapNDKRecipe
from pythonforandroid.toolchain import current_directory, shprint

if TYPE_CHECKING:
    from pythonforandroid.archs import Arch



class FontconfigRecipe(BootstrapNDKRecipe):
    version = "really_old"
    url = 'https://github.com/vault/fontconfig/archive/androidbuild.zip'
    depends = ['sdl2']
    dir_name = 'fontconfig'

    def build_arch(self, arch: 'Arch'):
        env = self.get_recipe_env(arch)

        with current_directory(self.get_jni_dir()):
            shprint(
                sh.Command(join(self.ctx.ndk_dir, "ndk-build")),
                "V=1",
                "APP_ALLOW_MISSING_DEPS=true",
                "fontconfig",
                _env=env,
            )


recipe = FontconfigRecipe()
