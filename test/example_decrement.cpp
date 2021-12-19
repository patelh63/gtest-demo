#include <gtest/gtest.h>

#include "example.h"

TEST(example, decrement){
    double res;
    res = decrement_number(1.0);
    ASSERT_TRUE(res == 0.0);
}