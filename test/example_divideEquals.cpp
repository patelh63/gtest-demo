#include <gtest/gtest.h>

#include "example.h"

TEST(example, divideEquals){
    double res;
    res = divideEquals_number(25.0,5.0);
    ASSERT_TRUE(res == 5.0);
}