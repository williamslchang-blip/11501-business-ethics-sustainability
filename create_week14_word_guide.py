import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def generate_week14_word_guide():
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
    RED_CRISIS = RGBColor(225, 29, 72)

    # Title
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_title = p_title.add_run("📘 企業倫理與永續經營 (Business Ethics and Sustainable Management)\n"
                              "第 14 週：ESG危機管理、企業韌性與聲譽管理 —— 教師深度教學指引與授課手冊")
    r_title.font.name = "Microsoft JhengHei"
    r_title.font.size = Pt(20)
    r_title.font.bold = True
    r_title.font.color.rgb = DARK_BLUE

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_sub = p_sub.add_run("AACSB / PRME / Harvard / INSEAD / MIT Sloan Standard • ESG Crisis Management • Golden Hour • Corporate Resilience • CEO Simulation")
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
            r.font.color.rgb = DARK_BLUE if level == 1 else RED_CRISIS
            r.font.bold = True
        return h

    # Section 1: Philosophy
    add_sec_heading("📌 一、第 14 週課程設計理念與 AACSB 能力指標 (Week 14 Philosophy & Competencies)")
    
    p = doc.add_paragraph()
    p.add_run("第 14 週主題為「ESG危機管理、企業韌性與聲譽管理 (ESG Crisis Management, Corporate Resilience, and Reputation)」。"
              "本週為整門課程在 Capstone 專案之前的頂峰情境模擬章節！\n"
              "W1–W13 學生已理解倫理理論、ESG 規範、永續金融、供應鏈、AI 與案例分析，"
              "W14 引導學生面對企業管理者最艱難的時刻：『當黑天鵝降臨，發生食安風暴、工安天災、資訊洩漏、AI 失控或漂綠醜聞時，CEO 如何在黃金 1 小時內回應並重建信任？』\n"
              "本週結合 Harvard Business School 與 INSEAD 經典 Case Method 與 CEO 實境模擬，"
              "全面剖析：Johnson & Johnson Tylenol 1982 黃金典範、Volkswagen Dieselgate 柴油門、Boeing 737 MAX 安全文化崩壞、Meta Cambridge Analytica 隱私危機、Equifax 網攻、OpenAI 董事會政變與 CrowdStrike 全球 IT 中斷案例；\n"
              "並導入 AACSB 升級主題：全球變局下的企業韌性 (Corporate Resilience under Global Disruptions)，探討 ESG 韌性如何幫助企業在氣候地緣政治與科技變局下存續！")

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
        ("00:00 - 00:15", "15m", "Part 1：ESG 危機與風險識別\n(ESG Crisis Identification)", "【Slide 1-5】暖身問題（公司明天爆發食安/污染危機第一小時怎麼辦？）、什麼是 ESG Crisis？5 大危機類型 (E, S, G, AI, Cyber) 及對股價與聲譽的毀滅性衝擊。"),
        ("00:15 - 00:45", "30m", "Part 2：企業韌性與聲譽管理\n(Resilience & Reputation)", "【Slide 6-13】Corporate Resilience (企業韌性) 定義、Business Continuity (BCM)、ERM 早期預警系統、利害關係人危機溝通、社群媒體延燒應對、J&J Tylenol 1982 黃金典範；【活動一】Crisis Timeline Workshop。"),
        ("00:45 - 01:15", "30m", "Part 3：現代 ESG & 科技危機案例\n(Modern ESG Crises)", "【Slide 16-22】剖析 6 大現代危機案例：Volkswagen (Dieselgate)、Meta (Cambridge Analytica)、Boeing (737 MAX)、Equifax (資安洩漏)、OpenAI (董事會政變)、CrowdStrike (全球 IT 中斷) 與失敗根因分析。"),
        ("01:15 - 01:45", "30m", "Part 4：危機溝通與【活動二】CEO 模擬\n(CEO Crisis Simulation)", "【Slide 23-27】Golden Hour 黃金 1 小時回應原則；AACSB 升級單元：Global Disruptions 下的 Resilience；【活動二】CEO Crisis Simulation (模擬 CEO 於 20 分鐘撰寫第一份聲明、處理計畫與 3 大改善措施，全班票選最佳團隊)。"),
        ("01:45 - 02:00", "15m", "Part 5：W14 總整與 W15 預告\n(Summary & HW14)", "【Slide 28-30】Trust → Transparency → Resilience 總結、W15 Capstone 專案預告、Homework 14 (2,500字) 危機管理報告交代與 5 大 AACSB 評分權重。")
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
        ("Slide 1: 課程封面 (Week 14 ESG Crisis Management)", 
         "【授課腳本】：「歡迎來到第 14 週《ESG危機管理、企業韌性與聲譽管理》。本週我們將面對企業最嚴峻的黑天鵝時刻：危機降臨時如何做決策與重建誠信！」"),
        ("Slide 2: 暖身思考 (1-Hour Food Safety Dilemma)", 
         "【提問引導】：如果你的公司明天上午爆發食安風暴或毒廢水外洩，作為 CEO 你的第一小時處置與第一份對外聲明是什麼？引導體會黃金 1 小時的決策壓力。"),
        ("Slide 3: 什麼是 ESG Crisis？ (What is ESG Crisis?)", 
         "【授課腳本】：定義 ESG 危機：因違反環境、社會、治理、AI 倫理或資安規範，引發公眾憤怒、監管重罰與商業生存危機之重大事件。"),
        ("Slide 4: 5 大 ESG 危機類型 (5 Types of ESG Crises)", 
         "【授課指引】：解析 5 大類型：1. Environment (工廠爆炸/毒廢水)；2. Social (過勞/歧視/血汗)；3. Governance (財報舞弊/收賄)；4. AI Ethics (偏誤/幻覺)；5. Cybersecurity (個資洩漏)。"),
        ("Slide 5: 危機如何打擊企業估值與聲譽？ (Valuation Impact)", 
         "【授課腳本】：展示數據：重大 ESG 危機平均導致股價當週暴跌 20%-40%、機構撤資與品牌商譽永久折損。"),
        ("Slide 6: 什麼是 Corporate Resilience？ (企業韌性)", 
         "【授課指引】：定義企業韌性：企業在遭遇極端衝擊時，吸收震波、迅速恢復營運並從危機中進化學習的能力。"),
        ("Slide 7: Business Continuity Management (BCM 營運持續管理)", 
         "【授課腳本】：介紹 BCM 體系：建立備援系統、演練緊急災害防救與極端情境替代供應鏈。"),
        ("Slide 8: Enterprise Risk Management (ERM 企業風險管理)", 
         "【授課腳本】：介紹 ERM 早期預警系統：設置 KRI (關鍵風險指標) 實時監測內部違規與外部爭議。"),
        ("Slide 9: Stakeholder Crisis Communication (利害關係人溝通)", 
         "【授課指引】：強調溝通 4 原則：Speed (速度)、Transparency (透明)、Empathy (同理心) 與 Action (具體行動)。"),
        ("Slide 10: 傳統媒體與新聞發布會應對 (Media Management)", 
         "【授課腳本】：解析發言人制度、記者會控管與統一發言口徑之重要性。"),
        ("Slide 11: 社群媒體延燒與炎上處理 (Social Media Crisis)", 
         "【授課腳本】：解析網路炎上 (Digital Firestorm) 特性：絕不可隱瞞謊報、迅速回應澄清並發表誠懇道歉影片。"),
        ("Slide 12: Reputation Capital (聲譽資本的累積與修復)", 
         "【授課指引】：說明聲譽資本如同銀行存款：平時累積的 ESG 信譽能在危機爆發時獲得利害關係人的諒解。"),
        ("Slide 13: 經典標竿：Johnson & Johnson Tylenol 1982 危機", 
         "【案例剖析】：J&J Tylenol 遭投毒事件，CEO 第一時間不計成本全面回收 3,100 萬瓶藥品，並發明安全防封口，成為企業倫理與危機處理的世紀黃金典範！"),
        ("Slide 14: 活動一：Crisis Timeline Workshop", 
         "【活動執行】：4人一組抽取 VW, Boeing, Meta, Equifax, Starbucks, 統一, TSMC, OpenAI，畫出危機發生→回應→利害關係人反應→結果之 Crisis Timeline。"),
        ("Slide 15: 活動一：各組發表與點評 (Class Debrief)", 
         "【活動點評】：點評各組 Timeline：掩蓋真相永遠是加速企業滅亡的催化劑！"),
        ("Slide 16: 現代案例一：Volkswagen Dieselgate 柴油門", 
         "【案例剖析】：VW 安裝作弊軟體欺騙環保署驗車，引發天價罰款、CEO 辭職與嚴重的品牌漂綠危機。"),
        ("Slide 17: 現代案例二：Meta Cambridge Analytica 隱私危機", 
         "【案例剖析】：Facebook 8,700 萬用戶資料遭不當抓取干預大選，祖克柏遭受國會聽證質詢與鉅額罰款。"),
        ("Slide 18: 現代案例三：Boeing 737 MAX 安全文化崩壞", 
         "【案例剖析】：波音為追趕競爭對手，忽視 MCAS 軟體缺陷導致兩起慘重空難，凸顯將利潤置於安全之上的公司治理徹底失敗。"),
        ("Slide 19: 現代案例四：Equifax 1.47 億人個資外洩案", 
         "【案例剖析】：Equifax 延遲 6 週才公開重大資安外洩，高層更在消息公開前內線交易賣股，遭全美公憤。"),
        ("Slide 20: 現代案例五：OpenAI 董事會突發政變危機", 
         "【案例剖析】：Altman 遭無預警解僱事件，凸顯 AI 安全派與商業擴張派的劇烈衝突及治理漏洞。"),
        ("Slide 21: 現代案例六：CrowdStrike 全球 IT 系統癱瘓案", 
         "【案例剖析】：CrowdStrike 軟體更新出包引發全球航空與銀行系統藍屏大癱瘓，凸顯單點故障的科技韌性風險。"),
        ("Slide 22: 危機處置失敗的共同根因分析", 
         "【授課總結】：總結 5 大失敗原因：傲慢隱瞞、延遲回應、推卸責任、利潤優先與公關謊言。"),
        ("Slide 23: 危機溝通黃金原則 (Golden Hour Response)", 
         "【授課腳本】：解析 Golden Hour 原則：事件爆發 1 小時內公開表態，誠實承擔責任並公布調查小組。"),
        ("Slide 24: AACSB 升級單元：Global Disruptions 下的 Resilience", 
         "【授課指引】：AACSB 升級主題：解析企業如何在極端氣候、地緣政治、天災、網攻與 AI 故障下建立強韌營運體系。"),
        ("Slide 25: 長期聲譽修復與信任重建 4 步驟", 
         "【授課腳本】：展示修復步驟：獨立調查 → 懲處高層 → 制度改造 → 定期公開追蹤報告。"),
        ("Slide 26: 活動二：CEO Crisis Simulation (CEO 實境模擬)", 
         "【活動執行】：每組擔任 CEO 處置食安/AI失誤/資安/污染/歧視/童工危機，20 分鐘內撰寫第一份聲明、一週計畫與 3 大改善措施。"),
        ("Slide 27: 活動二：CEO 提案 Pitch 與全班票選最佳團隊", 
         "【活動點評】：各組進行 5 分鐘 CEO Pitch，全班票選最具同理心與決策力之最佳危機處理團隊。"),
        ("Slide 28: 本週重點總結 (Trust → Transparency → Resilience)", 
         "【課程總結】：展示 Trust → Transparency → Resilience 貫穿軸。"),
        ("Slide 29: 下週預告 (Preview Week 15 Capstone Project)", 
         "【課程預告】：預告 Week 15 主題：《永續策略實務專題與企劃 (Capstone Project: Sustainable Strategy Proposal)》。"),
        ("Slide 30: 課程總結與 Homework 14 作業交代", 
         "【課程總結】：交代 Homework 14 (2,500字) ESG 危機管理分析報告作業與 5 大 AACSB 評分權重（危機分析 30%、危機管理策略 25%、利害關係人分析 20%、改善建議 15%、報告品質 10%）。")
    ]

    for title, text in slides_detail:
        p = doc.add_paragraph()
        r_t = p.add_run(f"📌 {title}\n")
        r_t.bold = True
        r_t.font.name = "Microsoft JhengHei"
        r_t.font.color.rgb = RED_CRISIS
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
        ("1. 危機分析 (Crisis Audit)", "30%", "深刻分析目標企業爆發之 ESG 危機背景、影響範圍與根源性漏洞。"),
        ("2. 危機管理策略 (Crisis Strategy)", "25%", "精準評估企業第一時間應對措施、黃金一小時溝通與制度改造方案。"),
        ("3. 利害關係人分析 (Stakeholder Impact)", "20%", "靈活分析危機對品牌、消費者、投資人與員工之衝擊與信任修復。"),
        ("4. 改善建議 (Managerial Recommendations)", "15%", "提出三項具備強韌性 (Resilience) 與長線預防價值之具體改善建議。"),
        ("5. 報告品質 (Report Quality)", "10%", "篇幅達 2,500 字左右，結構嚴謹，正確引用危機事件 Timeline 與公關數據。")
    ]

    for r_data in rubric_data:
        row_cells = table_rubric.add_row().cells
        for i, val in enumerate(r_data):
            row_cells[i].text = val
            for p_cell in row_cells[i].paragraphs:
                for r in p_cell.runs:
                    r.font.name = "Microsoft JhengHei"
                    r.font.size = Pt(9)

    doc.save(r"C:\Users\User\Desktop\第1週_企業為何需要倫理\第14週_ESG危機管理與企業韌性.docx")
    print("Successfully generated Week 14 Word .docx file!")

if __name__ == "__main__":
    generate_week14_word_guide()
