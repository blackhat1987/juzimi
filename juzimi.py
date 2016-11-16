#-*-coding=utf-8 -*-
"""
	date:2016.4.12
	爬取句子迷句子到Mysql
	启动自动查看mysql里进度 返回int
	拒绝访问403失败 发送邮件到QQ邮箱后结束运行
	每条间隔65-90s
"""


class SendEmail(object):
	"""
	QQ邮箱邮件发送脚本
	初始化传入三个参数 
		第一个参数是内容 必须为字符 支持中文
		第二个参数为 'html'(网页邮件) 或 'plain'(纯文本邮件)
	"""
	#服务器 账号 密码等设置
	addr_from = 'xxx@qq.com'	# 发送邮箱
	password = 'xxx'	# QQ邮箱开启smtp时所给的秘钥
	smtp_server = 'smtp.qq.com'		# SMTP服务器
	smtp_port = 465					# ssl端口号
	addr_to = 'xxx@qq.com'	# 接收邮箱
	
	def __init__(self, content, type):
		#邮件内容构造
		from email.mime.text import MIMEText
		global msg
		if type == 'html':
			# html邮件的格式
			msg = MIMEText(content, 'html', 'utf-8')
		elif type == 'plain':
			# 纯文本邮件格式
			msg = MIMEText(content,'plain','utf-8')
		msg['From'] = self._format_addr(u'不懂陶醉 <%s>' % self.addr_from) 	# 发信人昵称
		msg['To'] = self._format_addr(u'Just <%s>' % self.addr_to)	# 收信人昵称
		from email.header import Header
		msg['Subject'] = Header(u'句子迷爬虫停止运行', 'utf-8').encode()	# 邮件主题
	# 邮件头的构造函数
	def _format_addr(self, s):
		from email.utils import parseaddr,formataddr
		from email.header import Header
		name, addr = parseaddr(s)
		return formataddr((\
			Header(name, 'utf-8').encode(),\
			addr.encode('utf-8') if isinstance(addr, unicode) else addr
			))
	# 发送邮件
	def send(self):
		import smtplib
		server = smtplib.SMTP_SSL(self.smtp_server, self.smtp_port)
		server.set_debuglevel(1)
		server.login(self.addr_from, self.password)
		server.sendmail(self.addr_from, [self.addr_to], msg.as_string())
		server.quit()

def getNum(num):
	import urllib2
	import re
	import random

	headers1 = {
		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		'Accept-Language':'zh-CN,zh;q=0.8',
		'Cache-Control':'max-age=0',
		'Connection':'keep-alive',
		'Host':'www.juzimi.com',
		'If-Modified-Since':'Sat, 12 Mar 2016 05:32:47 GMT',
		'If-None-Match':'"56b9095c33f20062955b0fec340c3b8e"',
		'Referer':'http://www.juzimi.com/new',
		'Upgrade-Insecure-Requests':'1',
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'
	}
	headers2 = {
		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		'Accept-Language':'zh-CN,zh;q=0.8',
		'Cache-Control':'max-age=0',
		'Connection':'keep-alive',
		'Host':'www.juzimi.com',
		'If-Modified-Since':'Sat, 12 Mar 2016 05:32:47 GMT',
		'If-None-Match':'"56b9095c33f20062955b0fec340c3b8e"',
		'Referer':'http://www.juzimi.com/',
		'Upgrade-Insecure-Requests':'1',
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36 Core/1.47.163.400 QQBrowser/9.3.7175.400'
	}
	headers3 = {
		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		'Accept-Language':'zh-CN,zh;q=0.8',
		'Cache-Control':'max-age=0',
		'Connection':'keep-alive',
		'Host':'www.juzimi.com',
		'If-Modified-Since':'Sat, 12 Mar 2016 05:32:47 GMT',
		'If-None-Match':'"56b9095c33f20062955b0fec340c3b8e"',
		'Referer':'http://www.juzimi.com/new',
		'Upgrade-Insecure-Requests':'1',
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240'
	}
	headers = random.choice([headers1, headers2, headers3])
	if num==-1:
		url = 'http://www.juzimi.com/'
	else:
		url = 'http://www.juzimi.com/ju/' + str(num)
	request = urllib2.Request(url, headers=headers)
	response = urllib2.urlopen(request, timeout=15)
	html = response.read()

	pattern = r'<a href="/ju/(.*?)" title="与千万个佳句随机相遇'

	num = re.search(pattern, html).group(1)
	return num

