####if2
##### "$(FULL_CURRENT_PATH)"
lines = 100000
if lines < 1000:
    print("small")
elif lines < 10000:
    print("medium")
else:
    print("large")