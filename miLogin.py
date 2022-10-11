import base64
import json
import requests
import hashlib
import random
from Crypto.Cipher import AES
import rsa
# AES CBC pkcs7padding 128bit key:generate(16) iv：0102030405060708
# https://cdn.web-global.fds.api.mi-img.com/mcfe--mi-account/static/static/js/crypto.6d2e227b.chunk.js:formatted
# lines:2959
headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "DNT": "1",
    "Host": "account.xiaomi.com",
    "Origin": "https://account.xiaomi.com",
    "Referer": "https://account.xiaomi.com/fe/service/login/password?_locale=zh_CN",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",

}
cookie = {
    "pass_ua": "web",
    "pass_ptd": "1",
    "uLocale": "zh_CN",
    "pExpireTime": "0",
    "passInfo": "login-end",
    "sns_bind_ph": "OXcAgYqKhqwKnia2Hiyw9vvgxowYeMnXThxQbd8XOWbWCxZ0LfNpE53qDm/hwzSF"
}
username = '17876052538'
password = '52XYX1t1f040227.'

url = 'https://account.xiaomi.com/pass/serviceLogin?callback=https:%2F%2Faccount.xiaomi.com&sid=passport&qs=%253Fsid%253Dpassport&serviceParam=&_sign=&_loginSign=pwd&_json=true'
r = requests.get(url, headers=headers, cookies=cookie)
# 掉&&&START&去&&
j = json.loads(r.text[11:])
cryptedPWD = hashlib.md5(password.encode()).hexdigest().upper()

# generate key-----------------------------------
'''
function Pt(t) {
    var e, r;
    t = t || {};
    var i = function (t) {
        for (var e = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*", r = "", i = 0; i < t; i++) {
            var n = Math.floor(Math.random() * e.length);
            r += e.substring(n, n + 1)
        }
        return r
    }(16)
    return i
}
'''
string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*'
randomLetter = ''
for i in range(0, 16):
    randInt = random.randint(0, len(string)-1)
    randomLetter += string[randInt:randInt+1]
# RSA
# MIGeMA0GCSqGSIb3DQEBAQUAA4GMADCBiAKBgGvY+cQDF+WyS1/6bb735Oe+Zbm7h+jrW68B2zs0wK6GrWnjH300cpEEOHgtvk8rJuUmML4daP18VxWRQgXAZXE878EXotSZwSdNMUKULKMpOCUx11xSQ82XMEaBaVm8/RfnM1YWM1g0I/RT+iCEd2pHOw4S9Kl8Tf40t9xrusRRAgMBAAE=
# 1024bit
# EUI
#i = '0w^3%sS^9D$ANZU2'
# 'user'
# h = s.encrypt(window.btoa(i))
# p = window.btoa(a()(t).join(","))
# this.getPublicKey()
# generate key-----------------------------------

