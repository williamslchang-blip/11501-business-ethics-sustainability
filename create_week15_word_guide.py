import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def generate_week15_word_guide():
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
    INDIGO = RGBColor(99, 102, 241)

    # Title
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_title = p_title.add_run("📘 企業倫理與永續經營 (Business Ethics and Sustainable Management)\n"
                              "第 15 週：ESG企業顧問專題：永續策略提案 —— 教師深度教學指引與授課手冊")
    r_title.font.name = "Microsoft JhengHei"
    r_title.font.size = Pt(20)
    r_title.font.bold = True
    r_title.font.color.rgb = DARK_BLUE

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_sub = p_sub.add_run("AACSB AoL Standard • Capstone Consulting Project • ESG Health Check • Board Room Pitch • 2035 Roadmap")
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
            r.font.color.rgb = DARK_BLUE if level == 1 else INDIGO
            r.font.bold = True
        return h

    # Section 1: Philosophy
    add_sec_heading("📌 一、第 15 週課程設計理念與 AACSB 能力指標 (Week 15 Philosophy & Competencies)")
    
    p = doc.add_paragraph()
    p.add_run("第 15 週主題為「ESG企業顧問專題：永續策略提案 (ESG Consulting Capstone Project)」。"
              "本週為整門課程最具 AACSB『學習成果導向 (Assurance of Learning, AoL)』特色與頂峰知識總整合的 Capstone 專案週！\n"
              "W1–W14 學生已完成 Ethics, CSR, ESG, Climate, Governance, Reporting, Finance, Supply Chain, AI, Strategy, Case Analysis 與 Crisis Management 的全維度訓練，"
              "W15 不再講授新內容，而是要求學生扮演 McKinsey, BCG, Deloitte, PwC, EY 或 KPMG 的高階 ESG 顧問團隊，為真實企業進行完整『診斷—分析—策略—KPI—董事會提案』！\n"
              "本週高度對接 AACSB 董事會模擬 (Board Presentation)，教師與全班同學扮演企業董事會成員與投資人，對各組提案的可行性、資本預算、風險控管與 ROI 進行質詢，展示高階企管人的溝通與策略企劃力！")

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
        ("00:00 - 00:15", "15m", "Part 1：Capstone 專案說明\n(Capstone Project Mandate)", "【Slide 1-5】W1-W14 全課程 14 週知識總回顧、顧問角色設定 (McKinsey/BCG/Big 4)、顧問思維 4 步驟（找問題/找原因/提方案/評估效益）、專案流程宣告。"),
        ("00:15 - 00:35", "20m", "Part 2：企業診斷與工具\n(ESG Health Check)", "【Slide 6-12】SWOT、PESTEL、Stakeholder Mapping、Materiality Matrix 工具整合；【活動一】ESG Health Check (為台積電/Apple/IKEA/Unilever/Starbucks/Tesla/玉山金/中華電 進行 7 大維度健康檢查)。"),
        ("00:35 - 01:10", "35m", "Part 3：策略設計與藍圖\n(Strategy & KPI Dashboard)", "【Slide 13-20】2035 ESG Strategy Roadmap 構建、E/S/G/AI/Supply Chain/BMI 6 大柱石策略規劃、ESG KPI Dashboard (量化 3 年與 5 年指標)。"),
        ("01:10 - 01:45", "35m", "【活動二】：董事會提案大賽\n(Consulting Pitch & Board Q&A)", "【Slide 21-23】【活動二】ESG Consulting Pitch (各組 10 分鐘向董事會進行策略簡報)、教師與同儕扮演董事會質詢、同儕評分表填寫。"),
        ("01:45 - 02:00", "15m", "Part 4：總整與 W16 預告\n(Summary & HW15)", "【Slide 24-25】Capstone 專案核心成果梳理、W16 課程總回顧與未來趨勢預告、Homework 15 (4,000-5,000字小組期末報告) 交代與 5 大 AACSB 評分權重。")
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
        ("Slide 1: 課程封面 (Week 15 ESG Consulting Capstone)", 
         "【授課腳本】：「歡迎來到第 15 週《ESG企業顧問專題：永續策略提案》。本週是我們全學期最核心的 Capstone Project 頂峰展示！」"),
        ("Slide 2: W1-W14 全課程 14 週知識總回顧", 
         "【授課腳本】：展示脈絡：Ethics → CSR → ESG → Climate → Governance → Reporting → Finance → Supply Chain → AI → Strategy → Cases → Crisis。"),
        ("Slide 3: 今天，你們是頂尖 ESG 策略顧問！", 
         "【授課腳本】：角色設定：各組扮演 McKinsey, BCG, Deloitte, PwC, EY, KPMG 顧問團隊，向企業董事會提出轉型簡報。"),
        ("Slide 4: Capstone 專案流程 5 步驟", 
         "【授課指引】：說明步驟：1. 診斷 (Diagnosis) → 2. 分析 (Analysis) → 3. 策略 (Strategy) → 4. KPI 設計 → 5. 執行路徑 (Execution)。"),
        ("Slide 5: 顧問思維：問題、原因、方案與 ROI", 
         "【授課腳本】：強調顧問邏輯：精準定位痛點、根因剖析、提出前瞻方案與評估財務/ESG 雙重回報 (ROI)。"),
        ("Slide 6: 企業背景分析與現況診斷 (Context Audit)", 
         "【授課腳本】：教導學生梳理目標企業所屬產業、主要營運市場與當前永續困境。"),
        ("Slide 7: SWOT 工具在 ESG 轉型中的應用", 
         "【授課指引】：運用 SWOT 評估內部綠色優勢/劣勢與外部碳關稅/法規威脅。"),
        ("Slide 8: PESTEL 外部環境分析工具", 
         "【授課腳本】：運用 PESTEL 評估政治、經濟、社會、技術、環境與法律 6 大宏觀趨勢。"),
        ("Slide 9: Stakeholder Mapping (利害關係人圖譜)", 
         "【授課腳本】：運用 Salience Model 識別核心利害關係人期待與優先順序。"),
        ("Slide 10: Materiality Matrix (雙重重大性矩陣)", 
         "【授課指引】：繪製重大性矩陣，篩選出 5 大最影響企業財務與社會衝擊的 ESG 議題。"),
        ("Slide 11: 活動一：ESG Health Check (企業健檢)", 
         "【活動執行】：4人一組，抽籤台積電, Apple, IKEA, Unilever, Starbucks, Tesla, 玉山金, 中華電，完成 7 大維度「ESG 健康檢查報告」。"),
        ("Slide 12: 活動一：各組討論與初步點評 (Class Debrief)", 
         "【活動點評】：點評各組健康檢查：診斷切忌泛泛而談，必須精準抓出產業專屬痛點！"),
        ("Slide 13: 2035 ESG Strategy Roadmap 架構", 
         "【授課腳本】：引導設計 10 年期藍圖：分為短期 (1年)、中期 (3年) 與長期 (5-10年) 轉型行動。"),
        ("Slide 14: Environment 板塊策略 (淨零/ Scope 1-3 / CBAM)", 
         "【授課指引】：規劃環境策略：RE100 時程、範疇 3 供應鏈減碳與應對歐盟 CBAM 方案。"),
        ("Slide 15: Social 板塊策略 (DEI / 人權 / 生態系共榮)", 
         "【授課腳本】：規劃社會策略：多元包容 (DEI)、無血汗供應鏈與在地社區共榮專案。"),
        ("Slide 16: Governance 板塊策略 (董事會 / COSO / 反貪腐)", 
         "【授課腳本】：規劃治理策略：獨立董事席次、高管薪酬與 ESG KPI 掛鉤及 COSO 內控。"),
        ("Slide 17: AI Governance 板塊策略 (Responsible AI)", 
         "【授課指引】：規劃 AI 治理策略：Responsible AI 5 原則、偏誤控制與歐盟 AI Act 風險分級合規。"),
        ("Slide 18: Supply Chain 板塊策略 (負責任採購 / 綠電)", 
         "【授課腳本】：規劃供應鏈策略：行為守則、無預警稽核與供應商綠電共購 (Co-PPA)。"),
        ("Slide 19: Business Model Innovation 板塊策略 (PaaS)", 
         "【授課腳本】：規劃商業模式策略：Product-as-a-Service 訂閱制與閉環循環經濟。"),
        ("Slide 20: ESG KPI Dashboard (可量化儀表板設計)", 
         "【授課指引】：設計 Dashboard：提出至少 5 項量化 KPI (如減碳%、綠電%、DEI%、高管薪酬綁定%）。"),
        ("Slide 21: 活動二：ESG Consulting Pitch (董事會提案大賽)", 
         "【活動執行】：各組以顧問角色進行 10 分鐘 Board Presentation (現況/3關鍵問題/藍圖/3年計畫/KPI/預期效益)。"),
        ("Slide 22: 活動二：董事會質詢與教師回饋 (Board Q&A)", 
         "【活動點評】：教師與同儕扮演董事會，針對資本預算、執行可行性與 ROI 進行高強度質詢。"),
        ("Slide 23: 同儕評分與最佳顧問團隊票選 (Peer Review)", 
         "【活動點評】：全班依據診斷完整性、策略設計、KPI 規劃與簡報表現填寫同儕評分表。"),
        ("Slide 24: Module 4 Capstone 核心成果梳理", 
         "【課程總結】：總結學生從學習者轉變為具備高階企劃能力的 ESG 策略顧問成果。"),
        ("Slide 25: 下週預告與 Homework 15 期末報告指引", 
         "【課程預告】：預告 Week 16 結業主題《課程回顧、永續領導力與未來趨勢 (Course Reflection & Future Trends)》，交代 Homework 15 (4,000-5,000字小組期末專題書面報告) 與 AACSB 評分權重。")
    ]

    for title, text in slides_detail:
        p = doc.add_paragraph()
        r_t = p.add_run(f"📌 {title}\n")
        r_t.bold = True
        r_t.font.name = "Microsoft JhengHei"
        r_t.font.color.rgb = INDIGO
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
        ("1. ESG 診斷完整性 (ESG Diagnosis)", "25%", "活用 SWOT, PESTEL, Materiality 完整分析目標企業 E/S/G/AI 痛點。"),
        ("2. 策略設計 (Strategic Roadmap Design)", "30%", "提出涵蓋短中長期之創新 ESG 策略、商業模式轉型與 VRIO 護城河。"),
        ("3. KPI 與執行規劃 (KPI & Execution Plan)", "20%", "設計包含至少 5 項量化指標之 Dashboard，並明訂執行路徑與資本預算。"),
        ("4. 簡報表現 (Board Presentation Pitch)", "15%", "以專業顧問口吻進行 10 分鐘提案，邏輯嚴謹，展現高強說服力與 Q&A 應答。"),
        ("5. 書面報告品質 (Report Quality)", "10%", "小組完成 4,000-5,000 字期末專題報告，格式規範，圖表與數據引用完整。")
    ]

    for r_data in rubric_data:
        row_cells = table_rubric.add_row().cells
        for i, val in enumerate(r_data):
            row_cells[i].text = val
            for p_cell in row_cells[i].paragraphs:
                for r in p_cell.runs:
                    r.font.name = "Microsoft JhengHei"
                    r.font.size = Pt(9)

    doc.save(r"C:\Users\User\Desktop\第1週_企業為何需要倫理\第15週_ESG企業顧問專題.docx")
    print("Successfully generated Week 15 Word .docx file!")

if __name__ == "__main__":
    generate_week15_word_guide()
