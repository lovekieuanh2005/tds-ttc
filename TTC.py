from function import *; import requests as s; from sys import exit; import json, platform, time

def main():
    ttc = TuongTacCheo()
    clearTerminal()
    #Login tài khoản mật khẩu
    userTtc = input("\033[1;32mNhập tài khoản TTC: \033[1;33m")
    passTtc = input("\033[1;32mNhập mật khẩu TTC: \033[1;33m")

    
    login = ttc.loginTtc(userTtc, passTtc)
    if login['status'] == "success":
        user = login['data']['user']
        xu = login['data']['xu']
        print("\033[1;32mĐăng nhập thành công")
    else:
        exit("\033[1;31mĐăng nhập TTC thất bại")
    time.sleep(2)

    ##Nếu dùng muốn dùng bằng token thì comment đoạn code trên thay cho đoạn này
    # token = input("\033[1;32mNhập token TTC: \033[1;33m")
    # login = ttc.loginTtcToken(token)
    # if login['status'] == "success":
    #     user = login['data']['user']
    #     xu = login['data']['xu']
    #     print("\033[1;32mĐăng nhập thành công")
    # else:
    #     exit("\033[1;31mĐăng nhập TTC thất bại")
    # time.sleep(2)

    thanhNgang(42)
    while(True):
        userTik = input("\033[1;32mNhập user Tik Tok ( sau chữ @ ): \033[1;33m")
        idTik = getUserTik(userTik)
        if idTik == False:
            print("\033[1;31mUser Tik Tok không hợp lệ")
        else:
            break
    
    clearTerminal()
    job = int(input("\033[1;31m1 \033[1;37m=> \033[1;36mFollow\n\033[1;31m2 \033[1;37m=> \033[1;36mTym Video\n\033[1;32mVui lòng chọn nhiệm vụ: \033[1;33m"))
    delay = int(input("\033[1;32mNhập delay làm nhiệm vụ: \033[1;33m"))
    datNick = ttc.datNickTTC(idTik)
    thanhNgang(42)
    if datNick == True:
        print(f"\033[1;32mĐặt nick \033[1;33m{userTik}\033[1;32m | \033[1;33m{idTik} \033[1;32mlàm nick chạy thành công")
    else:
        exit(f"\033[1;31m{datNick}")
    time.sleep(3)
    clearTerminal()
    thanhNgang(42)
    print(f"\033[1;33mUser: \033[1;36m{userTik} \033[1;37m| \033[1;33mID: \033[1;36m{idTik}")
    thanhNgang(42)
    h = 0
    while(True):
        if job == 1:
            getFollow = ttc.getJobFollow()
            if len(getFollow) != 0:
                for x in getFollow:
                    id = x['idpost']
                    user = x['link']
                    link = f"https://www.tiktok.com/@{user}"
                    h+=1
                    print(f"\033[1;31m{h} \033[1;37m| \033[1;32mTài Lê Official \033[1;37m| \033[1;33mFollow \033[1;37m| \033[1;33mUser \033[1;36m{user}")
                    openWeb(link)
                    for i in range(delay, 0, -1):
                        print(f"\033[1;32mLàm nhiệm vụ tiếp theo trong \033[1;33m{i} \033[1;32mgiây   ", end="\r")
                        time.sleep(1)
                    cache = ttc.postCache(id, "FOLLOW")
                    if int(cache) >= 8:
                        time.sleep(3)
                        getxu = ttc.getXuJob("FOLLOW")
                        print(f"\033[1;32mNhận thành công \033[1;33m{getxu} \033[1;32mxu                ")
                    killBroser()
                    time.sleep(3)
                else:
                    print("\033[1;31mHiện đang hết nhiệm vụ, vui lòng thử lại sau   ", end  = '\r')
        if job == 2:
            getTym = ttc.getJobTym()
            for x in getTym:
                id = x['id']
                link = x['link']
                h+=1
                print(f"\033[1;31m{h} \033[1;37m| \033[1;32mTài Lê Official \033[1;37m| \033[1;33mTym Video \033[1;37m| \033[1;33mID Video \033[1;36m{str(link).split('video/')[1]}")
                openWeb(link)
                for i in range(delay, 0, -1):
                    print(f"\033[1;32mLàm nhiệm vụ tiếp theo trong \033[1;33m{i} \033[1;32mgiây   ", end="\r")
                    time.sleep(1)
                cache = ttc.postCache(id, "TYM")
                print(cache)
                if int(cache) >= 8:
                    time.sleep(3)
                    getxu = ttc.getXuJob("TYM")
                    print(f"\033[1;32mNhận thành công \033[1;33m{getxu} \033[1;32mxu                ")
                killBroser()
                time.sleep(3)


if (__name__ == "__main__"):
    main()