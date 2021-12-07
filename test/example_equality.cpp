#include <gtest/gtest.h>

#include "example.h"

TEST(example, equality) {
  bool res;
  res = check_number_equality(1.0, 1.0);
  ASSERT_TRUE(res);
}
