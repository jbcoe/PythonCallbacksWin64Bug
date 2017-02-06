import callback_consumer

def f(my_list):
    my_list.append("foo")

def test_callback_invocation():
    myList = []
    callback_consumer.invoke(f, myList)

    assert "foo" in myList
