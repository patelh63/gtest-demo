cmake_minimum_required(VERSION 3.13)

project(gtest-demo LANGUAGES CXX)

# set the C++ standard
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# place binaries and libraries according to GNU standards
include(GNUInstallDirs)
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/${CMAKE_INSTALL_LIBDIR})
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/${CMAKE_INSTALL_LIBDIR})
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/${CMAKE_INSTALL_BINDIR})

# we cannot analyse results without gcov
find_program(GCOV_PATH gcov)
if(NOT GCOV_PATH)
  message(FATAL_ERROR "Code coverage analysis requires gcov!")
endif()

add_subdirectory(src)

enable_testing()

add_subdirectory(test)

#add_custom_target(
#	generate_mutants ALL
#	COMMAND ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/mutator/GenerateMutants.py ${CMAKE_CURRENT_SOURCE_DIR}/mutator
#	BYPRODUCT ${CMAKE_CURRENT_SOURCE_DIR}/mutants
#)

#add_dependencies(unit_tests generate_mutants)

add_subdirectory(mutants)


