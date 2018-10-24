from cowpy import cow


def cow_style(msg):

    msg1 = cow.milk_random_cow(msg)
    msg2 = cow.milk_random_cow(msg1)

    return msg2


ret = cow_style("林彪")
print(ret)


