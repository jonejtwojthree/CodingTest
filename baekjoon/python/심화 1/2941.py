# words = input()

# total_length = (
#     words.count("c=") * 1
#     + words.count("c-") * 1
#     + words.count("d-") * 1
#     + words.count("lj") * 1
#     + words.count("nj") * 1
#     + words.count("s=") * 1
#     + words.count("dz=") * 1
#     + words.count("z=") * 1
# )
# print(len(words) - total_length)


croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
words = input()

for i in croatia:
    words = words.replace(i, "*")
print(words)
