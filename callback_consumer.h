#define EXPORT __attribute__((visibility("default"))) extern "C"

EXPORT int callback_consumer_invoke(void(*callback)(void*), void* callback_input);