'''
-----BEGIN RSA PRIVATE KEY-----
MIICXgIBAAKBgQC8Qqn9mjHiW6ejgK313bNFM0mhrS6yYfAOBUpmgis9m5ajXu2T
bXS+Ht4AAEvKm9ORuruIpkfcWPspg3gUFEjgSqTzbNO1rYI8t4CIF2qnYv0sccgf
E0Q2lmiKcy5YbxNoYdJe8gutJqDds39Z3r86IGVv5wOkA41A6Zq7UaTBOQIDAQAB
AoGBAKRSu/Y0RR6DSgwZIb7dyMC6R6brdzsU6WgTjiFztTKNQCtRjKWGgMQCRVxS
5dTvtvgYueBI46idsn1F1+YO3pwIFaSCAEXwgY7fb3HPKxWJ7YAA1kBRGP4NRhuq
es3zWZy5uapaoeMjZ29MddEmZwMkofc6ylrDVKgCPdFUlrtRAkEA6V3WR+GA4b+4
n5tv8N3NQ822DPgJwD0s3Js9zaCzJ3PWsuWmmGqz2pY6hAuwoh6Z31z6c07z9VjT
oO0ai69rCwJBAM6E56h+9fp3I2gLZYY1VOYxgy601UKWsjLLBZPkWvtLyvN5ZwsL
ArBvlgvueLl8MNvREv5yu+qMhRjSM4yoT0sCQQDjxNepDrr5G2P6O/7U69c1T2lZ
XRo/TDYmF0sKEMfrQM+TijvA1Zw3Q5tXWAWNJiru7FPyCWRo2cqsbd8T6SGjAkEA
u7dOoneUum9kfYQuagk7/Gjw5pl0Zyx3GXg0v7MHh/fip+Cn6v+9GAa1im7eySq7
dnLaIvLDIHVN3bvjI20xdQJABAHmUJcs7xBvrUz85UXLWq5YDYyYaYr1nUnrguSE
iLVx8Y/2kCdWC9fC3XYaSAVxEzUcQKhX27VBxyR1R11mCQ==
-----END RSA PRIVATE KEY-----

-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC8Qqn9mjHiW6ejgK313bNFM0mh
rS6yYfAOBUpmgis9m5ajXu2TbXS+Ht4AAEvKm9ORuruIpkfcWPspg3gUFEjgSqTz
bNO1rYI8t4CIF2qnYv0sccgfE0Q2lmiKcy5YbxNoYdJe8gutJqDds39Z3r86IGVv
5wOkA41A6Zq7UaTBOQIDAQAB
-----END PUBLIC KEY-----

'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC8Qqn9mjHiW6ejgK313bNFM0mh\nrS6yYfAOBUpmgis9m5ajXu2TbXS+Ht4AAEvKm9ORuruIpkfcWPspg3gUFEjgSqTz\nbNO1rYI8t4CIF2qnYv0sccgfE0Q2lmiKcy5YbxNoYdJe8gutJqDds39Z3r86IGVv\n5wOkA41A6Zq7UaTBOQIDAQAB\n-----END PUBLIC KEY-----'

'-----BEGIN RSA PRIVATE KEY-----\nMIICXgIBAAKBgQC8Qqn9mjHiW6ejgK313bNFM0mhrS6yYfAOBUpmgis9m5ajXu2T\nbXS+Ht4AAEvKm9ORuruIpkfcWPspg3gUFEjgSqTzbNO1rYI8t4CIF2qnYv0sccgf\nE0Q2lmiKcy5YbxNoYdJe8gutJqDds39Z3r86IGVv5wOkA41A6Zq7UaTBOQIDAQAB\nAoGBAKRSu/Y0RR6DSgwZIb7dyMC6R6brdzsU6WgTjiFztTKNQCtRjKWGgMQCRVxS\n5dTvtvgYueBI46idsn1F1+YO3pwIFaSCAEXwgY7fb3HPKxWJ7YAA1kBRGP4NRhuq\nes3zWZy5uapaoeMjZ29MddEmZwMkofc6ylrDVKgCPdFUlrtRAkEA6V3WR+GA4b+4\nn5tv8N3NQ822DPgJwD0s3Js9zaCzJ3PWsuWmmGqz2pY6hAuwoh6Z31z6c07z9VjT\noO0ai69rCwJBAM6E56h+9fp3I2gLZYY1VOYxgy601UKWsjLLBZPkWvtLyvN5ZwsL\nArBvlgvueLl8MNvREv5yu+qMhRjSM4yoT0sCQQDjxNepDrr5G2P6O/7U69c1T2lZ\nXRo/TDYmF0sKEMfrQM+TijvA1Zw3Q5tXWAWNJiru7FPyCWRo2cqsbd8T6SGjAkEA\nu7dOoneUum9kfYQuagk7/Gjw5pl0Zyx3GXg0v7MHh/fip+Cn6v+9GAa1im7eySq7\ndnLaIvLDIHVN3bvjI20xdQJABAHmUJcs7xBvrUz85UXLWq5YDYyYaYr1nUnrguSE\niLVx8Y/2kCdWC9fC3XYaSAVxEzUcQKhX27VBxyR1R11mCQ==\n-----END RSA PRIVATE KEY-----'
'''

publicKey = rsa.PublicKey.load_pkcs1_openssl_pem(
    '-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDBbVSac1gjYgFFb7typb4grH25\nhC99t0+m155AEvGTgLSZyi6fnUsmnV6usVKQnq41EBXO8DOD6MhzLL8IkmMc4pCy\nfEWTWMqPbLAw+d8+JeKsecD9y5AAum2i2vuVN7PqiyB2nIol3C0Vb8znbzlmtuii\nJ1nCVzRPNrHxptL0dwIDAQAB\n-----END PUBLIC KEY-----'.encode())
h1 = base64.b64encode(rsa.encrypt(base64.b64encode(
    randomLetter.encode()), pub_key=publicKey)).decode()
h2 = base64.b64encode('user'.encode()).decode()
EUI = '{}.{}'.format(h1, h2)
print(EUI)
headers.update({'EUI': EUI})
# encrypt username   ----------------------------
'''
 var r = t[e]
    , i = c.a.encrypt(r, f, {
    iv: u,
    padding: d.a
});
'''
cipher = AES.new(randomLetter.encode(),
                 iv='0102030405060708'.encode(), mode=AES.MODE_CBC)
bs = 16
def pad(s): return s + (bs - len(s) % bs) * chr(bs - len(s) % bs)


data = cipher.encrypt(pad(username).encode())
usernameEncrypted = base64.b64encode(data).decode()
# encrypt username   ----------------------------

data = {
    'bizDeviceType': '',
    'needTheme': 'false',
    'theme': '',
    'showActiveX': 'false',
    'callback': j['callback'],
    'sid': j['sid'],
    'qs': j['qs'],
    'serviceParam': j['serviceParam'],
    '_sign': j['_sign'],
    'user': usernameEncrypted,
    'cc': '+86',
    'hash': cryptedPWD,
    '_json': 'true',
    'captCode': ''

}

print(data, headers)
url = 'https://account.xiaomi.com/pass/serviceLoginAuth2'
r = requests.post(url, data=data, headers=headers, cookies=cookie)
print(r.text)
