"""
给你一个字符串，如果一个字符在它前面k个字符中已经出现过了，就把这个字符改成’-’。

比如

Input: abcdefaxc 10

Output abcdef-x-

Input: abcdefaxcqwertba 10

Output abcdef-x-qw-rtb-

完成后，请将py文件放在一个公开的github repo里

请将repo链接发送至：core@dreamschool.com

"""


def modify_string(s, k):
    output = ''
    appeared_chars = set()
    for i in range(len(s)):
        if s[i] in appeared_chars:
            output += '-'
        else:
            output += s[i]
            appeared_chars.add(s[i])

        if i > k:
            appeared_chars.remove(s[i - k])

    return output


# 从用户输入获取字符串和数字
string = input("请输入一个字符串：")
k = int(input("请输入一个整数k："))

output_string = modify_string(string, k)
print('Output:', output_string)
