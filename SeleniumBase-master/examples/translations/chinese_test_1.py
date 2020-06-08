# Chinese Language Test
from seleniumbase.translate.chinese import 硒测试用例  # noqa


class 我的测试类(硒测试用例):

    def test_例子1(self):
        self.开启网址("https://xkcd.in/comic?lg=cn&id=353")
        self.断言标题("Python - XKCD中文站")
        self.断言元素("#content div.comic-body")
        self.断言文本("上漫画")
        self.单击("div.nextLink")
        self.断言文本("老妈的逆袭", "#content h1")
        self.单击链接文本("下一篇")
        self.断言文本("敲桌子", "#content h1")
        self.断言文本("有时候无聊就是最棒的乐趣")
        self.回去()
        self.单击链接文本("兰德尔·门罗")
        self.断言文本("兰德尔·门罗", "#firstHeading")
        self.更新文本("#searchInput", "程式设计")
        self.单击("#searchButton")
        self.断言文本("程序设计", "#firstHeading")
