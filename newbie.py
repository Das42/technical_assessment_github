def get_tz_int(x):
    if x[0] == "":
        desc = "nada lotta"
    else:
        desc = "whole lotta"
    return desc

stuff = "stuff"

def get_schedule_str(x):
    desc = get_tz_int(x)
    return desc + " " + global stuff 