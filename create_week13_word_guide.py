import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def generate_week13_word_guide():
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
    ORANGE = RGBColor(245, 158, 11)

    # Title
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_title = p_title.add_run("📘 企業倫理與永續經營 (Business Ethics and Sustainable Management)\n"
                              "第 13 週：全球企業永續策略案例分析 —— 教師深度教學指引與授課手冊")
    r_title.font.name = "Microsoft JhengHei"
    r_title.font.size = Pt(20)
    r_title.font.bold = True
    r_title.font.color.rgb = DARK_BLUE

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_sub = p_sub.add_run("AACSB / PRME / Harvard / INSEAD / MIT Sloan / NUS Standard • Module 4 Integration • Benchmark Case Audits • Consultant Challenge")
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
            r.font.color.rgb = DARK_BLUE if level == 1 else ORANGE
            r.font.bold = True
        return h

    # Section 1: Philosophy
    add_sec_heading("📌 一、第 13 週課程設計理念與 AACSB 能力指標 (Week 13 Philosophy & Competencies)")
    
    p = doc.add_paragraph()
    p.add_run("第 13 週主題為「全球企業永續策略案例分析 (Global Corporate Sustainability Case Studies)」。"
              "本週為整門課程邁入『模組四：整合應用 (Integration & Application)』的核心實戰章節！\n"
              "W1–W12 學生已融會貫通 Ethics → CSR → ESG → Climate → Governance → Reporting → Sustainable Finance → Supply Chain → AI → ESG Strategy 12 大領域，"
              "W13 不再介紹新理論，而是全面採取 Harvard Business School 與 INSEAD 標竿之 Case-Based Learning (案例教學) 與 Problem-Based Learning (問題導向學習)。\n"
              "本週精選全球與台灣 10 大頂尖標竿企業：\n"
              "國際標竿：Patagonia (目的導向/循環)、Microsoft (Carbon Negative/AI Governance)、Ørsted (石油轉型風電)、Unilever (USLP 品牌策略)、IKEA (循環家具)；\n"
              "台灣標竿：台積電 (製造業/綠電供應鏈)、台Delta (節能科技/綠建築)、玉山金控 (永續金融/綠色授信)、統一企業 (食安與減塑)、中華電信 (數位治理與 5G 節能)；\n"
              "培養學生進行跨產業、跨國企業之診斷—分析—評估—策略提案完整能力！")

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
        ("00:00 - 00:15", "15m", "Part 1：從理論到企業實踐\n(Theory to Practice)", "【Slide 1-4】暖身問題（哪家公司代表最成功的 ESG 標竿？）、W1-W12 知識全景回顧、企業永續成功的 5 大共同特徵（C-suite 支持/策略融合/創新商業模式/利害關係人/揭露）。"),
        ("00:15 - 00:55", "40m", "Part 2：國際企業標竿案例\n(Global Leaders)", "【Slide 5-10】剖析 5 大國際案例：Patagonia (目的導向)、Microsoft (Carbon Negative 2030 & Responsible AI)、Ørsted (石油轉型風電)、Unilever (USLP)、IKEA (循環家具與租賃) 及國際案例交叉比較矩陣。"),
        ("00:55 - 01:25", "30m", "Part 3：臺灣企業標竿案例\n(Taiwan Leaders)", "【Slide 11-16】剖析 5 大臺灣案例：台積電 (半導體製造/綠電輔導)、台達電 (節能科技/綠建築)、玉山金控 (永續金融/責任投資)、統一企業 (食安/農採/減塑)、中華電信 (數位治理/5G節能) 及臺灣產業特色。"),
        ("01:25 - 01:50", "25m", "Part 4 & 【活動一/二】：案例整合與顧問競賽\n(Consultant Challenge)", "【Slide 17-26】哪些企業真正做到 ESG vs 僅死守 Compliance；【活動一】Global ESG Benchmark 評分卡；【活動二】ESG Consultant Challenge (模擬 Big 4/BCG 顧問於 20 分鐘為落後企業診斷並提出 3 策略 2 KPI)。"),
        ("01:50 - 02:00", "10m", "Part 5：總結與 W14 預告\n(Summary & HW13)", "【Slide 27-30】ESG Global Best Practices 總結、W14 ESG 危機管理預告、Homework 13 (2,500字) 案例比較報告交代與 5 大 AACSB 評分權重。")
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

    # Section 3: 30 Slides Detailed Notes
    add_sec_heading("🗣️ 三、30 頁投影片逐頁深度授課指引 (Slide-by-Slide Instructional Notes)")

    slides_detail = [
        ("Slide 1: 課程封面 (Week 13 Global Case Studies)", 
         "【授課腳本】：「歡迎來到第 13 週《全球企業永續策略案例分析》。本週我們將整合前 12 週的核心知識，深入診斷全球與台灣 10 大頂尖標竿企業的實戰永續轉型方案！」"),
        ("Slide 2: 暖身思考 (Which Enterprise Represents ESG Benchmark?)", 
         "【提問引導】：在你看來，哪一家企業最能代表 ESG 的成功典範？是 Patagonia, Microsoft, 還是台積電？引導體會不同產業與商業模式下 ESG 成功的多元維度。"),
        ("Slide 3: W1-W12 全課程知識地圖回顧", 
         "【授課腳本】：展示進程：Ethics → CSR → ESG → Climate → Governance → Reporting → Sustainable Finance → Supply Chain → AI → Strategy 12 大柱石。"),
        ("Slide 4: 企業永續成功的 5 大共同特徵", 
         "【授課指引】：強調冠軍企業共通點：1. 高階主管親自支持；2. ESG 融入核心策略；3. 創新商業模式；4. 利害關係人深度參與；5. 透明高品質揭露。"),
        ("Slide 5: 國際案例一：Patagonia 目的導向與品牌溢價", 
         "【案例剖析】：Patagonia 推出 Worn Wear、宣佈「Earth is Now Our Only Shareholder」，成功將環保理念轉化為全球極高的品牌忠誠度與定價權。"),
        ("Slide 6: 國際案例二：Microsoft 負碳排與 Responsible AI", 
         "【案例剖析】：Microsoft 承諾 2030 實現 Carbon Negative (負碳排)，並發表 Copilot Responsible AI Standard，打造全球科技治理標竿。"),
        ("Slide 7: 國際案例三：Ørsted 從黑化石燃料轉型風電龍頭", 
         "【案例剖析】：Ørsted 在 10 年內拋售石油天然氣資產，全力押注離岸風電，黑能佔比翻轉為 90%+ 綠能，市值暴增 10 倍！"),
        ("Slide 8: 國際案例四：Unilever 永續生活計畫 (USLP)", 
         "【案例剖析】：Unilever 將永續融入 400+ 品牌，永續品牌成長速度比其他傳統品牌快 69%，貢獻 75% 營業額成長。"),
        ("Slide 9: 國際案例五：IKEA 循環經濟與家具租賃", 
         "【案例剖析】：IKEA 承諾 2030 年 100% 使用再生與可回收原料，推動 Buy Back 舊家具買回與商業辦公家具租賃 PaaS。"),
        ("Slide 10: 5 大國際標竿案例交叉比較矩陣", 
         "【授課對比】：比較 Patagonia (品牌/使命)、Microsoft (技術/負碳)、Ørsted (營運轉型)、Unilever (消費品/USLP) 與 IKEA (循環/供應鏈) 的 ESG 優勢。"),
        ("Slide 11: 臺灣案例六：台積電 (TSMC 綠色製造與供應鏈綠電)", 
         "【案例剖析】：台積電推動綠色製造，成為全球首家加入 RE100 的半導體晶圓代工廠，並輔導數百家國內供應商減碳。"),
        ("Slide 12: 臺灣案例七：台達電 (Delta 節能科技與綠建築)", 
         "【案例剖析】：台達電將 ESG 融入商業模式，研發極致高效能電源與智慧綠建築解決方案，協助全球客戶節省數百億度電。"),
        ("Slide 13: 臺灣案例八：玉山金控 (E.SUN 永續金融與綠色授信)", 
         "【案例剖析】：玉山金控全面導入赤道原則 (Equator Principles)，推動永續連結貸款 (SLL) 與氣候壓力測試，為台灣綠色金融領航者。"),
        ("Slide 14: 臺灣案例九：統一企業 (食安透明、農採與包裝減塑)", 
         "【案例剖析】：統一企業建構嚴格食品安全檢驗體系、永續農業採購與輕量化減塑包裝，守護消費大眾福祉。"),
        ("Slide 15: 臺灣案例十：中華電信 (數位治理、5G 節能與電子廢棄物)", 
         "【案例剖析】：中華電信建立資安與數據隱私強韌治理，推動 5G 基地台 C-RAN 智慧節能技術與廢棄電子產品回收。"),
        ("Slide 16: 臺灣企業 ESG 發展之四大產業特色", 
         "【授課指引】：總結臺灣產業特色：製造業 (減碳與範疇 3 壓力)、金融業 (投融資綠色引導)、科技業 (綠電共購) 與服務業 (農採減塑)。"),
        ("Slide 17: 活動一：Global ESG Benchmark (企業評分卡)", 
         "【活動執行】：4人一組抽取 Patagonia, Microsoft, IKEA, Ørsted, 台積電, 台達電, 玉山金, 統一，製作一頁「企業永續評分卡」。"),
        ("Slide 18: 活動一：各組發表與點評 (Class Debrief)", 
         "【活動點評】：點評各組評分卡：優秀企業皆具備明確 Purpose 與可量化的 KPI 達成進度！"),
        ("Slide 19: 哪些企業真正做到 ESG 策略融入？", 
         "【授課腳本】：分析 Patagonia, Ørsted, Tesla 成功將 ESG 轉化為核心獲利引擎。"),
        ("Slide 20: 哪些企業仍滯留在被動 Compliance 階段？", 
         "【授課指引】：警示：僅停留在被動合規的企業，容易在碳關稅與國際法規衝擊下失去市場。"),
        ("Slide 21: 哪些企業建立了難以模仿的 VRIO 競爭護城河？", 
         "【授課腳本】：解析台積電與 Microsoft 憑藉技術與生態系打造的永續 VRIO 壁壘。"),
        ("Slide 22: 哪些企業仍面臨轉型的重大瓶頸與爭議？", 
         "【授課指引】：剖析高碳排產業與傳統供應鏈面臨的綠電不足與成本暴漲挑戰。"),
        ("Slide 23: 企業永續成功因素綜合矩陣", 
         "【授課總結】：展示貫穿 10 大案例的永續成功矩陣。"),
        ("Slide 24: 活動二：ESG Consultant Challenge (顧問模擬大賽)", 
         "【活動執行】：每組模擬 Deloitte / PwC / KPMG / BCG 顧問團隊，20 分鐘內為 ESG 落後企業找出 3 大問題、提出 3 大策略、設計 2 大 KPI 與競爭力提升方案。"),
        ("Slide 25: 活動二：各組 5 分鐘 Consultant Pitches", 
         "【活動點評】：各組進行 5 分鐘顧問簡報提案。"),
        ("Slide 26: 教師回饋與綜合評分 (Faculty Evaluation)", 
         "【活動點評】：教師依據問題診斷精準度、策略可行性與 KPI 邏輯給予專業點評。"),
        ("Slide 27: 模組四整合單元重點梳理", 
         "【課程總結】：梳理案例診斷 — 策略提案 — 評分卡構建之實戰能力。"),
        ("Slide 28: Global ESG Best Practices 典範架構", 
         "【授課總結】：展示全球頂尖企業 ESG Best Practices 典範藍圖。"),
        ("Slide 29: 下週預告 (Preview Week 14 ESG Crisis)", 
         "【課程預告】：預告 Week 14 主題：《ESG 危機管理與公關溝通 (ESG Crisis Management and Stakeholder Communication)》。"),
        ("Slide 30: 課程總結與 Homework 13 作業交代", 
         "【課程總結】：交代 Homework 13 (2,500字) 全球企業 ESG 案例比較報告作業（比較 1 家國際 + 1 家臺灣企業）與 5 大 AACSB 評分權重。")
    ]

    for title, text in slides_detail:
        p = doc.add_paragraph()
        r_t = p.add_run(f"📌 {title}\n")
        r_t.bold = True
        r_t.font.name = "Microsoft JhengHei"
        r_t.font.color.rgb = ORANGE
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
        ("1. 企業背景分析 (Firm Audit)", "25%", "完整比較分析 1 家國際與 1 家台灣企業背景與產業特勢。"),
        ("2. ESG 策略比較 (ESG Strategy Audit)", "30%", "深入對比兩家企業在 E、S、G 三大構面之策略執行深度與品質。"),
        ("3. 商業模式與競爭優勢 (Business Model & VRIO)", "20%", "精準評估企業是否真正做到商業模式轉型，並創造長線 VRIO 競爭優勢。"),
        ("4. 建議品質 (Strategic Recommendations)", "15%", "提出三項具備實務可行性與創新價值的企業永續改善建議。"),
        ("5. 報告品質 (Report Quality)", "10%", "篇幅達 2,500 字左右，結構嚴謹，正確引用永續報告書與數據圖表。")
    ]

    for r_data in rubric_data:
        row_cells = table_rubric.add_row().cells
        for i, val in enumerate(r_data):
            row_cells[i].text = val
            for p_cell in row_cells[i].paragraphs:
                for r in p_cell.runs:
                    r.font.name = "Microsoft JhengHei"
                    r.font.size = Pt(9)

    doc.save(r"C:\Users\User\Desktop\第1週_企業為何需要倫理\第13週_全球企業永續案例分析.docx")
    print("Successfully generated Week 13 Word .docx file!")

if __name__ == "__main__":
    generate_week13_word_guide()
