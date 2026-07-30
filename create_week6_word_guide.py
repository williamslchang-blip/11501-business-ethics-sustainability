import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def generate_week6_word_guide():
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
    PURPLE = RGBColor(110, 40, 180)

    # Title
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_title = p_title.add_run("📘 企業倫理與永續經營 (Business Ethics and Sustainable Management)\n"
                              "第 6 週：利害關係人管理與企業社會責任實務 —— 教師深度教學指引與授課手冊")
    r_title.font.name = "Microsoft JhengHei"
    r_title.font.size = Pt(20)
    r_title.font.bold = True
    r_title.font.color.rgb = DARK_BLUE

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_sub = p_sub.add_run("AACSB / PRME / Harvard Business School Standard • Stakeholder Theory • Power-Interest Matrix • DEI & Human Rights")
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
            r.font.color.rgb = DARK_BLUE if level == 1 else PURPLE
            r.font.bold = True
        return h

    # Section 1: Philosophy
    add_sec_heading("📌 一、第 6 週課程設計理念與 AACSB 能力指標 (Week 6 Philosophy & Competencies)")
    
    p = doc.add_paragraph()
    p.add_run("第 6 週主題為「利害關係人管理與企業社會責任實務 (Stakeholder Management and Corporate Social Responsibility in Practice)」。"
              "本週為整門課程從『理論與氣候』銜接至『社會責任 (S) 與公司治理 (G)』的靈魂樞紐週！\n"
              "W1–W5 已建立『Ethics → CSR → ESG → Climate』的知識基礎，W6 開始解答企業最核心的問題：『企業究竟應該對誰負責？如何平衡多元且衝突的利害關係人權益？』"
              "本週深入探討 Edward Freeman 的利害關係人理論 (Stakeholder Theory)、Power-Interest Matrix 權力利益矩陣、人權 (Human Rights)、DEI 多元包容、供應鏈責任與現代奴隸法案。")

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
        ("00:00 - 00:15", "15m", "Part 1：對誰負責？\n(Accountability)", "【Slide 1-5】暖身思考（只滿足一個人該選誰？）、Milton Friedman 股東至上 vs Edward Freeman 利害關係人理論、Shareholder vs Stakeholder 對比矩陣。"),
        ("00:15 - 00:45", "30m", "Part 2：利害關係人理論\n(Stakeholder Theory)", "【Slide 6-12】8 大 Stakeholders 分類、Power-Interest Matrix 權力利益矩陣 (Key Players, Keep Satisfied, Keep Informed, Minimal Effort)、Salience 顯著性模型、Starbucks/Apple/Nike 標竿案例。"),
        ("00:45 - 01:00", "15m", "【活動一】：Mapping 實戰\n(Stakeholder Mapping)", "【Slide 13-14】小組抽籤 Apple/Starbucks/Uniqlo/Tesla/TSMC 繪製 Power-Interest Map，分析 Power 與 Interest 最高者與溝通策略。"),
        ("01:00 - 01:30", "30m", "Part 3：Social (S) 構面\n(Social In-Depth)", "【Slide 15-21】S 構面範疇、Human Rights 聯合國人權原則 (UNGPs)、DEI (Diversity, Equity, Inclusion)、Employee Well-being 心理安全感、供應鏈責任與現代奴隸法案 (Modern Slavery Act)。"),
        ("01:30 - 01:50", "20m", "Part 4 & 【活動二】：Role Play\n(Stakeholder Negotiation)", "【Slide 22-25】【活動二】新設建廠談判模擬（CEO, 居民, 政府, 股東, NGO, 媒體跨角色協商）、真正的 ESG 即是動態平衡不同利害關係人利益。"),
        ("01:50 - 02:00", "10m", "Part 5：W1-W6 總結與預告\n(Summary & HW6)", "【Slide 26】W1–W6 完整知識架構總結、W7 公司治理預告、Homework 6 (1,500–1,800字) Stakeholder Analysis Report 作業交代與 5 大 AACSB 評分權重。")
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
        ("Slide 1: 課程封面 (Week 6 Stakeholder Management)", 
         "【授課腳本】：「歡迎來到第 6 週《利害關係人管理與企業社會責任實務》。本週我們將解答企業營運最核心的抉擇：企業究竟該對誰負責？如何平衡衝突的利益？」"),
        ("Slide 2: 課程轉折與脈絡 (Course Journey)", 
         "【授課腳本】：展示進程：W1-5 建立 Ethics → CSR → ESG → Climate 防線；W6 正式深入 S (Social) 與利害關係人管理。"),
        ("Slide 3: 暖身問題 (Single Stakeholder Dilemma)", 
         "【提問引導】：如果企業只能滿足一個角色，應該選股東、員工、顧客還是社區？引導體會單一至上思維的盲點。"),
        ("Slide 4: Milton Friedman vs. Edward Freeman", 
         "【授課腳本】：對比兩大宗師：Friedman (1970 股東至上) vs. Freeman (1984 利害關係人理論)。"),
        ("Slide 5: Shareholder vs. Stakeholder 比較表", 
         "【授課指引】：對比兩者在經營目標、決策視角、時間軸與成功指標上的本質差異。"),
        ("Slide 6: 誰是 Stakeholder？ (8 Key Stakeholders)", 
         "【授課腳本】：介紹 8 大關鍵利害關係人：顧客、員工、供應商、政府、社區、NGOs、媒體與投資人。"),
        ("Slide 7: Power–Interest Matrix 權力利益矩陣", 
         "【授課腳本】：展示經典 2x2 矩陣：橫軸為 Interest (利益關切度)，縱軸為 Power (影響力權力)。"),
        ("Slide 8: 權力利益矩陣的 4 大溝通策略", 
         "【授課指引】：解析 4 象限策略：\n"
         "1. High Power & High Interest：Key Players (密切合作/核心夥伴)\n"
         "2. High Power & Low Interest：Keep Satisfied (保持滿意/防範反彈)\n"
         "3. Low Power & High Interest：Keep Informed (保持溝通/即時告知)\n"
         "4. Low Power & Low Interest：Minimal Effort (精準關注/最低維護)"),
        ("Slide 9: 利害關係人排序 Salience Model", 
         "【授課腳本】：介紹 Mitchell 顯著性模型：從 Power (權力)、Legitimacy (正當性) 與 Urgency (緊迫性) 三維度排序。"),
        ("Slide 10: 案例一：Starbucks 員工與公平貿易", 
         "【案例剖析】：Starbucks 將員工稱為「夥伴 (Partners)」，提供全職/兼職醫療保險與大學學費補助，兼顧農民公平貿易採購。"),
        ("Slide 11: 案例二：Apple & Foxconn 供應鏈責任", 
         "【案例剖析】：Apple 針對代工廠發布 Supplier Code of Conduct，年度公開稽核勞工工時與超時加班。"),
        ("Slide 12: 案例三：Nike 人權與勞工權益重塑", 
         "【案例剖析】：Nike 遭遇童工危機後，建立全球公開供應廠地圖與公平勞動協會 (FLA) 獨立查核。"),
        ("Slide 13: 活動一：Stakeholder Mapping 實戰", 
         "【活動執行】：4人一組，抽籤 Apple, Starbucks, Uniqlo, Tesla, TSMC 繪製 Power-Interest Map，標註 Key Players。"),
        ("Slide 14: 活動一：各組分享與點評", 
         "【活動點評】：點評科技業 (顧客/供應商 Power 高) vs 零售餐飲 (員工/社區 Interest 高) 的差異。"),
        ("Slide 15: Social (S) 到底包含什麼？", 
         "【授課腳本】：拆解 S 構面 5 大維度：人權保障、DEI 多元包容、員工福祉、供應鏈責任與現代奴隸法案。"),
        ("Slide 16: Human Rights 聯合國商業與人權原則", 
         "【授課腳本】：介紹 UNGPs (Protect, Respect, Remedy) 框架：企業有責任尊重所有人權，防止營運傷害。"),
        ("Slide 17: DEI (Diversity, Equity, Inclusion)", 
         "【授課指引】：解析 Diversity (多元性)、Equity (公平性) 與 Inclusion (包容性)，解決同工不同酬與升遷玻璃天花板。"),
        ("Slide 18: Employee Well-being 與心理安全感", 
         "【授課腳本】：介紹工作與生活平衡、心理健康支持與 Google 倡議的「心理安全感 (Psychological Safety)」。"),
        ("Slide 19: Supply Chain Responsibility 供應鏈社會責任", 
         "【授課腳本】：從 Tier 1 直屬廠擴大稽核至 Tier 2/3 原料廠，防範血汗工廠與環境污染轉嫁。"),
        ("Slide 20: Modern Slavery 現代奴隸法案", 
         "【授課指引】：解析 UK Modern Slavery Act 與美國強迫勞動預防法案，要求企業公開揭露防範強迫勞動聲明。"),
        ("Slide 21: Case Study: Apple & Foxconn 勞工管理重塑", 
         "【案例剖析】：剖析 Apple 針對 Foxconn 廠區工時、宿舍條件與心理健康防範的具體治理改進。"),
        ("Slide 22: Shared Value, CSR, and ESG 整合策略", 
         "【授課腳本】：說明如何將 CSV (共享價值)、CSR (社會責任) 與 ESG (G與S數據) 整合為企業核心 Social Strategy。"),
        ("Slide 23: 企業如何建立雙贏的 Social Strategy", 
         "【授課腳本】：從被動回應社會抗爭，轉為主動將社會需求轉化為產品創新與高吸引力的雇主品牌。"),
        ("Slide 24: 活動二：新設建廠協商 Role Play", 
         "【活動執行】：角色扮演模擬（CEO, 在地居民, 政府, 股東, NGO, 媒體），針對新設化學工廠議題進行高壓談判。"),
        ("Slide 25: 活動二：教師總結與雙贏談判", 
         "【活動點評】：總結：真正的 ESG 不是某一方獨贏，而是在多方限制下達成兼顧環境、經濟與社區共榮的動態平衡。"),
        ("Slide 26: W1–W6 總結、W7 預告與 Homework 6", 
         "【課程總結】：展示 W1–W6 完整知識體系架構。預告 W7 公司治理 (Corporate Governance)，並說明 Homework 6 (1,500–1,800字) 作業與 AACSB 評分權重。")
    ]

    for title, text in slides_detail:
        p = doc.add_paragraph()
        r_t = p.add_run(f"📌 {title}\n")
        r_t.bold = True
        r_t.font.name = "Microsoft JhengHei"
        r_t.font.color.rgb = PURPLE
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
        ("1. Stakeholder 分析 (Stakeholder Identification)", "30%", "精準分析至少 5 個核心利害關係人及其期望與利益衝突。"),
        ("2. Mapping 品質 (Power-Interest Mapping)", "20%", "正確運用 Power-Interest Matrix 進行權力與利益維度之圖譜定位。"),
        ("3. 策略分析 (Social Strategy Analysis)", "25%", "深入分析目標企業如何管理衝突最大的利害關係人族群。"),
        ("4. 改善建議 (Managerial Recommendations)", "15%", "提出具備雙贏思維與可行性的利害關係人溝通與改善方案。"),
        ("5. 報告品質 (Report Quality)", "10%", "篇幅達 1,500–1,800 字，結構嚴謹，正確標註參考文獻與報告資料。")
    ]

    for r_data in rubric_data:
        row_cells = table_rubric.add_row().cells
        for i, val in enumerate(r_data):
            row_cells[i].text = val
            for p_cell in row_cells[i].paragraphs:
                for r in p_cell.runs:
                    r.font.name = "Microsoft JhengHei"
                    r.font.size = Pt(9)

    doc.save(r"C:\Users\User\Desktop\第1週_企業為何需要倫理\第6週_利害關係人管理.docx")
    print("Successfully generated Week 6 Word .docx file!")

if __name__ == "__main__":
    generate_week6_word_guide()
