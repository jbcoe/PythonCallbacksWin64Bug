#ifdef _MBCS
#ifdef callback_consumer_EXPORT
#define EXPORT extern "C" __declspec(dllexport)
#else
#define EXPORT extern "C" __declspec(dllimport)
#endif
#else
#define EXPORT __attribute__((visibility("default"))) extern "C"
#endif

EXPORT int callback_consumer_invoke(void(*callback)(void*), void* callback_input);

