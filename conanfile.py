from conans import ConanFile, tools


class BoostCoroutine2Conan(ConanFile):
    name = "Boost.Coroutine2"
    version = "1.65.1"
    requires = \
        "Boost.Assert/1.65.1@bincrafters/testing", \
        "Boost.Config/1.65.1@bincrafters/testing", \
        "Boost.Context/1.65.1@bincrafters/testing"
    lib_short_names = ["coroutine2"]
    is_header_only = True

    # BEGIN

    url = "https://github.com/bincrafters/conan-boost-coroutine2"
    description = "Please visit http://www.boost.org/doc/libs/1_65_1/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    short_paths = True
    build_requires = "Boost.Generator/1.65.1@bincrafters/testing"

    def package_id(self):
        if self.is_header_only:
            self.info.header_only()

    @property
    def env(self):
        try:
            with tools.pythonpath(super(self.__class__, self)):
                import boostgenerator  # pylint: disable=F0401
                boostgenerator.BoostConanFile(self)
        except:
            pass
        return super(self.__class__, self).env

    # END
