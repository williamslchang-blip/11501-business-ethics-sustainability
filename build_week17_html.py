import sys

html_week17 = """<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Week 17: Boardroom Simulation | ESG董事會決策模擬</title>
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
                <h1 class="deck-title">Week 17: Boardroom Simulation: Responsible Leadership and Strategic Decision Making</h1>
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
            <a href="第17週_ESG董事會決策模擬.docx" download class="btn btn-secondary" title="Download Teaching Facilitation Guide (.docx)">
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
                            <span class="meta-tag alt">Week 17 • Module 5 Boardroom Simulation</span>
                        </div>
                        <h1 class="main-heading">
                            <span class="lang-zh">ESG董事會決策模擬</span>
                            <span class="lang-en">Boardroom Simulation</span>
                        </h1>
                        <h2 class="sub-heading">
                            <span class="lang-zh">Boardroom Simulation: Responsible Leadership and Strategic Decision Making</span>
                            <span class="lang-en">Boardroom Simulation: Responsible Leadership and Strategic Decision Making</span>
                        </h2>
                        <p class="lead-text">
                            <span class="lang-zh">不確定情境下的高階決策力、7 大利害關係人利益折衝、閉門會議表決與 CEO 危機記者會</span>
                            <span class="lang-en">Strategic Decision Making under Uncertainty, Board Voting & CEO Press Conference</span>
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
                            <img src="week17_board_cover.jpg" alt="Week 17 Cover Visual" class="slide-img">
                            <div class="visual-badge">
                                <i class="fa-solid fa-gavel"></i> Boardroom Simulation • Governance
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 2: Today, You Are Board Members! -->
            <section class="slide" id="slide-2" data-title="Slide 2: 今天，你就是董事！">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-user-group"></i> Role Assignment</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">今天，你就是董事會成員！</span>
                            <span class="lang-en">Today, You Are Board Members!</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-sitemap accent-icon"></i> <span class="lang-zh">扮演董事長、CEO、CFO、CSO、獨董、員工/投資人/NGO代表</span><span class="lang-en">Roleplaying Chairman, CEO, CFO, CSO, Directors & Reps</span></h3>
                            <p><span class="lang-zh">每組 6-8 人組成董事會，各角色具備明確但互相關突的績效指標與倫理承諾。你們必須在有限時間與壓力下達成策略決議！</span>
                            <span class="lang-en">Simulating a real corporate board negotiating under conflicting stakeholder mandates.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 3: The Board's 4 Core Mandates -->
            <section class="slide" id="slide-3" data-title="Slide 3: 董事會 4 大核心職能">
                <div class="slide-container center-header-layout">
                    <div class="header-block center-text">
                        <div class="section-tag"><i class="fa-solid fa-shield"></i> 4 Board Mandates</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">董事會 4 大核心治理與受託責任</span>
                            <span class="lang-en">The Board's 4 Core Fiduciary Mandates</span>
                        </h2>
                    </div>

                    <div class="cards-grid-4 mt-3">
                        <div class="rc-card glass-card">
                            <h4>1. Strategy (策略)</h4>
                            <p><span class="lang-zh">審判轉型方向與資本預算。</span><span class="lang-en">Strategic direction & CapEx</span></p>
                        </div>
                        <div class="rc-card glass-card">
                            <h4>2. Governance (治理)</h4>
                            <p><span class="lang-zh">監督高管行為與合規度。</span><span class="lang-en">Executive oversight</span></p>
                        </div>
                        <div class="rc-card glass-card">
                            <h4>3. Risk (風險管控)</h4>
                            <p><span class="lang-zh">防範黑天鵝與極端黑天鵝。</span><span class="lang-en">ERM & tail risk control</span></p>
                        </div>
                        <div class="rc-card glass-card">
                            <h4>4. Ethics (倫理誠信)</h4>
                            <p><span class="lang-zh">維護企業誠信與聲譽資產。</span><span class="lang-en">Ethical compass guardian</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 4: Simulation Scenario Introduction -->
            <section class="slide" id="slide-4" data-title="Slide 4: 模擬決策情境發放">
                <div class="slide-container center-header-layout">
                    <div class="header-block center-text">
                        <div class="section-tag warning-tag"><i class="fa-solid fa-triangle-exclamation"></i> Simulation Scenarios</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">無標準答案的高難度衝突情境</span>
                            <span class="lang-en">High-Stakes Decision Dilemmas</span>
                        </h2>
                    </div>

                    <div class="cards-grid-3 gap-4 mt-3">
                        <div class="rc-card glass-card">
                            <h4>情境 A: 高污染工廠</h4>
                            <p><span class="lang-zh">提前關閉（財務巨虧） vs 繼續運作（污染環境）。</span><span class="lang-en">Early Plant Closure Dilemma</span></p>
                        </div>
                        <div class="rc-card glass-card">
                            <h4>情境 B: AI 招募偏誤</h4>
                            <p><span class="lang-zh">全面下架系統（效率暴跌） vs 隱瞞修正（歧視風險）。</span><span class="lang-en">AI Bias System Recall</span></p>
                        </div>
                        <div class="rc-card glass-card">
                            <h4>情境 C: 爭議供應商</h4>
                            <p><span class="lang-zh">解約切割（供應鏈斷鏈） vs 輔導轉型（遭爆料漂綠）。</span><span class="lang-en">Supplier Labor Violation</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 5: Corporate Baseline Context -->
            <section class="slide" id="slide-5" data-title="Slide 5: 企業財務與營運背景資訊">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-chart-pie"></i> Baseline Context</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">企業財務與營運背景資訊 (Baseline)</span>
                            <span class="lang-en">Corporate Baseline & Financial Context</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-coins accent-icon"></i> <span class="lang-zh">營收市占率、現金流與即將爆發的法規處分</span><span class="lang-en">Revenue Baseline & Regulatory Fines Exposure</span></h3>
                            <p><span class="lang-zh">董事會成員必須清楚：公司帳上現金有限，任何巨額環保罰款或解約賠償，都可能引發短期信用流動性危機！</span>
                            <span class="lang-en">Understanding cash flow boundaries when weighing environmental fines vs CapEx investments.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 6: Stakeholder 1: Shareholders -->
            <section class="slide" id="slide-6" data-title="Slide 6: 利害關係人 1 - 股東">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-sack-dollar"></i> Stakeholder 1</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">利害關係人 1：股東 (Shareholders)</span>
                            <span class="lang-en">Stakeholder 1: Shareholders</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-arrow-trend-up accent-icon"></i> <span class="lang-zh">要求維持短線每股盈餘 (EPS) 與股利發放</span><span class="lang-en">Demanding Short-Term EPS & Dividend Returns</span></h3>
                            <p><span class="lang-zh">股東與 CFO 代表主張：企業若無法存活，何談永續？堅決反對短期會大幅削弱季度獲利的昂貴處置方案。</span>
                            <span class="lang-en">Focusing on quarterly profits, ROI metrics, and protecting dividend distributions.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 7: Stakeholder 2: Employees -->
            <section class="slide" id="slide-7" data-title="Slide 7: 利害關係人 2 - 員工">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-people-group"></i> Stakeholder 2</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">利害關係人 2：員工 (Employees)</span>
                            <span class="lang-en">Stakeholder 2: Employees</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-person-shelter accent-icon"></i> <span class="lang-zh">關心工作崗位保障、工安與合理資遣補償</span><span class="lang-en">Demanding Job Security, Safety & Compensation</span></h3>
                            <p><span class="lang-zh">員工代表與工會主張：關廠或系統轉型絕不能以犧牲基層員工生計為代價，必須提供完整的轉職培訓與安置預算。</span>
                            <span class="lang-en">Defending worker employment, safety standards, and retraining compensation.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 8: Stakeholder 3: Regulators -->
            <section class="slide" id="slide-8" data-title="Slide 8: 利害關係人 3 - 政府與監管">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-building-flag"></i> Stakeholder 3</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">利害關係人 3：政府與監管機構 (Regulators)</span>
                            <span class="lang-en">Stakeholder 3: Regulators & Government</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-scale-balanced accent-icon"></i> <span class="lang-zh">要求符合淨零碳排、CBAM 與嚴懲隱瞞違規</span><span class="lang-en">Mandating Net Zero Compliance & Strict Fines</span></h3>
                            <p><span class="lang-zh">環保署與金管會代表警告：若延遲改善或謊報數據，將面臨停工勒令、天價罰款與董事長刑責起訴。</span>
                            <span class="lang-en">Enforcing legal compliance, carbon tax rules, and criminal liability for misrepresentation.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 9: Stakeholder 4: NGOs -->
            <section class="slide" id="slide-9" data-title="Slide 9: 利害關係人 4 - NGO">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag warning-tag"><i class="fa-solid fa-handshake-angle"></i> Stakeholder 4</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">利害關係人 4：NGO 與環保團體 (Activists)</span>
                            <span class="lang-en">Stakeholder 4: NGOs & Activists</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-bullhorn red-text"></i> <span class="lang-zh">要求立即停止污染、公開調查與透明揭露</span><span class="lang-en">Demanding Immediate Pollution Halt & Total Transparency</span></h3>
                            <p><span class="lang-zh">CSO 與 NGO 代表主張：任何妥協都是漂綠！企業必須公開全盤真相，並承諾在最短時間內完成退場或修復。</span>
                            <span class="lang-en">Pressuring the board for total disclosure, independent audits, and zero-tolerance for greenwashing.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 10: Stakeholder 5: Media -->
            <section class="slide" id="slide-10" data-title="Slide 10: 利害關係人 5 - 媒體">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag warning-tag"><i class="fa-solid fa-newspaper"></i> Stakeholder 5</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">利害關係人 5：媒體與社會大眾 (Media)</span>
                            <span class="lang-en">Stakeholder 5: Media & Public</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-eye red-text"></i> <span class="lang-zh">追逐黑幕真相、聚焦公關失誤與社會憤怒</span><span class="lang-en">Focusing on Scandals & Public Outrage</span></h3>
                            <p><span class="lang-zh">媒體聚焦於公關謊言與利益衝突細節。發言人若有任何失言，將迅速在網路上引發毀滅性炎上風暴。</span>
                            <span class="lang-en">Social media firestorms can amplify any board misstep within minutes.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 11: Stakeholder 6: ESG Funds -->
            <section class="slide" id="slide-11" data-title="Slide 11: 利害關係人 6 - 機構投資人">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-chart-line"></i> Stakeholder 6</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">利害關係人 6：機構 ESG 投資人 (ESG Funds)</span>
                            <span class="lang-en">Stakeholder 6: Institutional ESG Investors</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-building-columns accent-icon"></i> <span class="lang-zh">關注 MSCI 評級是否被降級與剔除成分股</span><span class="lang-en">Monitoring MSCI ESG Ratings & Fund Divestment</span></h3>
                            <p><span class="lang-zh">獨立董事與 ESG 基金代表警告：若董事會做出違反 ESG 倫理的決策，將觸發基金大量拋售與股價暴跌。</span>
                            <span class="lang-en">ESG funds threaten immediate divestment if board decisions violate MSCI ratings or UN PRI principles.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 12: Activity 1 - Board Meeting Simulation -->
            <section class="slide" id="slide-12" data-title="Slide 12: 活動一 - 董事會決策會議">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag activity-tag"><i class="fa-solid fa-gavel"></i> Activity 1 • 30 Minutes</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">Board Meeting Simulation</span>
                            <span class="lang-en">Board Meeting Simulation</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="scenario-card glass-card highlight-border">
                            <h3><span class="lang-zh">任務：6-8 人董事會進行閉門辯論折衝並投票表決</span><span class="lang-en">30-Min Closed-Door Board Debate & Voting</span></h3>
                            <div class="grid-2col mt-3 gap-2">
                                <div class="opt-choice"><p>1. 各角色輪流發表陳述與底線</p></div>
                                <div class="opt-choice"><p>2. 進行利益折衝與資本預算分配討論</p></div>
                                <div class="opt-choice"><p>3. 董事長主持正式舉手表決</p></div>
                                <div class="opt-choice"><p>4. 形成正式《董事會決議文》</p></div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 13: Activity 1 - Board Debrief -->
            <section class="slide" id="slide-13" data-title="Slide 13: 活動一 - 董事會表決點評">
                <div class="slide-container center-header-layout">
                    <div class="header-block center-text">
                        <div class="section-tag activity-tag"><i class="fa-solid fa-comments"></i> Class Debrief</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">決策沒有完美解答，平衡與擔當才是關鍵</span>
                            <span class="lang-en">Activity 1: Leadership Means Accountability</span>
                        </h2>
                    </div>

                    <div class="debrief-box glass-card glow-card">
                        <i class="fa-solid fa-lightbulb debrief-icon"></i>
                        <div class="debrief-content">
                            <h4><span class="lang-zh">教師觀點帶出 (Key Takeaway)：</span><span class="lang-en">Faculty Debrief:</span></h4>
                            <p><span class="lang-zh">「真正的 Responsible Leadership 不是試圖討好所有人，而是在多方高度衝突的情境下，做出符合企業倫理底線並敢於公開擔當的決策！」</span>
                            <span class="lang-en">"Responsible leadership isn't pleasing everyone; it's holding the ethical line under fire."</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 14: Formal Resolution Adoption -->
            <section class="slide" id="slide-14" data-title="Slide 14: 董事會決議文正式通過">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-file-signature"></i> Resolution</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">董事會正式投票與決議文通過</span>
                            <span class="lang-en">Formal Board Voting & Resolution Adoption</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-check-double accent-icon"></i> <span class="lang-zh">記錄贊成與反對票數，簽署官方公告文</span><span class="lang-en">Recording Votes & Signing Board Resolution</span></h3>
                            <p><span class="lang-zh">紀錄各董事與代表的表決票數，正式簽署包含『處理時間表、專款預算、獨立監督機制與賠償方案』之董事會決議文。</span>
                            <span class="lang-en">Signing formal resolutions detailing timelines, budgets, and independent oversight committees.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 15: CEO Public Statement Drafting -->
            <section class="slide" id="slide-15" data-title="Slide 15: CEO 聲明稿撰寫">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-scroll"></i> CEO Statement</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">CEO 第一份對外決策公開聲明稿</span>
                            <span class="lang-en">Drafting the CEO Public Decision Statement</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-pen-fancy accent-icon"></i> <span class="lang-zh">包含坦承事實、決議方案與對利害關係人的承諾</span><span class="lang-en">Acknowledging Facts & Communicating Board Action</span></h3>
                            <p><span class="lang-zh">撰寫 3 分鐘記者會公開發言稿：遵守 Golden Hour 原則，誠實交代事件、公佈董事會決議並展現真誠同理心。</span>
                            <span class="lang-en">Crafting a 3-minute opening statement for the upcoming live press conference.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 16: Activity 2 - CEO Press Conference -->
            <section class="slide" id="slide-16" data-title="Slide 16: 活動二 - CEO 危機記者會">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag activity-tag"><i class="fa-solid fa-bullhorn"></i> Activity 2 • 30 Minutes</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">CEO Press Conference (記者會)</span>
                            <span class="lang-en">Live CEO Crisis Press Conference</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="scenario-card glass-card highlight-border">
                            <h3><span class="lang-zh">任務：各組 CEO 上台召開記者會，接受全班尖銳質詢</span><span class="lang-en">CEO Press Pitch & Hostile Class Q&A</span></h3>
                            <div class="grid-2col mt-3 gap-2">
                                <div class="opt-choice"><p>1. CEO 發言 3 分鐘公開宣讀決議文</p></div>
                                <div class="opt-choice"><p>2. 全班扮演記者/投資人/NGO/政府</p></div>
                                <div class="opt-choice"><p>3. 進行 10 分鐘火爆尖銳 Q&A 即席攻防</p></div>
                                <div class="opt-choice"><p>4. CEO 與發言人展示危機處置能力</p></div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 17: Stock Price & Valuation Impact -->
            <section class="slide" id="slide-17" data-title="Slide 17: 即時市場股價與估值波動">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag warning-tag"><i class="fa-solid fa-chart-line-down"></i> Market Reaction</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">即時市場股價與估值波動影響</span>
                            <span class="lang-en">Stock Price & Valuation Market Reaction</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-arrow-trend-down red-text"></i> <span class="lang-zh">模擬記者會後華爾街與台股的即時波動</span><span class="lang-en">Simulating Immediate Post-Conference Market Fluctuations</span></h3>
                            <p><span class="lang-zh">評估決策後市場反應：透明公開且願意承擔成本的決策，股價開低走高；含糊其辭的決策則導致股價跌停並遭拋售。</span>
                            <span class="lang-en">Transparent board actions stabilize valuations, whereas ambiguous answers trigger stock sell-offs.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 18: ESG Rating Agency Response -->
            <section class="slide" id="slide-18" data-title="Slide 18: MSCI 評級調升/調降">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-star-half-stroke"></i> ESG Rating</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">ESG 評級機構 (MSCI) 評級調升/調降</span>
                            <span class="lang-en">MSCI ESG Rating Upgrade/Downgrade</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-ranking-star accent-icon"></i> <span class="lang-zh">剖析決策透明度如何影響 MSCI AAA / BBB 等級</span><span class="lang-en">Analyzing Rating Impacts from Board Transparency</span></h3>
                            <p><span class="lang-zh">MSCI 與 Sustainalytics 如何根據董事會成立獨立監督委員會與資訊揭露，決定維持 AAA 級或調降至 CCC 垃圾級。</span>
                            <span class="lang-en">Evaluating how ratings agencies re-score corporate governance following board actions.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 19: Long-term Trust Impact -->
            <section class="slide" id="slide-19" data-title="Slide 19: 長期利害關係人信任">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-hand-holding-heart"></i> Long-Term Trust</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">長期利害關係人信任與品牌聲譽</span>
                            <span class="lang-en">Long-Term Stakeholder Trust Impact</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-shield-heart accent-icon"></i> <span class="lang-zh">決策誠信決定未來 3 年的客戶忠誠度與留任</span><span class="lang-en">Board Integrity Shaping 3-Year Customer Loyalty</span></h3>
                            <p><span class="lang-zh">短期財務折損能靠營運恢復，但喪失誠信則需要數年甚至十年時間重建。Responsible Leadership 是維繫長線信任的關鍵。</span>
                            <span class="lang-en">Financial losses can be recovered; lost trust takes a decade to rebuild.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 20: Activity 2 - Debrief -->
            <section class="slide" id="slide-20" data-title="Slide 20: 活動二 - 記者會總評">
                <div class="slide-container center-header-layout">
                    <div class="header-block center-text">
                        <div class="section-tag activity-tag"><i class="fa-solid fa-comments"></i> Class Debrief</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">直面痛點與提出數據是公關最高防線</span>
                            <span class="lang-en">Activity 2: Data & Transparency Beat Spin</span>
                        </h2>
                    </div>

                    <div class="debrief-box glass-card glow-card">
                        <i class="fa-solid fa-lightbulb debrief-icon"></i>
                        <div class="debrief-content">
                            <h4><span class="lang-zh">教師觀點帶出 (Key Takeaway)：</span><span class="lang-en">Faculty Debrief:</span></h4>
                            <p><span class="lang-zh">「記者會最忌諱打太極與推卸責任！坦承失誤、拿出可驗證數據與第三條監督機制，才能贏得公眾尊重。」</span>
                            <span class="lang-en">"Never offer excuses to the press. Present verified data, own errors, and show independent audits."</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 21: Hostile Q&A Defense -->
            <section class="slide" id="slide-21" data-title="Slide 21: 尖銳質詢應對技巧">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-shield-cat"></i> Q&A Mastery</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">尖銳質詢應對技巧與公關防線</span>
                            <span class="lang-en">Mastering Hostile Q&A Under Pressure</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-headset accent-icon"></i> <span class="lang-zh">不推諉、不臆測、同理回應與數據舉證</span><span class="lang-en">No Excuses, No Speculation, Data Evidence</span></h3>
                            <p><span class="lang-zh">掌握公關防線 3 原則：1. 先同理受害者；2. 說明已查明事實，未知不硬答；3. 公開獨立第三方調查時間表。</span>
                            <span class="lang-en">Empathize first, present verified facts, and commit to independent timelines.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 22: Post-Board Audit -->
            <section class="slide" id="slide-22" data-title="Slide 22: 董事會會後檢討">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-clipboard-check"></i> Post-Board Audit</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">董事會會後檢討與 Governance 改進</span>
                            <span class="lang-en">Post-Board Audit & Governance Reform</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-boxes-packing accent-icon"></i> <span class="lang-zh">獨立董事席次是否足夠？資訊披露是否充分？</span><span class="lang-en">Assessing Board Independent Oversight Gaps</span></h3>
                            <p><span class="lang-zh">檢討本次演練漏洞：董事會是否過度被短線 CFO 綁架？獨立董事是否發揮獨立監督功能？未來如何改善 Governance 流程。</span>
                            <span class="lang-en">Reviewing whether independent directors effectively counterbalanced short-term financial pressure.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 23: Leadership under Uncertainty -->
            <section class="slide" id="slide-23" data-title="Slide 23: 不確定下的負責任領導">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-compass"></i> True Leadership</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">不確定情境下的 Responsible Leadership</span>
                            <span class="lang-en">Responsible Leadership Under Uncertainty</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-mountain-city accent-icon"></i> <span class="lang-zh">在資訊不完備與衝突下勇敢擔當與堅守道德</span><span class="lang-en">Courage to Stand for Ethics Under High Conflict</span></h3>
                            <p><span class="lang-zh">這正是 AACSB 最核心的學習成果：當完美的解答不存在時，負責任的領導者勇敢承擔責任，用道德底線指引企業前行！</span>
                            <span class="lang-en">When no perfect answer exists, responsible leaders uphold ethics and bear the burden of choice.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 24: Module 5 Synthesis -->
            <section class="slide" id="slide-24" data-title="Slide 24: 董事會決策單元總融會">
                <div class="slide-container center-header-layout">
                    <div class="header-block center-text">
                        <div class="section-tag"><i class="fa-solid fa-trophy"></i> Module 5 Synthesis</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">Module 5 董事會決策單元核心成果總融會</span>
                            <span class="lang-en">Module 5 Board Simulation Core Synthesis</span>
                        </h2>
                    </div>

                    <div class="cards-grid-4 mt-3">
                        <div class="rc-card glass-card">
                            <h4>Fiduciary Duty</h4>
                            <p><span class="lang-zh">深刻體會董事會受託責任。</span><span class="lang-en">Fiduciary board duty</span></p>
                        </div>
                        <div class="rc-card glass-card">
                            <h4>Conflict Negotiation</h4>
                            <p><span class="lang-zh">掌握多方利害關係人折衝。</span><span class="lang-en">Stakeholder negotiation</span></p>
                        </div>
                        <div class="rc-card glass-card">
                            <h4>Press Mastery</h4>
                            <p><span class="lang-zh">具備 CEO 記者會應答能力。</span><span class="lang-en">Live press Q&A mastery</span></p>
                        </div>
                        <div class="rc-card glass-card">
                            <h4>Ethical Courage</h4>
                            <p><span class="lang-zh">展現高階倫理決策擔當。</span><span class="lang-en">Ethical courage under fire</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 25: Preview W18 & Homework 17 -->
            <section class="slide" id="slide-25" data-title="Slide 25: Preview W18 & Homework 17">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag homework-tag"><i class="fa-solid fa-flag-checkered"></i> Preview W18 & HW17</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">W18 終極大結業預告與 Homework 17</span>
                            <span class="lang-en">W18 Preview & Homework 17</span>
                        </h2>
                    </div>

                    <div class="main-panel">
                        <div class="glass-card feature-card mb-2">
                            <h3><i class="fa-solid fa-graduation-cap accent-icon"></i> <span class="lang-zh">W18 終極大結業預告：課程總回顧、個人永續領導力與畢業圓滿</span><span class="lang-en">W18 Preview: Course Reflection & Graduation</span></h3>
                            <p class="mb-2"><span class="lang-zh">下一週我們將迎來 18 週課程的大結業：《課程總回顧、個人永續領導力與畢業圓滿 (Reflection & Future Leadership)》！</span><span class="lang-en">Next week we celebrate our final 18-week course graduation!</span></p>
                        </div>

                        <div class="glass-card feature-card mb-2">
                            <h3><i class="fa-solid fa-file-contract accent-icon"></i> <span class="lang-zh">Homework 17：董事會個人反思報告 (約 1,500 字/個人)</span><span class="lang-en">Homework 17: Board Reflection Report (~1,500w)</span></h3>
                            <p><span class="lang-zh">個人完成：扮演角色、支持決策理由、若重新決策的改變、如何平衡股東與社會利益及對 Responsible Leadership 的體悟。</span>
                            <span class="lang-en">Individual report: board role, vote rationale, retrospectives, balancing EPS vs Society & leadership insights.</span></p>
                        </div>

                        <div class="glass-card rubrics-card">
                            <h4><i class="fa-solid fa-chart-bar accent-icon"></i> AACSB <span class="lang-zh">評分標準</span><span class="lang-en">Rubrics Breakdown</span></h4>
                            <div class="rubrics-bar">
                                <div class="r-seg seg-1" style="width: 25%;"><span class="lang-zh">決策分析 25%</span><span class="lang-en">Decision 25%</span></div>
                                <div class="r-seg seg-2" style="width: 25%;"><span class="lang-zh">董事參與 25%</span><span class="lang-en">Engagement 25%</span></div>
                                <div class="r-seg seg-3" style="width: 20%;"><span class="lang-zh">危機溝通 20%</span><span class="lang-en">Press Q&A 20%</span></div>
                                <div class="r-seg seg-4" style="width: 20%;"><span class="lang-zh">個人反思 20%</span><span class="lang-en">Reflect 20%</span></div>
                                <div class="r-seg seg-5" style="width: 10%;"><span class="lang-zh">專業表現 10%</span><span class="lang-en">Demeanor 10%</span></div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

        </main>

        <!-- Slide Overview Grid Modal (Toggled by G or button) -->
        <div class="grid-modal" id="gridModal">
            <div class="grid-modal-header">
                <h2><i class="fa-solid fa-table-cells"></i> <span class="lang-zh">投影片全覽 (25 Slides Overview)</span><span class="lang-en">25 Slides Overview</span></h2>
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
            <span class="slide-counter"><span id="currentSlideNum">1</span> / <span id="totalSlideNum">25</span></span>
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

with open(r"C:\Users\User\Desktop\第1週_企業為何需要倫理\第17週_ESG董事會決策模擬.html", "w", encoding="utf-8") as f:
    f.write(html_week17)

print("Successfully generated Week 17 HTML presentation file!")
