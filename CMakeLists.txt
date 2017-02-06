cmake_minimum_required(VERSION 2.8)

set(CMAKE_MACOSX_RPATH 1)

project(buggy_callbacks)

set(CMAKE_CXX_FLAGS "-std=c++14")

add_library(callback_consumer SHARED callback_consumer.cpp)
add_custom_command(TARGET callback_consumer
    POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E copy $<TARGET_FILE:callback_consumer> ${CMAKE_BINARY_DIR}/
    COMMAND ${CMAKE_COMMAND} -E copy ${CMAKE_SOURCE_DIR}/callback_consumer.py ${CMAKE_BINARY_DIR}/
    COMMAND ${CMAKE_COMMAND} -E copy ${CMAKE_SOURCE_DIR}/test_callback_consumer.py ${CMAKE_BINARY_DIR}/)

add_executable(test_callback_consumer test_callback_consumer.cpp)
target_link_libraries(test_callback_consumer callback_consumer)

enable_testing()

if(NOT PYTHON_EXECUTABLE)
	find_package(PythonInterp REQUIRED)
else()
  execute_process(COMMAND ${PYTHON_EXECUTABLE} -c "import this" RESULT_VARIABLE result OUTPUT_QUIET ERROR_QUIET)
	if(result)
		message(FATAL_ERROR "CMake failed: ${PYTHON_EXECUTABLE} cannot execute a simple Python script.")
	endif()
endif()

add_test(
  NAME test_callback_consumer
  COMMAND ${CMAKE_BINARY_DIR}/test_callback_consumer
  WORKING_DIRECTORY ${CMAKE_BINARY_DIR})

add_test(
  NAME test_python_callback_consumer
  COMMAND ${PYTHON_EXECUTABLE} test_callback_consumer.py
	WORKING_DIRECTORY ${CMAKE_BINARY_DIR})

