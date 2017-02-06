cmake_minimum_required(VERSION 2.8)

set(CMAKE_MACOSX_RPATH 1)

project(buggy_callbacks)

set(CMAKE_CXX_FLAGS "-std=c++14")

add_library(callback_consumer SHARED callback_consumer.cpp)

add_executable(test_callback_consumer test_callback_consumer.cpp)
target_link_libraries(test_callback_consumer callback_consumer)

enable_testing()

find_package(PythonInterp REQUIRED)

add_test(
  NAME test_callback_consumer
  COMMAND ${CMAKE_BINARY_DIR}/test_callback_consumer)

add_test(
  NAME test_python_callback_consumer
  COMMAND ${PYTHON_EXECUTABLE} ${CMAKE_SOURCE_DIR}/test_callback_consumer.py
  WORKING_DIRECTORY ${CMAKE_BINARY_DIR})

