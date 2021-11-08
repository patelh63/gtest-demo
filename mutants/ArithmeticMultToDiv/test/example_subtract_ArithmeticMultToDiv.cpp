#include <gtest/gtest.h>

#include "example_ArithmeticMultToDiv.h"

TEST(example_ArithmeticMultToDiv, subtract) {
  double res;
  res = subtract_numbers(1.0, 2.0);
  ASSERT_NEAR(res, -1.0, 1.0e-11);
}