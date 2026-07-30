import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def generate_week2_word_guide():
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

    # Title
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_title = p_title.add_run("📘 企業倫理與永續經營 (Business Ethics and Sustainable Management)\n"
                              "第 2 週：道德理論與商業決策 —— 教師深度教學指引與授課手冊")
    r_title.font.name = "Microsoft JhengHei"
    r_title.font.size = Pt(20)
    r_title.font.bold = True
    r_title.font.color.rgb = DARK_BLUE

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_sub = p_sub.add_run("AACSB 商管學院認證標竿 • Utilitarianism, Deontology & Virtue Ethics • EMI 雙語教學")
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
            r.font.color.rgb = DARK_BLUE if level == 1 else TEAL
            r.font.bold = True
        return h

    # Section 1: Philosophy
    add_sec_heading("📌 一、第 2 週課程設計理念與 AACSB 能力指標 (Week 2 Philosophy & Competencies)")
    
    p = doc.add_paragraph()
    p.add_run("第 2 週主題為「道德理論與商業決策 (Ethical Theories and Business Decision Frameworks)」。"
              "本週核心任務為引導學生從第一週的「直覺式道德判斷」轉化為「系統化倫理理論剖析」，"
              "深入學習西方三大經典倫理理論：效益主義 (Utilitarianism)、義務論 (Deontology) 與德行倫理學 (Virtue Ethics)，"
              "並透過福特平托案 (Ford Pinto Cost-Benefit Case) 與嬌生泰諾爾案 (Johnson & Johnson Tylenol Crisis) 進行實戰對比。")

    # Section 2: Timeline
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
        ("00:00 - 00:15", "15m", "第一部分：道德決策模型\n(Ethical Decision Models)", "【Slide 1-5】複習第一週、介紹 4-Step 倫理決策模型、Kohlberg 6階段道德發展理論與「道德失明 (Ethical Blindspots)」。"),
        ("00:15 - 00:40", "25m", "第二部分：三大經典倫理理論\n(Three Ethical Theories)", "【Slide 6-11】深入效益主義 (Bentham/Mill)、康德義務論 (Kant Categorical Imperative) 與亞里斯多德德行倫理學 (Virtue Ethics) 比較矩陣。"),
        ("00:40 - 00:55", "15m", "【活動一】：電車問題商業版\n(Activity 1: Trolley Problem)", "【Slide 12-13】4人小組情境演練（AI 自駕車演算法在危急時刻的人命保護優先順序）、Mentimeter 歸零表決與哲學理論思辨。"),
        ("00:55 - 01:25", "30m", "第三部分：經典與前沿個案\n(Real-World Case Studies)", "【Slide 14-19】對比 Ford Pinto $11 零件成本效益分析慘劇 vs J&J Tylenol $1億完全召回典範，延伸大數據演算法歧視個案。"),
        ("01:25 - 01:45", "20m", "【活動二】：倫理矩陣實戰演練\n(Activity 2: Ethics Matrix)", "【Slide 20-21】小組抽籤演練藥品高價專利、演算法解僱與綠色洗腦案例，運用 3 大理論矩陣進行 3 分鐘 Pitch 發表。"),
        ("01:45 - 02:00", "15m", "第四部分：融入 ESG & 作業\n(Ethics to ESG & HW)", "【Slide 22-24】道德理論如何內化至 ESG G治理指標、本週 4 大 Takeaways 總結與 Homework 2 案例寫作指引。")
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

    # Section 3: 24 Slides Notes
    add_sec_heading("🗣️ 三、24 頁投影片逐頁深度授課指引 (Slide-by-Slide Instructional Notes)")

    slides_detail = [
        ("Slide 1: 課程封面 (Course Title & Cover)", 
         "【授課腳本】：「歡迎來到第 2 週《道德理論與商業決策》。本週我們將學習哲學史上最強大的三大倫理工具，幫助高階經理人在商業巨浪中做出禁得起考驗的決策。」"),
        ("Slide 2: W1 複習與 W2 目標 (Bridge & Objectives)", 
         "【授課腳本】：複習 W1 信任崩潰。本週目標：(1) 掌握效益主義、義務論、德行倫理學；(2) 識別商業運作中的道德盲點；(3) 運用倫理矩陣分析 Ford Pinto 與 J&J 個案。"),
        ("Slide 3: 4-Step 倫理決策模型 (4-Step Decision Model)", 
         "【授課腳本】：介紹 4 階段模型：(1) 識別道德問題 → (2) 形成倫理判斷 → (3) 建立道德意圖 → (4) 展現道德行為。"),
        ("Slide 4: Kohlberg 6 階段道德發展 (Kohlberg's 6 Stages)", 
         "【授課腳本】：說明柯爾堡三層級六階段：前慣習期 (避罰/功利) → 慣習期 (順從/法制) → 後慣習期 (社會契約/普世倫理)。企業多處於法制階段，倫理引導走向後慣習期。"),
        ("Slide 5: 道德失明與有限倫理 (Bounded Ethicality)", 
         "【授課腳本】：解析心理學「道德失明 (Ethical Blindspots)」：高壓目標、框架效應 (Framing Effect) 與漸進式道德滑坡 (Gradual Erosion)。"),
        ("Slide 6: 效益主義 (Utilitarianism - Bentham & Mill)", 
         "【授課腳本】：解析 Jeremy Bentham 與 J.S. Mill 的效益主義：行為善惡取決於「能否為最多數人創造最大效益 (The greatest happiness for the greatest number)」。"),
        ("Slide 7: 效益主義在商業中的代價 (Cost-Benefit Analysis Risks)", 
         "【授課指引】：討論成本效益分析 (CBA) 的局限：當人命、尊嚴與健康被折算為金錢數字時，效益主義可能導致嚴重人權忽視。"),
        ("Slide 8: 義務論 / 康德倫理学 (Deontology - Immanuel Kant)", 
         "【授課腳本】：解析康德的定言令式 (Categorical Imperative)：(1) 普遍化原則 (Universalizability)；(2) 尊重人為目的而非工具 (Treat humanity as an end, never merely as a means)。"),
        ("Slide 9: 義務論在商業中的應用 (Unconditional Duties)", 
         "【授課指引】：說明義務論在產品安全、個資隱私與勞工權益中的不可妥協性。道德責任是無條件的，不能因為損益而犧牲。"),
        ("Slide 10: 德行倫理學 (Virtue Ethics - Aristotle)", 
         "【授課腳本】：解析亞里斯多德德行倫理學：關注「我是什麼樣的人？(What kind of person should I be?)」。強調卓越品質 (Virtue)、中庸之道 (Golden Mean) 與領導誠信。"),
        ("Slide 11: 三大理論對照矩陣 (Theoretical Comparison Matrix)", 
         "【授課指引】：展示比較表：效益主義 (強調結果) vs. 義務論 (強調動機與法則) vs. 德行倫理 (強調人格與品質)。"),
        ("Slide 12: 活動一：電車問題商業版 (The Corporate Trolley Problem)", 
         "【活動執行】：4 人一組討論 10m。情境：AI 自駕車緊急時刻，演算法選擇保護車內高階乘客，或是衝向路上行人？效益主義 vs 義務論選擇。"),
        ("Slide 13: 活動一：即時線上表決與點評 (Live Class Poll)", 
         "【活動執行】：進行 0% 歸零即時投票，點評演算法倫理與企業設計者的責任歸屬。"),
        ("Slide 14: 案例一：福斯平托案 (Ford Pinto Case)", 
         "【案例剖析】：1970s Ford Pinto 油箱設計瑕疵事故。Ford 進行內部成本效益分析：$11 零件修正費 ($1.37億) vs 預估死亡傷殘賠償 ($4,950萬)。選擇不修正！"),
        ("Slide 15: Ford Pinto 判決與社會反彈 (Fatal $11 Part)", 
         "【案例剖析】：揭露信件後引爆全美憤怒，法院判定天價懲罰性賠償。冷酷的效益算計讓 Ford 品牌遭受滅頂打擊。"),
        ("Slide 16: 案例二：嬌生泰諾爾案 (J&J Tylenol 1982 Crisis)", 
         "【案例剖析】：1982 芝加哥泰諾爾毒藥事件（千分之三機率）。J&J 執行長 James Burke 依據公司信條 (Credo)，主動花費 1 億美元全面下架 3,100 萬瓶藥品，並發明安全防撕封條瓶蓋。"),
        ("Slide 17: J&J Credo 企業信條 (The Johnson & Johnson Credo)", 
         "【解析信條】：展示 J&J 創立於 1943 年的信條：責任順序第一為顧客/醫生/護理師，第二為員工，第三為社區，最後才是股東。"),
        ("Slide 18: Ford Pinto vs. J&J 比較矩陣 (Comparative Matrix)", 
         "【矩陣對比】： Ford (純效益主義金額試算) vs J&J (義務論與德行信條優先)。試算省下小錢造成品牌毀滅，誠信大動作則換來數十年消費者鐵粉。"),
        ("Slide 19: 當代前沿個案：演算法差別取價 (Algorithmic Discrimination)", 
         "【前沿討論】：大數據演算法動態定價是否違反康德的「將人視為目的而非工具」？討論訂票平台大數據殺熟與信用評分偏見。"),
        ("Slide 20: 活動二：倫理矩陣實戰演練 (Ethical Matrix Workshop)", 
         "【活動執行】：小組抽籤演練：(1) 抗癌藥品天價專利、(2) AI 演算法無預警解僱、(3) 綠色洗腦行銷。同時運用三大理論診斷。"),
        ("Slide 21: 活動二：發表與點評 (Team Pitch)", 
         "【活動執行】：各組 3 分鐘 Pitch。教師總結如何將哲學理論轉化為企業內部的倫理檢核表 (Checklist)。"),
        ("Slide 22: 道德理論融入 ESG 治理結構 (Integrating Ethics into ESG)", 
         "【貫穿藍圖】：效益主義 (E: 環境總影響) → 義務論 (S: 人權與勞工防線) → 德行倫理 (G: 董事會誠信文化)。"),
        ("Slide 23: Week 2 核心重點總結 (Key Takeaways)", 
         "【課程總結】：4 大 Takeaways：(1) 結果非唯一考量、(2) 人是目的而非工具、(3) 企業品德決定長遠價值、(4) 倫理理論是決策的羅盤。"),
        ("Slide 24: 本週課堂作業說明 (Homework 2 Guidelines)", 
         "【作業交代】：說明 Homework 2 (1,000–1,200 字) 案例寫作題目、三大理論運用規範與 AACSB Rubrics 評分矩陣。")
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

    # Section 4: Rubrics
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
        ("1. 個案事實 (Case Background)", "20%", "精準還原個案背景，客觀呈現代價金額與事實細節。", "事件描述模糊，缺乏數據與時間點佐證。"),
        ("2. 三大倫理理論運用 (Theoretical Rigor)", "30%", "靈活運用效益主義、義務論與德行倫理進行交叉診斷。", "僅使用單一理論或偏向常識性感想主觀評判。"),
        ("3. 管理與 CEO 解方 (Managerial Solution)", "30%", "提出兼具倫理防線與長遠 ESG 價值的可行性方案。", "方案空洞無效（如僅寫「道德宣導」）。"),
        ("4. 個人倫理反思 (Personal Reflection)", "20%", "展現深刻批判性思考與個人領導誠信的反思。", "篇幅不足，或直接複製網路摘要。")
    ]

    for r_data in rubric_data:
        row_cells = table_rubric.add_row().cells
        for i, val in enumerate(r_data):
            row_cells[i].text = val
            for p_cell in row_cells[i].paragraphs:
                for r in p_cell.runs:
                    r.font.name = "Microsoft JhengHei"
                    r.font.size = Pt(9)

    doc.save(r"C:\Users\User\Desktop\第1週_企業為何需要倫理\第2週_道德理論與商業決策.docx")
    print("Successfully generated Week 2 Word .docx file!")

if __name__ == "__main__":
    generate_week2_word_guide()
