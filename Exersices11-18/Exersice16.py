def generate_dict(n):
    sroot_dict = {}
    for i in range(1, n+1):
        sroot_dict[i] = i*i
    return sroot_dict


print(generate_dict(4))

