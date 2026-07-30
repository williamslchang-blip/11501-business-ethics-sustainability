import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def generate_week4_word_guide():
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
    GREEN = RGBColor(16, 185, 129)

    # Title
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_title = p_title.add_run("📘 企業倫理與永續經營 (Business Ethics and Sustainable Management)\n"
                              "第 4 週：ESG 與永續發展：企業競爭力的新標準 —— 教師深度教學指引與授課手冊")
    r_title.font.name = "Microsoft JhengHei"
    r_title.font.size = Pt(20)
    r_title.font.bold = True
    r_title.font.color.rgb = DARK_BLUE

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_sub = p_sub.add_run("AACSB / PRME / UN SDGs / Global Business Schools Standard • GRI, SASB, TCFD, ISSB • MSCI ESG Ratings")
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
            r.font.color.rgb = DARK_BLUE if level == 1 else GREEN
            r.font.bold = True
        return h

    # Section 1: Philosophy
    add_sec_heading("📌 一、第 4 週課程設計理念與 AACSB 能力指標 (Week 4 Philosophy & Competencies)")
    
    p = doc.add_paragraph()
    p.add_run("第 4 週主題為「ESG 與永續發展：企業競爭力的新標準 (ESG and Sustainable Development: The New Standard for Business Competitiveness)」。"
              "本週為整門課程最核心的能力建構週！W1–W3 建立了倫理與 CSR 的基礎，W4 正式開啟 ESG 三大構面（Environmental, Social, Governance）與國際評比架構。\n"
              "本週重點不在於死記 E、S、G 詞彙，而是引導學生理解：「ESG 並非 CSR 的替代新名詞，而是資本市場、投資人、政府與高階經理人用來評估『企業風險管理與永續治理』的核心戰略工具。」")

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
        ("00:00 - 00:15", "15m", "Part 1：ESG 為什麼誕生？\n(Why ESG Born?)", "【Slide 1-5】從 Ethics/CSR 到 ESG、投資人兩難問題（相同 EPS 污染 vs ESG全球前10%）、驅動 ESG 5 大力量 (Climate, Investors, Consumers, Gov, Employees) 與 CSR vs ESG 比較矩陣。"),
        ("00:15 - 00:50", "35m", "Part 2：ESG 三大構面\n(ESG 3 Pillars)", "【Slide 6-13】E 氣候能源/廢棄物 (Apple 2030)、S 人權/DEI/供應鏈 (Nike 童工)、G 董事會獨立性/內控/薪酬 (Toyota 品質治理)；強調 ESG 是一套完整管理系統。"),
        ("00:50 - 01:05", "15m", "【活動一】：ESG 分類挑戰\n(ESG Sorting Challenge)", "【Slide 14-15】20 張情境卡分類演練（董事會女性比例、安衛訓練、再生能源、吹哨者制度、社區志工、節能設備、高階薪酬、個資保護），釐清 E/S/G 邊界。"),
        ("01:05 - 01:25", "20m", "Part 3：SDGs 與企業\n(SDGs & Enterprises)", "【Slide 16-18】聯合國 17 SDGs 圖譜、企業最常結合的 5 大 SDGs (SDG 7, 8, 9, 12, 13) 與台灣標竿案例（台積電、玉山金、中華電信）。"),
        ("01:25 - 01:45", "20m", "Part 4 & 【活動二】：評比與診斷\n(Ratings & Diagnosis)", "【Slide 19-24】國際準則 (GRI, ISSB, SASB, TCFD, CDP)、MSCI ESG Rating (AAA to CCC)、ESG Washing 疑慮；【活動二】小組抽籤診斷 Apple/TSMC/Tesla/Uniqlo/Google。"),
        ("01:45 - 02:00", "15m", "Part 5：總結與 W5 預告\n(Summary & Preview)", "【Slide 25-26】CSR → ESG → SDGs → Rating → Competitiveness 演進總結、W5 氣候變遷與淨零排放預告、Homework 4 (1,500–2,000字) 永續報告書分析作業交代與 5 大 AACSB 評分權重。")
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

    # Section 3: 26 Slides Detailed Notes
    add_sec_heading("🗣️ 三、26 頁投影片逐頁深度授課指引 (Slide-by-Slide Instructional Notes)")

    slides_detail = [
        ("Slide 1: 課程封面 (Week 4 ESG & Sustainable Development)", 
         "【授課腳本】：「歡迎來到第 4 週《ESG 與永續發展：企業競爭力的新標準》。本週我們正式邁入全球資本市場與高階經理人最重視的 ESG 核心維度！」"),
        ("Slide 2: 演進路徑 (Business Ethics → CSR → ESG)", 
         "【授課腳本】：展示進程：W1-2 Ethics (道德基石) → W3 CSR (社會責任行動) → W4 ESG (永續治理與資本評比)。"),
        ("Slide 3: 暖身問題 (Investor Dilemma: Pollution EPS vs ESG Top 10%)", 
         "【提問引導】：假設你是投資人，兩家公司獲利完全相同：A 公司污染嚴重但 EPS 高；B 公司 EPS 稍低但 ESG 是全球前 10%，你會選哪一家？引導資本市場資金偏好轉移。"),
        ("Slide 4: 為什麼企業開始談 ESG？ (5 Driving Forces)", 
         "【授課腳本】：解析 5 大驅動力量：氣候變遷危機 (Climate Change) → 投資人機構減碳要求 (Investors) → 消費者價值選品 (Consumers) → 各國碳關稅法規 (Governments) → 頂尖人才留任 (Employees)。"),
        ("Slide 5: CSR vs. ESG 比較矩陣 (CSR vs. ESG)", 
         "【授課腳本】：深度對比：\n"
         "• CSR：企業自願、公益活動、公關形象、社會責任 (Voluntary & Philanthropic)\n"
         "• ESG：投資人強制需求、風險管理、企業治理、核心競爭力 (Investor Demand & Risk Management)"),
        ("Slide 6: ESG 三大構面概述 (What is ESG?)", 
         "【授課腳本】：拆解 E (Environment 環保)、S (Social 社會責任)、G (Governance 公司治理) 核心定義。"),
        ("Slide 7: Environment (E) 構面指標", 
         "【授課腳本】：E 的 5 大核心指標：溫室氣體排放 (Carbon)、能源使用效率 (Energy)、廢棄物循環 (Waste)、水資源管理 (Water) 與生物多樣性 (Biodiversity)。"),
        ("Slide 8: E 構面案例：Apple 2030 碳中和 (Apple Case)", 
         "【案例剖析】：Apple 承諾 2030 年全價值鏈（包含全球供應鏈製造與產品生命週期）實現 100% 碳中和，倒逼供應商全面使用綠電。"),
        ("Slide 9: Social (S) 構面指標", 
         "【授課腳本】：S 的 5 大核心指標：員工權益與人權 (Human Rights)、勞工安全與健康 (Labor Safety)、多元平等包容 (DEI)、社區關係 (Community) 與消費者保護 (Customer Protection)。"),
        ("Slide 10: S 構面案例：Nike 供應鏈童工風暴與改造 (Nike Case)", 
         "【案例剖析】：1990s Nike 海外代工廠童工與血汗工廠醜聞重創品牌。Nike 隨後建立業界最嚴格的供應鏈勞工稽核與 100% 資訊公開機制。"),
        ("Slide 11: Governance (G) 構面指標", 
         "【授課腳本】：G 的 5 大核心指標：董事會獨立性 (Board Independence)、資訊透明揭露 (Disclosure)、內部控制與風險管理 (Internal Controls)、誠信經營與反貪腐 (Integrity)、高階主管薪酬連結 ESG (Executive Pay)。"),
        ("Slide 12: G 構面案例：Toyota 品質認證治理危機 (Toyota Case)", 
         "【案例剖析】：解析 Toyota 測試數據造假疑雲，凸顯公司治理（董事會監督、內部舉報機制與高層問責）才是企業長青的真正保險。"),
        ("Slide 13: ESG 不是三件事，而是一套管理系統 (ESG System Diagram)", 
         "【授課指引】：展示流程圖：Governance (G 治理靈魂) 驅動 Environment (E 環保轉型) 與 Social (S 社會包容)，最終體現在企業戰略價值。"),
        ("Slide 14: 活動一：ESG 分類挑戰 (ESG Sorting Challenge)", 
         "【活動執行】：4人一組，發放 20 張情境卡（董事會女性比例、安衛訓練、再生能源、吹哨者制度、社區志工、節能設備、高階薪酬、個資保護）。"),
        ("Slide 15: 活動一：答案公布與分類迷思辯論 (Class Debrief)", 
         "【活動點評】：釐清常見混淆點：如「個資保護屬於 S (顧客權益) 還是 G (內動資安)？」說明 ESG 三者交叉影響。"),
        ("Slide 16: 聯合國 17 項 SDGs 永續發展目標 (UN 17 SDGs)", 
         "【授課腳本】：介紹 2015 聯合國提出的 17 項 Sustainable Development Goals (SDGs)，作為全球 2030 年永續發展共通語言。"),
        ("Slide 17: 企業最常對應的 5 大 SDGs (Top 5 Corporate SDGs)", 
         "【授課腳本】：聚焦企業最常對接的 5 大目標：SDG 7 可負擔清潔能源、SDG 8 體面工作與經濟成長、SDG 9 產業創新與基礎建設、SDG 12 責任消費與生產、SDG 13 氣候行動。"),
        ("Slide 18: 台灣企業 SDGs 標竿案例 (Taiwan SDGs Cases)", 
         "【案例剖析】：\n"
         "• 台積電 (TSMC)：對接 SDG 7 & 13，全球首家加入 RE100 的半導體巨擘。\n"
         "• 玉山金控 (E.SUN)：對接 SDG 8 & 13，推動零碳綠色金融與永續放款。\n"
         "• 中華電信：對接 SDG 9，推動數位包容與偏鄉 5G 建設。"),
        ("Slide 19: 全球主要 ESG 國際報導與揭露準則 (Global ESG Standards)", 
         "【授課指引】：解析 5 大國際框架：\n"
         "1. GRI (Global Reporting Initiative)：涵蓋廣泛利害關係人的揭露標準。\n"
         "2. SASB (Sustainability Accounting Standards Board)：聚焦特定產業財務重大性指標。\n"
         "3. TCFD (Task Force on Climate-related Financial Disclosures)：氣候財務風險揭露。\n"
         "4. ISSB (International Sustainability Standards Board)：國際永續準則理事會整合新標準。\n"
         "5. CDP (Carbon Disclosure Project)：全球碳揭露問卷。"),
        ("Slide 20: MSCI ESG Rating 評比系統 (MSCI ESG Ratings)", 
         "【授課腳本】：介紹全球權威 MSCI ESG 評級：包含 7 級（AAA, AA 領先者 → A, BBB, BB 平均 → B, CCC 落後者）。全球機構投資人據此調整持股部位。"),
        ("Slide 21: ESG 評比如何影響企業資本運作 (Financial Impacts)", 
         "【授課腳本】：說明 ESG 高分企業的三大優勢：(1) 吸引外資與 ESG 基金買進；(2) 獲得銀行綠色融資貸款利率優惠；(3) 降低企業資本成本 (Cost of Capital)。"),
        ("Slide 22: 什麼是 ESG Washing 漂洗疑慮？ (ESG Washing Risks)", 
         "【授課指引】：剖析 3 種漂洗型態：\n"
         "• Greenwashing (綠色漂洗)：誇大減碳效益。\n"
         "• Social Washing (社會漂洗)：標榜 DEI 但內部性騷與低薪氾濫。\n"
         "• Governance Washing (治理漂洗)：宣稱獨立董事但由家族傀儡控制。"),
        ("Slide 23: 活動二：企業 ESG 實務診斷 (ESG Company Diagnosis)", 
         "【活動執行】：小組抽籤審查 Apple、TSMC、Tesla、Uniqlo、Google，回答：(1) 最強構面？(2) 最需改善構面？(3) 爭議事件？(4) CEO 未來 3 年優先順序？"),
        ("Slide 24: 活動二：各組分享與教師引導點評 (Team Pitches)", 
         "【活動點評】：各組 3 分鐘 Pitch。教師總結製造業 (E為主) vs 金融/科技業 (G與S為主) 的策略差異。"),
        ("Slide 25: 本週重點總結 (Week 4 Key Takeaways)", 
         "【課程總結】：展示 CSR → ESG → SDGs → Ratings → Competitive Advantage 戰略鏈。ESG 是企業長遠競爭力的硬實力。"),
        ("Slide 26: 下週課程預告 (Week 5 Preview)", 
         "【課程預告】：預告 Week 5 主題：《氣候變遷、碳中和與淨零排放 (Climate Change, Carbon Neutrality & Net Zero)》，深入探索 E 構面最前沿趨勢。")
    ]

    for title, text in slides_detail:
        p = doc.add_paragraph()
        r_t = p.add_run(f"📌 {title}\n")
        r_t.bold = True
        r_t.font.name = "Microsoft JhengHei"
        r_t.font.color.rgb = GREEN
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
        ("1. ESG 三構面分析 (ESG 3 Pillars Analysis)", "30%", "精準分析目標企業在 E、S、G 三個構面的重點措施與成效。"),
        ("2. SDGs 與國際準則應用 (SDGs & Standards)", "25%", "正確連結 UN SDGs 目標，並分析是否引用 GRI、ISSB、SASB 或 TCFD。"),
        ("3. 永續報告書解讀能力 (Report Audit Skills)", "20%", "展現解讀上市公司真實永續報告書 (Sustainability Report) 的專業能力。"),
        ("4. 批判分析與改善建議 (Critical Analysis)", "15%", "客觀辨識企業最成功處與最需改善之處（包含 ESG Washing 疑慮診斷）。"),
        ("5. 文字表達與資料引用 (Writing & Citation)", "10%", "篇幅達 1,500–2,000 字，結構嚴謹，正確標註參考文獻與報告書來源。")
    ]

    for r_data in rubric_data:
        row_cells = table_rubric.add_row().cells
        for i, val in enumerate(r_data):
            row_cells[i].text = val
            for p_cell in row_cells[i].paragraphs:
                for r in p_cell.runs:
                    r.font.name = "Microsoft JhengHei"
                    r.font.size = Pt(9)

    doc.save(r"C:\Users\User\Desktop\第1週_企業為何需要倫理\第4週_ESG與永續發展.docx")
    print("Successfully generated Week 4 Word .docx file!")

if __name__ == "__main__":
    generate_week4_word_guide()
