def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")


print_kwargs(name='Optimus Prime', power='Star Saber')
print_kwargs(name='Megatron')
print_kwargs(name='Luffy', power='Gomu Gomu Fruit', enemy='BlackBeard')