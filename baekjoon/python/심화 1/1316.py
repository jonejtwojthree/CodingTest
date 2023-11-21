# N = int(input())
# cnt = N

# for i in range(N):
#     word = input()
#     for j in range(len(word)-1):
#         if word[j] == word[j+1]:
#             pass
#         else:
#             if word[j] in word[j+1:]:
#                 cnt-=1
#                 break

result = 0
for i in range(int(input())):
    word = input()
    print(sorted(word, key=word.find))
