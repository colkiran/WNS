
# maketrans, transalte

print("maketrans".center(40,"-"))
st = "hello world"
print(f"st :{st}")
a = 'helowrd'
b = 'HELOWRD'       # no of chars in a and b should be the same
trnsTbl = st.maketrans(a, b)
print(f"trnsTbl :{trnsTbl}")

# translate(tbl)
res = st.translate(trnsTbl)
print(f"res :{res}")

print("-" * 40)
st = "*******hello*******"

# lstrip
res1 = st.lstrip("*")
print(f"res1 :{res1}")

# rstrip
res2 = st.rstrip("*")
print(f"res2 :{res2}")

# strip
res3 = st.strip("*")
print(f"res3 :{res3}")
