
# coding=utf-8
from flask import Flask, render_template, request,jsonify, send_from_directory
from flask_cors import CORS
import execute
import time
import os
import threading
import jieba

"""
定义心跳检测函数
"""
def heartbeat():
    print (time.strftime('%Y-%m-%d %H:%M:%S - heartbeat', time.localtime(time.time())))
    timer = threading.Timer(60, heartbeat)
    timer.start()
timer = threading.Timer(60, heartbeat)
timer.start()

"""
ElementTree在 Python 标准库中有两种实现。
一种是纯 Python 实现例如 xml.etree.ElementTree ，
另外一种是速度快一点的 xml.etree.cElementTree 。
 尽量使用 C 语言实现的那种，因为它速度更快，而且消耗的内存更少
"""


app = Flask(__name__,static_url_path="/static") 

@app.route('/message', methods=['POST'])

#"""定义应答函数，用于获取输入信息并返回相应的答案"""
def reply():
    #从请求中获取参数信息
    req_msg = request.form['msg']
    
    #对用户传来的消息进行保存，用于进一步训练
    f1=open('records/user_msg.txt','a+')
    f1.write(req_msg+'\n')
    f1.close()
    
    #将语句使用结巴分词进行分词
    req_msg=" ".join(jieba.cut(req_msg))
    
    #调用decode_line对生成回答信息
    res_msg = execute.predict(req_msg)
    
    #将unk值的词用微笑符号袋贴
    res_msg = res_msg.replace('_UNK', '^_^')
    res_msg=res_msg.strip()
    
    # 如果接受到的内容为空，则给出相应的回复
    if res_msg == ' ' or res_msg=="":
      res_msg = '你别沉默呀'
    
    #更新访问数量
    msg_num_f = open("records/msg_num.txt","r")
    msg_num = msg_num_f.read()
    mn=int(msg_num)
    mn+=1
    msg_num_f.close()
    msg_num = open("records/msg_num.txt","w")
    msg_num.write(str(mn))
    msg_num.flush()#刷新的意思(一种好的习惯而已)
    msg_num.close()
    
    return jsonify( { 'text': res_msg } )

"""
jsonify:是用于处理序列化json数据的函数，就是将数据组装成json格式返回

http://flask.pocoo.org/docs/0.12/api/#module-flask.json
"""
root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")

@app.route("/")
def index(): 
    #获取上传的总消息数
    msg_num_file = open("records/msg_num.txt","r")
    msg_num = msg_num_file.read()
    mn=int(msg_num)
    msg_num_file.close()
    
    #获取并更新访问数
    login_num_file = open("records/msg_num.txt","r")
    login_num = login_num_file.read()
    ln=int(login_num)
    ln+=1
    login_num_file.close()
    login_num_file = open("records/msg_num.txt","w")
    login_num_file.write(str(ln))
    login_num_file.flush()#刷新的意思(一种好的习惯而已)
    login_num_file.close()
    
    return render_template("index.html",msg_num=mn,login_num=ln)
'''
'''
# 启动APP
if (__name__ == "__main__"): 
    CORS(app, supports_credentials=True)
    app.run(host = '127.0.0.5', port = 8808) 
