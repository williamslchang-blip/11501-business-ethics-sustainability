import sys

html_week9 = """<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Week 9: Sustainable Finance & ESG Investing | 永續金融與ESG投資</title>
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&family=Noto+Sans+TC:wght@300;400;500;700;900&family=Outfit:wght@400;600;800&display=swap" rel="stylesheet">
    <!-- FontAwesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="index.css">
</head>
<body class="canva-theme dark-mode lang-zh">

    <!-- Canva Top Header Navigation Bar -->
    <header class="canva-header">
        <div class="header-left">
            <div class="brand-logo">
                <i class="fa-solid fa-graduation-cap glow-icon"></i>
                <span class="brand-title">AACSB / ESG Series</span>
            </div>
            <div class="deck-title-container">
                <h1 class="deck-title">Week 9: Sustainable Finance and ESG Investing</h1>
                <span class="badge emi-badge"><i class="fa-solid fa-globe"></i> EMI Course</span>
                <span class="badge esg-badge"><i class="fa-solid fa-leaf"></i> ESG Aligned</span>
            </div>
        </div>
        <div class="header-right">
            <button class="btn btn-secondary" id="langToggleBtn" title="Switch Language (中/EN)">
                <i class="fa-solid fa-language"></i> <span id="langDisplay">中 / EN</span>
            </button>
            <button class="btn btn-secondary" id="timerBtn" title="Lecture Timer">
                <i class="fa-regular fa-clock"></i> <span id="timerDisplay">110:00</span>
            </button>
            <a href="第9週_永續金融與ESG投資.docx" download class="btn btn-secondary" title="Download Teaching Facilitation Guide (.docx)">
                <i class="fa-regular fa-bookmark"></i> <span class="lang-zh">教學指引</span><span class="lang-en">Facilitation Guide</span>
            </a>
            <button class="btn btn-secondary" id="gridToggleBtn" title="Slide Overview (Press G)">
                <i class="fa-solid fa-table-cells"></i> <span class="lang-zh">總覽</span><span class="lang-en">Overview</span>
            </button>
            <button class="btn btn-primary" id="presentBtn" title="Full Screen Presentation (Press F)">
                <i class="fa-solid fa-play"></i> <span class="lang-zh">播放簡報</span><span class="lang-en">Present</span>
            </button>
        </div>
    </header>

    <!-- Main Presentation Workspace -->
    <div class="canva-workspace">

        <!-- Slide Stage Area -->
        <main class="slide-stage" id="slideStage">
            
            <!-- SLIDE 1: Cover -->
            <section class="slide active" id="slide-1" data-title="Slide 1: 課程封面">
                <div class="slide-bg-overlay"></div>
                <div class="slide-container cover-layout">
                    <div class="cover-content">
                        <div class="course-meta">
                            <span class="meta-tag">Master of Business Administration / AACSB Standard</span>
                            <span class="meta-tag alt">Week 09 • Sustainable Finance Presentation</span>
                        </div>
                        <h1 class="main-heading">
                            <span class="lang-zh">永續金融與 ESG 投資</span>
                            <span class="lang-en">Sustainable Finance & ESG Investing</span>
                        </h1>
                        <h2 class="sub-heading">
                            <span class="lang-zh">Sustainable Finance and ESG Investing</span>
                            <span class="lang-en">Sustainable Finance and ESG Investing</span>
                        </h2>
                        <p class="lead-text">
                            <span class="lang-zh">UN PRI 責任投資、綠色債券 (Green Bonds)、SLL 貸款、MSCI 評等分歧與資本市場動能</span>
                            <span class="lang-en">UN PRI Principles, Green Bonds, SLL Loans, Rating Divergence, and Capital Market Dynamics</span>
                        </p>
                        
                        <div class="cover-footer">
                            <div class="instructor-info">
                                <i class="fa-solid fa-chalkboard-user"></i> 
                                <span class="lang-zh">授課教授：商學院 企業管理學系 教授群</span>
                                <span class="lang-en">Instructor: Department of Business Administration Faculty</span>
                            </div>
                            <div class="time-info">
                                <i class="fa-regular fa-calendar-check"></i> 
                                <span class="lang-zh">上課時間：2 小時 (120 分鐘)</span>
                                <span class="lang-en">Lecture Duration: 2 Hours (120 Mins)</span>
                            </div>
                        </div>
                    </div>
                    <div class="cover-visual">
                        <div class="glass-card visual-card">
                            <img src="week9_finance_cover.jpg" alt="Week 9 Cover Visual" class="slide-img">
                            <div class="visual-badge">
                                <i class="fa-solid fa-coins"></i> PRI • Green Bonds • MSCI Rating
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 2: Evolution Thread -->
            <section class="slide" id="slide-2" data-title="Slide 2: 課程邏輯主線">
                <div class="slide-container center-header-layout">
                    <div class="header-block center-text">
                        <div class="section-tag"><i class="fa-solid fa-diagram-project"></i> Course Journey</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">課程邏輯主線：從企業管理邁向金融資本市場</span>
                            <span class="lang-en">Course Journey: Shifting from Firm Management to Capital Markets</span>
                        </h2>
                    </div>

                    <div class="evolution-chain-card glass-card">
                        <div class="chain-items">
                            <div class="c-node"><div class="c-icon"><i class="fa-solid fa-heart"></i></div><h4>W1-3 Ethics/CSR</h4><p><span class="lang-zh">倫理基因</span><span class="lang-en">Ethics & CSR</span></p></div>
                            <div class="c-connector"><i class="fa-solid fa-arrow-right-long"></i></div>
                            <div class="c-node"><div class="c-icon"><i class="fa-solid fa-chart-pie"></i></div><h4>W4-7 ESG (E/S/G)</h4><p><span class="lang-zh">三大構面</span><span class="lang-en">ESG Pillars</span></p></div>
                            <div class="c-connector"><i class="fa-solid fa-arrow-right-long"></i></div>
                            <div class="c-node"><div class="c-icon"><i class="fa-solid fa-file-contract"></i></div><h4>W8 Disclosure</h4><p><span class="lang-zh">永續報告揭露</span><span class="lang-en">ESG Reporting</span></p></div>
                            <div class="c-connector"><i class="fa-solid fa-arrow-right-long"></i></div>
                            <div class="c-node highlight-node"><div class="c-icon"><i class="fa-solid fa-landmark"></i></div><h4>W9 Today</h4><p><span class="lang-zh">Sustainable Finance<br>(永續金融與ESG投資)</span><span class="lang-en">Sustainable Finance<br>(Capital Markets Drive)</span></p></div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 3: Warm-up Question -->
            <section class="slide" id="slide-3" data-title="Slide 3: 暖身問題 - 相同 EPS 投哪家？">
                <div class="slide-container center-header-layout">
                    <div class="header-block center-text">
                        <div class="section-tag warning-tag"><i class="fa-solid fa-sack-dollar"></i> Investor Choice</div>
                        <h2 class="slide-heading giant-title">
                            <span class="lang-zh">暖身問題：如果兩家公司 EPS 完全相同，你投哪一家？</span>
                            <span class="lang-en">Warm-up: If 2 Firms Have Identical EPS, Which Do You Pick?</span>
                        </h2>
                    </div>

                    <div class="dilemma-box glass-card glow-card">
                        <div class="dilemma-statement">
                            <p class="quote-text">
                                <span class="lang-zh">「傳統金融只看歷史 EPS；永續金融則評估未來 10 年的氣候風險、碳稅威脅與治理漏洞。<strong>ESG 不是取代財務分析，而是評估企業長期風險與隱形估值的核心補充！</strong>」</span>
                                <span class="lang-en">"ESG does not replace financial analysis; it evaluates long-term tail risks and invisible value!"</span>
                            </p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 4: BlackRock Larry Fink Letter -->
            <section class="slide" id="slide-4" data-title="Slide 4: BlackRock 執行長公開信">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag warning-tag"><i class="fa-solid fa-envelope-open-text"></i> BlackRock Mandate</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">BlackRock 執行長 Larry Fink 致 CEO 公開信</span>
                            <span class="lang-en">Larry Fink's Annual Letter to CEOs</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-quote-left accent-icon"></i> <span class="lang-zh">「氣候風險即是投資風險！」</span><span class="lang-en">"Climate Risk is Investment Risk!"</span></h3>
                            <p><span class="lang-zh">掌管超過 10 兆美元的全球最大資產管理巨擘 BlackRock 宣告：全面將 ESG 風險納入投資組合，對忽視氣候轉型的企業董事會投票反對或撤資！</span>
                            <span class="lang-en">Managing $10T+ AUM, BlackRock mandates ESG integration and threatens divestment for climate-negligent firms.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 5: Sustainable Finance Definition -->
            <section class="slide" id="slide-5" data-title="Slide 5: Sustainable Finance 定義">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-landmark"></i> Part I • Sustainable Finance</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">什麼是 Sustainable Finance (永續金融)？</span>
                            <span class="lang-en">What is Sustainable Finance?</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-money-bill-trend-up accent-icon"></i> <span class="lang-zh">將 E、S、G 標準整合至金融服務與資本配置</span><span class="lang-en">Integrating ESG Criteria into Capital Allocation</span></h3>
                            <p><span class="lang-zh">永續金融是指銀行、基金、保險與證券在進行投資、放款、承銷與保險決策時，全面納入環境、社會與治理標準，引導資本投入永續轉型。</span>
                            <span class="lang-en">Financial activities steering capital towards sustainable projects by integrating ESG criteria into lending and investment.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 6: Responsible Investment -->
            <section class="slide" id="slide-6" data-title="Slide 6: 責任投資 (PRI)">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-handshake"></i> Part II • ESG Investing</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">責任投資 (Responsible Investment)</span>
                            <span class="lang-en">Responsible Investment (PRI)</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-shield-halved accent-icon"></i> <span class="lang-zh">兼顧財務回報與利害關係人長遠福祉</span><span class="lang-en">Balancing Returns & Stakeholder Well-being</span></h3>
                            <p><span class="lang-zh">投資人在尋求長期競爭力財務回報的同時，承諾將 ESG 風險與社會影響力系統化納入資產管理決策中。</span>
                            <span class="lang-en">An approach to investing that aims to incorporate ESG factors into investment decisions to manage risk.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 7: UN PRI 6 Principles -->
            <section class="slide" id="slide-7" data-title="Slide 7: 聯合國 PRI 6 大原則">
                <div class="slide-container center-header-layout">
                    <div class="header-block center-text">
                        <div class="section-tag"><i class="fa-solid fa-list-check"></i> UN PRI Framework</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">聯合國責任投資 6 大原則 (UN PRI)</span>
                            <span class="lang-en">UN Principles for Responsible Investment</span>
                        </h2>
                    </div>

                    <div class="cards-grid-3x2 mt-3">
                        <div class="rc-card glass-card"><h4>1. Incorporation</h4><p><span class="lang-zh">將 ESG 納入投資分析與決策</span><span class="lang-en">Incorporate ESG into analysis</span></p></div>
                        <div class="rc-card glass-card"><h4>2. Active Owner</h4><p><span class="lang-zh">成為積極股東，將 ESG 納入政策</span><span class="lang-en">Active ownership & voting</span></p></div>
                        <div class="rc-card glass-card"><h4>3. Disclosure</h4><p><span class="lang-zh">要求被投資企業適當揭露 ESG</span><span class="lang-en">Seek ESG disclosure by firms</span></p></div>
                        <div class="rc-card glass-card"><h4>4. Adoption</h4><p><span class="lang-zh">推動投資產業普遍採行 PRI</span><span class="lang-en">Promote PRI adoption</span></p></div>
                        <div class="rc-card glass-card"><h4>5. Effectiveness</h4><p><span class="lang-zh">合作提升 PRI 執行有效性</span><span class="lang-en">Enhance effectiveness</span></p></div>
                        <div class="rc-card glass-card"><h4>6. Reporting</h4><p><span class="lang-zh">定期報導責任投資執行進度</span><span class="lang-en">Report progress on PRI</span></p></div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 8: ESG Integration -->
            <section class="slide" id="slide-8" data-title="Slide 8: ESG Integration 整合">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-chart-line"></i> Strategy 1 • Integration</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">策略 1：ESG Integration (ESG 整合)</span>
                            <span class="lang-en">ESG Integration Strategy</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-calculator accent-icon"></i> <span class="lang-zh">將 ESG 風險系統化調整現金流與折現率</span><span class="lang-en">Adjusting Cash Flows & Discount Rates</span></h3>
                            <p><span class="lang-zh">最主流的投資策略：基金經理人將碳費、工安處罰與治理爭議直接反映在企業財務 DCF 估值模型的 WACC 資本成本與折現率中！</span>
                            <span class="lang-en">Systematically incorporating ESG factors into traditional valuation models (DCF/WACC).</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 9: Negative Screening -->
            <section class="slide" id="slide-9" data-title="Slide 9: Negative Screening 負向排除">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag warning-tag"><i class="fa-solid fa-ban"></i> Strategy 2 • Exclusion</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">策略 2：Negative Screening (負向排除)</span>
                            <span class="lang-en">Negative Screening / Exclusion</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-filter-circle-xmark red-text"></i> <span class="lang-zh">全面排除軍火、菸草、賭博與高排碳煤炭</span><span class="lang-en">Excluding Weapons, Tobacco, and Coal</span></h3>
                            <p><span class="lang-zh">依據道德價值或法規規範，直接將爭議性產業（軍火製造、菸草、博弈、燃煤發電比率過高者）自可投資黑名單中刪除。</span>
                            <span class="lang-en">Excluding specific sectors or companies based on moral or environmental criteria (e.g. thermal coal).</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 10: Positive Screening -->
            <section class="slide" id="slide-10" data-title="Slide 10: Positive Screening 正向篩選">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-thumbs-up"></i> Strategy 3 • Best-in-Class</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">策略 3：Positive Screening (正向篩選)</span>
                            <span class="lang-en">Positive Screening (Best-in-Class)</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-award accent-icon"></i> <span class="lang-zh">同業比較中挑選 ESG 評級前 20% 領先企業</span><span class="lang-en">Selecting Top 20% Performers in Sector</span></h3>
                            <p><span class="lang-zh">最佳同業法 (Best-in-Class)：在特定產業內，優先購買 ESG 評級最高、風險管理最扎實的前 20% 標竿企業股票。</span>
                            <span class="lang-en">Investing in companies that perform better on ESG metrics relative to industry peers.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 11: Impact Investing -->
            <section class="slide" id="slide-11" data-title="Slide 11: Impact Investing 影響力投資">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-hand-holding-heart"></i> Strategy 4 • Impact</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">策略 4：Impact Investing (影響力投資)</span>
                            <span class="lang-en">Impact Investing Strategy</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-bullseye accent-icon"></i> <span class="lang-zh">追求財務回報的同時创造可量化社會效益</span><span class="lang-en">Generating Measurable Social/Environmental Benefits</span></h3>
                            <p><span class="lang-zh">明確鎖定具備特定永續專案的企業或基金（如平價住宅、綠色科技、偏鄉醫療），要求定期報導可量化的社會/環境影響力成果。</span>
                            <span class="lang-en">Investments made with the intention to generate positive, measurable social and environmental impact.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 12: Stewardship & Engagement -->
            <section class="slide" id="slide-12" data-title="Slide 12: Stewardship 股東參與">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-users-gear"></i> Strategy 5 • Stewardship</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">策略 5：Stewardship & Engagement (股東參與)</span>
                            <span class="lang-en">Stewardship & Shareholder Engagement</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-comments accent-icon"></i> <span class="lang-zh">行使投票權與高層對話督促企業轉型</span><span class="lang-en">Active Dialogue & Proxy Voting</span></h3>
                            <p><span class="lang-zh">不輕易賣出股票，而是透過大股東身份與被投資公司高層對話、提出股東案與行使投票權 (Proxy Voting)，直接推動企業減碳。</span>
                            <span class="lang-en">Engaging with corporate boards and voting at AGMs to actively influence corporate behavior towards sustainability.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 13: Activity 1 - ESG Investment Challenge -->
            <section class="slide" id="slide-13" data-title="Slide 13: 活動一 - 你會投資誰？">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag activity-tag"><i class="fa-solid fa-gamepad"></i> Activity 1 • 15 Minutes</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">ESG Investment Challenge</span>
                            <span class="lang-en">ESG Investment Challenge</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="scenario-card glass-card highlight-border">
                            <h3><span class="lang-zh">任務：比較下列 5 家公司的財務與 ESG Rating，決定投資</span><span class="lang-en">Pick 1 Firm Based on Financials & ESG</span></h3>
                            <div class="cards-grid-5 mt-3">
                                <div class="opt-choice"><p>TSMC</p></div>
                                <div class="opt-choice"><p>Apple</p></div>
                                <div class="opt-choice"><p>Tesla</p></div>
                                <div class="opt-choice"><p>Coca-Cola</p></div>
                                <div class="opt-choice"><p>ExxonMobil</p></div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 14: Activity 1 - Debrief -->
            <section class="slide" id="slide-14" data-title="Slide 14: 活動一 - 答案與點評">
                <div class="slide-container center-header-layout">
                    <div class="header-block center-text">
                        <div class="section-tag activity-tag"><i class="fa-solid fa-comments"></i> Class Debrief</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">ESG 不是取代財務，而是風險補充</span>
                            <span class="lang-en">Activity 1: ESG Complements Financials</span>
                        </h2>
                    </div>

                    <div class="debrief-box glass-card glow-card">
                        <i class="fa-solid fa-lightbulb debrief-icon"></i>
                        <div class="debrief-content">
                            <h4><span class="lang-zh">教師觀點帶出 (Key Takeaway)：</span><span class="lang-en">Faculty Debrief:</span></h4>
                            <p><span class="lang-zh">「ExxonMobil 當前 EPS 很高，但面臨巨大的長線碳轉型風險；Tesla 成長率高但治理 (G) 爭議不斷。ESG 提供的是長線防護罩！」</span>
                            <span class="lang-en">"ExxonMobil has strong current EPS but high carbon risk; Tesla has high growth but G controversy. ESG acts as a tail-risk shield!"</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 15: Green Finance Concept -->
            <section class="slide" id="slide-15" data-title="Slide 15: 綠色金融 Green Finance">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-seedling"></i> Part III • Green Finance</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">綠色金融 (Green Finance) 體系</span>
                            <span class="lang-en">The Green Finance Ecosystem</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-money-bill-wave accent-icon"></i> <span class="lang-zh">驅動資本投入環保、綠能與減碳科技</span><span class="lang-en">Directing Capital into Climate Solutions</span></h3>
                            <p><span class="lang-zh">綠色金融涵蓋綠色債券 (Green Bonds)、綠色授信貸款、永續指數 ETF 與氣候衍生性金融商品，為淨零轉型提供龐大資金。</span>
                            <span class="lang-en">Financial products dedicated to environmental projects, renewable energy, and low-carbon infrastructure.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 16: Green Bonds -->
            <section class="slide" id="slide-16" data-title="Slide 16: Green Bonds 綠色債券">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-file-invoice-dollar"></i> Green Debt</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">Green Bonds (綠色債券與 GBP 原則)</span>
                            <span class="lang-en">Green Bonds & ICMA GBP Principles</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-stamp accent-icon"></i> <span class="lang-zh">發行資金 100% 專款專用於綠色減碳專案</span><span class="lang-en">100% Use of Proceeds Dedicated to Eco-Projects</span></h3>
                            <p><span class="lang-zh">依據 ICMA 綠色債券原則 (GBP)，綠色債券募得資金必須 100% 用於太陽能/風電、綠建築或資源回收專案，並定期發表資金追蹤報告。</span>
                            <span class="lang-en">Bonds where 100% of proceeds are earmarked exclusively for certified green projects.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 17: SLL & Transition Finance -->
            <section class="slide" id="slide-17" data-title="Slide 17: SLL 貸款與轉型金融">
                <div class="slide-container center-header-layout">
                    <div class="header-block center-text">
                        <div class="section-tag"><i class="fa-solid fa-link"></i> Innovative Instruments</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">SLL 永續連結貸款與 Transition Finance (轉型金融)</span>
                            <span class="lang-en">Sustainability-Linked Loans & Transition Finance</span>
                        </h2>
                    </div>

                    <div class="grid-2col gap-4 mt-3">
                        <div class="theory-card glass-card">
                            <div class="theory-header"><h3>SLL (永續連結貸款)</h3></div>
                            <p class="mt-2"><span class="lang-zh">銀行貸款利率與企業 ESG KPI 達成率掛鉤，達標者可享受優惠降息優惠。</span><span class="lang-en">Loan interest rates tied directly to corporate ESG KPI achievements.</span></p>
                        </div>
                        <div class="theory-card glass-card highlight-card">
                            <div class="theory-header"><h3>Transition Finance (轉型金融)</h3></div>
                            <p class="mt-2"><span class="lang-zh">專門融資給高碳排傳統產業（如鋼鐵、水泥），資助其導入低碳轉型技術。</span><span class="lang-en">Financing high-carbon sectors to transition towards net-zero technology.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 18: ESG ETFs -->
            <section class="slide" id="slide-18" data-title="Slide 18: ESG ETF 與被動投資">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-chart-pie"></i> Passive Investing</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">ESG ETFs 與指數型基金</span>
                            <span class="lang-en">ESG ETFs & Passive Index Funds</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-arrow-trend-up accent-icon"></i> <span class="lang-zh">追蹤 MSCI ESG Leaders 與 S&P ESG 指數</span><span class="lang-en">Tracking MSCI & S&P ESG Benchmarks</span></h3>
                            <p><span class="lang-zh">全球散戶與機構法人透過買進 ESG ETF 被動基金，自動將資金分配至 ESG 高評級企業，帶動高評級股價表現。</span>
                            <span class="lang-en">Passive funds tracking ESG indexes channel retail and institutional capital directly into high-rated ESG leaders.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 19: BlackRock Case -->
            <section class="slide" id="slide-19" data-title="Slide 19: BlackRock 案例">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-building"></i> Case Audit • BlackRock</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">BlackRock 永續投資與股東投票</span>
                            <span class="lang-en">BlackRock Sustainable Investing Practice</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-vote-yea accent-icon"></i> <span class="lang-zh">發起 Engine No. 1 投票改組 ExxonMobil 董事會</span><span class="lang-en">Supporting Board Room Climate Reform</span></h3>
                            <p><span class="lang-zh">BlackRock 支持對衝基金 Engine No. 1，成功在 ExxonMobil 股東大會中爭取 3 席具氣候背景的獨立董事，強制老牌油企轉型！</span>
                            <span class="lang-en">BlackRock backed activist fund Engine No. 1 to replace 3 board seats at ExxonMobil with climate experts.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 20: Taiwan Policy -->
            <section class="slide" id="slide-20" data-title="Slide 20: 台灣綠色金融 3.0">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-flag"></i> Taiwan Policy</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">台灣金管會綠色金融 3.0 政策</span>
                            <span class="lang-en">Taiwan FSC Green Finance 3.0</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-gavel accent-icon"></i> <span class="lang-zh">強制要求金融機構進行氣候壓力測試</span><span class="lang-en">Mandating Climate Stress Tests for Banks</span></h3>
                            <p><span class="lang-zh">台灣金管會推動綠色金融 3.0：要求國泰、玉山等金融機構完成投融資範疇 3 碳盤查，並進行極端氣候壓力測試。</span>
                            <span class="lang-en">FSC mandates carbon accounting for bank portfolios and climate stress testing across financial institutions.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 21: MSCI ESG Rating Scale -->
            <section class="slide" id="slide-21" data-title="Slide 21: MSCI ESG 評級架構">
                <div class="slide-container center-header-layout">
                    <div class="header-block center-text">
                        <div class="section-tag"><i class="fa-solid fa-chart-bar"></i> Part IV • Ratings & Empirical</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">MSCI ESG Rating 評級架構 (AAA to CCC)</span>
                            <span class="lang-en">MSCI ESG Rating Tiers (AAA to CCC)</span>
                        </h2>
                    </div>

                    <div class="rubrics-bar mt-3">
                        <div class="r-seg seg-1" style="width: 30%;">AAA / AA (Leaders)</div>
                        <div class="r-seg seg-2" style="width: 40%;">A / BBB / BB (Average)</div>
                        <div class="r-seg seg-4" style="width: 30%;">B / CCC (Laggards)</div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 22: Rating Divergence -->
            <section class="slide" id="slide-22" data-title="Slide 22: 評等分歧 Rating Divergence">
                <div class="slide-container center-header-layout">
                    <div class="header-block center-text">
                        <div class="section-tag warning-tag"><i class="fa-solid fa-triangle-exclamation"></i> AACSB Advanced Topic</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">評等分歧 (Rating Divergence: MIT 聚合混淆)</span>
                            <span class="lang-en">Rating Divergence: MIT Aggregate Confusion</span>
                        </h2>
                    </div>

                    <div class="debrief-box glass-card glow-card mt-3">
                        <i class="fa-solid fa-code-fork debrief-icon"></i>
                        <div class="debrief-content">
                            <h4><span class="lang-zh">為何不同評等機構給出截然不同的分數？</span><span class="lang-en">Why Ratings Diverge Across Agencies?</span></h4>
                            <p><span class="lang-zh">MIT Sloan 著名研究《Aggregate Confusion》指出：MSCI, Sustainalytics, Refinitiv 等機構對同一家公司的評級相關係數僅 0.61（傳統信用評級為 0.99）！原因在於：範疇定義 (Scope)、權重配置 (Weighting) 與衡量方法 (Measurement) 差異極大！</span>
                            <span class="lang-en">MIT study shows ESG rating correlation is only 0.61 due to differing scopes, weightings, and metrics.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 23: Empirical Research -->
            <section class="slide" id="slide-23" data-title="Slide 23: ESG 是否提升財務績效？">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-chart-line"></i> Academic Empirical Data</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">ESG 是否提升財務績效？實證研究</span>
                            <span class="lang-en">Does ESG Boost Financial Performance?</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-shield-cat accent-icon"></i> <span class="lang-zh">降低資本成本 (Cost of Capital) 與尾端風險</span><span class="lang-en">Lowering Cost of Capital & Tail Risk</span></h3>
                            <p><span class="lang-zh">全球實證研究顯示：高 ESG 評級企業不一定創造暴利超額 Alpha，但能顯著降低 WACC 資本成本、債務違約率與暴跌尾端風險 (Tail Risk)！</span>
                            <span class="lang-en">Empirical data proves high ESG firms enjoy lower cost of capital and significantly reduced tail risk during crises.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 24: Fund Mislabeling & SFDR -->
            <section class="slide" id="slide-24" data-title="Slide 24: 基金防漂綠：歐盟 SFDR">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag warning-tag"><i class="fa-solid fa-gavel"></i> EU SFDR Regulation</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">基金防漂綠規範：歐盟 SFDR 分類</span>
                            <span class="lang-en">EU SFDR Anti-Greenwashing Rules</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="grid-3col gap-3">
                            <div class="info-box glass-card"><h4>Article 6</h4><p><span class="lang-zh">一般傳統基金（無特定 ESG 訴求）</span><span class="lang-en">General mainstream funds</span></p></div>
                            <div class="info-box glass-card"><h4>Article 8</h4><p><span class="lang-zh">促進 ESG 特性基金 (淺綠基金)</span><span class="lang-en">Promoting ESG features</span></p></div>
                            <div class="info-box glass-card"><h4>Article 9</h4><p><span class="lang-zh">具備明確永續目標基金 (深綠基金)</span><span class="lang-en">Dark green sustainable goal</span></p></div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 25: Activity 2 - Build ESG Portfolio -->
            <section class="slide" id="slide-25" data-title="Slide 25: 活動二 - 打造 ESG 組合">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag activity-tag"><i class="fa-solid fa-wallet"></i> Activity 2 • 15 Minutes</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">Build Your ESG Portfolio</span>
                            <span class="lang-en">Build Your ESG Portfolio</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="scenario-card glass-card highlight-border">
                            <h3><span class="lang-zh">任務：用 1,000 萬虛擬資金建構 ESG 投資組合</span><span class="lang-en">Construct a $10M NTD ESG Portfolio</span></h3>
                            <p><span class="lang-zh">從 10 家企業中挑選，限制：至少跨 3 產業、至少 1 家高 ESG Rating，並評估可能面臨的氣候/治理風險與權重分配。</span>
                            <span class="lang-en">Pick from 10 firms, across 3 sectors, featuring at least 1 top ESG rating firm, explaining risk mitigation.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 26: Activity 2 - Team Pitches -->
            <section class="slide" id="slide-26" data-title="Slide 26: 活動二 - 各組簡報">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag activity-tag"><i class="fa-solid fa-microphone"></i> Team Pitches</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">各組 5 分鐘 Pitch 與風險控管辯論</span>
                            <span class="lang-en">5-Min Pitches & Risk Debate</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-check-double accent-icon"></i> <span class="lang-zh">教師點評：平衡 Alpha 回報與 ESG 防禦</span><span class="lang-en">Balancing Alpha & ESG Defense</span></h3>
                            <p><span class="lang-zh">點評各組配置：純高評級組合獲利穩定但成長可能受限；適度搭配低碳轉型企業（Transition Finance）能兼顧高成長與永續價值！</span>
                            <span class="lang-en">Evaluating portfolio tradeoffs: Pure AAA portfolios offer stability, while adding transition firms captures growth.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 27: Summary -->
            <section class="slide" id="slide-27" data-title="Slide 27: 本週重點總結">
                <div class="slide-container center-header-layout">
                    <div class="header-block center-text">
                        <div class="section-tag"><i class="fa-solid fa-bookmark"></i> Part V • Summary</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">Week 9 核心重點總結</span>
                            <span class="lang-en">Week 9 Key Takeaways</span>
                        </h2>
                    </div>

                    <div class="takeaways-grid-4">
                        <div class="t-card glass-card">
                            <div class="t-number">01</div>
                            <h3><span class="lang-zh">資本市場倒逼 ESG</span><span class="lang-en">1. Capital Market Drive</span></h3>
                            <p><span class="lang-zh">永續金融透過幾十兆資產直接重塑企業決策與融資成本。</span><span class="lang-en">Trillions of capital reshape corporate decisions via cost of capital.</span></p>
                        </div>
                        <div class="t-card glass-card">
                            <div class="t-number">02</div>
                            <h3><span class="lang-zh">UN PRI 5 大策略</span><span class="lang-en">2. PRI 5 Strategies</span></h3>
                            <p><span class="lang-zh">從 ESG Integration 到負向/正向篩選、影響力投資與股東參與。</span><span class="lang-en">Ranging from ESG Integration to Screening and Stewardship.</span></p>
                        </div>
                        <div class="t-card glass-card">
                            <div class="t-number">03</div>
                            <h3><span class="lang-zh">綠色金融商品創新</span><span class="lang-en">3. Green Instruments</span></h3>
                            <p><span class="lang-zh">綠色債券 (Green Bonds)、SLL 貸款與轉型金融引導資金。</span><span class="lang-en">Green Bonds and SLL loans channeling transition funds.</span></p>
                        </div>
                        <div class="t-card glass-card">
                            <div class="t-number">04</div>
                            <h3><span class="lang-zh">Rating 分歧與尾端防禦</span><span class="lang-en">4. Divergence & Defense</span></h3>
                            <p><span class="lang-zh">理解評等分歧本質，利用 ESG 防禦營運尾端崩盤風險。</span><span class="lang-en">Understanding rating divergence and hedging tail risks.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 28: Preview W10 & Homework 9 -->
            <section class="slide" id="slide-28" data-title="Slide 28: Preview W10 & Homework 9">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag homework-tag"><i class="fa-solid fa-forward"></i> Preview W10 & HW9</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">W10 預告與 Homework 9</span>
                            <span class="lang-en">W10 Preview & Homework 9</span>
                        </h2>
                    </div>

                    <div class="main-panel">
                        <div class="glass-card feature-card mb-2">
                            <h3><i class="fa-solid fa-truck-ramp-box accent-icon"></i> <span class="lang-zh">W10 預告：永續供應鏈與循環經濟</span><span class="lang-en">W10 Preview: Sustainable Supply Chain</span></h3>
                            <p class="mb-2"><span class="lang-zh">下一週我們將探討《永續供應鏈與循環經濟 (Sustainable Supply Chain & Circular Economy)》！</span><span class="lang-en">Next week we dive into Sustainable Supply Chain & Circular Economy!</span></p>
                        </div>

                        <div class="glass-card feature-card mb-2">
                            <h3><i class="fa-solid fa-file-invoice accent-icon"></i> <span class="lang-zh">Homework 9：ESG 投資分析報告 (約 2,000 字)</span><span class="lang-en">Homework 9: ESG Investment Report (~2,000w)</span></h3>
                            <p><span class="lang-zh">選擇一家上市公司：分析概況、ESG 表現與優勢、投資判斷（是否值得持有、ESG 風險）與兩項改善建議。</span>
                            <span class="lang-en">Audit a listed firm: company profile, ESG performance, investment thesis (risks/value), and 2 recommendations.</span></p>
                        </div>

                        <div class="glass-card rubrics-card">
                            <h4><i class="fa-solid fa-chart-bar accent-icon"></i> AACSB <span class="lang-zh">評分標準</span><span class="lang-en">Rubrics Breakdown</span></h4>
                            <div class="rubrics-bar">
                                <div class="r-seg seg-1" style="width: 20%;"><span class="lang-zh">產業分析 20%</span><span class="lang-en">Sector 20%</span></div>
                                <div class="r-seg seg-2" style="width: 30%;"><span class="lang-zh">ESG分析 30%</span><span class="lang-en">ESG 30%</span></div>
                                <div class="r-seg seg-3" style="width: 25%;"><span class="lang-zh">投資論證 25%</span><span class="lang-en">Invest 25%</span></div>
                                <div class="r-seg seg-4" style="width: 15%;"><span class="lang-zh">改善建議 15%</span><span class="lang-en">Action 15%</span></div>
                                <div class="r-seg seg-5" style="width: 10%;"><span class="lang-zh">報告品質 10%</span><span class="lang-en">Quality 10%</span></div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

        </main>

        <!-- Slide Overview Grid Modal (Toggled by G or button) -->
        <div class="grid-modal" id="gridModal">
            <div class="grid-modal-header">
                <h2><i class="fa-solid fa-table-cells"></i> <span class="lang-zh">投影片全覽 (28 Slides Overview)</span><span class="lang-en">28 Slides Overview</span></h2>
                <button class="close-btn" id="closeGridBtn"><i class="fa-solid fa-xmark"></i></button>
            </div>
            <div class="grid-modal-body" id="gridContainer">
                <!-- Rendered dynamically by JS -->
            </div>
        </div>

    </div>

    <!-- Canva Bottom Control Dock Bar -->
    <footer class="canva-footer">
        <div class="footer-left">
            <button class="icon-btn" id="prevSlideBtn" title="Previous (Left Arrow)"><i class="fa-solid fa-chevron-left"></i></button>
            <span class="slide-counter"><span id="currentSlideNum">1</span> / <span id="totalSlideNum">28</span></span>
            <button class="icon-btn" id="nextSlideBtn" title="Next (Right Arrow)"><i class="fa-solid fa-chevron-right"></i></button>
        </div>
        
        <div class="footer-center">
            <div class="slide-progress-track">
                <div class="slide-progress-bar" id="progressBar"></div>
            </div>
            <span class="slide-title-preview" id="currentSlideTitlePreview">Slide 1: 課程封面</span>
        </div>

        <div class="footer-right">
            <button class="icon-btn" id="printDeckBtn" title="Print/Export Deck PDF"><i class="fa-solid fa-print"></i></button>
            <button class="icon-btn" id="fullScreenToggleBtn" title="Toggle Fullscreen Mode"><i class="fa-solid fa-expand"></i></button>
        </div>
    </footer>

    <script src="app.js"></script>
</body>
</html>"""

with open(r"C:\Users\User\Desktop\第1週_企業為何需要倫理\第9週_永續金融與ESG投資.html", "w", encoding="utf-8") as f:
    f.write(html_week9)

print("Successfully generated Week 9 HTML presentation file!")
