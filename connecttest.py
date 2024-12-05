from rcon import MCRcon

if __name__ == '__main__':

    # with MCRcon('121.41.172.247','data708983',25575) as mcr:
    #     resp = mcr.command("/say helloworld")
    #     print(resp)  # 输出

    mcr = MCRcon("121.41.172.247", "data708983", 1243, 2)
    mcr.connect()  # 连接建立

    resp = mcr.command("list")
    print(resp)  # 输出

    mcr.disconnect()  # 断开连接