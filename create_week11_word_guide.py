import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def generate_week11_word_guide():
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
    CYAN = RGBColor(6, 182, 212)

    # Title
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_title = p_title.add_run("📘 企業倫理與永續經營 (Business Ethics and Sustainable Management)\n"
                              "第 11 週：AI、數位治理與企業倫理 —— 教師深度教學指引與授課手冊")
    r_title.font.name = "Microsoft JhengHei"
    r_title.font.size = Pt(20)
    r_title.font.bold = True
    r_title.font.color.rgb = DARK_BLUE

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_sub = p_sub.add_run("AACSB / Harvard / MIT Sloan / Wharton Standard • Responsible AI • EU AI Act • ISO 42001 • AI for Sustainability")
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
            r.font.color.rgb = DARK_BLUE if level == 1 else CYAN
            r.font.bold = True
        return h

    # Section 1: Philosophy
    add_sec_heading("📌 一、第 11 週課程設計理念與 AACSB 能力指標 (Week 11 Philosophy & Competencies)")
    
    p = doc.add_paragraph()
    p.add_run("第 11 週主題為「AI、數位治理與企業倫理 (Artificial Intelligence, Digital Governance, and Business Ethics)」。"
              "本週為整門課程邁入 2026 最新前沿科技與數位信任 (Digital Trust) 的重大轉折章節！\n"
              "W1–W10 已建立『Ethics → CSR → ESG → E → S → G → Disclosure → Finance → Supply Chain』完整體系，"
              "W11 聚焦解決當前企業最嚴峻的新興倫理挑戰——AI 治理與數位倫理 (AI Governance & Digital Ethics)。\n"
              "本週結合 Harvard, MIT Sloan, Wharton 與 Cambridge Judge 2025–2026 最新 AACSB 規範，全面解析：\n"
              "1. Responsible AI 5 大原則 (Fairness 公平、Transparency 透明、Accountability 問責、Safety 安全、Privacy 隱私)；\n"
              "2. AI 算法偏誤 (Algorithmic Bias)、幻覺 (Hallucination)、可解釋性 (XAI) 與深偽 (Deepfake) 風險；\n"
              "3. 全球 AI 治理法規 (歐盟 EU AI Act、ISO 42001 AI 管理系統、OECD AI 原則)；\n"
              "4. AACSB 前瞻升級主題：AI × ESG (Artificial Intelligence for Sustainability)，探討 AI 如何加速企業減碳，以及 AI 資料中心能源消耗帶來的全新 ESG 衝擊。")

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
        ("00:00 - 00:15", "15m", "Part 1：AI 正在改變企業\n(AI Revolution)", "【Slide 1-5】暖身問題（AI決定招募錄取能否接受？）、AI 革命浪潮 (Google, Microsoft, OpenAI, Apple, Tesla)、AI 最大的問題不是能力而是信任。"),
        ("00:15 - 00:45", "30m", "Part 2：Responsible AI & Ethics\n(AI Ethics)", "【Slide 6-13】Responsible AI 5 大原則、Algorithmic Bias 演算法偏誤、AI Hallucination 幻覺、Explainable AI (XAI)、Privacy & 版權爭議、Deepfake 危機；【活動一】AI Ethics Debate 辯論。"),
        ("00:45 - 01:15", "30m", "Part 3：AI Governance & 法規\n(AI Governance)", "【Slide 16-25】AI 治理架構、EU AI Act (歐盟 AI 法案風險分級)、ISO 42001 AI 管理系統、OECD AI 原則、OpenAI/Microsoft/Google 標竿；【活動二】AI Governance Policy Design 工作坊。"),
        ("01:15 - 01:45", "30m", "Part 4：AI × ESG 永續策略\n(AI for Sustainability)", "【Slide 26-29】AACSB 升級單元：AI 如何協助 ESG (電網最佳化、Scope 3 碳追蹤、ESG 報告自動化) vs AI 資料中心龐大耗電與電子廢棄物新風險、Responsible AI Framework。"),
        ("01:45 - 02:00", "15m", "Part 5：W1-W11 總整與預告\n(Summary & HW11)", "【Slide 30】W1–W11 模組三體系總整、W12 預告、Homework 11 (2,000字) AI倫理與企業治理分析報告交代與 5 大 AACSB 評分權重。")
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
        ("Slide 1: 課程封面 (Week 11 AI & Business Ethics)", 
         "【授課腳本】：「歡迎來到第 11 週《AI、數位治理與企業倫理》。本週我們將探索 2026 年企業永續最前沿的新防線 —— 負責任 AI 與數位信任！」"),
        ("Slide 2: 課程轉折與脈絡 (Course Journey)", 
         "【授課腳本】：展示進程：W1-10 完成 Ethics/CSR/ESG/Climate/Finance/Supply Chain → W11 進入 AI Governance (數位治理與信任)。"),
        ("Slide 3: 暖身思考 (AI Automated Hiring Dilemma)", 
         "【提問引導】：如果企業 100% 讓 AI 決定員工招聘、考績與解僱，你作為員工或主管能接受嗎？引導體會演算法黑箱與倫理焦慮。"),
        ("Slide 4: 全球企業的 AI 革命 (AI Revolution)", 
         "【授課腳本】：介紹 Google, Microsoft, OpenAI, Apple, Tesla, Meta 全面將 AI 融入營運產品。"),
        ("Slide 5: AI 最大的問題不是能力，而是信任 (Trust Deficit)", 
         "【授課指引】：強調觀念：AI 技術突破極快，但若缺乏數位信任 (Digital Trust) 與倫理治理，一次模型偏誤或資料洩漏即足以摧毀品牌信任。"),
        ("Slide 6: 什麼是 Responsible AI？ (What is Responsible AI?)", 
         "【授課腳本】：定義 Responsible AI：在設計、開發與部署 AI 系統時，以倫理規範、人類福祉與法律合規為核心架構。"),
        ("Slide 7: Responsible AI 5 大核心原則 (5 Core Principles)", 
         "【授課指引】：解析 5 大柱石：Fairness (公平無偏誤)、Transparency (透明公開)、Accountability (人為主控問責)、Safety (安全與防禦)、Privacy (個資隱私)。"),
        ("Slide 8: Algorithmic Bias 演算法偏誤", 
         "【授課腳本】：分析訓練資料偏誤 (Training Data Bias) 如何導致 AI 在性別、種族與履歷篩選中產生歧視。"),
        ("Slide 9: AI Hallucination 幻覺與事實風險", 
         "【授課腳本】：解析生成式 AI 捏造虛假事實 (Hallucination) 帶來的法律訴訟與企業信譽風險。"),
        ("Slide 10: Explainable AI (XAI) 可解釋性 AI", 
         "【授課指引】：說明黑箱模型 (Black Box Dilemma) 挑戰，強調金融與醫療 AI 必須具備可解釋性 (XAI)。"),
        ("Slide 11: Privacy & Data Ethics 資料倫理", 
         "【授課腳本】：解析 GDPR 與數據抓取 (Data Scraping) 爭議，確保用戶個資知情同意與隱私保護。"),
        ("Slide 12: Copyright & 版權侵權爭議", 
         "【授課腳本】：分析生成式 AI 模型訓練未授權藝術作品與新聞內容所引發的著作權集體訴訟。"),
        ("Slide 13: Deepfake 深偽與合成媒體危機", 
         "【授課指引】：解析 Deepfake 冒充高階主管進行天價詐騙與企業品牌形象攻擊。"),
        ("Slide 14: 活動一：AI Ethics Debate (AI 倫理辯論)", 
         "【活動執行】：全班分正反兩方辯論：「企業是否應讓 AI 全面參與 HR 招聘與考績決策？」，代表員工、主管、消費者與監管者表態。"),
        ("Slide 15: 活動一：各組分享與點評 (Class Debrief)", 
         "【活動點評】：點評：AI 可提升篩選效率，但終極決策必須保有 Human-in-the-Loop (人工監督) 與問責！"),
        ("Slide 16: 什麼是 AI Governance？ (AI Governance)", 
         "【授課腳本】：介紹 AI 治理：企業建立 AI 倫理委員會、風險評估矩陣與內部使用合規審查。"),
        ("Slide 17: 全球首部 AI 法案：歐盟 EU AI Act", 
         "【授課指引】：解析 EU AI Act 4 級風險分級：\n"
         "1. Unacceptable Risk (不可接受風險：如社會信用評分，直接禁止)；\n"
         "2. High Risk (高風險：如 HR 招募、金融信用，強制嚴格審查)；\n"
         "3. Specific Risk (特定風險：如 Chatbot，強制透明揭露)；\n"
         "4. Minimal Risk (最低風險：如遊戲 AI)。"),
        ("Slide 18: ISO 42001 AI 管理系統標準", 
         "【授課腳本】：介紹全球首個 ISO 42001 AI Management System 驗證標準。"),
        ("Slide 19: OECD AI 原則 (OECD AI Principles)", 
         "【授課腳本】：介紹 OECD 包容性成長、以人為本、透明度、穩健性與問責原則。"),
        ("Slide 20: 企業 AI 治理 3 道防線 (3 Lines of Defense)", 
         "【授課指引】：建構防線：研發團隊自我評估 → AI 倫理委員會審查 → 內部稽核與獨立第三方認證。"),
        ("Slide 21: 案例一：OpenAI 模型安全與董事會危機", 
         "【案例剖析】：剖析 OpenAI 針對 GPT-4 進行 Red Teaming (紅隊演練) 防禦，以及政變事件反映出的 AI 安全與商業化博弈。"),
        ("Slide 22: 案例二：Microsoft Responsible AI Standard", 
         "【案例剖析】：Microsoft 發布 Responsible AI Standard，將 Copilot 企業資料進行強監管隔絕，保護客戶資產。"),
        ("Slide 23: 案例三：Google Gemini AI 原則與偏誤修復", 
         "【案例剖析】：剖析 Google 頒布 7 大 AI Principles，針對圖像生成偏誤進行緊急修復與自我審查。"),
        ("Slide 24: 活動二：AI Governance Policy Design (政策設計工作坊)", 
         "【活動執行】：每組選擇 Microsoft, Google, OpenAI, Amazon, TSMC, 玉山金控，制定一份 Responsible AI Policy (包含使用原則、資料治理、偏誤控制、人工監督)。"),
        ("Slide 25: 活動二：各組發表與點評 (Policy Pitches)", 
         "【活動點評】：各組 5 分鐘 Pitch。教師對比科技業 vs 金融業對 AI 隱私與偏誤控制的策略差異。"),
        ("Slide 26: AACSB 升級單元：AI × ESG (AI for Sustainability)", 
         "【授課腳本】：介紹 AI 如何賦能 ESG：AI 最佳化綠電電網發電、精準預測氣候天災、自動化追蹤 Scope 1-3 碳排放與生成永續報告書草案！"),
        ("Slide 27: AI 帶來的全新 ESG 風險 (AI Carbon Footprint)", 
         "【授課指引】：警示負面衝擊：大型語言模型 (LLM) 訓練與 AI 資料中心運算引發龐大電力消耗、水資源冷卻需求與電子廢棄物。"),
        ("Slide 28: 企業 Responsible AI 整合框架", 
         "【授課腳本】：展示將 AI 治理、數位倫理與 ESG 永續目標相互結合的完整企業戰略圖表。"),
        ("Slide 29: 本週重點總結 (AI → Governance → Trust)", 
         "【課程總結】：展示 AI → Governance → Digital Trust 貫穿軸。"),
        ("Slide 30: 下週預告 (Preview Week 12 Innovation)", 
         "【課程預告】：預告 Week 12 主題：《社會創新、永續轉型與未來趨勢 (Social Innovation & Future Trends)》，說明 Homework 11 (2,000字) 作業與 AACSB 評分權重。")
    ]

    for title, text in slides_detail:
        p = doc.add_paragraph()
        r_t = p.add_run(f"📌 {title}\n")
        r_t.bold = True
        r_t.font.name = "Microsoft JhengHei"
        r_t.font.color.rgb = CYAN
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
        ("1. AI 應用分析 (AI Application Audit)", "25%", "完整介紹目標企業背景及其 AI 落地應用場景（如招募、客服、製程、風控）。"),
        ("2. AI 倫理與治理分析 (AI Ethics & Governance)", "30%", "深刻剖析該企業 AI 應用是否涉及演算法偏誤、隱私洩漏、智慧財產或黑箱風險。"),
        ("3. Responsible AI 架構應用 (Responsible AI Framework)", "25%", "精準對接公平、透明、可解釋、問責與隱私保護 5 大原則評估企業治理措施。"),
        ("4. 改善建議 (Managerial Recommendations)", "10%", "提出三項具備可行性與前瞻性的 Responsible AI 制度改善建議。"),
        ("5. 報告品質 (Report Quality)", "10%", "篇幅達 2,000 字左右，結構嚴謹，正確引用 AI 法規與案例資料。")
    ]

    for r_data in rubric_data:
        row_cells = table_rubric.add_row().cells
        for i, val in enumerate(r_data):
            row_cells[i].text = val
            for p_cell in row_cells[i].paragraphs:
                for r in p_cell.runs:
                    r.font.name = "Microsoft JhengHei"
                    r.font.size = Pt(9)

    doc.save(r"C:\Users\User\Desktop\第1週_企業為何需要倫理\第11週_AI與數位治理.docx")
    print("Successfully generated Week 11 Word .docx file!")

if __name__ == "__main__":
    generate_week11_word_guide()
