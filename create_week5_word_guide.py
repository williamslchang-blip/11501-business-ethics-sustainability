import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def generate_week5_word_guide():
    doc = docx.Document()

    # Page Margins
    for section in doc.sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)

    # Color Palette
    DARK_BLUE = RGBColor(11, 27, 61)
    TEAL = RGBColor(0, 168, 181)
    EMERALD = RGBColor(16, 185, 129)

    # Title
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_title = p_title.add_run("📘 企業倫理與永續經營 (Business Ethics and Sustainable Management)\n"
                              "第 5 週：氣候變遷、淨零排放與企業永續策略 —— 教師深度教學指引與授課手冊")
    r_title.font.name = "Microsoft JhengHei"
    r_title.font.size = Pt(20)
    r_title.font.bold = True
    r_title.font.color.rgb = DARK_BLUE

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_sub = p_sub.add_run("AACSB / PRME / Harvard / MIT Sloan / NUS Standard • Net Zero • Scope 1,2,3 • CBAM • SBTi")
    r_sub.font.name = "Microsoft JhengHei"
    r_sub.font.size = Pt(11)
    r_sub.font.color.rgb = TEAL

    doc.add_paragraph().paragraph_format.space_after = Pt(12)

    def add_sec_heading(text, level=1):
        h = doc.add_heading(text, level=level)
        h.paragraph_format.space_before = Pt(16)
        h.paragraph_format.space_after = Pt(8)
        for r in h.runs:
            r.font.name = "Microsoft JhengHei"
            r.font.color.rgb = DARK_BLUE if level == 1 else EMERALD
            r.font.bold = True
        return h

    # Section 1: Philosophy
    add_sec_heading("📌 一、第 5 週課程設計理念與 AACSB 能力指標 (Week 5 Philosophy & Competencies)")
    
    p = doc.add_paragraph()
    p.add_run("第 5 週主題為「氣候變遷、淨零排放與企業永續策略 (Climate Change, Net Zero and Corporate Sustainability Strategy)」。"
              "本週為整門課程第一個深入探討 ESG 中『E（Environment）』核心維度的極致重點週！\n"
              "本週不流於通俗環境倡議，而是結合 Harvard、MIT Sloan、Cambridge Judge 與 NUS Business School 的授課框架，"
              "全面解析：全球氣候治理 (IPCC AR6 & 巴黎協定 1.5°C 目標)、Net Zero 淨零 vs Carbon Neutral 碳中和精準界定、"
              "Scope 1, 2, 3 碳盤查實務、碳定價與歐盟 CBAM 碳關稅，並透過 7 大國際標竿企業案例（Apple, Microsoft, IKEA, Unilever, TSMC, Delta, Ørsted）解析低碳策略。")

    # Section 2: Timeline
    add_sec_heading("⏱️ 二、2 小時 (120 分鐘) 時間配比與流程總覽 (Time Allocation Timeline)")

    table_time = doc.add_table(rows=1, cols=4)
    table_time.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr = table_time.rows[0].cells
    headers = ["時間段 (Time)", "分鐘 (Mins)", "單元主題 (Module)", "授課重點與教學任務 (Key Facilitation Tasks)"]
    for i, h in enumerate(headers):
        hdr[i].text = h
        shading = parse_xml(r'<w:shd {} w:fill="00F2FE"/>'.format(nsdecls('w')))
        hdr[i]._tc.get_or_add_tcPr().append(shading)
        for p_cell in hdr[i].paragraphs:
            p_cell.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for r in p_cell.runs:
                r.font.name = "Microsoft JhengHei"
                r.font.bold = True
                r.font.size = Pt(10)

    time_rows = [
        ("00:00 - 00:15", "15m", "Part 1：全球氣候變遷\n(Climate Change)", "【Slide 1-5】地球升溫 2°C 衝擊、IPCC AR6 極端氣候發現、企業 3 大氣候風險 (Physical Risk 實體風險, Transition Risk 轉型風險, Reputation Risk 信譽風險)。"),
        ("00:15 - 00:40", "25m", "Part 2：巴黎協定與 Net Zero\n(Paris & Net Zero)", "【Slide 6-11】2015 巴黎協定 (1.5°C vs 2°C 差異)、Net Zero 定義、Carbon Neutral vs Net Zero 比較表、2050 Net Zero 承諾與 SBTi、全球標竿企業 (Apple, MSFT, TSMC, IKEA, Ørsted)。"),
        ("00:40 - 00:55", "15m", "【活動一】：Net Zero Challenge\n(Activity 1: Net Zero Quiz)", "【Slide 12-13】10 題 True/False 搶答遊戲 ( Carbon Neutral=Net Zero?, 巴黎協定 2050 強制性?, Scope 3 可否控制?)，釐清常錯觀念。"),
        ("00:55 - 01:25", "30m", "Part 3：碳排放管理\n(Carbon Accounting)", "【Slide 14-20】Carbon Footprint 碳足跡、Scope 1 直接排放, Scope 2 能源間接排放, Scope 3 價值鏈上下游 (80-90% 最難減範疇)、Apple 供應鏈減碳、台積電/台達電標竿、ISO 14064 碳盤查與 CDP。"),
        ("01:25 - 01:45", "20m", "Part 4：碳定價與 CBAM\n(Carbon Pricing)", "【Slide 21-24】Carbon Tax 碳稅, ETS 碳交易系統, EU CBAM 歐盟碳邊境調整機制細節、CBAM 如何衝擊台灣出口供應鏈。"),
        ("01:45 - 02:00", "20m", "Part 5 & 【活動二】：減碳策略\n(Design Net Zero Firm)", "【Slide 25-27】【活動二】小組抽籤設計 Starbucks/Apple/Uniqlo/TSMC/7-Eleven 之 2050 Net Zero 藍圖（能源、運輸、供應鏈、產品、碳管理）、W5 總結與 Homework 5 指引。")
    ]

    for r_data in time_rows:
        row_cells = table_time.add_row().cells
        for i, val in enumerate(r_data):
            row_cells[i].text = val
            for p_cell in row_cells[i].paragraphs:
                for r in p_cell.runs:
                    r.font.name = "Microsoft JhengHei"
                    r.font.size = Pt(9)

    doc.add_paragraph().paragraph_format.space_after = Pt(12)

    # Section 3: 27 Slides Detailed Notes
    add_sec_heading("🗣️ 三、27 頁投影片逐頁深度授課指引 (Slide-by-Slide Instructional Notes)")

    slides_detail = [
        ("Slide 1: 課程封面 (Week 5 Climate & Net Zero)", 
         "【授課腳本】：「歡迎來到第 5 週《氣候變遷、淨零排放與企業永續策略》。本週我們將深入探討全球企業面臨的最嚴峻挑戰與最大轉型商機 —— 碳管理與 Net Zero 藍圖！」"),
        ("Slide 2: 課程轉折與脈絡 (Course Journey)", 
         "【授課腳本】：展示進程：W1-2 Ethics → W3 CSR/CSV → W4 ESG 全貌 → W5 E (氣候變遷與淨零碳排) 實務策略。"),
        ("Slide 3: 暖身思考 (Earth Warming +2°C Impact)", 
         "【提問引導】：如果地球平均升溫 2°C，企業真的會受到實質影響嗎？引導討論供應鏈中斷、保費暴增與淹水廠房風險。"),
        ("Slide 4: 全球氣候現實與 IPCC AR6 報告 (IPCC AR6 Findings)", 
         "【授課腳本】：展示 IPCC 最新報告：熱浪 (Heatwaves)、暴雨洪災 (Floods)、野火 (Wildfires)、海平面上升 (Sea Level Rise) 與極端氣候常態化。"),
        ("Slide 5: 企業面臨的三大氣候風險 (3 Climate Risks)", 
         "【授課腳本】：解析 TCFD 氣候風險框架：\n"
         "1. Physical Risk (實體風險)：廠房淹水、極端氣候中斷供應鏈。\n"
         "2. Transition Risk (轉型風險)：碳稅課徵、高碳排設備強制報廢、法規趨嚴。\n"
         "3. Reputation Risk (信譽風險)：高碳排企業遭消費者抵制與法人抽資。"),
        ("Slide 6: 巴黎協定 (Paris Agreement 2015)", 
         "【授課腳本】：解析 2015 巴黎協定目標：將全球平均升溫控制在遠低於 2°C，並努力限制在 1.5°C 以內。"),
        ("Slide 7: 1.5°C vs 2°C 的關鍵差異 (1.5°C vs 2°C Impact)", 
         "【授課指引】：對比差異：1.5°C 下極端熱浪受災人口減少 4.2 億人，珊瑚礁消失 70-90%（2°C 則全滅 99%）。1.5°C 是地球生態系防線。"),
        ("Slide 8: Net Zero 淨零排放精準定義 (What is Net Zero?)", 
         "【授課腳本】：定義 Net Zero：企業或全球透過極致減碳，將人為溫室氣體排放量降至接近零，殘餘排放量透過負碳技術（植樹、CCUS 碳捕集）完全抵銷，實現「人為排放 - 人為移除 ＝ 0」。"),
        ("Slide 9: Carbon Neutral vs. Net Zero 比較表 (Carbon Neutral vs Net Zero)", 
         "【授課指引】：深度對比：\n"
         "• Carbon Neutral (碳中和)：通常僅涵蓋 CO2，允許大量購買廉價碳權抵銷，減碳幅度無強制。\n"
         "• Net Zero (淨零排放)：涵蓋全溫室氣體 (GHGs)，要求範疇 1,2,3 進行 90-95% 深度實質減碳 (Deep Decarbonization)，殘餘 5-10% 才可永久碳移除！"),
        ("Slide 10: 企業 2050 Net Zero 承諾與 SBTi (SBTi Framework)", 
         "【授課腳本】：介紹 SBTi (科學基礎減碳目標倡議)：要求企業依據 1.5°C 目標制定具科學依據的近遠期減碳路徑。"),
        ("Slide 11: 國際 7 大標竿企業減碳承諾 (7 International Leaders)", 
         "【案例對比分析】：\n"
         "• Apple：2030 全價值鏈碳中和。\n"
         "• Microsoft：2030 實現 Carbon Negative (負碳)，2050 移除自 1975 成立以來所有累積碳排！\n"
         "• IKEA：2030 氣候正效益 (Climate Positive) 與 100% 循環家具。\n"
         "• Unilever：永續供應鏈與產品生命週期減碳。\n"
         "• 台積電 (TSMC)：全球半導體龍頭，承諾 2040 100% RE100，2050 淨零。\n"
         "• 台達電 (Delta)：能源效率龍頭，提供全球低碳自動化解方。\n"
         "• Ørsted (沃旭)：從傳統石油煤炭企業 10 年內轉型為全球離岸風電領導者！"),
        ("Slide 12: 活動一：Net Zero Challenge 搶答 (Net Zero Quiz)", 
         "【活動執行】：10 題 True/False 觀念搶答（例如：Carbon Neutral 等於 Net Zero？巴黎協定要求 2050 全球強制零碳？Scope 3 企業無法控制？）。"),
        ("Slide 13: 活動一：答案解析與迷思釐清 (Class Debrief)", 
         "【活動點評】：澄清：Carbon Neutral ≠ Net Zero；Scope 3 雖然難控，但佔企業碳足跡 80%+，是 Net Zero 評比的核心關鍵！"),
        ("Slide 14: 什麼是 Carbon Footprint 碳足跡？ (Carbon Footprint)", 
         "【授課腳本】：解析 GHG Protocol 溫室氣體盤查協定，介紹產品生命週期 (LCA) 碳足跡計算方式。"),
        ("Slide 15: Scope 1, Scope 2, Scope 3 範疇拆解 (Scope 1, 2, 3)", 
         "【授課腳本】：\n"
         "• Scope 1 (直排)：公司公務車、製程發酵、緊急發電機煙囪直排。\n"
         "• Scope 2 (外購能源)：外購電力、蒸氣、冷氣之間接排放。\n"
         "• Scope 3 (價值鏈)：原料採購、供應鏈製造、產品使用與廢棄棄置。"),
        ("Slide 16: 為什麼 Scope 3 最難卻最重要？ (Why Scope 3 Matters)", 
         "【授課指引】：展示數據：Apple、Nike、Walmart 等企業 Scope 3 佔總碳足跡高達 80%–95%。不推動供應鏈減碳，就無法實現真正的 Net Zero。"),
        ("Slide 17: Case 1: Apple 供應鏈減碳實務 (Apple Supply Chain)", 
         "【案例剖析】：Apple 推出 Clean Energy Program，提供技術協助並要求全球 200+ 關鍵供應商（含台積電、鴻海）100% 承諾使用綠電。"),
        ("Slide 18: Case 2: 台積電與台達電減碳標竿 (TSMC & Delta Cases)", 
         "【案例剖析】：台積電簽訂全球最大離岸风電購電合約 (PPA)；台達電導入內部碳定價 (ICP)，將碳費獎勵研發低碳新技術。"),
        ("Slide 19: 碳盤查與量化標準 (Carbon Accounting Standards)", 
         "【授課指引】：介紹 ISO 14064 溫室氣體盤查與 ISO 14067 產品碳足跡核算標準。"),
        ("Slide 20: CDP 碳揭露專案評級 (CDP Ratings)", 
         "【授課腳本】：介紹全球最權威 CDP (Carbon Disclosure Project) 評級：包含 A 到 D- 級，全美標普500企業 80% 以上均參與揭露。"),
        ("Slide 21: 碳定價工具 1：Carbon Tax 碳稅 (Carbon Tax)", 
         "【授課腳本】：介紹國家政府依排放噸數直接課徵的 Carbon Tax（如新加坡、台灣碳費機制）。"),
        ("Slide 22: 碳定價工具 2：ETS 總量管制碳交易 (Emissions Trading System)", 
         "【授課腳本】：介紹歐盟 EU ETS 總量管制與交易：政府發放配額，額度不足企業需於市場購買碳權。"),
        ("Slide 23: 歐盟 CBAM 碳邊境調整機制 (EU CBAM)", 
         "【授課指引】：深度解析 2026 正式實施的 CBAM (Carbon Border Adjustment Mechanism)：對進口至歐盟的高碳排商品（鋼鐵、水泥、鋁、化肥、電力、氫氣）課徵碳關稅！"),
        ("Slide 24: CBAM 如何衝擊台灣出口產業 (Impact on Exporting Firms)", 
         "【授課腳本】：分析對台灣鋼鐵、扣件、電子供應鏈衝擊：未進行碳盤查與減碳的企業，產品出口將面臨天價關稅而失去國際競爭力！"),
        ("Slide 25: 活動二：設計你的 Net Zero 企業 (Design Net Zero Company)", 
         "【活動執行】：小組抽籤審查 Starbucks, Apple, Uniqlo, TSMC, 7-Eleven，設計 2050 Net Zero 藍圖（能源、運輸、供應鏈、產品、碳管理）。"),
        ("Slide 26: 活動二：各組分享與點評 (Team Pitches)", 
         "【活動點評】：各組 3 分鐘 Pitch。教師總結服務業（門市與物流減碳）vs 製造業（製程綠電與原料替代）的 Net Zero 藍圖差異。"),
        ("Slide 27: 本週重點總結與作業 (Summary & Homework 5)", 
         "【課程總結】：展示 Climate → Net Zero → Carbon Accounting → Corporate Strategy 貫穿軸。說明 Homework 5 (1,500字) 企業碳管理分析作業與 AACSB 評分比重。")
    ]

    for title, text in slides_detail:
        p = doc.add_paragraph()
        r_t = p.add_run(f"📌 {title}\n")
        r_t.bold = True
        r_t.font.name = "Microsoft JhengHei"
        r_t.font.color.rgb = EMERALD
        r_d = p.add_run(text)
        r_d.font.name = "Microsoft JhengHei"

    doc.add_paragraph().paragraph_format.space_after = Pt(12)

    # Section 4: Rubrics Table
    add_sec_heading("📝 四、課堂作業規範與 AACSB 評分量規 (Rubric Matrix)")

    table_rubric = doc.add_table(rows=1, cols=3)
    table_rubric.alignment = WD_TABLE_ALIGNMENT.CENTER
    r_hdr = table_rubric.rows[0].cells
    r_headers = ["評分項目 (Dimension)", "比例 (Weight)", "評分標準與要求 (Evaluation Criteria)"]
    for i, h in enumerate(r_headers):
        r_hdr[i].text = h
        shading = parse_xml(r'<w:shd {} w:fill="00F2FE"/>'.format(nsdecls('w')))
        r_hdr[i]._tc.get_or_add_tcPr().append(shading)
        for p_cell in r_hdr[i].paragraphs:
            p_cell.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for r in p_cell.runs:
                r.font.name = "Microsoft JhengHei"
                r.font.bold = True
                r.font.size = Pt(10)

    rubric_data = [
        ("1. 資料蒐集 (Data Collection)", "20%", "正確引用目標企業永續報告書、CDP揭露問卷與 Net Zero 宣告資料。"),
        ("2. Net Zero 分析 (Net Zero Audit)", "30%", "精準分析 Net Zero 目標年份、減碳路徑與是否符合巴黎協定 1.5°C。"),
        ("3. 碳管理策略 (Carbon Strategy)", "25%", "深入剖析 Scope 1、2、3 之具體減碳措施與供應鏈管理手段。"),
        ("4. 個人建議 (Managerial Recommendations)", "15%", "具體指出該企業轉型面臨的最大挑戰，並提出可行性戰略建議。"),
        ("5. 報告品質 (Report Quality)", "10%", "篇幅達 1,500 字，邏輯嚴謹，圖表引用與文獻標註完整。")
    ]

    for r_data in rubric_data:
        row_cells = table_rubric.add_row().cells
        for i, val in enumerate(r_data):
            row_cells[i].text = val
            for p_cell in row_cells[i].paragraphs:
                for r in p_cell.runs:
                    r.font.name = "Microsoft JhengHei"
                    r.font.size = Pt(9)

    doc.save(r"C:\Users\User\Desktop\第1週_企業為何需要倫理\第5週_氣候變遷與淨零排放.docx")
    print("Successfully generated Week 5 Word .docx file!")

if __name__ == "__main__":
    generate_week5_word_guide()
