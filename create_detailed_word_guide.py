import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def generate_comprehensive_guide():
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
    DARK_GRAY = RGBColor(60, 64, 67)
    RED = RGBColor(180, 40, 40)

    # Document Header
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_title = p_title.add_run("📘 企業倫理與永續經營 (Business Ethics and Sustainable Management)\n"
                              "第 1 週：企業為何需要倫理？ —— 教師深度教學指引與授課手冊")
    r_title.font.name = "Microsoft JhengHei"
    r_title.font.size = Pt(20)
    r_title.font.bold = True
    r_title.font.color.rgb = DARK_BLUE

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_sub = p_sub.add_run("AACSB 商管學院認證標竿 • Harvard Case Method • EMI 雙語教學 • ESG 永續治理架構")
    r_sub.font.name = "Microsoft JhengHei"
    r_sub.font.size = Pt(11)
    r_sub.font.color.rgb = TEAL

    doc.add_paragraph().paragraph_format.space_after = Pt(12)

    # Helper function for section headings
    def add_sec_heading(text, level=1):
        h = doc.add_heading(text, level=level)
        h.paragraph_format.space_before = Pt(16)
        h.paragraph_format.space_after = Pt(8)
        for r in h.runs:
            r.font.name = "Microsoft JhengHei"
            r.font.color.rgb = DARK_BLUE if level == 1 else TEAL
            r.font.bold = True
        return h

    # Section 1: Course Overview & Philosophy
    add_sec_heading("📌 一、課程設計理念與 AACSB 能力指標 (Course Philosophy & Competencies)")
    
    p = doc.add_paragraph()
    p.add_run("本課程第一週主題為「企業為何需要倫理？(Why Business Ethics Matters?)」，打破傳統一般課程僅進行冰冷課程說明的陋習，"
              "採用 Harvard Business School 個案討論法與 AACSB Assurance of Learning (AoL) 標準，將第一週直接定位為「企業倫理思維的建立 (Developing an Ethical Mindset)」。\n"
              "透過 24 頁投影片、2 個互動小組活動（CEO 決策挑戰賽、最新企業倫理新聞分析）與 1 個課後深度個案作業，貫穿「企業倫理 → CSR → ESG → 永續經營」的全學期戰略軸線。")

    # Section 2: Time Allocation Table
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
        ("00:00 - 00:15", "15m", "第一部分：課程介紹\n(Course Overview)", "【Slide 1-5】建立 AACSB 5 大學習目標、18週課程地圖藍圖與 5 個 20% 多元評分機制。"),
        ("00:15 - 00:40", "25m", "第二部分：為何需要倫理？\n(Why Ethics Matters)", "【Slide 6-11】剖析「合法 vs 道德」兩難、Milton Friedman vs Edward Freeman 理論衝突、6大營運倫理決策現場與「信任崩潰 (Trust Crisis)」。"),
        ("00:40 - 00:55", "15m", "【活動一】：CEO 決策挑戰賽\n(Activity 1: CEO Game)", "【Slide 12-13】4人小組情境模擬（合規保健品萬分之一健康疑慮，召回 vs 加警語）、Mentimeter 歸零即時表決與倫理推理 (Ethical Reasoning) 點評。"),
        ("00:55 - 01:25", "30m", "第三部分：倫理失敗案例\n(Failure Cases)", "【Slide 14-19】深入 Enron（會計詐欺、SPE 與 SOX 法案）與 VW Dieselgate（柴油門軟體詐欺與 4 大組織根因）個案，延伸 AI 時代 Responsible AI 新倫理。"),
        ("01:25 - 01:45", "20m", "【活動二】：新聞分析競賽\n(Activity 2: News Competition)", "【Slide 20-21】近一年真實新聞抽籤（Toyota/Meta/Nike/Tesla）、4-Step 框架討論與 3 分鐘 Pitch 發表，總結企業「法律近視眼」集體盲點。"),
        ("01:45 - 02:00", "15m", "第四部分：倫理到 ESG & 作業\n(Ethics to ESG)", "【Slide 22-24】說明 Business Ethics → CSR → ESG 演進藍圖、本週 4 大 Takeaways 總結與 Homework 1 個案分析作業交代。")
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

    # Section 3: Slide-by-Slide Facilitation Guide (All 24 Slides)
    add_sec_heading("🗣️ 三、24 頁投影片逐頁深度授課指引 (Slide-by-Slide Instructional Notes)")

    slides_detail = [
        ("Slide 1: 課程封面 (Course Title & Cover)", 
         "【授課指引】：開啟簡報按 F 進入全螢幕。\n"
         "【口述腳本】：「各位同學好，歡迎來到《企業倫理與永續經營》。這門課不是傳統教條式的道德宣導，而是從商學院高階決策者的角度，探討企業如何透過誠信治理與 ESG 打造不可替代的長遠競爭力。」\n"
         "【EMI 雙語重點】：強調 Business Ethics, CSR, ESG, Sustainable Governance 等核心詞彙。"),

        ("Slide 2: 教師介紹與授課資訊 (Admin & EMI)", 
         "【授課指引】：介紹授課團隊背景、Office Hour 預約機制與 Email。\n"
         "【教學提示】：說明課堂採用 Harvard Case Method (哈佛個案討論法)，強調商業倫理著重論證過程而非死記硬背。"),

        ("Slide 3: 課程目標 (AACSB AoL 5 大勝任力)", 
         "【授課指引】：詳細解說 5 大學習目標：(1) 分析倫理事件、(2) 評估 ESG 策略、(3) 閱讀永續報告書、(4) 解讀企業治理、(5) 建立永續思維。\n"
         "【問答引導】：「大家覺得『企業倫理』跟『個人道德』最大的差別是什麼？」"),

        ("Slide 4: 18 週課程內容地圖 (Roadmap)", 
         "【授課指引】：畫出 18 週演進流程：倫理理論 (W1-3) → CSR 責任 (W4-6) → ESG 數據 (W7-10) → 公司治理 (W11-13) → 淨零碳排 (W14-16) → Capstone 發表 (W17-18)。"),

        ("Slide 5: 評分方式與考核標準 (Assessment Scheme)", 
         "【授課指引】：說明 5 個 20% 的多元評量方式（課堂參與、小組個案、期中分析、小組簡報、期末 Capstone）。強調即時投票與課堂問答的比重。"),

        ("Slide 6: 暖身思考：合法，但不道德？ (Warm-up Dilemma)", 
         "【授課指引】：拋出震撼提問：「如果一家公司的商業行為完全合法，但卻傷害社會道德（例如演算法誘導青少年成癮），你會支持它嗎？」\n"
         "【板書引導】：將學生分成「法律派 (Legalistic View)」與「道德過濾派 (Ethical View)」，為後續理論鋪墊。"),

        ("Slide 7: 企業的真正目的 (Friedman vs. Freeman)", 
         "【授課指引】：對比兩大經典理論：\n"
         "• Milton Friedman (1970 股東至上)：企業唯一社會責任是在法律範圍內最大化股東財富。\n"
         "• Edward Freeman (1984 利害關係人)：企業需兼顧顧客、員工、供應商、社區與股東價值。\n"
         "【實務補充】：提及 2019 美國商業圓桌會議 (BRT) 181 位全球 CEO 宣言正式轉向利害關係人資本主義。"),

        ("Slide 8: 企業倫理的精準定義 (Ethics, Morality, Law)", 
         "【授課指引】：說明三層金字塔：\n"
         "• Law (法律)：國家強制的「最低道德底線 (Floor)」。\n"
         "• Morality (道德)：個人與社會內化的「善惡信念」。\n"
         "• Business Ethics (企業倫理)：商業決策中追求誠信與社會責任的「系統化原則 (Ceiling)」。"),

        ("Slide 9: 企業每天面對的倫理決策 (Everyday Decisions)", 
         "【授課指引】：列舉 6 大營運現場：HR 招聘裁員、行銷綠色漂洗、定價壟斷、供應鏈血汗工廠、AI 數據隱私偏見、產品瑕疵召回。證明倫理決策無處不在。"),

        ("Slide 10: 企業倫理的核心價值 (Strategic Advantage)", 
         "【授課指引】：引用 Ethisphere 研究數據：全球最具倫理企業長期股票報酬超越 S&P 500 大盤 28%。說明倫理能建立信任、提升品牌溢價、降低風險與吸引人才。"),

        ("Slide 11: 全球企業最大的危機：信任崩潰 (Trust Crisis)", 
         "【授課指引】：引用巴菲特名言：「建立名聲需要 20 年，摧毀它只需要 5 分鐘。」強調產品瑕疵可改善，但「誠信崩潰 (Trust Crisis)」對企業是致命打擊。"),

        ("Slide 12: 活動一：CEO 決策挑戰賽 (Scenario)", 
         "【活動執行】：4 人一組討論 10m。情境：熱銷保健品（貢獻 35% 營收）內部發現萬分之一肝功能風險，現行法規完全合規。決策 A (全面召回) vs 決策 B (加註警語) vs 決策 C (替代方案)。"),

        ("Slide 13: 活動一：即時表決與點評 (Live Poll)", 
         "【活動執行】：學生透過介面進行即時點擊投票（長條圖由 0% 開始實態成長）。\n"
         "【教師點評金句】：「商業倫理沒有標準解答！重點在於當法律沒有強制你時，你的倫理推理 (Ethical Reasoning) 邏輯與責任排位是什麼？」"),

        ("Slide 14: 案例一：安隆案 (Enron Collapse)", 
         "【案例剖析】：美國第 7 大企業破產。解析 Mark-to-Market (按市值計價) 提早認列未來估計收益，以及特殊目的實體 (SPE) 隱瞞百億負債的會計詐欺。"),

        ("Slide 15: Enron 時間軸與制度崩壞 (Timeline & SOX)", 
         "【制度變革】：介紹內部舉報者 Sherron Watkins 的勇氣，以及此案導致安達信 (Arthur Andersen) 解體與美國《薩班斯法案 (SOX Act)》的誕生。"),

        ("Slide 16: 案例二：福斯汽車柴油門 (VW Dieselgate)", 
         "【案例剖析】：2015 美國 EPA 揭發福斯 1,100 萬輛車安裝「作弊軟體 (Defeat Device)」，檢驗時開啟最大減排，平時廢氣超標 40 倍。天價罰金賠償超 330 億歐元。"),

        ("Slide 17: VW 根因分析 (Root Cause Analysis)", 
         "【組織診斷】：剖析 4 大失靈：(1) 高壓極端目標、(2) 高層權威恐懼文化 (Toxic Tone at Top)、(3) 工程倫理盲點與合理化、(4) 內部合規防線失靈。"),

        ("Slide 18: Enron vs VW 失敗模式比較 (Comparative Matrix)", 
         "【矩陣對比】：引導學生總結共通失敗模式：利用專業技術壁壘隱瞞真相、出於恐懼的集體沈默、缺乏獨立有效監督機制。"),

        ("Slide 19: AI 時代的企業倫理 (Responsible AI)", 
         "【前沿拓展】：延伸至 Big Tech (Google, Meta, OpenAI)。說明 Responsible AI 4 大柱石：透明度 (Transparency)、公平性 (Fairness)、隱私 (Privacy)、問責 (Accountability)。"),

        ("Slide 20: 活動二：最新新聞分析競賽 (News Competition)", 
         "【活動執行】：各組隨機抽籤 Toyota (測試造假)、Meta (青少年成癮)、Nike (供應鏈爭議)、Tesla (FSD 宣傳)。運用 4-Step 框架討論 12m。"),

        ("Slide 21: 活動二：發表與點評 (Team Pitch)", 
         "【活動執行】：每組 3 分鐘 Pitch。教師總結企業集體盲點「法律沒禁止就先做 (Legalistic Myopia)」與「大家都這樣做 (Normalization of Deviance)」。"),

        ("Slide 22: 倫理到 ESG 的演進藍圖 (Evolutionary Path)", 
         "【邏輯串聯】：說明演進路徑：Business Ethics (內在基因) → CSR (責任行動) → ESG Data (量化數據) → Sustainable Enterprise (永續經營)。"),

        ("Slide 23: 本週重點整理 (Key Takeaways)", 
         "【課程總結】：複習 4 大 Takeaways：(1) 企業非僅賺錢機器、(2) 法律≠倫理上限、(3) 信任是關鍵無形資產、(4) 倫理是 ESG 的基因。"),

        ("Slide 24: 本週課堂作業說明 (Homework 1 Guidelines)", 
         "【作業交代】：說明 1,000–1,200 字個案分析作業規範（背景、利害關係人圖譜、倫理診斷、CEO 方案、反思）與 AACSB 4-Level Rubrics 評分比重。")
    ]

    for title, text in slides_detail:
        p = doc.add_paragraph()
        r_t = p.add_run(f"📌 {title}\n")
        r_t.bold = True
        r_t.font.name = "Microsoft JhengHei"
        r_t.font.color.rgb = TEAL
        r_d = p.add_run(text)
        r_d.font.name = "Microsoft JhengHei"

    doc.add_paragraph().paragraph_format.space_after = Pt(12)

    # Section 4: Homework Rubric Table
    add_sec_heading("📝 四、課堂作業規範與 AACSB 4-Level 評分量規 (Rubric Matrix)")

    table_rubric = doc.add_table(rows=1, cols=4)
    table_rubric.alignment = WD_TABLE_ALIGNMENT.CENTER
    r_hdr = table_rubric.rows[0].cells
    r_headers = ["評分面向 (Dimension)", "權重", "卓越 (Exceeds Expectation) 90-100分", "待加強 (Below Expectation) 60-74分"]
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
        ("1. 事件介紹 (Background)", "20%", "精準還原事件細節與時間線，引用權威資料與媒體數據。", "內容流於籠統，缺乏具體時間、地點與事實佐證。"),
        ("2. 倫理分析 (Ethical Analysis)", "30%", "靈活運用利害關係人理論與倫理模型，深入剖析深層兩難。", "缺乏倫理與管理理論分析，僅停留在主觀好壞感想。"),
        ("3. 解決方案 (CEO Action Plan)", "30%", "提供具高度可行性且兼顧短中期危機處理與長期 ESG 方案。", "方案空洞無效（例如僅寫「加強員工道德教育」）。"),
        ("4. 個人反思 (Personal Reflection)", "20%", "展現深刻的批判性思考 (Critical Thinking) 與個人誠信啟示。", "篇幅嚴重不足，或直接複製網路摘要結論。")
    ]

    for r_data in rubric_data:
        row_cells = table_rubric.add_row().cells
        for i, val in enumerate(r_data):
            row_cells[i].text = val
            for p_cell in row_cells[i].paragraphs:
                for r in p_cell.runs:
                    r.font.name = "Microsoft JhengHei"
                    r.font.size = Pt(9)

    # Save Word files
    doc.save(r"C:\Users\User\Desktop\第1週_企業為何需要倫理_教學指引.docx")
    print("Successfully generated ultra-detailed Word .docx file!")

if __name__ == "__main__":
    generate_comprehensive_guide()
