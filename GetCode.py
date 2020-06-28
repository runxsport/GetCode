"""获取验证码"""

from redis import StrictRedis
# host='115.28.208.71'
# host='47.99.47.109'
while True:
    phone = input("请输入手机号：")
    string = ['provider-app:smsCode:register:', 'provider-app:smsCode:login:','provider-app:smsCode:resetPassword:']
    txt = ['注册验证码为：','登录验证码为：','修改密码验证码为：']
    for host1 in range(0,3):
        host = ['115.28.208.71', '47.99.47.109','47.111.146.118']
        host_txt = ['测试环境', '开发环境','预发布环境']
        host2 = host[host1]
        redispool = StrictRedis(host=host2, port=6379, db=0, password='bXIHkKSona8+QQ==')
        for range01 in range(0,3):
            redisp = string[range01] + phone
            code = str(redispool.get(redisp))
            if code not in 'None':
                print("%s、%s\n%s" % (host_txt[host1],txt[range01],code[3:9]))