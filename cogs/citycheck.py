def city(sid):
    cid: int = 0
    if sid == "稚内":
        cid = 011000
    elif sid == "旭川":
        cid = 012010
    elif sid == "留萌":
        cid = 012020  
    elif sid == "網走":
        cid = 013010
    elif sid == "北見":
        cid = 013020
    elif sid == "紋別":
        cid = 013030
    elif sid == "根室":
        cid = 014010
    elif sid == "釧路":
        cid = 014020
    elif sid == "帯広":
        cid == 014030
    elif sid == "室蘭":
        cid = 015010
    elif sid == "浦賀":
        cid = 015020
    elif sid == "札幌":
        cid = 016010
    elif sid == "岩見沢":
        cid = 016020   
    elif sid == "倶知安":
        cid = 016030
    elif sid == "函館":
        cid = 017010
    elif sid == "江差":
        cid = 017020
    elif sid == "青森":
        cid = 020010
    elif sid == "むつ":
        cid = 020020
    elif sid == "八戸":
        cid = 020030
    elif sid == "盛岡":
        cid = 030010
    elif sid == "宮古":
        cid = 030020
    elif sid == "大船渡":
        cid = 030030
    elif sid == "仙台":
        cid = 040010
    elif sid == "白石":
        cid = 040020
    elif sid == "秋田":
        cid = 050010
    elif sid == "横手":
        cid = 050020
    elif sid == "山形":
        cid = 060010
    elif sid == "米沢":
        cid = 060020
    elif sid == "酒田":
        cid = 060030
    elif sid == "新庄":
        cid = 060040
    elif sid == "福島":
        cid = 070010
    elif sid == "小名浜":
        cid = 070020
    elif sid == "若松":
        cid = 070030
    elif sid == "水戸":
        cid = 080010
    elif sid == "土浦":
        cid = 080020
    elif sid == "宇都宮":
        cid = 090010
    elif sid == "大田原":
        cid = 090020
    elif sid == "前橋":
        cid = 100010
    elif sid == "みなかみ":
        cid = 100020
    elif sid == "さいたま":
        cid = 110010
    elif sid == "熊谷":
        cid = 110020
    elif sid == "秩父":
        cid = 110030
    elif sid == "千葉":
        cid = 120010
    elif sid == "銚子":
        cid = 120020
    elif sid == "舘山":
        cid = 120030
    elif sid == "東京":
        cid = 130010
    elif sid == "大島":
        cid = 130020
    elif sid == "八丈島":
        cid = 130030
    elif sid == "父島":
        cid = 130040
    elif sid == "横浜":
        cid = 140010
    elif sid == "小田原":
        cid = 140020
    elif sid == "新潟":
        cid = 150010
    elif sid == "長岡":
        cid = 150020
    elif sid == "高田":
        cid = 150030
    elif sid == "相川":
        cid = 150040
    elif sid == "富山":
        cid = 160010
    elif sid == "伏木":
        cid = 160020
    elif sid == "金沢":
        cid = 170010
    elif sid == "輪島":
        cid = 170020
    elif sid == "福井":
        cid = 180010
    elif sid == "敦賀":
        cid = 180020
    elif sid == "甲府":
        cid = 190010
    elif sid == "河口湖":
        cid = 190020
    elif sid == "長野":
        cid = 200010
    elif sid == "松本":
        cid = 200020
    elif sid == "飯田":
        cid = 200030
    elif sid == "岐阜":
        cid = 210010
    elif sid == "高山":
        cid = 210020
    elif sid == "静岡":
        cid = 220010
    elif sid == "網代":
        cid = 220020
    elif sid == "三島":
        cid = 220030
    elif sid == "浜松":
        cid = 220040
    elif sid == "名古屋":
        cid = 230010
    elif sid == "豊橋":
        cid = 230020
    elif sid == "津":
        cid = 240010
    elif sid == "尾鷲":
        cid = 240020
    elif sid == "大津":
        cid = 250010
    elif sid == "彦根":
        cid = 250020
    elif sid == "京都":
        cid = 260010
    elif sid == "舞鶴":
        cid = 260020
    elif sid == "大阪":
        cid == 270000
    elif sid == "神戸":
        cid = 280010
    elif sid == "豊岡":
        cid = 280020
    elif sid == "奈良":
        cid = 290010
    elif sid == "風屋":
        cid = 290020
    elif sid == "和歌山":
        cid = 300010
    elif sid == "潮岬":
        cid = 300020
    elif sid == "鳥取":
        cid = 310010
    elif sid == "米子":
        cid = 310020
    elif sid == "松江":
        cid = 320010
    elif sid == "浜田":
        cid = 320020
    elif sid == "西郷":
        cid = 320030
    elif sid == "岡山":
        cid = 330010
    elif sid == "津山":
        cid = 330020
    elif sid == "広島":
        cid = 340010
    elif sid == "庄原":
        cid = 340020
    elif sid == "下関":
        cid = 350010
    elif sid == "山口":
        cid = 350020
    elif sid == "柳井":
        cid = 350030
    elif sid == "萩":
        cid = 350040
    elif sid == "徳島":
        cid = 360010
    elif sid == "日和佐":
        cid = 360020
    elif sid == "高松":
        cid = 370000
    elif sid == "松山":
        cid = 380010
    elif sid == "新居浜":
        cid = 380020
    elif sid == "宇和島":
        cid = 380030
    elif sid == "高知":
        cid = 390010
    elif sid == "室戸岬":
        cid = 390020
    elif sid == "清水":
        cid = 390030
    elif sid == "福岡":
        cid = 400010
    elif sid == "八幡":
        cid = 400020
    elif sid == "飯塚":
        cid = 400030
    elif sid == "久留米":
        cid = 400040
    elif sid == "佐賀":
        cid = 410010
    elif sid == "伊万里":
        cid = 410020
    elif sid == "長崎":
        cid = 420010
    elif sid == "佐世保":
        cid = 420020
    elif sid == "厳原":
        cid = 420030
    elif sid == "福江":
        cid = 420040
    elif sid == "熊本":
        cid = 430010
    elif sid == "阿蘇乙姫":
        cid = 430020
    elif sid == "牛深":
        cid = 430030
    elif sid == "人吉":
        cid = 430040
    elif sid == "大分":
        cid = 440010
    elif sid == "中津":
        cid = 440020
    elif sid == "日田":
        cid = 440030
    elif sid == "佐伯":
        cid = 440040
    elif sid == "宮崎":
        cid = 450010
    elif sid == "延丘":
        cid = 450020
    elif sid == "都城":
        cid = 450030
    elif sid == "高千穂":
        cid = 450040
    elif sid == "鹿児島":
        cid = 460010
    elif sid == "鹿屋":
        cid = 460020
    elif sid == "種子島":
        cid = 460030
    elif sid == "名瀬":
        cid = 460040
    elif sid == "那覇":
        cid = 471010
    elif sid == "名護":
        cid = 471020
    elif sid == "久米島":
        cid = 471030
    elif sid == "南大東":
        cid = 472000
    elif sid == "宮古島":
        cid = 473000
    elif sid == "石垣島":
        cid = 474010
    elif sid == "与那国島":
        cid = 474020
        
    return cid