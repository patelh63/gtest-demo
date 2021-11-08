include(FetchContent)
FetchContent_Declare(gtest
  QUIET
  URL https://github.com/google/googletest/archive/release-1.10.0.tar.gz
)
# configure build of googletest
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
set(BUILD_GMOCK OFF CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(gtest)

add_executable(
    unit_tests_ArithmeticMultToDiv
    example_add_ArithmeticMultToDiv.cpp
    example_subtract_ArithmeticMultToDiv.cpp
    )

target_link_libraries(unit_tests_ArithmeticMultToDiv
  PRIVATE
  example_ArithmeticMultToDiv
    gtest_main
  )

# automatic discovery of unit tests
include(GoogleTest)
gtest_discover_tests(unit_tests_ArithmeticMultToDiv
  PROPERTIES
    LABELS "unit"
  DISCOVERY_TIMEOUT  # how long to wait (in seconds) before crashing
    240
  )
