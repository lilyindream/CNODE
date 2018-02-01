项目结构：
1.se_node: src,chrome.driver,readme.md，nodenv

2.nodenv:虚拟环境(安装有selenium，Lib文件夹下有HTMLTestRunner)
    导入的HTMLTestRunner:
    http://tungwaiyip.info/software/HTMLTestRunner.html
    下载好并做如下修改
    第94行
    import StringIO
    改为
    import io
    第539行
    self.outputBuffer = StringIO.StringIO()
    改为
    self.outputBuffer = io.StringIO()
    第631行
          print >>sys.stderr, '\nTime Elapsed: %s' % (self.stopTime-self.startTime)
       改为
          print(sys.stderr, '\nTime Elapsed: %s' % (self.stopTime-self.startTime))
    第642行
    if not rmap.has_key(cls):
    改为
    if not cls in rmap:
    第766行
    uo = o.decode('latin-1')
    改为
    uo = e
    第772行
    ue = e.decode('latin-1')
    改为
    ue = e
    第774行
    ue = e.decode('latin-1')
    改为
    ue = e
    第778行
    output=saxutils.escape(uo+ue)
    改为
    output=saxutils.escape(str(uo)+str(ue))
    修改好后保存到项目python环境的lib下

3 src:data,report,screenshots,senarios

4 data:register_testdata 测试数据

5.library:
getRootPath.py 获得项目根路径
getData.py 获得测试数据
asserting.py 判断测试用例是否成功
capturing.py 截图
pdata.py   公共变量
register.py  注册
mongodb.py  激活注册的账号
loginout.py 登录和退出
post.py  发帖

6 senarios： 测试场景
TestCnode.py
运行的时候不要右击运行unittest(会不执行main函数部分，会导致无法生成测试报告和截图)，可以到EditConfiguration里配置脚本路径后，再右击执行