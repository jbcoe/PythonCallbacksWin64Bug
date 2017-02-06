#ifdef _MBCS
#ifdef callback_consumer_EXPORTS
#define EXPORT extern "C" __declspec(dllexport)
#else
#define EXPORT extern "C" __declspec(dllimport)
#endif
#else
#define EXPORT __attribute__((visibility("default"))) extern "C"
#endif

struct callback_padding_t
{
    int _kind_id;
    int xdata; 
    const void *data[3];
};

EXPORT int callback_consumer_invoke(void(*callback)(callback_padding_t, void*), callback_padding_t padding, void* callback_input);

