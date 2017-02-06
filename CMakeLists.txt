cmake_minimum_required(VERSION 2.8)

set(CMAKE_MACOSX_RPATH 1)

project(buggy_callbacks)

set(CMAKE_CXX_FLAGS "-std=c++14")

add_library(callback_consumer callback_consumer.cpp)
include_directories(externals/catch/include)

add_executable(test_callback_consumer test_callback_consumer.cpp)

enable_testing()

add_test(
  NAME test_callback_consumer
  COMMAND ${CMAKE_BINARY_DIR}/test_callback_consumer)

