#include <cassert>
#include "callback_consumer.h"

int main()
{
  auto increment = [](void* i){ ++*static_cast<int*>(i); };
  int x = 0;
  callback_consumer_invoke(increment, &x);

  assert(x == 1);
}
