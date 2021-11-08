add_library(example_ArithmeticMultToDiv)

target_sources(example_ArithmeticMultToDiv
  PRIVATE
    example_ArithmeticMultToDiv.cpp
  PUBLIC
    example_ArithmeticMultToDiv.h
  )

target_include_directories(example_ArithmeticMultToDiv
  PUBLIC
    ${CMAKE_CURRENT_LIST_DIR}
  )

# we use this to get code coverage
# flags are only valid with the GNU compiler and on Linux
if(CMAKE_CXX_COMPILER_ID MATCHES GNU AND CMAKE_HOST_SYSTEM_NAME STREQUAL "Linux")
  target_compile_options(example_ArithmeticMultToDiv
    PUBLIC
      "--coverage"
    )
  target_link_options(example_ArithmeticMultToDiv
    INTERFACE
      "--coverage"
    )
endif()