def getJuzi(num):
	import urllib2
	import re
	import random
	headers1 = {
		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		'Accept-Language':'zh-CN,zh;q=0.8',
		'Cache-Control':'max-age=0',
		'Connection':'keep-alive',
		'Host':'www.juzimi.com',
		'If-Modified-Since':'Sat, 12 Mar 2016 05:32:47 GMT',
		'If-None-Match':'"56b9095c33f20062955b0fec340c3b8e"',
		'Referer':'http://www.juzimi.com/new',
		'Upgrade-Insecure-Requests':'1',
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'
	}
	headers2 = {
		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		'Accept-Language':'zh-CN,zh;q=0.8',
		'Cache-Control':'max-age=0',
		'Connection':'keep-alive',
		'Host':'www.juzimi.com',
		'If-Modified-Since':'Sat, 12 Mar 2016 05:32:47 GMT',
		'If-None-Match':'"56b9095c33f20062955b0fec340c3b8e"',
		'Referer':'http://www.juzimi.com/',
		'Upgrade-Insecure-Requests':'1',
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36 Core/1.47.163.400 QQBrowser/9.3.7175.400'
	}
	headers3 = {
		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		'Accept-Language':'zh-CN,zh;q=0.8',
		'Cache-Control':'max-age=0',
		'Connection':'keep-alive',
		'Host':'www.juzimi.com',
		'If-Modified-Since':'Sat, 12 Mar 2016 05:32:47 GMT',
		'If-None-Match':'"56b9095c33f20062955b0fec340c3b8e"',
		'Referer':'http://www.juzimi.com/new',
		'Upgrade-Insecure-Requests':'1',
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240'
	}
	headers = random.choice([headers1, headers2, headers3])
	url = 'http://www.juzimi.com/ju/' + str(num)
	request = urllib2.Request(url, headers=headers)
	response = urllib2.urlopen(request, timeout=15)
	html = response.read()

	pattern_juzi = r'<h1 class="with-tabs" id="xqtitle">(.*?)</h1>'
	pattern_author = r'<a title=".*?" rel="tag" href="/writer/.*?">(.*?)</a>'
	pattern_article = r'<a title=".*?" rel="tag" href="/article/.*?">(.*?)</a>'


	juzi = re.search(pattern_juzi, html).group(1).replace(r'<br/>', '      ').replace(r'&quot;',r'"')
	try:
		author = re.search(pattern_author, html).group(1)
	except AttributeError:
		author = ''
	try:
		article = re.search(pattern_article, html).group(1)
	except AttributeError:
		article = ''

	result =[juzi, author, article]
	return result

def saveJuzi(juzi):
	import MySQLdb
	try:
		conn = MySQLdb.connect(host='localhost', user='root', passwd='violet', db='juzimi', charset='utf8')
		cursor = conn.cursor()
		sql = "insert into juzi(id, juzi, author, article) values(%s,%s,%s,%s)"
		param = (juzi[0], juzi[1], juzi[2], juzi[3])
		# a = cursor.execute("SELECT Sname FROM students where sno='1310411001'")
		a = cursor.execute(sql, param)
		return a
	except MySQLdb.IntegrityError,e:
		print e
	finally:
		cursor.close()
		conn.commit()
		conn.close()

# 统计已抓取的数量
def getCount():
	import MySQLdb
	try:
		conn = MySQLdb.connect(host='localhost', user='root', passwd='xxx', db='juzimi', charset='utf8')
		cursor = conn.cursor()
		cursor.execute("SELECT num FROM count where id=1")
		a = cursor.fetchone()[0]
		a = int(a)
		return a
	except MySQLdb.IntegrityError,e:
		print e
	finally:
		cursor.close()
		conn.commit()
		conn.close()

def setCount(num):
	import MySQLdb
	try:
		conn = MySQLdb.connect(host='localhost', user='root', passwd='xxx', db='juzimi', charset='utf8')
		cursor = conn.cursor()
		sql = 'update count set num='+str(num)+' where id=1'
		cursor.execute(sql)
	except MySQLdb.IntegrityError,e:
		print e
	finally:
		cursor.close()
		conn.commit()
		conn.close()


if __name__=="__main__":
	import datetime
	import time
	import sys
	import urllib2
	import random

	# count = getCount() + 1
	num = -1
	for i in range(50): #设置访问数量
		num = int(getNum(num))
		try:
			result = getJuzi(num)
			print num, 'is ok'
		except urllib2.HTTPError,e:
			if e.code==403:
				print num,'refuse to response',e.code
				#发送邮件提醒
				clock = datetime.datetime.now()
				content = str(clock) + '<br/><br/>' + str(e.code)	# 邮件内容
				send_email = SendEmail(content, 'html')
				send_email.send()

				sys.exit(0)
			elif e.code==404:
				# setCount(num)
				continue
			print num, e.code
			continue
		juzi = [num,result[0],result[1],result[2]]
		# for i in juzi:
		# 	print i
		# print num
		# print result[0]
		# print result[1]
		# print result[2]
		code = saveJuzi(juzi)	
		print code,'\n'
		# setCount(num)
		time.sleep(random.randint(4,10))	#设置间隔时间
	print 'exit......'
