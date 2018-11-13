def checkException():
    raise Exception





try:
    {checkException()}
except Exception:
    print("the functoin returned the exception")


