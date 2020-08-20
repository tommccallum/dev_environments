cmake_minimum_required(VERSION 3.10)
set(PROJ_NAME "new_project")
project(${PROJ_NAME} LANGUAGES CXX VERSION 0.1)
string(TIMESTAMP TODAY "%Y-%m-%d %H:%m")

include(cmake/standard_project_settings.cmake)
include(cmake/prevent_in_source_builds.cmake)
# Link this 'library' to set the c++ standard / compile-time options requested
add_library(project_options INTERFACE)
target_compile_features(project_options INTERFACE cxx_std_17)



message(${CMAKE_CXX_COMPILER_ID})

option(BUILD_SHARED_LIBS "Enable compilation of shared libraries" OFF)
option(ENABLE_TESTING "Enable Test Builds" ON)
option(ENABLE_FUZZING "Enable Fuzzing Builds, requires Clang compiler" OFF)
option(ENABLE_DOXYGEN "Enable doxygen doc builds of source" OFF)
option(USE_CLANG "build application with clang (ON) or gcc (OFF)" OFF) 
option(ENABLE_BUILD_WITH_TIME_TRACE "Enable -ftime-trace to generate time tracing .json files on clang" OFF)
option(ENABLE_CPPCHECK "Enable static analysis with cppcheck" OFF)
option(ENABLE_CLANG_TIDY "Enable static analysis with clang-tidy" OFF)

# turned on by .travis.yml script
option(ENABLE_COVERAGE "Enable coverage reporting for gcc/clang" OFF)

# Configuration types
# SET(CMAKE_CONFIGURATION_TYPES "Debug;Release" CACHE STRING "Configs" FORCE)
# IF(DEFINED CMAKE_BUILD_TYPE AND CMAKE_VERSION VERSION_GREATER "2.8")
#   SET_PROPERTY(CACHE CMAKE_BUILD_TYPE PROPERTY STRINGS  ${CMAKE_CONFIGURATION_TYPES})
# ENDIF()

# SET(${PROJ_NAME}_PATH_INSTALL     "/opt/project"                     CACHE PATH "This directory contains installation Path")
# SET(CMAKE_DEBUG_POSTFIX "d")
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${PROJECT_BINARY_DIR}/bin)


if(CMAKE_CXX_COMPILER_ID MATCHES ".*Clang")  
  if(ENABLE_BUILD_WITH_TIME_TRACE)
    add_compile_definitions(project_options INTERFACE -ftime-trace)
  endif()
endif()

# Link this 'library' to use the warnings specified in CompilerWarnings.cmake
add_library(project_warnings INTERFACE)

# enable cache system
include(cmake/cache.cmake)

# standard compiler warnings
include(cmake/compiler_warnings.cmake)
set_project_warnings(project_warnings)

# sanitizer options if supported by compiler
include(cmake/sanitizers.cmake)
enable_sanitizers(project_options)

# enable doxygen
include(cmake/doxygen.cmake)
build_documentation()

# allow for static analysis options
include(cmake/static_analyzers.cmake)

# Set up some extra Conan dependencies based on our needs before loading Conan
set(CONAN_EXTRA_REQUIRES "")
set(CONAN_EXTRA_OPTIONS "")

include(cmake/conan.cmake)
run_conan()

if(ENABLE_TESTING)
  enable_testing()
  message("Building Tests. Be sure to check out test/constexpr_tests for constexpr testing")
  add_subdirectory(tests)
endif()


if(ENABLE_FUZZING)
  message("Building Fuzz Tests, using fuzzing sanitizer https://www.llvm.org/docs/LibFuzzer.html")
  add_subdirectory(fuzz_tests)
endif()

add_subdirectory(src)





# TODO make man pages
# TODO add an install capability to /usr/share/app or something like that

# add_custom_target(
#   doc ALL
#   COMMAND $<$<CONFIG:Release>:${DOXYGEN_EXECUTABLE} ${doxyfile_in}>
#   WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/docs
#   COMMENT "Generating API documentation with Doxygen"
#   VERBATIM
# )

# uninstall target
if(NOT TARGET uninstall)
  configure_file(
    "${CMAKE_CURRENT_SOURCE_DIR}/cmake/uninstall.cmake"
    "${CMAKE_CURRENT_BINARY_DIR}/uninstall.cmake"
    IMMEDIATE @ONLY)

  add_custom_target(uninstall
    COMMAND ${CMAKE_COMMAND} -P ${CMAKE_CURRENT_BINARY_DIR}/uninstall.cmake)
endif()

# Install target
INSTALL(TARGETS ${PROJ_NAME}
    DESTINATION  "${${PROJ_NAME}_PATH_INSTALL}/lib/${CMAKE_BUILD_TYPE}/"
    )
