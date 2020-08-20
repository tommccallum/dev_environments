message("Building executable")

configure_file(version.hpp.in version.hpp)
add_executable(
  new_project
  main.cpp
  )
target_include_directories(new_project PUBLIC ${PROJECT_BINARY_DIR}/src)
target_link_libraries(
  new_project
  PRIVATE project_options
          project_warnings
          CONAN_PKG::fmt
          )
