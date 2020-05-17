import speedtest
st=speedtest.Speedtest()
option=int(input('''Which speed do you want to test:
1)DOWNLOAD
2.UPLOAD
3.PING
YOUR CHOICE:'''))
if option==1:
    print(st.download())
elif option==2:
    print(st.upload())
elif option==3:
    servernames=[]
    st.get_servers[servernames]
    print(st.results.ping)
else:
    print("PLEASE ENTER CORRECT CHOICE")
    
