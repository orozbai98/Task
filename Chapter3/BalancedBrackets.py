# определить баланс в скобках

# open_l = ["[", "{", "("]
# close_l = ["]", "}", ")"]
#
# def balance(myStr):
#     stack= []
#     for i in myStr:
#         if i in open_l:
#             stack.append(i)
#         elif i in close_l:
#             pos = close_l.index(i)
#             if ((len(stack) > 0) and (open_l[pos] ==
#                                       stack[len(stack)-1])):
#                 stack.pop()
#             else:
#                 return "No"
#     if len(stack) == 0:
#         return "Yes"
#
# print(balance("{[()]}"))
# print(balance("{[(])}"))
# print(balance("{{[[(())]]}}"))
# print("если есть другие примеры, "
#       "можете написать их снизу ↓")
#
# # print(balance())
# # print(balance())
# # print(balance())
# print(balance("{}({})[]"))


# {[()]}
# {[(])}
# {{[[(())]]}}