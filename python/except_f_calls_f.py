def f():
    try:
        f()
    except Exception as e:
        print(e)
        f()
