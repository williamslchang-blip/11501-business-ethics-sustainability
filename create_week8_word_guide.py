import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def generate_week8_word_guide():
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
    INDIGO = RGBColor(79, 70, 229)

    # Title
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_title = p_title.add_run("📘 企業倫理與永續經營 (Business Ethics and Sustainable Management)\n"
                              "第 8 週：永續報告、ESG資訊揭露與企業透明度 —— 教師深度教學指引與授課手冊")
    r_title.font.name = "Microsoft JhengHei"
    r_title.font.size = Pt(20)
    r_title.font.bold = True
    r_title.font.color.rgb = DARK_BLUE

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_sub = p_sub.add_run("AACSB / Harvard / Wharton / MIT Sloan / INSEAD Standard • GRI • ISSB (IFRS S1/S2) • SASB • TCFD • Double Materiality")
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
    add_sec_heading("📌 一、第 8 週課程設計理念與 AACSB 能力指標 (Week 8 Philosophy & Competencies)")
    
    p = doc.add_paragraph()
    p.add_run("第 8 週主題為「永續報告、ESG資訊揭露與企業透明度 (Sustainability Reporting, ESG Disclosure, and Corporate Transparency)」。"
              "本週為前半學期（W1–W8）倫理與永續管理基礎總整合的關鍵實務驗收週！\n"
              "W1–W7 已完整建立『Ethics → CSR → ESG → E → S → G』理論與策略架構，W8 核心回答：『企業做了這麼多 ESG 措施，如何透過高品質透明揭露，讓投資人、政府與消費者客觀驗證並轉化為企業估值與信任？』"
              "本週全面解構 GRI (廣泛利害關係人)、ISSB IFRS S1/S2 (全球資本市場基準)、SASB (77產業財務重大性)、TCFD (氣候財務風險) 5 大國際框架，"
              "並深入探討歐盟雙重重大性 (Double Materiality)、Materiality Matrix (重大性矩陣) 繪製，防範 Greenwashing 與 Disclosure Washing。")

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
        ("00:00 - 00:15", "15m", "Part 1：為什麼要揭露？\n(Why Disclose?)", "【Slide 1-5】暖身問題（做很好但不公開投資人知道嗎？）、揭露鏈條 (Disclosure → Transparency → Trust → Investment → Value)、揭露是成本還是競爭力？"),
        ("00:15 - 00:40", "25m", "Part 2：永續報告書拆解\n(Report Anatomy)", "【Slide 6-12】Integrated Report vs Annual Report vs Sustainability Report 差異、報告書核心章節 (CEO致詞, 重大議題, ESG績效數據, 第三方確信)、台積電報告書標竿。"),
        ("00:40 - 00:55", "15m", "【活動一】：重大性工作坊\n(Materiality Workshop)", "【Slide 13-14】20 項企業議題分類演練（碳排、用水、AI治理、資安、董事會多元、供應鏈、隱私、生物多樣性），為航空/銀行/科技/食品劃出 Materiality Matrix。"),
        ("00:55 - 01:30", "35m", "Part 3：5 大國際準則\n(Global Standards)", "【Slide 15-22】GRI (多重利害關係人), ISSB IFRS S1/S2 (資本基準), SASB (產業財務重大性), TCFD (氣候4柱石), CDP (氣候問卷)、5 大準則整理比較表、Double Materiality 雙重重大性。"),
        ("01:30 - 01:50", "20m", "Part 4 & 【活動二】：揭露品質\n(Quality & Challenge)", "【Slide 23-27】ESG 揭露品質 5 要素、Greenwashing vs Disclosure Washing 辨識、VW Dieselgate 案例；【活動二】小組實務審查 TSMC/Apple/Microsoft/Unilever/Starbucks/玉山金 永續報告書。"),
        ("01:50 - 02:00", "10m", "Part 5：W1-W8 總整與預告\n(W1-W8 Synthesis)", "【Slide 28】W1–W8 第一階段完整能力總整、W9 永續金融與 ESG 投資預告、Homework 8 (2,000字) 永續報告書分析作業交代與 5 大 AACSB 評分權重。")
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
        ("Slide 1: 課程封面 (Week 8 Sustainability Reporting)", 
         "【授課腳本】：「歡迎來到第 8 週《永續報告、ESG資訊揭露與企業透明度》。本週我們將整合前半學期的所有知識，學習如何閱讀、審查與製作國際標準的永續報告書！」"),
        ("Slide 2: 課程轉折與脈絡 (Course Journey)", 
         "【授課腳本】：展示進程：W1-3 Ethics/CSR → W4-7 ESG/E/S/G 基礎 → W8 Disclosure (資訊揭露與企業透明度)。"),
        ("Slide 3: 暖身問題 (Unseen ESG Dilemma)", 
         "【提問引導】：如果一家企業 ESG 做得非常好，但從不對外公開揭露，全球投資人會知道嗎？引導思考資訊不對稱與資本市場規則。"),
        ("Slide 4: 企業透明度鏈條 (Transparency Chain)", 
         "【授課腳本】：展示價值鏈：Disclosure (透明揭露) → Transparency (企業透明) → Trust (投資人信任) → Investment (資本挹注) → Corporate Value (企業估值提升)。"),
        ("Slide 5: 資訊揭露：成本還是競爭力？ (Cost vs Competitiveness)", 
         "【授課指引】：辯證思考：合規揭露看似增加審計與會計成本，實則是吸引外資、降低融資利率與展現高階治理的頂級競爭力！"),
        ("Slide 6: 什麼是 Sustainability Report？ (What is Sustainability Report?)", 
         "【授課腳本】：介紹永續報告書 (Sustainability Report / ESG Report)：企業對外溝通非財務績效 (E/S/G) 的官方權威文件。"),
        ("Slide 7: 三大報告書類型對比 (Integrated vs Annual vs Sustainability)", 
         "【授課對比】：\n"
         "• Annual Report (年報)：傳統財務數字與股東權益。\n"
         "• Sustainability Report (永續報告書)：非財務 E/S/G 指標與利害關係人溝通。\n"
         "• Integrated Report (整合報告書 IR)：將財務資本與自然/人力/社會資本融合揭露。"),
        ("Slide 8: 一份 ESG 報告書的核心章節 (Anatomy of ESG Report)", 
         "【授課腳本】：拆解四大必備章節：(1) CEO 致詞與永續願景；(2) 重大議題與利害關係人溝通；(3) E/S/G 績效數據；(4) 第三方獨立確信聲明書。"),
        ("Slide 9: CEO Message & Tone at the Top", 
         "【授課腳本】：分析 CEO 致詞：高層親自承諾減碳與 ESG 目標，代表全公司的資源挹注與願景方向。"),
        ("Slide 10: Material Topics 重大議題與利害關係人溝通", 
         "【授課指引】：說明企業如何透過問卷調查與深度訪談，搜集利害關係人最關心的 ESG 議題。"),
        ("Slide 11: Quantitative ESG Performance 數據績效", 
         "【授課腳本】：展示可量化指標：溫室氣體範疇 1-3 排放量、綠電使用率、女性主管比例、離職率與工安事故次數。"),
        ("Slide 12: 標竿案例：台積電永續報告書 (TSMC Case)", 
         "【案例剖析】：台積電率先整合 GRI, SASB, TCFD 與 ISSB 揭露，並提供第三方獨立會計師查驗確信，為全球半導體透明度標竿。"),
        ("Slide 13: 活動一：Materiality Workshop (找重大議題)", 
         "【活動執行】：4人一組，發放 20 項企業議題（碳排、用水、AI治理、資安、董事會多元、供應鏈、隱私、生物多樣性），抽籤航空/銀行/科技/食品劃出 Materiality Matrix。"),
        ("Slide 14: 活動一：各組分享與點評 (Class Debrief)", 
         "【活動點評】：點評：航空公司最重碳排 (E)；銀行最重金融資安與風險控制 (G)；科技業最重供應鏈與隱私 (S/G)。"),
        ("Slide 15: 國際揭露準則 1：GRI (Global Reporting Initiative)", 
         "【授課腳本】：介紹全球最普及的 GRI 標準：面向多重利害關係人 (Multi-stakeholders)，提供涵蓋廣泛的揭露架構。"),
        ("Slide 16: 國際揭露準則 2：ISSB (IFRS S1 / IFRS S2)", 
         "【授課腳本】：介紹國際會計準則理事會出的 ISSB：IFRS S1 (一般揭露) 與 IFRS S2 (氣候揭露)，建立全球資本市場統一的投資人揭露基準！"),
        ("Slide 17: 國際揭露準則 3：SASB (Sustainability Accounting Standards Board)", 
         "【授課指引】：介紹 SASB：針對 77 個特定產業，精準提供具備「財務重大性 (Financial Materiality)」的定量指標。"),
        ("Slide 18: 國際揭露準則 4：TCFD 氣候財務揭露 4 大柱石", 
         "【授課腳本】：解析 TCFD 4 大核心柱石：Governance (治理)、Strategy (策略)、Risk Management (風險管理)、Metrics & Targets (指標與目標)。"),
        ("Slide 19: 國際揭露準則 5：CDP 氣候與水資源問卷", 
         "【授課腳本】：介紹 CDP 全球氣候問卷評級，作為機構投資人評估氣候轉型風險的硬指標。"),
        ("Slide 20: 5 大國際揭露準則整理比較表 (Standards Comparison)", 
         "【授課指引】：表格對比 5 大準則之客群、受眾 (投資人 vs 多重利害關係人)、焦點與權威機構。"),
        ("Slide 21: Double Materiality 雙重重大性", 
         "【授課腳本】：解析歐盟 CSRD 推動的 Double Materiality：\n"
         "1. Impact Materiality (由內而外)：企業營運對環境與社會的影響。\n"
         "2. Financial Materiality (由外而內)：氣候與社會風險對企業財務價值的影響。"),
        ("Slide 22: Materiality Matrix 重大性矩陣圖解", 
         "【授課指引】：圖解矩陣：X 軸為「對企業營運/財務影響度」，Y 軸為「利害關係人關切度」，右上角象限即為核心重大議題。"),
        ("Slide 23: 評估 ESG 資訊揭露品質的 5 大要素 (Disclosure Quality)", 
         "【授課腳本】：解析高品質揭露 5 要素：Balance (平衡性/不隱惡揚善)、Comparability (可比性)、Accuracy (準確性)、Timeliness (即時性)、Assurance (第三方確信)。"),
        ("Slide 24: Greenwashing vs. Disclosure Washing", 
         "【授課指引】：剖析 Disclosure Washing：選擇性揭露好數據 (Cherry-picking)、使用模糊行銷用語與掩蓋嚴重負面衝擊。"),
        ("Slide 25: 案例：Volkswagen 柴油門與漂綠揭露 (VW Case)", 
         "【案例剖析】：VW 在永續報告書中大肆宣揚環保柴油引擎，實際卻安裝舞弊軟體。突顯未經第三方客觀查驗確信的報告書風險！"),
        ("Slide 26: 活動二：ESG Report Reading Challenge", 
         "【活動執行】：小組閱讀台積電/Apple/Microsoft/Unilever/Starbucks/玉山金 最新永續報告書，分析 3 大重大議題、揭露準則與揭露品質。"),
        ("Slide 27: 活動二：各組簡報與點評", 
         "【活動點評】：各組 5 分鐘 Pitch。教師點評各產業報告書揭露優缺點。"),
        ("Slide 28: W1–W8 第一階段能力總整與 W9 預告", 
         "【課程總整與預告】：總結 W1–W8 第一階段完整永續管理能力建構（Ethics → Decision → CSR → ESG → E → S → G → Disclosure）。預告 W9《永續金融與 ESG 投資》，說明 Homework 8 (2,000字) 永續報告書分析作業與 AACSB 評分權重。")
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
        ("1. 永續報告書閱讀與整理 (Report Audit & Summary)", "25%", "完整閱讀並精準整理目標上市公司最新永續報告書之公司概況與永續策略。"),
        ("2. 重大性分析 (Materiality Audit)", "20%", "正確辨識並分析企業最重視的三項重大議題及選擇原因。"),
        ("3. ESG 揭露準則應用 (Standards Application)", "25%", "精準判斷並舉例說明企業如何對接 GRI、ISSB、SASB 或 TCFD 揭露框架。"),
        ("4. 批判思考與改善建議 (Critical Evaluation)", "20%", "客觀評估報告書之完整性與不足之處，辨識是否有 Greenwashing 或 Disclosure Washing 疑慮。"),
        ("5. 報告品質 (Report Quality)", "10%", "篇幅達 2,000 字左右，結構嚴謹，圖表引用與文獻標註完整。")
    ]

    for r_data in rubric_data:
        row_cells = table_rubric.add_row().cells
        for i, val in enumerate(r_data):
            row_cells[i].text = val
            for p_cell in row_cells[i].paragraphs:
                for r in p_cell.runs:
                    r.font.name = "Microsoft JhengHei"
                    r.font.size = Pt(9)

    doc.save(r"C:\Users\User\Desktop\第1週_企業為何需要倫理\第8週_永續報告與ESG揭露.docx")
    print("Successfully generated Week 8 Word .docx file!")

if __name__ == "__main__":
    generate_week8_word_guide()
