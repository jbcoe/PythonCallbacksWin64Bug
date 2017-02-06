#include "callback_consumer.h"

int callback_consumer_invoke(void(*callback)(void*), void* callback_input)
{
  callback(callback_input);
  return 0;
}
