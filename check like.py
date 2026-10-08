def check (like):
    if like >=1500:
        return f"very good this is the explor"
    elif like >=500:
        return f"god is ok"
    elif like >=200:
        return f"bad"
    else:
        return f"very bad"

my_like=1570
n=check(my_like)
print(f"your like is:\n{n}")
