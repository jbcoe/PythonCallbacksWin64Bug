#include <cassert>
#include "callback_consumer.h"

int main()
{
  auto increment = [](callback_padding_t, void* i)
  { 
    ++*static_cast<int*>(i); 
  };
  
  int x = 0;
  callback_consumer_invoke(increment, callback_padding_t{}, &x);

  assert(x == 1);
}
