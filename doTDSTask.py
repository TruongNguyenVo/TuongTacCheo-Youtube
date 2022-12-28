import json, sys, os, time,re,colorama,requests,time,random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
s = requests.Session()

def TDSTask(chanel, driver):
	user_task = 'dotdstask' # tài khoản lưu xu
	password_task = '0944058941nguyen' 
	cookieTask = ''
	def rundelay(k):
		while (k>0):
		print('                                        ', end='\r')
		print(' \033[1;31m=> \033[1;32m Đang Đợi Delay Khoảng:   '  +str(k), end='\r')
		time.sleep(1)
		k=k-1
		print(' \033[1;31m=> \033[1;32m Đang Đợi Delay Khoảng:   '  +str(k), end='\r')

	def login(user_task, password_task):

		global cookieTask

		hd = {
			'x-requested-with': 'XMLHttpRequest'
		}
		datal = {
			'username': user_task,
			'password': password_task
		}
		try:
			s1 = s.post('https://traodoisub.com/scr/login.php',headers=hd,data=datal)
			cookieTask = s1.cookies
			print("cookies: ",cookieTask)
		except:
			print('Sai Mật Khẩu')
			exit()
		setUpChanel()
		
	def setUpChanel():

		dat = {
			'iddat': chanel
		}
		s3 = s.post('https://traodoisub.com/scr/youtube_datnick.php',data=dat,headers=hd,cookies=cookieTask)
		if s3.text == '1':
			print('Cấu Hình Thành Công.ID: ',chanel)
		else:
			print('Cấu Hình Thất Bại')
			print(s3.text)
		getTask()

	def getTask():
			data = {
				'accept': '*/*',
				'content-type': 'application/json; charset=UTF-8',
				'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
				'referer': 'https://traodoisub.com/ex/youtube_follow/',
				'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
				'sec-ch-ua-mobile': '?0',
				'sec-ch-ua-platform': '"Windows"',
				'sec-fetch-dest': 'empty',
				'sec-fetch-mode': 'cors',
				'sec-fetch-site': 'same-origin',
				'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
					}
		loadTask = s.get('https://traodoisub.com/ex/youtube_follow/load.php',data= data,cookies=cookieTask).json()
		print('--------------------TASK--------------------')
		print(loadTask)
		print('--------------------------------------------')

		try:
			for i in loadTask['data']:
			chanelSub = i['id']
			linkVideo = i['link']
			print(i['id'])
			print(i['link'])
			doTask(chanelSub, linkVideo)
		except:
			print('Hết Nhiệm Vụ')
			doneTask()
	def doTask(chanelSub, linkVideo):
		hd_cache = {
			'x-requested-with': 'XMLHttpRequest'
		}

		hd_batdau ={
			'x-requested-with': 'XMLHttpRequest'
		}	

		data_batdau = {
			'id': chanelSub,
			'type': 'follow'
		}

		bat_dau=s.post("https://traodoisub.com/ex/youtube_follow/cache.php",data=data_batdau,headers=hd_cache,cookies=cookieTask)
		# print('batdau==============================')
		print('Response Start Cache: ',bat_dau)
		try:
			dr = driver.get(linkVideo)
			rd_delay = random.randint(25, 35)
			rundelay(rd_delay)
		except:
			print('Error in line is: 85')
			exit()
			pass
		try:
			dtt = {
			'id': 'tracking',
			'type': 'tracking'
			}

			cch=s.post("https://traodoisub.com/ex/youtube_follow/cache.php",data=dtt,headers=hd_cache,cookies=cookieTask)
			# print('================================')
			print('Response Cachie: ', cch)
			# print('=======================')
			#driver.find_element_by_xpath('//*[@id="subscribe-button"]/ytd-subscribe-button-renderer/tp-yt-paper-button/yt-formatted-string').click()
			tag = '//div[@id = "subscribe-button"]'
			if click(tag) == True:
				# print("["+str(Dem_nhiem_vu)+"] >> "+"\033[1;33;40mSub >> "+"\033[92mĐã Làm Nhiệm Vụ Sub:>> "+id[y])
				print("Subcribe: ", chanelSub)
				rundelay(3)	
			print('------------------------------')
		except:
			print("Error in line is: 93")
			exit()
			pass

	def doneTask():
		dt = {
			'key': '0257272C744254'
			}
		hd_nhantien ={	
			'x-requested-with': 'XMLHttpRequest'
			}
		rundelay(5)
		receiveTask = s.post("https://traodoisub.com/ex/youtube_follow/nhantien.php",data=dt,headers=hd_nhantien,cookies=cookieTask)
		print('Response receiveTask', receiveTask.json())
		# print('Chuyển kênh mới ')
		# print('Tạm nghỉ')
		# rundelay(60)
		# main(dr,Bien_so_profile)	
	def click(tag):
		try:
			driver.find_element(By.XPATH,tag).click()
			return True
		except NoSuchElementException:	
			print('Không tìm được đường dẫn')
			return False
		except:
			print('Lỗi Khác')
			return False

	login(user_task,password_task)

	

