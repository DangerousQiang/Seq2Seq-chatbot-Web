# Seq2Seq-chatbot-Web
A Seq2Seq chatbot implementation just for study.

## Recomended Environment
```python
python3.5
tensorflow==2.0或者tensorflow-gpu==2.0
flask==0.11.1
```
## How to Start
1. Download the corpus and put it into the folder /data.
2. Run **data_utls.py(preprocess)-->execute.py(train)-->app.py(server)**.
3. You can modify the hyper parameters in seq2seq.ini and seq2seq_sever.ini

## Example Image
![avatar](https://github.com/DangerousQiang/Seq2Seq-chatbot-Web/blob/master/example_image/main.png?raw=true)

## Directory Structure
```
Root Directory
│  app.py
│  data_util.py
│  execute.py
│  getConfig.py
│  seq2seq.ini
│  seq2seqModel.py
│  tree.txt
│  
├─model_data
│      checkpoint
│      ckpt-48.data-00000-of-00002
│      ckpt-48.data-00001-of-00002
│      ckpt-48.index
│      
├─records
│      login_num.txt
│      msg_num.txt
│      user_msg.txt
│      
├─static
│      (web)
│                      
├─templates
│      index.html
│      
├─train_data
        dgk_shooter_z.conv
        seq.data
        xiaohuangji50w_nofenci.conv
```

## References
[http://blog.topspeedsnail.com/archives/10735/comment-page-1#comment-1161](http://blog.topspeedsnail.com/archives/10735/comment-page-1#comment-1161)

[http://www.easyapple.net/?p=1384&from=singlemessage&isappinstalled=0](http://www.easyapple.net/?p=1384&from=singlemessage&isappinstalled=0)
