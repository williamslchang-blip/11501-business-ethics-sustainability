import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def generate_week7_word_guide():
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
    AMBER = RGBColor(245, 158, 11)

    # Title
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_title = p_title.add_run("📘 企業倫理與永續經營 (Business Ethics and Sustainable Management)\n"
                              "第 7 週：公司治理、企業誠信與負責任領導 —— 教師深度教學指引與授課手冊")
    r_title.font.name = "Microsoft JhengHei"
    r_title.font.size = Pt(20)
    r_title.font.bold = True
    r_title.font.color.rgb = DARK_BLUE

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_sub = p_sub.add_run("AACSB / Harvard / Wharton / MIT Sloan / INSEAD Standard • Responsible Leadership • Agency Problem • Fraud Triangle")
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
            r.font.color.rgb = DARK_BLUE if level == 1 else AMBER
            r.font.bold = True
        return h

    # Section 1: Philosophy
    add_sec_heading("📌 一、第 7 週課程設計理念與 AACSB 能力指標 (Week 7 Philosophy & Competencies)")
    
    p = doc.add_paragraph()
    p.add_run("第 7 週主題為「公司治理、企業誠信與負責任領導 (Corporate Governance, Ethics and Responsible Leadership)」。"
              "本週為完成整門課程 ESG 三大構面最後一塊核心拼圖——Governance (G 治理) 的基石週！\n"
              "W1–W3 建立 Ethics/CSR，W4–W6 完成 ESG/Environment/Social 佈局，W7 必須深入 Governance (G)。"
              "本週拒絕走入傳統會計或純法律條文防線，而是結合 AACSB 核心指標 Responsible Leadership (負責任領導力)，"
              "解析代理人問題 (Agency Problem)、董事會與獨立董事監督、內部控制 (COSO/ERM)、舞弊三角理論 (Fraud Triangle)、吹哨者制度，以及 Wirecard、Boeing 737 MAX、Wells Fargo 等國際治理慘劇。")

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
        ("00:00 - 00:15", "15m", "Part 1：為什麼需要治理？\n(Why Governance?)", "【Slide 1-5】暖身問題（CEO無人監督會如何？）、代理人問題 (Agency Problem)、公司治理 4 大目的 (透明度、問責、責任、公平)。"),
        ("00:15 - 00:45", "30m", "Part 2：公司治理架構\n(Governance Framework)", "【Slide 6-12】董事會職責 (Board of Directors)、獨立董事制度 (Independent Directors)、審計委員會 (Audit Committee)、薪酬委員會 (Compensation Committee)、內部控制 (COSO) 與 ERM 全球風險管理。"),
        ("00:45 - 01:00", "15m", "【活動一】：董事會模擬\n(Board Meeting Simulation)", "【Slide 13-14】情境模擬演練（產品重大瑕疵未揭露，是否公告/召回？），角色扮演 CEO/董事長/獨董/CFO/法務長/股東。"),
        ("01:00 - 01:25", "25m", "Part 3：企業誠信與防弊\n(Business Integrity)", "【Slide 15-20】Code of Ethics 誠信守則、吹哨者保護 (Whistleblowing)、舞弊三角理論 (Pressure, Opportunity, Rationalization)、Wirecard 19億歐元假帳與 Enron/Wells Fargo 案例。"),
        ("01:25 - 01:45", "20m", "Part 4 & 【活動二】：負責任領導\n(Responsible Leadership)", "【Slide 21-25】Responsible Leader 觀念 (Profit, Planet, People, Purpose)、Good CEO vs Great Leader；【活動二】抽取 Boeing 737 MAX/Wells Fargo/VW/Wirecard/Toshiba/Uber 治理診斷。"),
        ("01:45 - 02:00", "15m", "Part 5：W1-W7 總結與預告\n(Summary & HW7)", "【Slide 26-27】W1–W7 完整主軸總結、W8 永續揭露與 ESG 報告書預告、Homework 7 (1,500–2,000字) 公司治理個案分析作業交代與 5 大 AACSB 評分權重。")
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

    # Section 3: 27 Slides Detailed Notes
    add_sec_heading("🗣️ 三、27 頁投影片逐頁深度授課指引 (Slide-by-Slide Instructional Notes)")

    slides_detail = [
        ("Slide 1: 課程封面 (Week 7 Governance & Leadership)", 
         "【授課腳本】：「歡迎來到第 7 週《公司治理、企業誠信與負責任領導》。本週我們將完成 ESG 最後且最重要的靈魂拼圖——Governance (G 治理)！」"),
        ("Slide 2: 課程轉折與脈絡 (Course Journey)", 
         "【授課腳本】：展示進程：W1-3 Ethics/CSR → W4-6 ESG/Environment/Social → W7 Governance (G 治理與負責任領導)。"),
        ("Slide 3: 暖身問題 (Unsupervised CEO Dilemma)", 
         "【提問引導】：如果一位 CEO 能力極強、績效卓越，但是完全沒有董事會與監督機制，會發生什麼事？引導思考權力集中與道德風險。"),
        ("Slide 4: 代理人問題 (Agency Problem)", 
         "【授課腳本】：解析經典 Agency Theory：委託人 (Principal 股東) 與代理人 (Agent 經理人) 之間的資訊不對稱與利益衝突。"),
        ("Slide 5: 公司治理四大目的 (4 Objectives)", 
         "【授課指引】：解析 4 大柱石：Transparency (透明度)、Accountability (問責性)、Responsibility (責任感)、Fairness (公平性)。"),
        ("Slide 6: 董事會 (Board of Directors)", 
         "【授課腳本】：介紹董事會作為公司最高治理與監督機關的運作模式、多元化背景要求。"),
        ("Slide 7: 董事會四大核心職責 (Core Board Duties)", 
         "【授課腳本】：解析 4 大職責：制定長遠策略 (Strategy)、監督管理層 (Supervision)、控管企業風險 (Risk) 與評估 CEO 績效與接班人 (CEO Succession)。"),
        ("Slide 8: 獨立董事制度 (Independent Directors)", 
         "【授課指引】：說明獨立董事的客觀獨立性與受託人責任 (Fiduciary Duty)，維護中小股東與利害關係人權益。"),
        ("Slide 9: 審計委員會 (Audit Committee)", 
         "【授課腳本】：介紹審計委員會審查財務報告真實性、監督外部會計師獨立性與防範會計舞弊。"),
        ("Slide 10: 薪酬委員會 (Compensation Committee)", 
         "【授課腳本】：介紹薪酬委員會設計高階主管激勵機制，避免短期炒作股價，並將 ESG KPI 納入薪酬發放。"),
        ("Slide 11: 內部控制系統 (Internal Control)", 
         "【授課指引】：解析 COSO 內控框架：控制環境、風險評估、控制活動、資訊溝通與監督。"),
        ("Slide 12: 全球企業風險管理 (ERM - Enterprise Risk Management)", 
         "【授課腳本】：說明 ERM 如何將氣候風險、資安威脅、供應鏈中斷與信譽風險納入董事會日常風險儀表板。"),
        ("Slide 13: 活動一：董事會模擬會議 (Board Meeting Simulation)", 
         "【活動執行】：角色扮演演練（產品發現重大隱患未曝光，討論是否立即公告與召回）。角色：CEO, 董事長, 獨董, CFO, 法務長, 股東。"),
        ("Slide 14: 活動一：教師點評與監督本質 (Class Debrief)", 
         "【活動點評】：總結：公司治理不是追求和氣一致，而是建立獨立批判、合規監督與勇於提出質疑的文化！"),
        ("Slide 15: 企業誠信 (Business Integrity)", 
         "【授課腳本】：強調誠信文化不是貼在牆上的宣言，而是高層示範 (Tone at the Top) 與每日商業行為。"),
        ("Slide 16: 誠信行為守則 (Code of Ethics)", 
         "【授課腳本】：規範反賄賂、反貪腐、禁止利益衝突、防範內線交易與餽贈標準。"),
        ("Slide 17: 吹哨者制度 (Whistleblowing System)", 
         "【授課指引】：解析匿名舉報管道、法律免受打壓保護與直通獨董審計委員會的調查機制。"),
        ("Slide 18: 舞弊三角理論 (Cressey's Fraud Triangle)", 
         "【授課腳本】：解析舞弊 3 要素：\n"
         "1. Pressure / Incentive (壓力/動機)：業績指標、個人債務。\n"
         "2. Opportunity (機會)：內控漏洞、權力過度集中。\n"
         "3. Rationalization (合理化)：「大家都這樣做」、「我只是暫時借用」。"),
        ("Slide 19: 案例一：Wirecard 德國科技巨擘倒閉案 (Wirecard Case)", 
         "【案例剖析】：德國 FinTech 巨擘 Wirecard 帳上 19 億歐元現金憑空消失。會計師與監管機構盲目信任，導致歐洲史上最大財務詐欺倒閉。"),
        ("Slide 20: 案例二：Enron & Wells Fargo 治理失靈 (Wells Fargo Case)", 
         "【案例剖析】：Wells Fargo 員工為達成高壓開戶 KPI 偷偷幫客戶開立數百萬假帳戶。激勵機制不當導致大規模系統性舞弊。"),
        ("Slide 21: 什麼是 Responsible Leader？ (Responsible Leadership)", 
         "【授課腳本】：介紹 AACSB 負責任領導力：管理者必須同時兼顧 Profit, Planet, People, Purpose 4P 平衡。"),
        ("Slide 22: Good CEO vs. Great Responsible Leader", 
         "【授課指引】：對比：Good CEO 創造漂亮短期財報；Great Responsible Leader 建立強健誠信文化與百年生態。"),
        ("Slide 23: ESG 時代 CEO 最大的責任 (CEO Duty in ESG Era)", 
         "【授課腳本】：CEO 最大的責任在於打造透明問責的組織、提供心理安全感並做出的榜樣。"),
        ("Slide 24: 活動二：CEO 危機決策 Challenge (CEO Crisis Simulation)", 
         "【活動執行】：小組抽籤審查 Boeing 737 MAX, Wells Fargo, VW, Wirecard, Toshiba, Uber，完成：核心問題？失靈機制？董事會處理方案？防範機制？"),
        ("Slide 25: 活動二：各組簡報與治理建議 (Team Pitches)", 
         "【活動點評】：各組 5 分鐘 Pitch。教師點評：董事會如何對 CEO 展現實質制衡力。"),
        ("Slide 26: 本週重點總結 (Governance → Integrity → Leadership)", 
         "【課程總結】：展示 Governance (G) → Integrity (誠信) → Responsible Leadership 貫穿軸。"),
        ("Slide 27: 課程全貌主軸與 W8 預告 (W1-W7 Thread & W8 Preview)", 
         "【課程總結與預告】：展現 W1–W7 完整軸線。預告 W8 《永續揭露與 ESG 報告 (ESG Reporting & Disclosure)》，說明 Homework 7 (1,500–2,000字) 公司治理個案分析作業與 AACSB 評分權重。")
    ]

    for title, text in slides_detail:
        p = doc.add_paragraph()
        r_t = p.add_run(f"📌 {title}\n")
        r_t.bold = True
        r_t.font.name = "Microsoft JhengHei"
        r_t.font.color.rgb = AMBER
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
        ("1. 公司治理分析 (Governance Analysis)", "30%", "精準分析目標企業之董事會、獨立董事、內控與資訊揭露機制。"),
        ("2. 問題診斷 (Root Cause Diagnosis)", "25%", "深刻剖析治理失靈事件之根因（如代理人問題、舞弊三角或不當激勵）。"),
        ("3. 改善方案 (Board Action Plan)", "20%", "提出具備獨立監督與制度制衡可行性的董事會改革方案。"),
        ("4. Responsible Leadership 應用 (Leadership Application)", "15%", "從負責任領導力角度評估 CEO 與高階管理層應展現之態度與責任。"),
        ("5. 報告品質 (Report Quality)", "10%", "篇幅達 1,500–2,000 字，結構嚴謹，正確標註參考文獻與新聞資料來源。")
    ]

    for r_data in rubric_data:
        row_cells = table_rubric.add_row().cells
        for i, val in enumerate(r_data):
            row_cells[i].text = val
            for p_cell in row_cells[i].paragraphs:
                for r in p_cell.runs:
                    r.font.name = "Microsoft JhengHei"
                    r.font.size = Pt(9)

    doc.save(r"C:\Users\User\Desktop\第1週_企業為何需要倫理\第7週_公司治理與企業誠信.docx")
    print("Successfully generated Week 7 Word .docx file!")

if __name__ == "__main__":
    generate_week7_word_guide()
