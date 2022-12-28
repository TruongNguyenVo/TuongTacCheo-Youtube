import json, sys, os, time,re,colorama,requests,time,random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import doTDSTask # thêm thư viện trao đổi sub nếu muốn làm nhiệm vụ đó
s = requests.Session()
Dem_mang = 1
Bien_so_profile = 0
Dem_nhiem_vu = 1
os.system('title TuongTacCheo YouTuBe')
def main():
	#n > số profile mà bạn đinh chạy
	# n > number all profile you will run 
	n = 20
	try:
		with open("C:\\Users\\Admin\\Desktop\\profile+url youtube.txt") as file:
			print("_____________________ĐÃ TÌM THẤY FILE ACC________________")
			y = file.read()
			# print(y)
			z = y.split('|')
			global Dem_nhiem_vu
			global Dem_mang
			global Bien_so_profile
			while Bien_so_profile < n:
				try:
					# print(z[y],z[y+1],z[y+2],z[y+3])
					
					# print(z[],'\t',z[2],'\t',z[3],'\t',z[4])
					ten_profile = z[Dem_mang]
					print("Đang Chạy Profile Là: ",ten_profile)
					id_kenh = z[Dem_mang+1]
					# print("Đang Chạy ID Kênh là: ", id_kenh)
					tai_khoan = z[Dem_mang+2]
					print("Đang Chạy Tài Khoản TTC Là: ", tai_khoan)
					mat_khau = z[Dem_mang+3]
					# print("Đang Chạy Mật Khẩu TTC Là ",mat_khau)
					Dem_mang = Dem_mang+5
					# print('--------------------------------')
					Start(tai_khoan,mat_khau,id_kenh,ten_profile,Bien_so_profile,Dem_nhiem_vu)

				except IndexError:
					print('Hết Profile! Đóng Chương Trình')
					os.system('cls')
					os.system("python checkxu.py")
					time.sleep(20)
					exit()
				
			# exit()

				
			


			
	except FileNotFoundError:
		print("Không tìm được file rồi	:(")
def Start(tai_khoan,mat_khau,id_kenh,ten_profile,Bien_so_profile,Dem_nhiem_vu):
	datal={
		'username': tai_khoan,
		'password': mat_khau,
		'submit': 'ĐĂNG NHẬP'
	    }
	check=s.post("https://tuongtaccheo.com/login.php",data=datal)
	cookiettc={"x-requested-with":"XMLHttpRequest",}

	requestc=s.get("https://tuongtaccheo.com/login.php",headers=cookiettc).text
	user=re.findall('Chào mừng <i>.*?<',requestc)[0].replace('Chào mừng <i>','').replace('<','')
	xr1 = requestc.split('id="soduchinh">')
	xr2 = xr1[1].split('</strong>')
	xu = xr2[0]
	print('\033[1;3len(id)-1m â»\033[1;36mâ¥ \033[1;35mTên Tài Khoản: \033[1;36m' + user)
	print('\033[1;3len(id)-1m â»\033[1;36mâ¥ \033[1;34mXu Hiện Tại: \033[1;33m' + xu) 

	hd={"x-requested-with":"XMLHttpRequest"}
	data = {
	'iddat[]': id_kenh,
	'loai': 'youtube'}

	sss = s.post('https://tuongtaccheo.com/cauhinh/datnick.php',data=data,headers=hd,allow_redirects=False,timeout=30)
	if sss.text == '1':
		print("Cấu Hình Thành Công: ",id_kenh)
	else:
		print('Cấu Hình Thất Bại')
		rundelay(60)
		main()
	NVSub(hd,ten_profile,Bien_so_profile,Dem_nhiem_vu)
def rundelay(k):
  while (k>0):
    print('                                        ', end='\r')
    print(' \033[1;31m=> \033[1;32m Đang Đợi Delay Khoảng:   '  +str(k), end='\r')
    time.sleep(1)
    k=k-1
    print(' \033[1;31m=> \033[1;32m Đang Đợi Delay Khoảng:   '  +str(k), end='\r')
