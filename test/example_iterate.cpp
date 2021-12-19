#include <gtest/gtest.h>

#include "example.h"

TEST(example, iterate){
    double res;
    res = iterate_number(1.0);
    ASSERT_TRUE(res == 2.0);
}