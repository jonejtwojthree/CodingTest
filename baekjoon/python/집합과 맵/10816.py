
# n = int(input())
# n_cards = list(input().split())

# n_dict = {}

# for n_card in n_cards:
#     try:
#         n_dict[n_card]+=1
#     except:
#         n_dict[n_card]=1

# m = int(input())
# m_cards = list(input().split())

# for m_card in m_cards:
#     try:
#         print(n_dict[m_card], end=' ')
#     except:
#         print(0, end=' ')


from collections import Counter

n = int(input())
n_cards = list(input().split())

n_dict = Counter(n_cards)

m = int(input())
m_cards = list(input().split())

for m_card in m_cards:
    if m_card in n_dict:
     print(n_dict[m_card], end=' ')
    else:
        print(0, end=' ')       
    # try:
    #     print(n_dict[m_card], end=' ')
    # except:
    #     print(0, end=' ')