def subYoutube(id, link,hd,ten_profile,Bien_so_profile,Dem_nhiem_vu):
	if len(id) < 8:
		# doTDSTask.TDSTask(chanel, driver)
		print("Tạm Thời Hết Nhiệm Vụ TuongTacCheo")
		rundelay(60)
		Bien_so_profile = Bien_so_profile+1
		main()
	options = webdriver.ChromeOptions()
	options.add_argument(r'--user-data-dir=D:\\a tool\\profile\\User Data')
	options.add_argument('profile-directory=Profile '+ten_profile)
	options.add_argument('--mute-audio')
	driver = webdriver.Chrome(executable_path=r'C:\\Program Files\\Google\Chrome\\Application\\chromedriver.exe', options=options)
	driver.set_window_size(500,600)
	# doTDSTask.TDSTask(chanel, driver):
	#thu nho web
	# driver.minimize_window()
	spam = 0
	id_tong = ''
	y = 0
	for i in id:
		try:
			dr = driver.get(link[y])
			rundelay(20)
		except:
			pass
		try:
			#tag = '//button[@aria-label = "Đăng ký"]'
			#bấm vào nút đăng kí
			driver.find_element(By.XPATH,'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[2]/div[1]/div/ytd-subscribe-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]').click()
			print("["+str(Dem_nhiem_vu)+"] >> "+"\033[1;33;40mSub >> "+"\033[92mĐã Làm Nhiệm Vụ Sub:>> "+id[y])
			Dem_nhiem_vu = Dem_nhiem_vu+1
			rundelay(2)
			if y == len(id)-1:
			# làm len(id)-1 nhiệm vụ sẽ nhận tiền
			# do len(id)-1 task, will receive gold
				id_tong = id_tong +id[y]
			else:
				id_tong = id_tong +id[y] +','			
			time.sleep(2)
		except NoSuchElementException:
			print('không kiếm được đường dẫn 1! Chuyển qua đường dẫn 2')
			try:
				
				driver.find_element(By.XPATH,"/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/div[len(id)-1]/div[2]/div[2]/ytd-video-secondary-info-renderer/div/div/div/ytd-subscribe-button-renderer/tp-yt-paper-button/yt-formatted-string").click()
											  
				print("["+str(Dem_nhiem_vu)+"] >> "+"\033[1;33;40mSub >> "+"\033[92mĐã Làm Nhiệm Vụ Sub:>> "+id[y])
				Dem_nhiem_vu = Dem_nhiem_vu+1
				if y == len(id)-1:
				# làm len(id)-1 nhiệm vụ sẽ nhận tiền
				# do len(id)-1 task, will receive gold
					id_tong = id_tong +id[y]
				else:
					id_tong = id_tong +id[y] +','			
				time.sleep(2)

			except:
				try:
					print("lỗi Khác! Chuyển qua đường dẫn 3.")
					driver.find_element(By.XPATH,'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/div[7]/div[2]/div[2]/ytd-video-secondary-info-renderer/div/div/div/ytd-subscribe-button-renderer/tp-yt-paper-button/yt-formatted-string').click()
					print("["+str(Dem_nhiem_vu)+"] >> "+"\033[1;33;40mSub >> "+"\033[92mĐã Làm Nhiệm Vụ Sub:>> "+id[y])
					Dem_nhiem_vu = Dem_nhiem_vu+1
					if y == len(id)-1:
					# làm len(id)-1 nhiệm vụ sẽ nhận tiền
					# do len(id)-1 task, will receive gold
						id_tong = id_tong +id[y]
					else:
						id_tong = id_tong +id[y] +','			
					time.sleep(2)
				except Exception as e:
					print("Không tìm được đường dẫn! ")
					pass
				

		except Exception as e:
			print('Lỗi khác nữa! Đang mệt làm biếng fix rồi')
			# print(e)
			pass
			# driver.quit()

		# if spam == 5:
		# 	exit()
		if y == len(id)-1:
			try:		
				nt=s.post("https://tuongtaccheo.com/youtube/kiemtien/subcheo/nhantien.php",data={"id":id_tong},headers=hd)
				print(nt.json())
				time.sleep(2)
					# data = nt.json()
					# print(data)
				driver.close()
				rundelay(3)
			except:
				pass
		y = y+1
		
	NVSub(hd,ten_profile,Bien_so_profile,Dem_nhiem_vu)
	



def NVSub(hd,ten_profile,Bien_so_profile,Dem_nhiem_vu):
	like=s.get('https://tuongtaccheo.com/youtube/kiemtien/subcheo/getpost.php',headers=hd)
	# print(like.json())
	list_sub = []
	list_video = []
	for i in like.json():
		# print(i)
		# id=json.loads(like.text)[]['idpost']
		id_sub = i['idpost']
		id_video = i['link']
		list_sub.append(str(id_sub))
		list_video.append(str(id_video))
	print(list_video)
		# link=json.loads(like.text)[0]['link']
	# id_sub = list_sub[0]
	# link = list_video[0]
	# print(list_sub[1],'\t',list_sub[2],'\t',list_sueb[3])
	ten_profile = ten_profile
	subYoutube(list_sub,list_video,hd,ten_profile,Bien_so_profile,Dem_nhiem_vu)
if __name__ == '__main__':
	
	main()
