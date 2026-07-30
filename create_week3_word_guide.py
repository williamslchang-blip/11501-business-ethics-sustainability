import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def generate_week3_word_guide():
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
                              "第 3 週：企業社會責任與共享價值 —— 教師深度教學指引與授課手冊")
    r_title.font.name = "Microsoft JhengHei"
    r_title.font.size = Pt(20)
    r_title.font.bold = True
    r_title.font.color.rgb = DARK_BLUE

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_sub = p_sub.add_run("AACSB 商管學院認證標竿 • Carroll CSR Pyramid • Porter & Kramer CSV • Greenwashing Audit")
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
    add_sec_heading("📌 一、第 3 週課程設計理念與 AACSB 能力指標 (Week 3 Philosophy & Competencies)")
    
    p = doc.add_paragraph()
    p.add_run("第 3 週主題為「企業社會責任與共享價值 (Corporate Social Responsibility & Creating Shared Value, CSR & CSV)」。"
              "本週為整門課程的關鍵轉折點！W1與W2建立了企業倫理 (Ethics) 概念，W3 必須回答：「企業是否只需要做到『有倫理』就夠了？」\n"
              "答案是引出 CSR，並進一步銜接至 Michael Porter 的 CSV (創造共享價值) 與綠色漂洗 (Greenwashing) 判讀，為 W4 的 ESG 奠定實務戰略基礎。")

    # Section 2: Timeline
    add_sec_heading("⏱️ 二、2 小時 (110 分鐘) 時間配比與流程總覽 (Time Allocation Timeline)")

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
        ("00:00 - 00:15", "15m", "Part 1：倫理走向 CSR\n(Ethics to CSR)", "【Slide 1-4】回顧倫理、暖身問題（不違法不上道德就是好企業嗎？）、企業角色演進 (1960 Profit → 1980 CSR → 2020 ESG)。"),
        ("00:15 - 00:50", "35m", "Part 2：CSR 理論與金字塔\n(CSR Theories)", "【Slide 5-12】CSR 演進歷史 (Bowen → Carroll → Porter)、Carroll CSR Pyramid 四階金字塔 (經濟/法律/倫理/慈善) 與企業實務案例。"),
        ("00:50 - 01:05", "15m", "【活動一】：CSR 分類遊戲\n(CSR Classification Game)", "【Slide 13-14】20 張企業行為卡分類演練（加薪、節能、捐款、避稅、志工、納稅、工安），Mentimeter 歸零表決與金字塔層級釐清。"),
        ("01:05 - 01:25", "20m", "Part 3：共享價值 CSV\n(Creating Shared Value)", "【Slide 15-19】CSR vs. CSV 深度對比、Porter & Kramer 3 大 CSV 途徑、Nestlé、Unilever (USLP) 與 Patagonia (Don't Buy This Jacket) 典範案例。"),
        ("01:25 - 01:45", "20m", "Part 4 & 【活動二】：漂綠診斷\n(Greenwashing Detective)", "【Slide 20-24】7 Sins of Greenwashing (漂綠七宗罪)、H&M/VW/Shell 醜聞剖析；【活動二】小組即時審查 H&M/Coca-Cola/Apple 廣告。"),
        ("01:45 - 02:00", "15m", "Part 5：重點整理與作業\n(Summary & Homework 3)", "【Slide 25】CSR → CSV → ESG 演進總結、Homework 3 (1,200–1,500字) CSR與漂綠分析作業交代與 AACSB 評分權重。")
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

    # Section 3: 25 Slides Detailed Notes
    add_sec_heading("🗣️ 三、25 頁投影片逐頁深度授課指引 (Slide-by-Slide Instructional Notes)")

    slides_detail = [
        ("Slide 1: 課程封面 (Week 3 CSR & CSV)", 
         "【授課腳本】：「歡迎來到第 3 週《企業社會責任與共享價值》。本週我們將解答商業世界最關鍵的問題：企業光是遵守倫理就夠了嗎？如何將社會責任轉化為商業競爭力？」"),
        ("Slide 2: 演進路徑 (Business Ethics → CSR → ESG)", 
         "【授課腳本】：展示演進鏈：W1-2 Business Ethics (內在基因) → W3 CSR & CSV (責任與價值行動) → W4 ESG (量化治理數據)。"),
        ("Slide 3: 暖身問題 (Legality, Morality & Good Business)", 
         "【提問引導】：「如果一家企業沒有違法，也沒有不道德，它就算好企業嗎？」引導討論：合規只是起點，企業需要積極創造社會價值。"),
        ("Slide 4: 企業角色的時代演進 (Changing Role of the Firm)", 
         "【授課腳本】：說明三階段演進：1960 單純獲利 (Profit Only) → 1980 企業社會責任 (CSR) → 2020 ESG 永續治理。"),
        ("Slide 5: CSR 精準定義 (What is CSR?)", 
         "【授課腳本】：解析 CSR 定義：企業在追求利潤的同時，對利害關係人與環境所承擔的責任行動。引用 ISO 26000 國際標準。"),
        ("Slide 6: CSR 發展歷史 (History of CSR)", 
         "【授課腳本】：介紹 4 大里程碑：1953 Bowen (CSR之父) → 1991 Carroll (CSR金字塔) → 2006 Porter & Kramer (CSV概念) → 現代 ESG。"),
        ("Slide 7: Carroll CSR Pyramid 經典金字塔 (The CSR Pyramid)", 
         "【授課指引】：展示金字塔 4 階：\n"
         "1. Economic (經濟責任 - 最底層基礎)：Be profitable (盈利賺錢)\n"
         "2. Legal (法律責任)：Obey the law (遵守法律)\n"
         "3. Ethical (倫理責任)：Be ethical (超越法律，追求公正對錯)\n"
         "4. Philanthropic (慈善責任 - 最頂層)：Be a good corporate citizen (企業公民公益慈善)"),
        ("Slide 8: 經濟責任 (Economic Responsibility)", 
         "【授課腳本】：賺錢是企業最根本的社會責任。連年虧損破產倒閉的企業，無法保障員工就業，本身就是對社會不負責任。"),
        ("Slide 9: 法律責任 (Legal Responsibility)", 
         "【授課腳本】：遵守勞基法、稅法、環保法規與食安法。法律是社會對企業行為的強制作業規範。"),
        ("Slide 10: 倫理責任 (Ethical Responsibility)", 
         "【授課腳本】：做對的事！即使法律沒有規定，企業主動進行產品安全性召回、公平貿易採購、員工心理健康支持。"),
        ("Slide 11: 慈善責任 (Philanthropic Responsibility)", 
         "【授課腳本】：企業公民 (Corporate Citizenship)。透過基金會捐款、員工志工服務、災後重建支持社會。"),
        ("Slide 12: CSR Pyramid 企業實務矩陣 (Applied CSR Matrix)", 
         "【授課指引】：舉例：依法納稅 (Legal) vs 主動給予產假 (Ethical) vs 設置教育基金會 (Philanthropic)。"),
        ("Slide 13: 活動一：CSR 分類遊戲 (CSR Classification Game)", 
         "【活動執行】：4人一組，發放 20 張企業行為卡（員工加薪、節能、公益捐款、避稅、志工、依法納稅、改善工安）。"),
        ("Slide 14: 全班分類討論與點評 (Class Debrief)", 
         "【活動點評】：釐清「依法納稅是 Legal」而非「Philanthropic」；「改善工安超越法規是 Ethical」。消除常見誤解。"),
        ("Slide 15: CSR vs. CSV 深度對比 (CSR vs. CSV)", 
         "【授課腳本】：對比兩者差異：\n"
         "• CSR：通常為善後補償、公關慈善、預算花費 (Cost Center)。\n"
         "• CSV：將社會需求融入商業模式，創造共享價值 (Value Center)，兼顧商業獲利與社會進步。"),
        ("Slide 16: Porter & Kramer CSV 3 大途徑 (3 Routes to CSV)", 
         "【授課腳本】：解析 CSV 3 大重塑途徑：(1) 重塑產品與市場 (Reconceiving products)；(2) 重新定義價值鏈生產力 (Redefining productivity)；(3) 建立在地產業聚落 (Enabling local clusters)。"),
        ("Slide 17: Case 1: Nestlé 雀巢 CSV 案例 (Nestlé Case)", 
         "【案例剖析】：Nestlé 直接採購 (Direct Sourcing) 輔導咖啡與可可農民提升技術與品質。農民收益提升，雀巢獲得穩定優質原料供應！"),
        ("Slide 18: Case 2: Unilever 永續生活計畫 (Unilever USLP)", 
         "【案例剖析】：Unilever 承諾「業務成長翻倍，環境足跡減半」。品牌如 Lifebuoy 肥皂推廣衛生洗手，降低疾病並創造天價銷售額！"),
        ("Slide 19: Case 3: Patagonia 震撼廣告 (Patagonia Case)", 
         "【案例剖析】：黑色星期五買一送一狂潮中，刊登 'Don't Buy This Jacket' 廣告。提供免費修補服務，極致透明與環保獲得強大消費者忠誠度！"),
        ("Slide 20: 什麼是 Greenwashing 漂綠？ (What is Greenwashing?)", 
         "【授課腳本】：定義漂綠：企業透過誇大、虛偽或誤導性的行銷手段，將自己包裝成環保永續，但實際行動卻背道而馳的欺罔行為。"),
        ("Slide 21: 漂綠七宗罪與常見用語 (7 Sins of Greenwashing)", 
         "【授課指引】：解析常見 buzzwords：'Carbon Neutral?' '100% Eco?'。介紹 7 Sins：隱藏權衡 (Hidden Trade-off)、缺乏證據 (No Proof)、模糊籠統 (Vagueness) 等。"),
        ("Slide 22: 漂綠失敗案例剖析 (Greenwashing Scandals)", 
         "【案例剖析】：\n"
         "• H&M Conscious Collection：回收衣服計畫被揭發多數焚燒或丟棄海外垃圾山。\n"
         "• Shell：刊登極大廣告推廣綠能，實質綠能投資不足總支出 1%。"),
        ("Slide 23: 活動二：漂綠偵探社 (Greenwashing Detective)", 
         "【活動執行】：每組拿到企業真實 ESG 廣告（H&M、Coca-Cola、Starbucks、Apple、Tesla）。運用 7 Sins 審查是真實 CSR 還是漂綠？"),
        ("Slide 24: 各組發表與改善建議 (Team Pitch & Solutions)", 
         "【活動點評】：各組 3 分鐘 Pitch。教師點評：企業如何透過透明數據與第三方檢驗避免漂綠。"),
        ("Slide 25: 本週重點整理與作業 (Summary & Homework 3)", 
         "【課程總結】：展示 CSR → CSV → ESG 演進軸。說明 Homework 3 (1,200–1,500字) 企業 CSR 與漂綠診斷作業與 5 大 AACSB 評分權重。")
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
        ("1. 資料蒐集 (Data Collection)", "20%", "正確引用企業近3年CSR/永續報告書與新聞報導資料。"),
        ("2. CSR 分析 (CSR Analysis)", "25%", "詳細分析至少 3 項具體 CSR 措施並評價實質影響。"),
        ("3. Carroll Pyramid 應用 (Pyramid Application)", "20%", "精準將 CSR 措施歸類至經濟、法律、倫理、慈善四階層。"),
        ("4. CSV 與 Greenwashing 分析 (CSV & Greenwashing)", "20%", "深度診斷企業是否具備 CSV 共享價值，或存在漂綠疑慮。"),
        ("5. 改善建議與反思 (Recommendations)", "15%", "提出 2 項兼具可行性與誠信價值的具體改善建議。")
    ]

    for r_data in rubric_data:
        row_cells = table_rubric.add_row().cells
        for i, val in enumerate(r_data):
            row_cells[i].text = val
            for p_cell in row_cells[i].paragraphs:
                for r in p_cell.runs:
                    r.font.name = "Microsoft JhengHei"
                    r.font.size = Pt(9)

    doc.save(r"C:\Users\User\Desktop\第1週_企業為何需要倫理\第3週_企業社會責任與共享價值.docx")
    print("Successfully generated Week 3 Word .docx file!")

if __name__ == "__main__":
    generate_week3_word_guide()
