import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def generate_week16_word_guide():
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
                              "第 16 週：企業倫理與永續管理的未來 —— 教師深度教學指引與授課手冊")
    r_title.font.name = "Microsoft JhengHei"
    r_title.font.size = Pt(20)
    r_title.font.bold = True
    r_title.font.color.rgb = DARK_BLUE

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_sub = p_sub.add_run("AACSB / PRME / Harvard / MIT Sloan / Wharton Standard • Responsible Leadership • Future Trends • Leadership Manifesto • Course Wrap-up")
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
    add_sec_heading("📌 一、第 16 週課程設計理念與 AACSB 能力指標 (Week 16 Philosophy & Competencies)")
    
    p = doc.add_paragraph()
    p.add_run("第 16 週主題為「企業倫理與永續管理的未來 (The Future of Business Ethics and Sustainable Management)」。"
              "本週為整門 16 週課程的最終大結業與『反思 (Reflection) + 整合 (Integration) + 前瞻 (Future)』最高章節！\n"
              "W1–W15 學生已完成完整的學習閉環：『基礎認知 (W1-W3) → 永續管理 (W4-W8) → 策略與創新 (W9-W12) → 整合應用與領導 (W13-W16)』。"
              "W16 不再安排期末考試或單純心得，而是對接 AACSB 最高標準的 Responsible Leadership (負責任領導力)。\n"
              "本週引導學生回答終極問題：『未來的企業管理者應具備哪些能力？在面對 2035 AI 治理、氣候變遷、生物多樣性 (TNFD) 與地緣政治挑戰時，如何保持倫理與誠信？』"
              "學生將於課堂撰寫與宣讀『我的領導宣言 (My Leadership Manifesto)』，並閱讀 Paul Polman 的《Net Positive》與 Simon Sinek 的《The Infinite Game》，為未來的企業領導生涯立下根基。")

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
        ("00:00 - 00:20", "20m", "Part 1：課程回顧與知識融會\n(Course Review)", "【Slide 1-5】W1-W16 全課程 16 週學習地圖總融會、Ethics → CSR → ESG → Sustainability → Responsible Leadership 演變軸、5 大核心觀念 (Integrity, Transparency, Accountability, Sustainability, Innovation)。"),
        ("00:20 - 00:50", "30m", "Part 2：企業永續的未來趨勢\n(Future Trends)", "【Slide 6-13】Future of ESG、AI + ESG 趨勢、Climate Transition、Nature & Biodiversity (TNFD)、Supply Chain Living Wage、Digital Trust & Cybersecurity；【活動一】Future of Business Workshop (討論 2035 企業最大挑戰)。"),
        ("00:50 - 01:15", "25m", "Part 3：Responsible Leadership\n(負責任領導力)", "【Slide 16-20】AACSB Responsible Leadership 5 大核心能力 (倫理判斷/系統思考/永續決策/跨領域合作/AI素養)、Leader vs Manager 對比、個人核心價值觀。"),
        ("01:15 - 01:45", "30m", "【活動二】：我的領導宣言\n(My Leadership Manifesto)", "【Slide 21-22】【活動二】My Leadership Manifesto (撰寫與宣讀 1 頁領導宣言：最重視的 3 價值觀、倫理實踐、5 年行動計畫)、教師與同儕點評。"),
        ("01:45 - 02:00", "15m", "Part 4：全課程大總結與閱讀\n(Graduation & Reflection)", "【Slide 23-25】16 週完整學習閉環大總結、推薦經典書單與影音 (Net Positive / Conscious Capitalism / The Infinite Game)、Homework 16 (1,500-2,000字個人期末反思報告) 交代與 5 大 AACSB 評分權重。")
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
        ("Slide 1: 課程封面 (Week 16 The Future of Business Ethics)", 
         "【授課腳本】：「歡迎來到第 16 週大結業《企業倫理與永續管理的未來》。本週我們將整合 16 週所學，建立屬於你們的 Responsible Leadership 負責任領導力！」"),
        ("Slide 2: 本學期 16 週完整學習地圖總融會", 
         "【授課腳本】：展示學習閉環：W1-3 基礎認知 → W4-8 永續管理 → W9-12 策略與創新 → W13-16 整合應用與領導。"),
        ("Slide 3: 企業倫理的百年演變歷程", 
         "【授課腳本】：解析演變：從傳統 Ethics (守法) → CSR (慈善) → ESG (指標) → Sustainability (策略) → Responsible Leadership (領導力)。"),
        ("Slide 4: 負責任領導者的 5 大核心觀念", 
         "【授課指引】：強調 5 大柱石：1. Integrity (誠信)；2. Transparency (透明)；3. Accountability (問責)；4. Sustainability (永續)；5. Innovation (創新)。"),
        ("Slide 5: 課程知識全景整合矩陣", 
         "【授課腳本】：梳理概念、資本、營運、數位治理與策略工具在企業中的綜合運用。"),
        ("Slide 6: Future of ESG (ESG 的未來演變趨勢)", 
         "【授課腳本】：展望未來：ESG 從『被動報告 (Reporting)』走向『系統性企業轉型 (Systemic Transformation)』。"),
        ("Slide 7: AI + ESG 雙軸趨勢的交會與博弈", 
         "【授課指引】：剖析 AI 賦能減碳與 AI 資料中心龐大耗電之平衡戰略。"),
        ("Slide 8: Climate Transition (淨零轉型加速)", 
         "【授課腳本】：分析 2050 淨零碳排對各國產業鏈的強烈過渡要求。"),
        ("Slide 9: Nature & Biodiversity (TNFD 自然資本與生物多樣性)", 
         "【授課指引】：介紹繼 TCFD 之後最新爆發的 TNFD (自然相關財務揭露) 與生物多樣性保護。"),
        ("Slide 10: Human Rights & 供應鏈生活薪資", 
         "【授課腳本】：分析各國法規對海外供應鏈 Living Wage (生活薪資) 與消除強迫勞動的強制要求。"),
        ("Slide 11: Cybersecurity & 數位隱私權保障", 
         "【授課腳本】：強調在萬物互聯時代，資安防護即是企業最核心的倫理責任。"),
        ("Slide 12: Digital Trust (數位信任) 作為企業核心資產", 
         "【授課指引】：說明數位信任是 2026 企業在 AI 與數據時代獲取顧客青睞的最高壁壘。"),
        ("Slide 13: Global Systemic Risks (全球系統性風險視角)", 
         "【授課腳本】：解析地緣政治衝擊、極端氣候天災與通貨膨脹對企業永續韌性的挑戰。"),
        ("Slide 14: 活動一：Future of Business Workshop", 
         "【活動執行】：4人一組，討論「2035 年，企業最大的倫理與永續挑戰會是什麼？」，選擇 AI、氣候、地緣政治、生物多樣性、人權、數位信任或資安，完成對策簡報。"),
        ("Slide 15: 活動一：各組分享與點評 (Class Debrief)", 
         "【活動點評】：點評各組前瞻分析：未來的管理者必須具備敏銳的宏觀雷達與風險防禦力！"),
        ("Slide 16: 什麼是 Responsible Leader？ (負責任領導者)", 
         "【授課腳本】：定義 Responsible Leader：在追求商業效益的同時，兼顧環境保護、社會正義與長遠利害關係人福祉的企業領導人。"),
        ("Slide 17: 未來管理者必備的 5 大核心能力", 
         "【授課指引】：對接 AACSB 5 大能力：1. 倫理判斷；2. 系統思考 (Systems Thinking)；3. 永續決策；4. 跨領域合作；5. AI 與數位素養。"),
        ("Slide 18: Leader vs. Manager (領導者 vs. 管理者)", 
         "【授課腳本】：對比：Manager 關注短期交易與執行效率 (Transaction)；Responsible Leader 關注長遠願景、使命與變革 (Transformation & Purpose)。"),
        ("Slide 19: 個人價值觀與領導力靈魂的形塑", 
         "【授課指引】：引導學生檢視個人最重視的核心價值觀（誠信、公平、同理心、永續）。"),
        ("Slide 20: Career & Sustainability (職涯與永續的融合)", 
         "【授課腳本】：說明如何在未來的職場崗位中（不論是財務、行銷、HR 或營運）落實 ESG 永續精神。"),
        ("Slide 21: 活動二：My Leadership Manifesto (我的領導宣言)", 
         "【活動執行】：每位學生撰寫 1 頁「我的領導宣言」(希望成為的管理者、3 大核心價值觀、倫理實踐、5 年行動計畫)。"),
        ("Slide 22: 學生宣言宣讀與教師結業點評", 
         "【活動點評】：學生自願上台宣讀宣言，教師與全班給予肯定，凝聚負責任領導者社群精神。"),
        ("Slide 23: 16 週全課程大總結 (The 16-Week Learning Loop)", 
         "【課程總結】：展示從 W1 基礎認知到 W16 負責任領導力的完整閉環成果！"),
        ("Slide 24: 推薦閱讀與影音靈感 (Recommended Reading)", 
         "【授課指引】：推薦大師著作：Paul Polman《Net Positive》、John Mackey《Conscious Capitalism》、Simon Sinek《The Infinite Game》與 Kate Raworth《Doughnut Economics》。"),
        ("Slide 25: Take Action & 結業挑戰 (Graduation & HW16)", 
         "【課程總結】：頒發結業挑戰「Take Action, Lead Responsibly!」，交代 Homework 16 (1,500-2,000字個人期末反思報告) 與 5 大 AACSB 評分權重。")
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
        ("1. 課程整合能力 (Course Integration)", "30%", "深刻整合 W1-16 全學期核心概念、ESG 工具與策略架構。"),
        ("2. 未來趨勢分析 (Future Trend Audit)", "25%", "精準評估 2035 AI、氣候、地緣政治、TNFD 生態與數位信任等宏觀挑戰。"),
        ("3. 個人反思 (Personal Reflection)", "20%", "真誠反思課程如何改變個人商業思維，並批判性評估過往認知。"),
        ("4. 領導理念與宣言 (Leadership Manifesto)", "15%", "清晰闡述 Responsible Leadership 觀點、3 大核心價值觀與 5 年行動計畫。"),
        ("5. 報告品質 (Report Quality)", "10%", "篇幅達 1,500-2,000 字左右，文字優美，結構嚴謹，充滿反思洞察。")
    ]

    for r_data in rubric_data:
        row_cells = table_rubric.add_row().cells
        for i, val in enumerate(r_data):
            row_cells[i].text = val
            for p_cell in row_cells[i].paragraphs:
                for r in p_cell.runs:
                    r.font.name = "Microsoft JhengHei"
                    r.font.size = Pt(9)

    doc.save(r"C:\Users\User\Desktop\第1週_企業為何需要倫理\第16週_企業倫理與永續的未來.docx")
    print("Successfully generated Week 16 Word .docx file!")

if __name__ == "__main__":
    generate_week16_word_guide()
