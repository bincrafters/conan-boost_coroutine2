from conans import ConanFile, tools, os

class BoostCoroutine2Conan(ConanFile):
    name = "Boost.Coroutine2"
    version = "1.64.0"
    url = "https://github.com/bincrafters/conan-boost-coroutine2"
    source_url = "https://github.com/boostorg/coroutine2"
    description = "Please visit http://www.boost.org/doc/libs/1_64_0/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    lib_short_name = "coroutine2"
    requires =  "Boost.Assert/1.64.0@bincrafters/testing", \
                      "Boost.Config/1.64.0@bincrafters/testing", \
                      "Boost.Context/1.64.0@bincrafters/testing"
                      
                      #assert1 config0 context12
                      
    def source(self):
        self.run("git clone --depth=50 --branch=boost-{0} {1}.git"
                 .format(self.version, self.source_url))

    def package(self):
        include_dir = os.path.join(self.build_folder, self.lib_short_name, "include")
        self.copy(pattern="*", dst="include", src=include_dir)

    def package_id(self):
        self.info.header_only()