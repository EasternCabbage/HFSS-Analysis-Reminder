import os
import time
import smtplib #邮件通知模块
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import tkinter as tk
from tkinter import messagebox
# 邮件发送方和接收方
sender_email = "1395429547@qq.com"
receiver_email = "1395429547@qq.com"  # 收件人邮箱
subject = "HFSS仿真完成！"
body = "这是通过 Python 发送的通知邮件。"

# 邮箱授权码
smtp_server = "smtp.qq.com"
smtp_port = 465  # QQ 邮箱 SMTP 使用的是 465 端口
smtp_user = sender_email
smtp_password = "izhzzgiezqttjefe"  # 这里填写你的授权码

# 创建邮件内容
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject

# 邮件正文内容
msg.attach(MIMEText(body, 'plain'))

def send_mail():# 连接 SMTP 服务器并发送邮件
    try:
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(smtp_user, smtp_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
            print("邮件发送成功！")
    except smtplib.SMTPAuthenticationError as e:
        print(f"邮件认证失败: {e}")
    except smtplib.SMTPConnectError as e:
        print(f"邮件连接失败: {e}")
    except smtplib.SMTPException as e:
        print("\^o^/")
        #print(f"SMTP 发生错误: {e}")
    except Exception as e:
        print(f"邮件发送失败: {e}")

#通知窗口初始化
root = tk.Tk()
root.withdraw()  # 隐藏主窗口
root.attributes("-topmost", True)#使消息漂浮在所有窗口最上方

#文件信息初始化
file_path = 'D:/Ansoft22Project/WaveGuideFilter.aedt'
file_mtime = os.path.getmtime(file_path)
pre_file_time = file_mtime #储存开始的文件修改时间

directory_path = 'D:/Ansoft22Project/WaveGuideFilter.aedtresults/filter.results'
def count_files_in_directory(directory_path):
    # 获取文件夹内所有文件和文件夹的列表
    files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
    return len(files)
file_count = count_files_in_directory(directory_path)
pre_file_count = file_count

readable_time = time.ctime(file_mtime)
print(f"文件 {file_path} 最后修改时间: {readable_time}")
print(f"文件夹内文件的数量：{file_count}")
while True:
    time.sleep(10)
    file_mtime = os.path.getmtime(file_path)#重新获得最新修改时间
    
    if file_mtime != pre_file_time:
        print("HFSS分析中。。。")
        while True:
            pre_file_count = file_count
            time.sleep(20)
            #print("等了20秒了")
            file_count = count_files_in_directory(directory_path)
            #print("file_count = "+ str(file_count))
            #print("prefile_count =" + str(pre_file_count))
            if file_count == pre_file_count:#如果文件数量不再变化
                pre_file_count = file_count# 更新基准文件数量
                pre_file_time = file_mtime#更新基准修改时间
                messagebox.showinfo("提示", "HFSS仿真完成！")
                send_mail()
                break;

            
    else:
       print("程序运行中")
        

             

        
