#include <gtest/gtest.h>

#include "example.h"

TEST(example, multiEquals){
    double res;
    res = multiEquals_number(2.0,6.0);
    ASSERT_TRUE(res == 12.0);
}