from os.path import join
from typing import TYPE_CHECKING

import sh

from pythonforandroid.archs import Arch
from pythonforandroid.recipe import NDKRecipe
from pythonforandroid.toolchain import current_directory, shprint

if TYPE_CHECKING:
    from pythonforandroid.archs import Arch



class VorbisRecipe(NDKRecipe):
    version = '1.3.6'
    url = 'http://downloads.xiph.org/releases/vorbis/libvorbis-{version}.tar.gz'
    opt_depends = ['libogg']

    generated_libraries = ['libvorbis.so', 'libvorbisfile.so', 'libvorbisenc.so']

    def get_recipe_env(self, arch=None):
        env = super().get_recipe_env(arch)
        ogg = self.get_recipe('libogg', self.ctx)
        env['CFLAGS'] += ' -I{}'.format(join(ogg.get_build_dir(arch.arch), 'include'))
        return env

    def build_arch(self, arch: 'Arch'):
        with current_directory(self.get_build_dir(arch.arch)):
            env = self.get_recipe_env(arch)
            flags = [
                '--host=' + arch.command_prefix,
            ]
            configure = sh.Command('./configure')
            shprint(configure, *flags, _env=env)
            shprint(sh.make, _env=env)
            self.install_libs(
                arch,
                join('lib', '.libs', 'libvorbis.so'),
                join('lib', '.libs', 'libvorbisfile.so'),
                join('lib', '.libs', 'libvorbisenc.so'))


recipe = VorbisRecipe()
