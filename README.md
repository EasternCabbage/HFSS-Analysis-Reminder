# HFSS-Analysis-Reminder
Notify HFSS developers that the simulation is complete through both email and desktop pop-up reminders.
what you need
- install python on your PC
  
- a mail support smpt （most mail support this indeed,but you should make sure it had been allowed on your account）
- get "Email Authorization Code",(usually it's a very long string,At first, I foolishly thought there were only four digits.)

how to run 
Modify some key parameters.
- sender_email = "1********@qq.com" //your send mail
- receiver_email = "*******@qq.com"   (mail who you send
- smtp_server = "smtp.qq.com"//chose your mail server
- smtp_port = 465  # QQ 邮箱 SMTP 使用的是 465 端口
- smtp_user = sender_email
- smtp_password = "***************"  # 这里填写你的授权码

  run this script before click analysis in HFSS,once you start analysis ,this script can detect it,and when analysis finished,this script will trick up a window on your PC to remind you,also send mail to you.

  by the way ,if you dont need mail notify,You can comment out the line that “send_mail()”
