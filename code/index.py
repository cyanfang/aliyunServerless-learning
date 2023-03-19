from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '''<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <title>Serverless Devs - Powered By Serverless Devs</title>
    <link href="https://example-static.oss-cn-beijing.aliyuncs.com/web-framework/style.css" rel="stylesheet" type="text/css"/>
</head>
<body>
<div class="website">
    <div class="ri-t">
        <h1>Devsapp</h1>
        <h2>����һ�� Flask ��Ŀ</h2>
        <span>�Ժ���ͨ��Serverless Devs���в���</span>
        <br/>
        <p>��Ҳ���Կ������飺 <br/>
            ? ����Serverless Devs���ߣ�npm install @serverless-devs/s<br/>
            ? ��ʼ����Ŀ��s init start-flask<br/>
            ? ��Ŀ����s deploy<br/>
            <br/>
            Serverless Devs ��������Ⱥ��33947367
        </p>
    </div>
</div>
</body>
</html>
'''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)