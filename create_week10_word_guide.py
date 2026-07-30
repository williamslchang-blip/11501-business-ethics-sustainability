import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def generate_week10_word_guide():
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
                              "第 10 週：永續供應鏈管理與循環經濟 —— 教師深度教學指引與授課手冊")
    r_title.font.name = "Microsoft JhengHei"
    r_title.font.size = Pt(20)
    r_title.font.bold = True
    r_title.font.color.rgb = DARK_BLUE

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_sub = p_sub.add_run("AACSB / PRME / Harvard / MIT Sloan / INSEAD Standard • Scope 3 • Responsible Sourcing • 5 R's • Circular Business Canvas")
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
    add_sec_heading("📌 一、第 10 週課程設計理念與 AACSB 能力指標 (Week 10 Philosophy & Competencies)")
    
    p = doc.add_paragraph()
    p.add_run("第 10 週主題為「永續供應鏈管理與循環經濟 (Sustainable Supply Chain and Circular Economy)」。"
              "本週為整門課程從『概念與資本』邁向『實體企業營運與供應鏈策略』的關鍵實踐週！\n"
              "W1–W9 已完成 Ethics → CSR → ESG → E → S → G → Disclosure → Sustainable Finance 的理論與金融鏈結，W10 深入解答：『企業如何落實 70%–95% 的 Scope 3 供應鏈減碳？如何將線性經濟 (Take-Make-Waste) 轉型為循環商業模式？』"
              "本週結合 Harvard, MIT Sloan, INSEAD 與 Cambridge Judge 的授課框架，"
              "全面解析：負責任採購 (Responsible Sourcing)、供應商行為守則 (Supplier Code of Conduct)、Scope 3 減碳管理、循環經濟 5 R's (Reduce, Reuse, Repair, Recycle, Recover)、產品生命週期 LCA (Cradle-to-Cradle) 與 Product-as-a-Service 循環商業模式。")

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
        ("00:00 - 00:15", "15m", "Part 1：為什麼供應鏈決定ESG？\n(Why Supply Chain Matters?)", "【Slide 1-5】暖身問題（Apple 單靠自己能做 ESG 嗎？）、Apple 200+ 供應商地圖、Scope 3 佔 70%-95% 碳排現狀、Supply Chain 即企業真正的 ESG 防線。"),
        ("00:15 - 00:45", "30m", "Part 2：永續供應鏈管理\n(Sustainable Supply Chain)", "【Slide 6-13】Traditional vs Sustainable 比較表、Responsible Sourcing 負責任採購、Supplier Code of Conduct 稽核、人權保障、Scope 3 減碳管理、Apple 綠電輔導案例；【活動一】Supply Chain Risk Mapping 實戰 (Apple, Nike, TSMC, Starbucks, IKEA, Unilever)。"),
        ("00:45 - 01:15", "30m", "Part 3：循環經濟\n(Circular Economy)", "【Slide 16-22】Linear (Take-Make-Waste) vs Circular Economy 比較、5 R's 框架 (Reduce, Reuse, Repair, Recycle, Recover)、LCA 生命週期、Patagonia (Worn Wear)、IKEA (循環家具)、Nike Grind 標竿案例。"),
        ("01:15 - 01:45", "30m", "Part 4 & 【活動二】：循環商業模式\n(Circular Business Models)", "【Slide 23-27】Circular Business Models (Product-as-a-Service 產品即服務)、ESG 供應鏈藍圖；【活動二】Circular Business Design (為手機/球鞋/咖啡杯/寶特瓶/家具設計 Business Model Canvas)。"),
        ("01:45 - 02:00", "15m", "Part 5：W1-W10 總整與預告\n(Summary & HW10)", "【Slide 28】W1–W10 完整能力體系總整、W11 AI 與數位治理預告、Homework 10 (2,000字) 永續供應鏈分析報告交代與 5 大 AACSB 評分權重。")
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
        ("Slide 1: 課程封面 (Week 10 Sustainable Supply Chain)", 
         "【授課腳本】：「歡迎來到第 10 週《永續供應鏈管理與循環經濟》。本週我們將深入企業營運的核心：如何管理占企業 80% 以上碳排的 Scope 3 供應鏈，並打造循環商業模式！」"),
        ("Slide 2: 課程轉折與脈絡 (Course Journey)", 
         "【授課腳本】：展示進程：W1-9 概念/ESG/資本市場 → W10 企業實體營運策略 (Supply Chain & Circular Economy)。"),
        ("Slide 3: 暖身問題 (Apple Single Firm Dilemma)", 
         "【提問引導】：Apple 總部自己做到 100% 綠電，但如果全球 200+ 代工廠繼續用煤電，Apple 能算真正實現 Net Zero 嗎？引導體會 Scope 3 供應鏈的絕對關鍵性。"),
        ("Slide 4: Apple 全球供應鏈地圖與 Scope 3 現狀 (Scope 3 Dominance)", 
         "【授課腳本】：展示數據：Apple、Nike、TSMC 等國際巨擘 70%–95% 的總碳足跡來自範疇 3 (Scope 3) 供應鏈上下游。"),
        ("Slide 5: Supply Chain 就是企業真正的 ESG (Supply Chain is ESG)", 
         "【授課指引】：強調觀念：企業的 ESG 聲譽並不取決於總部寫了什麼報告，而是由其供應鏈中每一家代工廠的工安、人權與碳排所決定！"),
        ("Slide 6: Traditional vs. Sustainable Supply Chain 比較表", 
         "【授課對比】：\n"
         "• Traditional：線性成本導向、價低者得、忽略環境外部性。\n"
         "• Sustainable：循環韌性導向、ESG 合規稽核、透明合作與減碳共榮。"),
        ("Slide 7: Responsible Sourcing 負責任採購", 
         "【授課腳本】：介紹負責任採購：在採購決策中納入勞工權益、環境影響、在地農採與公平貿易標準。"),
        ("Slide 8: Supplier Code of Conduct 供應商行為守則", 
         "【授課腳本】：解析 Supplier Code of Conduct：強制要求供應商遵守最高工安、反強迫勞動、禁止童工與環保合規。"),
        ("Slide 9: Supplier Audit 供應商稽核與輔導", 
         "【授課指引】：說明無預警實地稽核機制，結合違規懲罰與技術輔導升級。"),
        ("Slide 10: Human Rights 供應鏈人權保障", 
         "【授課腳本】：強調保障供應鏈基層勞工權益，防範血汗工廠與違法超時加班。"),
        ("Slide 11: Carbon Footprint & Scope 3 減碳", 
         "【授課腳本】：輔導代工廠進行 ISO 14064 碳盤查與制定具體減碳時程。"),
        ("Slide 12: Scope 3 價值鏈管理策略", 
         "【授課指引】：透過綠色採購標準、綠電共購 (PPA) 協助供應商進行轉型。"),
        ("Slide 13: 標竿案例：Apple Supplier Clean Energy Program", 
         "【案例剖析】：Apple 提供技術與資金協助全球 200+ 供應商轉用 100% 綠電，成為全球供應鏈減碳標竿。"),
        ("Slide 14: 活動一：Supply Chain Risk Mapping 實戰", 
         "【活動執行】：4人一組，抽籤 Apple, Nike, TSMC, Starbucks, IKEA, Unilever，繪製原料→製造→物流→零售→回收流程，找出 3 大 ESG 風險。"),
        ("Slide 15: 活動一：各組分享與點評 (Class Debrief)", 
         "【活動點評】：點評：供應鏈風險不只是成本控制，更是企業永續營運的韌性來源。"),
        ("Slide 16: Linear Economy vs. Circular Economy", 
         "【授課腳本】：對比：線性經濟 Take-Make-Waste (開採-製造-廢棄) 造成資源枯竭；循環經濟則透過設計實現資源永久循環。"),
        ("Slide 17: Take-Make-Waste 線性模式的瓶頸", 
         "【授課指引】：剖析原物料價格暴漲、天價廢棄物處置費與各國反拋棄式塑膠法規對線性模式的致命打擊。"),
        ("Slide 18: 循環經濟 5 R's 框架", 
         "【授課腳本】：解析 5 R's：Reduce (減量)、Reuse (再利用)、Repair (維修)、Recycle (回收)、Recover (能源回收)。"),
        ("Slide 19: Product Life Cycle LCA 產品生命週期", 
         "【授課指引】：介紹 Cradle-to-Cradle (從搖籃到搖籃) 設計理念，從產品設計階段即考慮可回收性。"),
        ("Slide 20: 案例一：Patagonia 循環文化與 Worn Wear", 
         "【案例剖析】：Patagonia 推出 Worn Wear 舊衣維修與二手回收拍賣，喊出「Don't Buy This Jacket」，顛覆快時尚。"),
        ("Slide 21: 案例二：IKEA 循環家具與回收租賃", 
         "【案例剖析】：IKEA 承諾 2030 年前 100% 使用再生或可回收原料，推動家具租賃 (Furniture-as-a-Service) 與舊家具回購。"),
        ("Slide 22: 案例三：Nike Grind 廢料再生技術", 
         "【案例剖析】：Nike 收集鞋履製造邊角廢料與舊運動鞋，磨碎重製為 Nike Grind 材料，用於鋪設運動場跑道與新鞋。"),
        ("Slide 23: Circular Business Models 循環商業模式", 
         "【授課腳本】：介紹 Product-as-a-Service (產品即服務，只賣使用權不賣所有權)、資源回收再製造與生命週期延長。"),
        ("Slide 24: ESG 供應鏈策略藍圖", 
         "【授課指引】：整合供應商賦能、透明數據追溯與數位雙生技術。"),
        ("Slide 25: 活動二：Circular Business Design (循環商業設計)", 
         "【活動執行】：每組選擇智慧型手機、球鞋、咖啡杯、寶特瓶或家具，運用 Business Model Canvas 設計循環商業模式。"),
        ("Slide 26: 活動二：各組發表與點評 (Canvas Pitches)", 
         "【活動點評】：各組 5 分鐘 Pitch。教師點評兼顧成本、獲利與循環價值的商業可行性。"),
        ("Slide 27: 本週重點總結 (Supply Chain & Circular Summary)", 
         "【課程總結】：展示 Supply Chain → Circular Economy → Sustainable Advantage 策略鏈。"),
        ("Slide 28: 下週預告 (Preview Week 11 AI & Ethics)", 
         "【課程預告】：預告 Week 11 主題：《AI、數位治理與企業倫理 (AI, Digital Governance & Corporate Ethics)》，說明 Homework 10 (2,000字) 作業與 AACSB 評分權重。")
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
        ("1. 供應鏈分析 (Supply Chain Audit)", "30%", "完整分析目標企業背景、主要產品與全球供應鏈流程佈局。"),
        ("2. ESG 與 Scope 3 應用 (Scope 3 & Supplier ESG)", "25%", "精準分析 Scope 3 碳排管理、供應商行為守則、人權與稽核機制。"),
        ("3. 循環經濟分析 (Circular Economy Audit)", "20%", "深刻剖析該企業是否導入循環經濟設計、產品回收或再利用機制。"),
        ("4. 改善建議 (Managerial Recommendations)", "15%", "提出三項具備可行性與商業價值的永續供應鏈提升建議。"),
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

    doc.save(r"C:\Users\User\Desktop\第1週_企業為何需要倫理\第10週_永續供應鏈與循環經濟.docx")
    print("Successfully generated Week 10 Word .docx file!")

if __name__ == "__main__":
    generate_week10_word_guide()
