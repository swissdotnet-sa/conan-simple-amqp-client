
from conans import ConanFile, CMake, tools
import os

class SimpleAmqpClientConan(ConanFile):
    name = 'simple-amqp-client'
    version = 'slepasteur_1ea1b72'
    commit_hash = '1ea1b72e2f98ea74f77cfb81a73fc514935fff27'
    license = 'MIT'
    homepage = 'https://github.com/slepasteur/SimpleAmqpClient'
    description = 'Simple C++ Interface to rabbitmq-c'
    author = 'Simon Lepasteur <simon.lepasteur@swissdotnet.ch>'
    url = 'https://github.com/swissdotnet-sa/conan-simple-amqp-client'
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "SSL": [True, False]}
    default_options = {"shared": False, "SSL": True}
    generators = "cmake"
    exports_sources = "CMakeLists.txt"
    _source_subfolder = "source_subfolder"
    
    
    def source(self):
        source_url = self.homepage
        git = tools.Git(folder=self._source_subfolder) 
        git.clone(source_url+".git")
        git.checkout(self.commit_hash)


    def configure(self):
        self.options["rabbitmq-c"].SSL = self.options.SSL

    
    # Library requirements.
    def requirements(self):
        self.requires("boost/[>=1.69.0]")
        self.requires("rabbitmq-c/0.10.0@swissdotnet/stable")

        
    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        #cmake.parallel = False
        #cmake.test()
        cmake.install()
        
    # You can choose to use package instead of the install step in build to have better control over what is included in the package.    
    #def package(self):
    #    self.copy("*.h", dst="include", src=os.path.join(self._source_subfolder, "include"))
    #    self.copy("*.lib", dst="lib", keep_path=False)
    #    self.copy("*.dll", dst="bin", keep_path=False)
    #    self.copy("*.so", dst="lib", keep_path=False)
    #    self.copy("*.dylib", dst="lib", keep_path=False)
    #    self.copy("*.a", dst="lib", keep_path=False)
        
    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
