# -*- coding: utf-8 -*-
import httplib, urllib2,json,random,time
jue1='QSMY_M_9000_30=%7B%22userId%22%3A49129%2C%22plat%22%3A24%2C%22platId%22%3A%2232342370%22%2C%22name%22%3A%22%5Cu300e%5Cu5fa1%5Cu98ce%5Cu300f%5Cu73cf%22%2C%22mCode%22%3A%2202DBA835D-BECC-4F09-9781-B13D35D549C3%22%2C%22sysType%22%3A%22ios%22%2C%22eqType%22%3A%22iPhone6%2C2_Darwin_15.0.0%22%2C%22ip%22%3A%22218.29.102.110%22%2C%22sig%22%3A%22f8d521cfc25c4ae0daeb929b50b6b2c6%22%7D'
    #jue2
jue2='QSMY_M_9000_30=%7B%22userId%22%3A49149%2C%22plat%22%3A24%2C%22platId%22%3A%2232365111%22%2C%22name%22%3A%22%5Cu73cf2%22%2C%22mCode%22%3A%2202DBA835D-BECC-4F09-9781-B13D35D549C3%22%2C%22sysType%22%3A%22ios%22%2C%22eqType%22%3A%22iPhone6%2C2_Darwin_15.0.0%22%2C%22ip%22%3A%22218.29.102.114%22%2C%22sig%22%3A%22a101f57889bf0c991202a0ebd9493864%22%7D'
class AutoQ(object):
    usercookie=jue1
    zj=29
    gk=8
    def getPage(self,url):
        try:
            opener = urllib2.build_opener()
            opener.addheaders=[("Host", "s9030.mobile01.qins.com"),
                    ("User-Agent", "秦时明月 4.0.1 (iPhone; iPhone OS 9.2; zh_CN)"),
                    ("Accept", "*/*"),
                    ("Cookie",self.usercookie)
                    ]
            page = opener.open(url).read()
            return page             
        except urllib2.URLError, e:
            print e
                    

    def explore(self):
        s=''
        if self.gk<10:
            s='0'
        url='http://s9030.mobile01.qins.com/interface.php?s=Explore&m=exec&a={"mid":'+str(self.zj)+s+str(self.gk)+'}&v=4.0&fv=4.0.1'
        while 1:
            page = self.getPage(url)
            print page
            data=json.loads(page[page.find('{"code"'):])#page中提取json数据     
            if not data['data']:
                break
            if not data['data']['pve']['power']:
                    break
                    

    def tower(self):
         login='http://s9030.mobile01.qins.com/interface.php?s=Activity&m=getLoginAward&a={}&v=4.0&fv=4.0.1'
         page = self.getPage(login)
         data = json.loads(page)
         if not data['data']:
                 return
         print data['data']
         st='http://s9030.mobile01.qins.com/interface.php?s=Tower&m=start&a={}&v=4.0&fv=4.0.1'
         page=self.getPage(st)
         data=json.loads(page[page.find('{"code"'):])
         st='http://s9030.mobile01.qins.com/interface.php?s=Tower&m=get&a={}&&v=4.0&fv=4.0.1'
         while 1:
             try:
                 page=self.getPage(st)
                 data=json.loads(page[page.find('{"code"'):])
                 print data
                 if data['data']['tower']['buffstr']!='':
                         res=data['data']['tower']['buffstr']
                         scores=data['data']['tower']['scores']
                         for i in range(2, -1, -1):
                                 if res[i]['cost']<=scores:
                                         print 'scores'
                                         st='http://s9030.mobile01.qins.com/interface.php?s=Tower&m=setBuff&a={"id"%3A'+str(res[i]['id'])+'}&&v=4.0&fv=4.0.1'
                                         break #加成
                 else:
                         if data['data']['tower']['rstatus']==2:
                            break#已死亡
                         if data['data']['tower']['rstatus']==3:
                                 print 'False'
                                 if data['data']['tower']['continue']<3:
                                         print 'send retry'
                                         st='http://s9030.mobile01.qins.com/interface.php?s=Tower&m=goOn&a={}&v=4.0&fv=4.0.1'
                                 else:
                                         break;
                         else:
                                 st='http://s9030.mobile01.qins.com/interface.php?s=Tower&m=fight&a={"lv"%3A3}&&v=4.0&fv=4.0.1'
             except Exception, e:
                print e
                st='http://s9030.mobile01.qins.com/interface.php?s=Tower&m=get&a={}&&v=4.0&fv=4.0.1'


    def hunt(self):
        #return 'haha'
        #return
        login='http://s9030.mobile01.qins.com/interface.php?s=Activity&m=getLoginAward&a={}&v=4.0&fv=4.0.1' 
        page = self.getPage(login)
        #print page
        data = json.loads(page)
        if not data['data']:
                return
        print data['data']
        #初始化我方数据
        st = 'http://s9030.mobile01.qins.com/interface.php?s=System&m=init&a={}&v=4.0&fv=4.0.1'
        page = self.getPage(st)
        data = json.loads(page[page.find('{"code"'):])
        #print data
        mylv=data['data']['user']['lv']
        warriors = data['data']['warriors']
        warriors = sorted(warriors, key=lambda warriors:warriors['lv'], reverse=True)
        #print warriors
        ok=1
        while ok:
            st="http://s9030.mobile01.qins.com/interface.php?s=Hunt&m=get&a={}&v=4.0&fv=4.0.1"
            page=self.getPage(st)
            data=json.loads(page[page.find('{"code"'):])
            if data['data']['hunt']['power']==0:
                print '体力不足'
                ok=0
                break
            num=random.randint(0, len(warriors)%22)#最多22个
            while ok:#持续刷新
                st='http://s9030.mobile01.qins.com/interface.php?s=Hunt&m=targets&a={"wid":'+str(warriors[num]['wid'])+"}&v=4.0&fv=4.0.1"
                print st
                page = self.getPage(st)
                data = json.loads(page[page.find('{"code"'):])
                print '获取猎物',data
                if data['data']:
                    ct=0
                    while ct<3:
                        if data['data']['huntTargets'][ct]['lv']<mylv-5 or data['data']['huntTargets'][ct]['isNpc']:
                            break
                        ct=ct+1
                    if ct<3:
                        err=0
                        while 1:
                            st='http://s9030.mobile01.qins.com/interface.php?s=Hunt&m=attack&a={"isNpc":'+str(data['data']['huntTargets'][ct]['isNpc'])+',"tid":'+str(data['data']['huntTargets'][ct]['uid'])+',"wid":'+str(warriors[num]['wid'])+'}&v=4.0&fv=4.0.1'
                            page=self.getPage(st)
                            print '检查猎物是否获取1',page[page.find('{"code"'):]
                            data2=json.loads(page[page.find('{"code"'):])
                            huntRes=1
                            try:
                                huntRes=data2['data']['huntRes']
                            except Exception,e:
                                print e
                                err+=1
                                huntRes=0
                                if err>5:
                                    ok=0
                                    print '出错次数太多'
                                    break
                            st="http://s9030.mobile01.qins.com/interface.php?s=Hunt&m=get&a={}&v=4.0&fv=4.0.1"
                            page=self.getPage(st)
                            data2=json.loads(page[page.find('{"code"'):])
                            print '查看体力剩余量',data2
                            if data2['data']['hunt']['power']==0:
                                ok=0
                                print '体力不足'
                                break
                else:#已达到当天猎取最多数
                   break       
                            
if __name__=='__main__':
    m=AutoQ()
    m.hunt()
