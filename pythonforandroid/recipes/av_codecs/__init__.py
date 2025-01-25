from pythonforandroid.toolchain import Recipe


class PyAVCodecsRecipe(Recipe):
    depends = ["libx264", "libshine", "libvpx"]

    def build_arch(self, arch: 'Arch'):
        pass


recipe = PyAVCodecsRecipe()
