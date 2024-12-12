from rcon import MCRcon
import atexit
import getpass
from mccolors.mccolors.mc_color_handler import mcwrite, mcreplace, mcremove

if __name__ == '__main__':

    def clearWindows():
        print('\033[2J\033[H', end='')


    class connectInit():

        ip = ''
        port = ''
        pwd = ''
        pwi = ''
        pwc = ''
        timeout = 2
        lts = False

        clearWindows()
        # print("\n\033[1;37;41m Minecraft-Rcon \033[0m console v0.0.1")
        while 1:
            print("\n\033[1;37;41m Minecraft-Rcon \033[0m console v0.0.1")
            print("\n配置你的服务器:")
            print("\n开始配置 [\033[1;30;43mEnter\033[0m]")
            if input() == '':
                break
            else:
                clearWindows()
        # ip
        while 1:
            clearWindows()
            print("\n\033[1;37;41m Minecraft-Rcon \033[0m console v0.0.1")
            print("\n配置你的服务器1/3:")
            ipi = input("\n你的ip地址(不包含端口):")
            if ipi == '':
                pass
            else:
                ipc = input("\n确定 [\033[1;30;43myes\033[0m]\n重设 [\033[1;30;43melse\033[0m]\n")
                if ipc == 'yes' or '':
                    ip = ipi
                    break
                else:
                    pass
        # port
        while 1:
            clearWindows()
            print("\n\033[1;37;41m Minecraft-Rcon \033[0m console v0.0.1")
            print("\n配置你的服务器2/3:")
            poi = input("\nRcon端口:")
            if poi == '':
                pass
            else:
                poc = input("\n确定 [\033[1;30;43myes\033[0m]\n重设 [\033[1;30;43melse\033[0m]\n")
                if poc == 'yes' or '':
                    port = poi
                    break
                else:
                    pass
        # pwd
        while 1:
            if pwi == '' and pwc == '':
                clearWindows()
            else:
                clearWindows()
                print('\n\033[1;30;43m两次密码不一致\033[0m')
            print("\n\033[1;37;41m Minecraft-Rcon \033[0m console v0.0.1")
            print("\n配置你的服务器3/3:")
            pwi = getpass.getpass("\n密码(不会显示):")
            if pwi == '':
                pass
            else:
                pwc = getpass.getpass("\n再次输入:")
                if pwc == pwi:
                    pwd = pwi
                    break
                else:
                    pass

        mcr = MCRcon(ip, pwd, int(port), 2)
        try:
            mcr.connect()  # 连接建立
        except:
            print("\n出现错误，请重试!")
            exit(3)

        atexit.register(mcr.disconnect)


    connection = connectInit()
    def beforeLoop():
        clearWindows()
        print("\n\033[1;37;41m Minecraft-Rcon \033[0m console v0.0.1")
        print("\n连接成功! [ IP: "+connection.ip+' : '+connection.port+' ]')
    beforeLoop()
    while 1:
        try:
            command = input(">")
            if command != 'stop' and command != 'exit':
                resp = connection.mcr.command(command)
                # print(resp)  # 输出
                mcwrite(resp, reset_all=True)
            elif command == 'exit':
                # connection.mcr.disconnect()
                # del connection
                # connection = connectInit()
                # clearWindows()
                # beforeLoop()
                print('\n已退出\n')
                break
            else: pass
        except:
            print('\n中断链接!')
            exit(3)

