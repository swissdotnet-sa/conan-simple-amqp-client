
cmake_minimum_required(VERSION 2.8)
PROJECT(conanwrapper)

message(STATUS "Conan CMake Wrapper")
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

include_directories(${CMAKE_SOURCE_DIR}/source_subfolder)
add_subdirectory(source_subfolder)
        