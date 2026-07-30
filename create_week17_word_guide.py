import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def generate_week17_word_guide():
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
    GOLD_BOARD = RGBColor(217, 119, 6)

    # Title
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_title = p_title.add_run("📘 企業倫理與永續經營 (Business Ethics and Sustainable Management)\n"
                              "第 17 週：ESG董事會決策模擬 —— 教師深度教學指引與授課手冊")
    r_title.font.name = "Microsoft JhengHei"
    r_title.font.size = Pt(20)
    r_title.font.bold = True
    r_title.font.color.rgb = DARK_BLUE

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_sub = p_sub.add_run("AACSB / PRME / Harvard / INSEAD Standard • Boardroom Simulation • Stakeholder Conflict • CEO Press Conference • Fiduciary Duty")
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
            r.font.color.rgb = DARK_BLUE if level == 1 else GOLD_BOARD
            r.font.bold = True
        return h

    # Section 1: Philosophy
    add_sec_heading("📌 一、第 17 週課程設計理念與 AACSB 能力指標 (Week 17 Philosophy & Competencies)")
    
    p = doc.add_paragraph()
    p.add_run("第 17 週主題為「ESG董事會決策模擬 (Boardroom Simulation: Responsible Leadership and Strategic Decision Making)」。"
              "本週為 18 週擴充架構中對接 AACSB『不確定情境下的高階決策力 (Decision-making under uncertainty)』之頂峰極限模擬課！\n"
              "W15 與 W16 完成了 Capstone 顧問提案與前瞻趨勢，W17 將學生推向企業治理的最高權力決策中心——董事會 (Boardroom)。"
              "當財務回報、員工生計、政府法規、NGO 監督與媒體壓力產生劇烈衝突時，董事會如何進行協商、投票表決並承擔決策後果？\n"
              "本週由 6–8 人小組分別飾演董事長、CEO、CFO、永續長 (CSO)、獨立董事、員工代表、投資人代表與 NGO 代表，針對『高污染工廠是否關閉』、『AI 招募系統偏誤下架』、『爭議供應商切割』等 6 大無標準答案之艱難困境進行現場開會表決，並隨後召開 CEO 新聞記者會接受全班尖銳質詢，展示最高層次的 Responsible Leadership！")

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
        ("00:00 - 00:15", "15m", "Part 1：董事會情境與角色設定\n(Board Context Setup)", "【Slide 1-5】角色指派（董事長/CEO/CFO/CSO/獨董/員工/投資人/NGO）、董事會 4 大職能（策略/治理/風險/倫理）、今日高難度衝突情境發放與背景說明。"),
        ("00:15 - 00:40", "25m", "Part 2：7 大利害關係人利益衝突\n(Stakeholder Conflicts)", "【Slide 6-11】剖析股東 (EPS)、員工 (工作權)、政府 (淨零合規)、NGO (零碳)、媒體 (熱度)、機構投資人 (MSCI AAA) 的劇烈訴求衝突與談判籌碼。"),
        ("00:40 - 01:10", "30m", "【活動一】：董事會決策會議\n(Board Meeting Simulation)", "【Slide 12-15】【活動一】Board Meeting Simulation (6-8 人董事會閉門會議，各角色陳述立場、辯論折衝、進行正式表決並形成正式決議文)。"),
        ("01:10 - 01:40", "30m", "【活動二】：CEO 危機記者會\n(CEO Press Conference)", "【Slide 16-22】【活動二】CEO Press Conference (CEO 與發言人召開記者會，全班扮演記者/投資人/NGO/政府，進行即席尖銳攻防與危機質詢)。"),
        ("01:40 - 02:00", "20m", "Part 3：總整與 W18 預告\n(Summary & HW17)", "【Slide 23-25】股價/MSCI 評級變化影響、Responsible Leadership 不確定決策總結、W18 終極大結業預告、Homework 17 (1,500字個人反思報告) 交代與 5 大 AACSB 評分權重。")
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
        ("Slide 1: 課程封面 (Week 17 Boardroom Simulation)", 
         "【授課腳本】：「歡迎來到第 17 週《ESG董事會決策模擬》。今天你們不再是學生，而是坐在最高權力核心的企業董事，必須在衝突情境下做出決策！」"),
        ("Slide 2: 今天，你就是董事！ (Role Allocation)", 
         "【授課腳本】：角色派任：每組 6-8 人分別擔任董事長、CEO、CFO、永續長 (CSO)、獨立董事、員工代表、投資人代表與 NGO 代表。"),
        ("Slide 3: 董事會的 4 大核心職能 (Board Mandates)", 
         "【授課指引】：說明 4 大職能：1. Strategy (策略)；2. Governance (治理)；3. Risk (風險管控)；4. Ethics (倫理誠信守護)。"),
        ("Slide 4: 今日模擬衝突情境介紹 (Simulation Scenarios)", 
         "【授課腳本】：發放情境：例如『高污染工廠是否提前關閉？』或『AI 招募系統偏誤是否下架？』或『爭議供應商解約？』。"),
        ("Slide 5: 企業財務與營運背景資訊 (Corporate Context)", 
         "【授課指引】：說明企業當前營收、現金流、市場市占率與即將發生的法規重罰風險。"),
        ("Slide 6: 利害關係人 1：股東 (Shareholders)", 
         "【授課腳本】：分析股東立場：要求維持短線 EPS 獲利、反對大幅增加 CapEx 資本支出。"),
        ("Slide 7: 利害關係人 2：員工 (Employees)", 
         "【授課指引】：分析員工立場：關心工作崗位保障、勞安環境與生活薪資 (Living Wage)。"),
        ("Slide 8: 利害關係人 3：政府與監管機構 (Regulators)", 
         "【授課腳本】：分析政府立場：要求符合淨零排放、歐盟 CBAM 與嚴懲污染違規。"),
        ("Slide 9: 利害關係人 4：NGO 與環保團體 (Activists)", 
         "【授課腳本】：分析 NGO 立場：要求立即停止污染、公開調查報告並進行去碳轉型。"),
        ("Slide 10: 利害關係人 5：媒體與社會大眾 (Media)", 
         "【授課指引】：分析媒體立場：追逐黑幕真相、聚焦公關失誤與高度社會關切。"),
        ("Slide 11: 利害關係人 6：機構 ESG 投資人 (ESG Funds)", 
         "【授課腳本】：分析投資人立場：關注 MSCI ESG 評級是否被降級與赤道原則合規。"),
        ("Slide 12: 活動一：Board Meeting Simulation", 
         "【活動執行】：各組進行 30 分鐘閉門董事會會議，各角色依據立場辯論折衝，最終進行正式舉手表決並寫出決議文。"),
        ("Slide 13: 活動一：董事會表決與決議文 (Board Debrief)", 
         "【活動點評】：點評各組表決結果：好的董事會決策必須在商業可行性與倫理責任間找到平衡！"),
        ("Slide 14: 董事會正式投票與決議通過 (Resolution)", 
         "【授課腳本】：紀錄各組表決結果（如 5 票贊成、2 票反對通過關閉工廠/下架系統）。"),
        ("Slide 15: CEO 第一份對外決策公開聲明稿 (CEO Statement)", 
         "【授課腳本】：指導 CEO 與發言人撰寫 3 分鐘對外記者會公開說明稿。"),
        ("Slide 16: 活動二：CEO 危機記者會 (Press Conference)", 
         "【活動執行】：各組 CEO 上台召開記者會，全班扮演尖銳記者、投資人與 NGO 提出即席火爆質詢。"),
        ("Slide 17: 即時市場股價與估值波動影響 (Stock Price Impact)", 
         "【授課腳本】：模擬決議發布後，華爾街與台股對該企業股價的當日波動反應。"),
        ("Slide 18: ESG 評級機構 (MSCI / Sustainalytics) 評級調升/調降", 
         "【授課指引】：分析評級機構如何根據董事會決策調整其 ESG Rating 等級。"),
        ("Slide 19: 長期利害關係人信任與品牌聲譽衝擊", 
         "【授課腳本】：評估該決策在未來 3 年對消費者忠誠度與員工留任率的影響。"),
        ("Slide 20: 活動二：記者會攻防總評與檢討", 
         "【活動點評】：點評 CEO 的應答表現：真誠同理與提出可驗證數據是化解媒體質疑的核心！"),
        ("Slide 21: 尖銳質詢應對技巧與公關防線 (Hostile Q&A)", 
         "【授課腳本】：解析尖銳問題處置：不推諉、不卸責、直面痛點並公布第三條監督機制。"),
        ("Slide 22: 董事會會後檢討與 Governance 改進", 
         "【授課腳本】：檢討董事會運作缺口：獨立董事席次是否足夠？資訊披露是否充分？"),
        ("Slide 23: 不確定情境下的 Responsible Leadership", 
         "【授課指引】：展示 Responsible Leadership 精髓：在資訊不完備與利益高度衝突下勇敢擔當！"),
        ("Slide 24: Module 5 董事會決策單元核心成果總融會", 
         "【課程總結】：總結學生從分析者提升至高階企業決策者的能力飛躍。"),
        ("Slide 25: Preview W18 終極大結業與 Homework 17 指引", 
         "【課程預告】：預告 Week 18 終極大結業《課程總回顧、個人永續領導力與畢業圓滿 (Course Reflection & Graduation)》，交代 Homework 17 (1,500字個人董事會反思報告) 與 AACSB 評分權重。")
    ]

    for title, text in slides_detail:
        p = doc.add_paragraph()
        r_t = p.add_run(f"📌 {title}\n")
        r_t.bold = True
        r_t.font.name = "Microsoft JhengHei"
        r_t.font.color.rgb = GOLD_BOARD
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
        ("1. 決策分析 (Decision Analysis)", "25%", "深刻分析衝突情境中財務、倫理、法規與永續之多方權衡與風險。"),
        ("2. 董事會參與 (Boardroom Engagement)", "25%", "在閉門會議中精準扮演派任角色，靈活談判折衝，貢獻高品質決議。"),
        ("3. 危機溝通 (Crisis Communication Pitch)", "20%", "在記者會中展現高度同理心、回答邏輯嚴謹，有效化解尖銳質問。"),
        ("4. 個人反思 (Board Reflection)", "20%", "撰寫 1,500 字報告，深入檢討決策妥協點與對 Responsible Leadership 的深刻領悟。"),
        ("5. 專業表現 (Professional Demeanor)", "10%", "全程展現高階企管人之專業口吻、溝通禮儀與董事會治理素養。")
    ]

    for r_data in rubric_data:
        row_cells = table_rubric.add_row().cells
        for i, val in enumerate(r_data):
            row_cells[i].text = val
            for p_cell in row_cells[i].paragraphs:
                for r in p_cell.runs:
                    r.font.name = "Microsoft JhengHei"
                    r.font.size = Pt(9)

    doc.save(r"C:\Users\User\Desktop\第1週_企業為何需要倫理\第17週_ESG董事會決策模擬.docx")
    print("Successfully generated Week 17 Word .docx file!")

if __name__ == "__main__":
    generate_week17_word_guide()
