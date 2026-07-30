import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def generate_week18_word_guide():
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
    PURPLE_LEADER = RGBColor(139, 92, 246)

    # Title
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_title = p_title.add_run("📘 企業倫理與永續經營 (Business Ethics and Sustainable Management)\n"
                              "第 18 週：負責任領導與永續未來 —— 教師深度教學指引與授課手冊 (課程大終結)")
    r_title.font.name = "Microsoft JhengHei"
    r_title.font.size = Pt(20)
    r_title.font.bold = True
    r_title.font.color.rgb = DARK_BLUE

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_sub = p_sub.add_run("AACSB / PRME / Harvard / INSEAD / MIT Sloan / Wharton Standard • Responsible Leadership • Future CEO Roundtable • Personal Portfolio • Graduation")
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
            r.font.color.rgb = DARK_BLUE if level == 1 else PURPLE_LEADER
            r.font.bold = True
        return h

    # Section 1: Philosophy
    add_sec_heading("📌 一、第 18 週課程設計理念與 AACSB 能力指標 (Week 18 Philosophy & Competencies)")
    
    p = doc.add_paragraph()
    p.add_run("第 18 週主題為「負責任領導與永續未來 (Responsible Leadership for a Sustainable Future)」。"
              "本週為整門 18 週頂尖商學院標準課程的終極圓滿結業章節！\n"
              "整門課歷經：『Module 1 倫理基礎 (W1-3) → Module 2 ESG管理 (W4-8) → Module 3 策略與創新 (W9-12) → Module 4 應用與提案 (W13-15) → Module 5 領導與決策 (W16-18)』。"
              "W18 不再講授新理論，而是完成學生從『學習者』到『未來企業領導者』的角色昇華與終身承諾！\n"
              "本週對接 AACSB 學習成果認證（知識 Knowledge + 技能 Skills + 價值觀 Values 兼備），引導學生回答：『你將成為什麼樣的管理者？』"
              "學生將參與『2035 CEO 圓桌論壇』、宣讀『Responsible Leadership 承諾書』，並完成『個人期末成果集 (Personal Leadership Portfolio)』，為自己的職涯與倫理價值立下宏偉藍圖。")

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
        ("00:00 - 00:20", "20m", "Part 1：18 週全景整合總回顧\n(Course Integration)", "【Slide 1-5】W1-W18 全課程 18 週學習地圖總融會、Ethics → Governance → ESG → Strategy → Innovation → Resilience → Leadership 整合架構、Responsible Leadership 5 大觀念（Integrity, Accountability, Transparency, Inclusiveness, Long-term Value）。"),
        ("00:20 - 00:50", "30m", "Part 2：未來的企業管理與 2035 挑戰\n(Future Business)", "【Slide 6-13】2035 企業 6 大挑戰（AI自主決策、氣候淨零、生物多樣性TNFD、供應鏈重組、數位信任、地緣政治）、未來 CEO 能力地圖；【活動一】Future CEO Roundtable (各組以 2035 CEO 圓桌論壇進行前瞻辯論)。"),
        ("00:50 - 01:15", "25m", "Part 3：個人領導力與管理哲學\n(Personal Philosophy)", "【Slide 16-20】我的領導風格 (Authentic Leadership)、個人核心價值觀（誠信/公平/同理/永續）、Ethics in Action 實踐、5 年職涯行動藍圖、終身學習承諾。"),
        ("01:15 - 01:45", "30m", "【活動二】：領導力承諾宣讀\n(Leadership Commitment)", "【Slide 21-22】【活動二】Leadership Commitment (撰寫與宣讀個人 Responsible Leadership 承諾書：管理者願景、3 條倫理原則、最大社會責任、5 年目標、創造長期價值)，全班簽署保存。"),
        ("01:45 - 02:00", "15m", "Part 4：大結業與 Homework 18\n(Graduation & Homework)", "【Slide 23-25】18 週完整學習歷程大結業宣言「Take Responsibility, Create Sustainable Value!」、推薦閱讀書單 (Net Positive / Conscious Capitalism / Infinite Game / Doughnut Economics / Age of AI)、Homework 18 (2,000-2,500字個人期末成果集) 交代與 5 大 AACSB 評分權重。")
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
        ("Slide 1: 課程封面 (Week 18 Responsible Leadership for a Sustainable Future)", 
         "【授課腳本】：「歡迎來到第 18 週大結業《負責任領導與永續未來》。恭喜大家邁入整門 18 週頂尖商學院課程的最終最高章節！」"),
        ("Slide 2: 18 週全景學習地圖終極融合", 
         "【授課腳本】：回顧 18 週軌跡：從 W1 倫理基礎，經歷 ESG 管理、策略創新、案例診斷、危機處理、顧問提案與董事會模擬，直到今天的領導力大成！"),
        ("Slide 3: 企業永續管理整合架構", 
         "【授課腳本】：展示整合鏈：Ethics → Governance → ESG → Strategy → Innovation → Resilience → Leadership。"),
        ("Slide 4: Responsible Leadership 5 大架構", 
         "【授課指引】：強調 5 大柱石：1. Integrity (誠信)；2. Accountability (問責)；3. Transparency (透明)；4. Inclusiveness (包容)；5. Long-term Value Creation (長期價值創造)。"),
        ("Slide 5: 從管理者 (Manager) 到領導者 (Leader) 的演進", 
         "【授課腳本】：說明轉變：從被動執行任務的傳統 Manager，轉變為具備高瞻遠矚與誠信靈魂的 Responsible Leader。"),
        ("Slide 6: 2035 年企業將面臨的 6 大極限挑戰", 
         "【授課腳本】：剖析未來 10 年衝擊：AI 自主決策、氣候淨零、生物多樣性 (TNFD)、供應鏈重組、數位信任與地緣政治。"),
        ("Slide 7: AI 與自主決策倫理治理 (AI Autonomy)", 
         "【授課指引】：討論 AI 系統獨立進行招聘、貸款審查與醫療診斷時的演算法責任歸屬。"),
        ("Slide 8: 淨零轉型與氣候治理 (Net Zero 2050)", 
         "【授課腳本】：強調 2035 年產業將步入強制去碳與能源轉型高峰期。"),
        ("Slide 9: 生物多樣性與自然資本會計 (TNFD)", 
         "【授課指引】：說明自然資本 (Natural Capital) 納入企業資產負債表與生態系恢復預算。"),
        ("Slide 10: 全球供應鏈重組與友岸外包 (Reshoring/Friendshoring)", 
         "【授課腳本】：分析地緣政治下供應鏈從『最低成本』轉向『最高韌性與可信』。"),
        ("Slide 11: 數位信任與網路安全防衛 (Digital Trust)", 
         "【授課腳本】：強調資安即是捍衛顧客隱私與企業誠信的第一防線。"),
        ("Slide 12: 地緣政治動盪與企業全方位韌性 (Resilience)", 
         "【授課指引】：說明企業在多極化地緣政治衝突中的彈性應變體系。"),
        ("Slide 13: 未來 CEO 的 5 大能力地圖 (CEO Competencies)", 
         "【授課腳本】：總結未來的 CEO 必須兼具倫理判斷、系統思考、永續決策、跨界合作與 AI 素養。"),
        ("Slide 14: 活動一：Future CEO Roundtable", 
         "【活動執行】：各組以「2035 CEO 圓桌論壇」形式選擇 AI/氣候/循環經濟/數位信任/人權/地緣政治進行 15 分鐘前瞻發言。"),
        ("Slide 15: 活動一：各組分享與點評 (Class Debrief)", 
         "【活動點評】：點評各組前瞻洞察：未來的 CEO 必須走在趨勢前端，化挑戰為新商業契機！"),
        ("Slide 16: 我的領導風格 (Authentic Leadership)", 
         "【授課腳本】：引導學生探索個人領導風格（真誠領導、服務型領導或變革型領導）。"),
        ("Slide 17: 我的核心價值觀 (My Core Values)", 
         "【授課指引】：確立個人最重視的 3 大不可妥協價值觀（誠信、公平、同理）。"),
        ("Slide 18: Ethics in Action (日常決策中的倫理實踐)", 
         "【授課腳本】：說明如何在日常商業決策中，拒絕黑箱、關懷員工與維持資訊透明。"),
        ("Slide 19: Career Roadmap (未來 5 年職涯與學習藍圖)", 
         "【授課指引】：引導規劃 5 年職涯路徑，將 ESG 永續思維融入個人職場專業。"),
        ("Slide 20: Lifelong Learning (終身學習承諾)", 
         "【授課腳本】：強調在快速變革的 AI 與永續時代，保持好奇與持續學習是領導者的必備習慣。"),
        ("Slide 21: 活動二：Leadership Commitment (承諾書)", 
         "【活動執行】：每位學生撰寫「Responsible Leadership 承諾書」(管理者願景、3條倫理原則、社會責任、5年目標、創造長遠價值)。"),
        ("Slide 22: 全班宣讀與教師圓滿總結", 
         "【活動點評】：學生自願宣讀承諾書，教師與全班共同見證，保存作為個人成長紀念。"),
        ("Slide 23: 18 週完整學習歷程大結業總融會", 
         "【課程總結】：展示 18 週完整學習脈絡：從基礎認知、管理工具、策略創新、應用提案到領導與決策的大成！"),
        ("Slide 24: 推薦大師閱讀書單 (Recommended Masters' Books)", 
         "【授課指引】：推薦大師名著：Paul Polman《Net Positive》, John Mackey《Conscious Capitalism》, Simon Sinek《The Infinite Game》, Kate Raworth《Doughnut Economics》, Kissinger《The Age of AI》。"),
        ("Slide 25: Take Responsibility, Create Sustainable Value!", 
         "【課程總結】：宣告「Take Responsibility, Create Sustainable Value!」，交代 Homework 18 (2,000-2,500字個人期末成果集 Portfolio) 與 5 大 AACSB 評分權重。")
    ]

    for title, text in slides_detail:
        p = doc.add_paragraph()
        r_t = p.add_run(f"📌 {title}\n")
        r_t.bold = True
        r_t.font.name = "Microsoft JhengHei"
        r_t.font.color.rgb = PURPLE_LEADER
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
        ("1. 知識整合 (Knowledge Integration)", "25%", "深刻融會 W1-18 全學期 18 週之倫理理論、ESG 工具、策略與董事會治理知識。"),
        ("2. 未來趨勢分析 (Future Trend Audit)", "20%", "前瞻分析 2035 AI、氣候淨零、TNFD、供應鏈與地緣政治對企業 CEO 的極限挑戰。"),
        ("3. 個人領導理念 (Leadership Philosophy)", "25%", "清晰確立個人 Responsible Leadership 願景、3 條倫理原則與 5 年職涯發展藍圖。"),
        ("4. 反思深度 (Reflection Depth)", "20%", "深刻反思顧問專案與董事會模擬體驗，展現高階管理者的自我批判與真誠度。"),
        ("5. 作品集品質 (Portfolio Quality)", "10%", "完成 2,000-2,500 字個人期末成果集 (Portfolio)，格式規範，內容豐富且極具典藏價值。")
    ]

    for r_data in rubric_data:
        row_cells = table_rubric.add_row().cells
        for i, val in enumerate(r_data):
            row_cells[i].text = val
            for p_cell in row_cells[i].paragraphs:
                for r in p_cell.runs:
                    r.font.name = "Microsoft JhengHei"
                    r.font.size = Pt(9)

    doc.save(r"C:\Users\User\Desktop\第1週_企業為何需要倫理\第18週_負責任領導與永續未來.docx")
    print("Successfully generated Week 18 Word .docx file!")

if __name__ == "__main__":
    generate_week18_word_guide()
