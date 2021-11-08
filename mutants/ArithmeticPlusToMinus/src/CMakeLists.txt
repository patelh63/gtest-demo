add_library(example_ArithmeticPlusToMinus)

target_sources(example_ArithmeticPlusToMinus
  PRIVATE
    example_ArithmeticPlusToMinus.cpp
  PUBLIC
    example_ArithmeticPlusToMinus.h
  )

target_include_directories(example_ArithmeticPlusToMinus
  PUBLIC
    ${CMAKE_CURRENT_LIST_DIR}
  )

# we use this to get code coverage
# flags are only valid with the GNU compiler and on Linux
if(CMAKE_CXX_COMPILER_ID MATCHES GNU AND CMAKE_HOST_SYSTEM_NAME STREQUAL "Linux")
  target_compile_options(example_ArithmeticPlusToMinus
    PUBLIC
      "--coverage"
    )
  target_link_options(example_ArithmeticPlusToMinus
    INTERFACE
      "--coverage"
    )
endif()
