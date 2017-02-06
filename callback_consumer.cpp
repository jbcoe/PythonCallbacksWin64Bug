#include "callback_consumer.h"

int callback_consumer_invoke(void(*callback)(callback_padding_t, void*), callback_padding_t padding, void* callback_input)
{
  callback(padding, callback_input);
  return 0;
}
