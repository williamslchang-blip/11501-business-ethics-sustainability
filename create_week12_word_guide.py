import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def generate_week12_word_guide():
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
    PURPLE = RGBColor(139, 92, 246)

    # Title
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_title = p_title.add_run("📘 企業倫理與永續經營 (Business Ethics and Sustainable Management)\n"
                              "第 12 週：永續創新、ESG策略與商業模式轉型 —— 教師深度教學指引與授課手冊")
    r_title.font.name = "Microsoft JhengHei"
    r_title.font.size = Pt(20)
    r_title.font.bold = True
    r_title.font.color.rgb = DARK_BLUE

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_sub = p_sub.add_run("AACSB / PRME / Harvard / MIT Sloan / INSEAD / NUS Standard • ESG Strategy • VRIO Framework • BSC x ESG • 2035 Roadmap")
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
    add_sec_heading("📌 一、第 12 週課程設計理念與 AACSB 能力指標 (Week 12 Philosophy & Competencies)")
    
    p = doc.add_paragraph()
    p.add_run("第 12 週主題為「永續創新、ESG策略與商業模式轉型 (Sustainability Innovation, ESG Strategy, and Business Model Transformation)」。"
              "本週為整門課程從『概念規範、資本與營運』全面昇華至『企業核心競爭策略 (Corporate Strategy)』的旗艦整合章節！\n"
              "W1–W11 學生已建立倫理、CSR、ESG、氣候、治理、揭露、金融、供應鏈與 AI 治理的完整體系，"
              "W12 解答企業 CEO 與高階主管最關心的終極問題：『如何將 ESG 從防守性的成本負擔，轉化為創造強大獲利與競爭優勢的商業策略？』\n"
              "本週結合 Harvard, MIT Sloan, INSEAD 與 NUS Business School 2026 最新授課標準，"
              "全面解析：Michael Porter 共享價值 (CSV)、三重底線 (Triple Bottom Line)、商業模式創新 (BMI)、Product-as-a-Service (PaaS)、平衡計分卡 (BSC × ESG)、Kotter 組織轉型 8 步驟；"
              "並導入 AACSB 升級主題：VRIO 分析矩陣，協助學生評估企業永續資產的價值 (Value)、稀有性 (Rarity)、不可模仿性 (Inimitability) 與組織匹配度 (Organization)。")

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
        ("00:00 - 00:15", "15m", "Part 1：ESG 如何創造競爭力？\n(ESG & Competitive Advantage)", "【Slide 1-5】暖身問題（ESG 到底是成本還是投資？）、Michael Porter 共享價值 (CSV) 與競爭優勢、從 Compliance (合規) 走向 Strategy (策略)。"),
        ("00:15 - 00:45", "30m", "Part 2：永續創新與商業模式\n(Business Model Innovation)", "【Slide 6-13】Sustainability Innovation 定義、Triple Bottom Line (People, Planet, Profit)、Product-as-a-Service (PaaS)、Patagonia & Tesla 標竿案例；【活動一】Business Model Innovation Workshop (為 Starbucks/Apple/IKEA/Netflix/TSMC/全聯 導入 ESG 商業模式畫布)。"),
        ("00:45 - 01:15", "30m", "Part 3：ESG Strategy & 平衡計分卡\n(ESG Strategy & BSC)", "【Slide 16-22】ESG 非慈善乃核心策略、ESG KPI 與高層激勵、Balanced Scorecard (BSC × ESG)、2035 永續藍圖、Unilever (USLP) & Ørsted (黑煤轉純綠能) 轉型案例。"),
        ("01:15 - 01:45", "30m", "Part 4：商業模式轉型與 VRIO\n(VRIO & Transformation)", "【Slide 23-27】AACSB 升級單元：VRIO 矩陣評估永續競爭優勢、Kotter 組織轉型 8 步驟；【活動二】ESG Strategy Design (為 Apple, Nike, TSMC, IKEA, Starbucks, Tesla 擔任顧問制定 2035 Roadmap)。"),
        ("01:45 - 02:00", "15m", "Part 5：W1-W12 總整與預告\n(Summary & HW12)", "【Slide 28-30】Innovation → Strategy → Competitive Advantage 總結、W13 台灣與國際案例預告、Homework 12 (2,000字) 策略報告交代與 5 大 AACSB 評分權重。")
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
        ("Slide 1: 課程封面 (Week 12 Sustainability Strategy)", 
         "【授課腳本】：「歡迎來到第 12 週《永續創新、ESG策略與商業模式轉型》。本週我們將解答企業 CEO 最關心的核心課題：如何將 ESG 轉化為企業強大的競爭優勢與商業獲利！」"),
        ("Slide 2: 課程轉折與脈絡 (Course Journey)", 
         "【授課腳本】：展示進程：W1-11 概念/規範/金融/供應鏈/AI → W12 進入 Corporate Strategy (商業策略與獲利轉型)。"),
        ("Slide 3: 暖身思考 (Cost vs. Investment Dilemma)", 
         "【提問引導】：ESG 到底是蠶食利潤的合規成本，還是能帶來高額回報的策略投資？引導體會被動合規 vs. 主動創新的巨大財務差異。"),
        ("Slide 4: Michael Porter 競爭優勢與 CSV 複習", 
         "【授課腳本】：引用大師 Michael Porter 觀點：重新定義產品與市場、重塑價值鏈生產力與建立在地產業聚落，透過 CSV 創造共榮。"),
        ("Slide 5: 從 ESG Compliance 走向 ESG Strategy", 
         "【授課指引】：強調觀念：消極防守 (Compliance) 只能避免開罰；積極策略 (Strategy) 才能攻佔新市場與創造溢價！"),
        ("Slide 6: 什麼是 Sustainability Innovation？", 
         "【授課腳本】：介紹永續創新範疇：包含產品創新 (綠色材質)、製程創新 (低碳自動化) 與商業模式創新。"),
        ("Slide 7: Business Model Innovation (BMI 商業模式創新)", 
         "【授課腳本】：解析 BMI：重構企業的價值主張 (Value Proposition)、顧客關係、關鍵資源與收益結構。"),
        ("Slide 8: Triple Bottom Line (三重底線框架)", 
         "【授課指引】：介紹 John Elkington 經典 Triple Bottom Line：兼顧 People (社會)、Planet (環境) 與 Profit (經濟利潤)。"),
        ("Slide 9: Circular Business Models 閉環經濟", 
         "【授課腳本】：說明閉環商業模式：將產品廢棄物重新轉化為高價值的原材料輸入。"),
        ("Slide 10: Sharing Economy (共享經濟)", 
         "【授課腳本】：說明共享模式：提高閒置資產使用率，減少整體資源消耗。"),
        ("Slide 11: Product-as-a-Service (PaaS 產品即服務)", 
         "【授課指引】：解析 PaaS：從賣斷硬體轉為訂閱服務（如 Philips 賣照明服務不賣燈泡），誘使企業設計高耐久產品。"),
        ("Slide 12: 案例一：Patagonia 永續品牌與目的導向獲利", 
         "【案例剖析】：Patagonia 將品牌使命定為「拯救地球」，推出 Worn Wear 並將 100% 股權轉入環保信託，創造無可取代的品牌溢價。"),
        ("Slide 13: 案例二：Tesla 加速全球轉向永續能源生態系", 
         "【案例剖析】：Tesla 不只是賣電動車，而是整合太陽能屋頂 (Solar Roof)、儲能系統 (Powerwall) 與超充網路，打造高壁壘能源生態系。"),
        ("Slide 14: 活動一：Business Model Innovation Workshop", 
         "【活動執行】：4人一組，抽籤 Starbucks, Apple, IKEA, Netflix, TSMC, 全聯，運用 Business Model Canvas 重新設計融入 ESG 價值的商業模式。"),
        ("Slide 15: 活動一：各組分享與點評 (Class Debrief)", 
         "【活動點評】：點評：優良的 ESG 商業模式創新必須能降低成本或提升顧客願意支付的價格 (Willingness to Pay)！"),
        ("Slide 16: ESG 不是慈善，而是企業核心策略", 
         "【授課腳本】：澄清誤區：ESG 絕非公關公關贈款，而是嵌入營運、產品與投資的長期策略。"),
        ("Slide 17: ESG 如何融入企業整體策略？", 
         "【授課指引】：說明策略制定 (Formulation) 到執行 (Execution) 的完整鏈結。"),
        ("Slide 18: ESG KPI 與高階主管薪酬掛鉤", 
         "【授課腳本】：介紹高階主管激勵機制：將 15%-30% 的變動年終獎金與範疇 1-3 減碳及 DEI 衡量指標綁定。"),
        ("Slide 19: Balanced Scorecard (BSC 平衡計分卡) × ESG", 
         "【授課指引】：展示 BSC 整合：將 ESG 指標跨界融入財務、顧客、內部流程與學習成長 4 大構面中。"),
        ("Slide 20: 2035 企業永續策略藍圖 (Sustainability Roadmap)", 
         "【授課腳本】：說明設定 10 年期遠大減碳與轉型 Milestone 之步驟。"),
        ("Slide 21: 案例三：Unilever Sustainable Living Plan (USLP)", 
         "【案例剖析】：Unilever 推出 USLP 計畫，將永續融入 400+ 品牌，結果永續品牌成長速度比其他品牌快 69%！"),
        ("Slide 22: 案例四：Ørsted 成功從黑煤石化轉型為全球風電龍頭", 
         "【案例剖析】：Ørsted (前身丹麥石油天然氣公司 DONG Energy) 在 10 年內將黑能佔比從 85% 翻轉為 90%+ 綠能，市值暴增，成為全球轉型典範！"),
        ("Slide 23: Transformation & 組織變革管理", 
         "【授課腳本】：引用 Kotter 8 步驟變革模型：建立緊迫感、引導團隊、溝通願景與消除障礙。"),
        ("Slide 24: AACSB 升級單元：VRIO 矩陣評估永續競爭優勢", 
         "【授課指引】：AACSB 升級主題：運用 VRIO 評估永續資產：\n"
         "• Value (價值)：能否降低成本或避險？\n"
         "• Rarity (稀有)：同業是否缺乏該永續技術？\n"
         "• Inimitability (不可模仿)：是否具備高專利與品牌護城河？\n"
         "• Organization (組織匹配)：企業結構是否能充分發揮其優勢？"),
        ("Slide 25: 企業永續轉型的 4 大成功關鍵因素", 
         "【授課腳本】：總結關鍵因素：CEO 親自承諾、跨部門協同、數據數位化與文化重塑。"),
        ("Slide 26: 活動二：ESG Strategy Design (擔任 ESG 顧問)", 
         "【活動執行】：每組擔任 Apple, Nike, TSMC, IKEA, Starbucks, Tesla 的策略顧問，設計一份 2035 ESG Strategy Roadmap (包含目標、KPI、投資、財務效益與 SDGs 貢獻)。"),
        ("Slide 27: 活動二：各組發表與點評 (Roadmap Pitches)", 
         "【活動點評】：各組 5 分鐘 Pitch。教師點評目標遠大度、財務自性與 VRIO 競爭優勢護城河。"),
        ("Slide 28: 本週重點總結 (Innovation → Strategy → Advantage)", 
         "【課程總結】：展示 Innovation → Strategy → Sustainable Competitive Advantage 貫穿軸。"),
        ("Slide 29: 下週預告 (Preview Week 13 Taiwan ESG Cases)", 
         "【課程預告】：預告 Week 13 主題：《台灣與國際企業永續標竿案例分析 (Taiwan & Global Corporate ESG Benchmark Cases)》。"),
        ("Slide 30: 階段二總結與 Homework 12 作業指引", 
         "【課程總結】：總結 12 週學習旅程，說明 Homework 12 (2,000字) 策略報告作業與 5 大 AACSB 評分權重。")
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
        ("1. ESG 策略分析 (ESG Strategy Audit)", "30%", "深刻分析目標企業現行 ESG 策略與其核心營運目標之整合深度。"),
        ("2. 商業模式分析 (Business Model Audit)", "25%", "精準剖析企業是否做到商業模式轉型（如 PaaS、循環經濟、共享模式）。"),
        ("3. 競爭優勢分析 (Competitive Advantage)", "20%", "靈活運用 SWOT 或 VRIO 矩陣，論證 ESG 如何形成長線不可模仿之護城河。"),
        ("4. 策略建議 (Strategic Recommendations)", "15%", "提出三項涵蓋產品創新、商業模式與永續治理的前瞻性策略建議。"),
        ("5. 報告品質 (Report Quality)", "10%", "篇幅達 2,000 字左右，結構嚴謹，圖表引用與財務/策略分析工具運用完整。")
    ]

    for r_data in rubric_data:
        row_cells = table_rubric.add_row().cells
        for i, val in enumerate(r_data):
            row_cells[i].text = val
            for p_cell in row_cells[i].paragraphs:
                for r in p_cell.runs:
                    r.font.name = "Microsoft JhengHei"
                    r.font.size = Pt(9)

    doc.save(r"C:\Users\User\Desktop\第1週_企業為何需要倫理\第12週_永續創新與ESG策略.docx")
    print("Successfully generated Week 12 Word .docx file!")

if __name__ == "__main__":
    generate_week12_word_guide()
