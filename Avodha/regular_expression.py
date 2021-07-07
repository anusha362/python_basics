import re
# pattern=r"avodha"
# # if re.match(pattern,"hi avodha,how r u?"):
# # if re.search(pattern,"hi avodha,how r u?"):
# #     print("matched")
# # else:
# #     print("not matched")
# print(re.findall(pattern,"hi avodha,avodhaghtrg avodhatyytyghj"))
# str="hi avodha, how r u?"
# pattern=r"avodha"
# new1=re.sub(pattern," AVODHA NEW",str)
# print(new1)

pattern=r"[A-Z][a-z][0-9]"
if re.search(pattern,"Av8"):
    print("correct")
else:
    print("not correct")