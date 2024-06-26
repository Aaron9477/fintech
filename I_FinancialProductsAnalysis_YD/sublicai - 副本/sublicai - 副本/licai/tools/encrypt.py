# -*- coding=utf-8 -*-
# --------------------------------
# @Time      : 2022/9/14 11:00 
# @Author    : Wangyd5 
# @File      : encrypt
# @Project   : sublicai
# @Function  ：
# --------------------------------


import base64
from Cryptodome.Cipher import AES


# aes补足16位
def add_to_16(value):
    while len(value) % 16 != 0:
        value += '\0'
    return str.encode(value)  # 返回bytes


def encrypt_source(source_text, key='citic@csc'):
    # 初始化加密器
    aes = AES.new(add_to_16(key), AES.MODE_ECB)
    # 先进行aes加密
    encrypt_aes = aes.encrypt(add_to_16(source_text))
    # 用base64转成字符串形式
    encrypted_text = str(base64.encodebytes(encrypt_aes), encoding='utf-8')  # 执行加密并转码返回bytes
    return encrypted_text


def decrypt_des(source_text, key='citic@csc'):
    # 初始化加密器
    aes = AES.new(add_to_16(key), AES.MODE_ECB)
    # 优先逆向解密base64成bytes
    base64_decrypted = base64.decodebytes(source_text.encode(encoding='utf-8'))
    # 执行解密密并转码返回str
    decrypted_text = str(aes.decrypt(base64_decrypted), encoding='utf-8').replace('\0', '')
    return decrypted_text


if __name__ == '__main__':
    decrypt_text = 'abc123'
    encrypt_text = encrypt_source(decrypt_text)
    print(encrypt_text)

    decrypt_text = decrypt_des('Ib87xP2r7avEQvQUUEssGQ==\n')
    print(decrypt_text)
