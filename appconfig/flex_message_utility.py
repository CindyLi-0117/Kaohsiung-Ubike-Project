class BubbleBuilder:
    def __init__(self, header, title, address, sbi, bemp, mday, map_label, map_url):
        self.header = header
        self.title = title
        self.address = address
        self.sbi = sbi
        self.bemp = bemp
        self.mday = mday
        self.map_label = map_label
        self.map_url = map_url

    def createBubble(self):
        return {
            "type": "bubble",
            "header": self.createHeader(),
            "body": self.createBody(),
            "footer": self.createFooter()
        }

    def createHeader(self):
        header_content_list = []
        
        header_content = {
            "type": "text",
            "text": self.header,
            "align": "center",
            "weight": "bold",
            "size": "xxl"
        }

        header_content_list.append(header_content)

        header_box = {
            "type": "box",
            "layout": "vertical",
            "borderWidth": "light",
            "background": {
                "type": "linearGradient",
                "angle": "0deg",
                "startColor": "#ffd700",
                "endColor": "#ff8c00"
            },
            "contents": header_content_list
        }

        return header_box

    def createBody(self):
        body_content_list = []

        body_content_title = {
            "type": "text",
            "text": self.title,
            "weight": "bold",
            "size": "md",
            "align": "center",
            "decoration": "underline"
        }

        body_content_list.append(body_content_title)

        body_content_info = {
            "type": "box",
            "layout": "vertical",
            "contents": [self.createBodyInfo("地址", self.address),
                         self.createBodyInfo("目前車輛數", self.sbi),
                         self.createBodyInfo("空位數量", self.bemp),
                         self.createBodyInfo("資料更新時間", self.mday)]
        }

        body_content_list.append(body_content_info)

        body_box = {
            "type": "box",
            "layout": "vertical",
            "margin": "md",
            "contents": body_content_list
        }

        return body_box

    def createFooter(self):
        footer_content_list = []

        footer_content = {
            "type": "button",
            "height": "sm",
            "action": {
              "type": "uri",
              "label": self.map_label,
              "uri": self.map_url
            }
        }

        footer_content_list.append(footer_content)

        footer_box = {
            "type": "box",
            "layout": "vertical",
            "contents": footer_content_list
        }

        return footer_box
    
    def createBodyInfo(self, label, value):
        info_content_list = [
            {
            "type": "text",
            "text": label,
            "color": "#aaaaaa",
            "size": "sm",
            "flex": 1,
            "margin": "md"
            },
            {
                "type": "text",
                "text": value,
                "wrap": True,
                "color": "#666666",
                "size": "md",
                "flex": 5,
                "margin": "sm"
            }
        ]

        info_box = {
            "type": "box",
            "layout": "vertical",
            "spacing": "md",
            "contents": info_content_list
        }

        return info_box

