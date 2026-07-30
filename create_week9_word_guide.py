import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def generate_week9_word_guide():
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
                              "第 9 週：永續金融與 ESG 投資 —— 教師深度教學指引與授課手冊")
    r_title.font.name = "Microsoft JhengHei"
    r_title.font.size = Pt(20)
    r_title.font.bold = True
    r_title.font.color.rgb = DARK_BLUE

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_sub = p_sub.add_run("AACSB / Harvard / Wharton / MIT Sloan Standard • Sustainable Finance • PRI • Green Bonds • MSCI Rating Divergence")
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
    add_sec_heading("📌 一、第 9 週課程設計理念與 AACSB 能力指標 (Week 9 Philosophy & Competencies)")
    
    p = doc.add_paragraph()
    p.add_run("第 9 週主題為「永續金融與 ESG 投資 (Sustainable Finance and ESG Investing)」。"
              "本週為整門課程從『內部企業管理』跨入『外部資本市場』的核心轉折週！\n"
              "W1–W8 建立了 Ethics → CSR → ESG → E → S → G → Disclosure 的管理解構，W9 引導學生思考最關鍵的問題：『ESG 到底有沒有商業價值？資本市場如何驅動企業永續轉型？』"
              "本週結合 Harvard、Wharton、MIT Sloan 與 Cambridge Judge 的 AACSB 升級框架，深入剖析：\n"
              "1. 傳統金融 vs 永續金融 (Sustainable Finance)；\n"
              "2. 聯合國責任投資原則 (UN PRI) 與 6 大投資策略 (Negative/Positive Screening, ESG Integration, Impact Investing, Stewardship)；\n"
              "3. 綠色金融工具 (Green Bonds 綠色債券, Sustainability-Linked Loans 永續連結貸款, Transition Finance 轉型金融)；\n"
              "4. AACSB 升級主題：評等分歧 (Rating Divergence, MIT Aggregate Confusion)、ESG 績效對財務價值的實證影響與台灣金管會綠色金融 3.0。")

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
        ("00:00 - 00:15", "15m", "Part 1：為什麼金融談ESG？\n(Why Finance Needs ESG?)", "【Slide 1-5】暖身問題（相同 EPS 選誰？）、BlackRock 執行長 Larry Fink 致 CEO 公開信（氣候風險即投資風險）、Sustainable Finance 定義與資金浪潮。"),
        ("00:15 - 00:45", "30m", "Part 2：ESG 投資與策略\n(ESG Investing)", "【Slide 6-13】UN PRI 責任投資 6 原則、ESG Integration 整合、Negative/Positive Screening 篩選、Impact Investing 影響力投資、Stewardship 股東參與；【活動一】ESG Investment Challenge (評估台積電/Apple/Tesla/可口可樂/ExxonMobil)。"),
        ("00:45 - 01:10", "25m", "Part 3：綠色金融與商品\n(Green Finance)", "【Slide 14-20】Green Bonds 綠色債券 (GBP 原則)、Sustainability-Linked Loans (SLL) 永續連結貸款、Transition Finance 轉型金融、ESG ETF、BlackRock 案例與台灣金管會綠色金融 3.0 政策。"),
        ("01:10 - 01:35", "25m", "Part 4：評級、實證與爭議\n(Ratings & Empirical)", "【Slide 21-25】MSCI & Sustainalytics 評級系統、Rating Divergence 評等分歧 (MIT 聚合混淆研究)、ESG 是否真的提升財務績效 (降低資本成本與尾端風險)、歐盟 SFDR 基金防漂綠分類。"),
        ("01:35 - 01:50", "15m", "【活動二】：打造 ESG 組合\n(Build ESG Portfolio)", "【Slide 26-27】1,000 萬虛擬資金於 10 家企業建立包含 3 產業與高 ESG 評級組合，進行風險與報酬 Pitch。"),
        ("01:50 - 02:00", "10m", "Part 5：總結與 W10 預告\n(Summary & HW9)", "【Slide 28】W9 總結、W10 永續供應鏈與循環經濟預告、Homework 9 (2,000字) 永續金融與 ESG 投資分析報告交代與 5 大 AACSB 評分權重。")
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

    # Section 3: 28 Slides Detailed Notes
    add_sec_heading("🗣️ 三、28 頁投影片逐頁深度授課指引 (Slide-by-Slide Instructional Notes)")

    slides_detail = [
        ("Slide 1: 課程封面 (Week 9 Sustainable Finance)", 
         "【授課腳本】：「歡迎來到第 9 週《永續金融與 ESG 投資》。本週我們將探討全球資本市場如何透過幾十兆美元的綠色資金，倒逼企業進行 ESG 永續轉型！」"),
        ("Slide 2: 課程轉折與脈絡 (Course Journey)", 
         "【授課腳本】：展示進程：W1-8 企業內部管理與揭露 → W9 外部金融資本市場 (Why ESG Matters to Investors)。"),
        ("Slide 3: 暖身思考 (Same EPS Investment Dilemma)", 
         "【提問引導】：如果兩家公司 EPS 完全相同，但 A 公司面臨天價碳稅風險，B 公司為全球 ESG 前 10%，你會把資金投給誰？引導理解非財務風險折現。"),
        ("Slide 4: 全球資金重組：BlackRock Larry Fink 聲明 (Larry Fink Letter)", 
         "【授課腳本】：解析全球最大資產管理巨擘 BlackRock 執行長 Larry Fink致 CEO 信：『氣候風險即投資風險 (Climate Risk is Investment Risk)』，全面重塑全球資本分配。"),
        ("Slide 5: Sustainable Finance 永續金融定義", 
         "【授課腳本】：定義永續金融：將 E、S、G 標準整合至金融服務、銀行放款與資產管理中，引導資金投入永續發展。"),
        ("Slide 6: 責任投資 Responsible Investment", 
         "【授課腳本】：介紹責任投資概念：投資人在尋求財務回報的同時，將 ESG 風險與利害關係人福祉納入投資決策。"),
        ("Slide 7: 聯合國責任投資原則 (UN PRI 6 Principles)", 
         "【授課指引】：解析 UN PRI 6 大原則：將 ESG 納入分析、成為積極股東、要求揭露、推動產業採行、提升營運效率與定期報導。"),
        ("Slide 8: 策略 1：ESG Integration (ESG 整合)", 
         "【授課腳本】：說明 ESG 整合：將 ESG 數據系統化納入傳統現金流折現 (DCF) 模型與企業估值中。"),
        ("Slide 9: 策略 2：Negative Screening (負向排除)", 
         "【授課腳本】：說明負向篩選：排除軍火、菸草、賭博與高污染煤炭產業。"),
        ("Slide 10: 策略 3：Positive Screening (正向篩選/Best-in-Class)", 
         "【授課指引】：說明正向篩選：在相同產業中挑選 ESG 評級最高的前 20% 領先企業。"),
        ("Slide 11: 策略 4：Impact Investing (影響力投資)", 
         "【授課腳本】：說明影響力投資：投資於具備明確、可量化之社會與環境改善目標之專案。"),
        ("Slide 12: 策略 5：Stewardship & Engagement (股東參與/盡職治理)", 
         "【授課腳本】：介紹機構投資人透過行使投票權 (Proxy Voting) 與高層對話，督促企業改善 ESG 治理。"),
        ("Slide 13: 活動一：ESG Investment Challenge (你會投資誰？)", 
         "【活動執行】：4人一組，比較台積電、Apple、Tesla、可口可樂、ExxonMobil 的 ROE, EPS, MSCI ESG Ratings 與新聞，回答投資決策。"),
        ("Slide 14: 活動一：公布答案與點評 (Class Debrief)", 
         "【活動點評】：總結：ESG 並非取代財務分析，而是作為評估企業長遠風險與隱形價值的核心補充！"),
        ("Slide 15: 綠色金融 Green Finance 概述", 
         "【授課腳本】：介紹綠色金融範疇：包含綠色債券、綠色貸款、綠色基金與氣候風險保險。"),
        ("Slide 16: Green Bonds 綠色債券 (GBP 原則)", 
         "【授課指引】：解析綠色債券 (Green Bonds) 與 ICMA 綠色債券原則 (GBP)：發行資金必須專款專用於綠能、減碳與循環經濟專案。"),
        ("Slide 17: Sustainability-Linked Loans (SLL) 永續連結貸款", 
         "【授課腳本】：介紹 SLL：銀行貸款利率與企業 ESG KPI 成效掛鉤，達到減碳目標可獲得利率調降。"),
        ("Slide 18: Transition Finance (轉型金融)", 
         "【授課腳本】：說明轉型金融：資助高碳排傳統產業（如鋼鐵、水泥）進行低碳技術轉型的專項融資。"),
        ("Slide 19: 標竿案例：BlackRock 永續投資實務 (BlackRock Case)", 
         "【案例剖析】：剖析 BlackRock 推出全系列 ESG ETF，並在股東大會中撤換忽視氣候風險的董事。"),
        ("Slide 20: 台灣綠色金融 3.0 政策 (Taiwan Policy)", 
         "【授課指引】：介紹金管會綠色金融行動方案 3.0：要求金融機構進行氣候壓力測試與投融資碳盤查。"),
        ("Slide 21: MSCI ESG Rating 評級架構 (AAA to CCC)", 
         "【授課腳本】：解析全球權威 MSCI ESG 評級：包含 7 個等級，評估企業相較同業的風險管理能力。"),
        ("Slide 22: Rating Divergence 評等分歧 (MIT Aggregate Confusion)", 
         "【授課指引】：AACSB 升級主題：引用 MIT Aggregate Confusion 研究，解析為何 MSCI, Sustainalytics, Refinitiv 對同一家公司評級不一（權重、範疇與衡量標準不同）。"),
        ("Slide 23: ESG 是否提升財務績效？實證研究 (ESG vs Financial Performance)", 
         "【授課腳本】：引用學術實證：高 ESG 評級企業具備較低的資本成本 (Cost of Capital)、較低的神仙股股價波動率與強大的防禦性！"),
        ("Slide 24: 基金防漂綠規範：歐盟 SFDR 規則 (EU SFDR)", 
         "【授課指引】：解析歐盟 SFDR 基金分類：Article 6 (一般基金)、Article 8 (促進 ESG 基金)、Article 9 (具備明確永續目標之深綠基金)，打擊基金標籤漂綠。"),
        ("Slide 25: 活動二：Build Your ESG Portfolio (建構投資組合)", 
         "【活動執行】：每組 1,000 萬虛擬資金，從 10 家企業中建立涵蓋 3 產業與高 ESG Rating 之投資組合並分析風險。"),
        ("Slide 26: 活動二：各組發表與點評 (Team Pitches)", 
         "【活動點評】：各組 5 分鐘 Pitch。教師點評風險控管與 ESG 權重配置策略。"),
        ("Slide 27: 本週重點總結 (Sustainable Finance Summary)", 
         "【課程總結】：展示 Traditional Finance → Sustainable Finance → ESG Investing 資本驅動鏈。"),
        ("Slide 28: 下週預告 (Preview Week 10 Supply Chain)", 
         "【課程預告】：預告 Week 10 主題：《永續供應鏈與循環經濟 (Sustainable Supply Chain & Circular Economy)》，說明 Homework 9 (2,000字) 作業與 AACSB 評分權重。")
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
        ("1. 公司與產業分析 (Firm & Sector Analysis)", "20%", "精準介紹目標上市公司背景、主要業務與所屬產業特勢。"),
        ("2. ESG 表現與優勢 (ESG Performance Audit)", "30%", "深入分析目標企業在 E、S、G 三構面之表現與永續競爭優勢。"),
        ("3. 投資判斷與論證 (Investment Valuation & Risks)", "25%", "客觀判斷是否具備長期投資價值，並深入評估氣候/治理等 ESG 風險。"),
        ("4. 改善建議 (Managerial Recommendations)", "15%", "提出兩項具體提升企業 ESG 評級與市場信任的改善建議。"),
        ("5. 報告品質 (Report Quality)", "10%", "篇幅達 2,000 字左右，結構嚴謹，正確引用財務與 ESG 評級資料。")
    ]

    for r_data in rubric_data:
        row_cells = table_rubric.add_row().cells
        for i, val in enumerate(r_data):
            row_cells[i].text = val
            for p_cell in row_cells[i].paragraphs:
                for r in p_cell.runs:
                    r.font.name = "Microsoft JhengHei"
                    r.font.size = Pt(9)

    doc.save(r"C:\Users\User\Desktop\第1週_企業為何需要倫理\第9週_永續金融與ESG投資.docx")
    print("Successfully generated Week 9 Word .docx file!")

if __name__ == "__main__":
    generate_week9_word_guide()
