import re

# We will construct a complete, ultra-rich bilingual index.html file
html_content = """<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Week 1: Why Business Ethics Matters? | 企業為何需要倫理？</title>
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&family=Noto+Sans+TC:wght@300;400;500;700;900&family=Outfit:wght@400;600;800&display=swap" rel="stylesheet">
    <!-- FontAwesome for Canva-style UI icons -->
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
                <h1 class="deck-title">Week 1: Business Ethics and Sustainable Management</h1>
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
            <a href="第1週_企業為何需要倫理_教學指引.docx" download class="btn btn-secondary" title="Download Teaching Facilitation Guide (.docx)">
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
                            <span class="meta-tag alt">Week 01 • Lecture Presentation</span>
                        </div>
                        <h1 class="main-heading">
                            <span class="lang-zh">企業為何需要倫理？</span>
                            <span class="lang-en">Why Business Ethics Matters?</span>
                        </h1>
                        <h2 class="sub-heading">
                            <span class="lang-zh">Business Ethics and Sustainable Management</span>
                            <span class="lang-en">Business Ethics and Sustainable Management</span>
                        </h2>
                        <p class="lead-text">
                            <span class="lang-zh">從企業倫理 (Ethics) 邁向 CSR、ESG 與永續經營 (Sustainable Governance) 的戰略思維</span>
                            <span class="lang-en">Strategic Mindset from Business Ethics to CSR, ESG, and Sustainable Governance</span>
                        </p>
                        
                        <div class="cover-footer">
                            <div class="instructor-info">
                                <i class="fa-solid fa-chalkboard-user"></i> 
                                <span class="lang-zh">授課教授：商學院 企業管理學系 教授群</span>
                                <span class="lang-en">Instructor: Department of Business Administration Faculty</span>
                            </div>
                            <div class="time-info">
                                <i class="fa-regular fa-calendar-check"></i> 
                                <span class="lang-zh">上課時間：2 小時 (110 分鐘)</span>
                                <span class="lang-en">Lecture Duration: 2 Hours (110 Mins)</span>
                            </div>
                        </div>
                    </div>
                    <div class="cover-visual">
                        <div class="glass-card visual-card">
                            <img src="business_ethics_cover.jpg" alt="Business Ethics Cover Visual" class="slide-img">
                            <div class="visual-badge">
                                <i class="fa-solid fa-shield-halved"></i> Trust • Ethics • ESG
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 2: Teacher & Course Info -->
            <section class="slide" id="slide-2" data-title="Slide 2: 教師介紹與授課資訊">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-id-card"></i> Part I • Course Overview</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">教師介紹與授課資訊</span>
                            <span class="lang-en">Instructor Profile & Admin</span>
                        </h2>
                        <p class="slide-sub">Instructor Profile & Course Administration</p>
                        
                        <div class="profile-card glass-card">
                            <div class="avatar-circle">
                                <i class="fa-solid fa-user-tie"></i>
                            </div>
                            <h3>
                                <span class="lang-zh">授課教師團隊</span>
                                <span class="lang-en">Faculty Research Team</span>
                            </h3>
                            <p class="title-text">
                                <span class="lang-zh">商學院 ESG 永續管理與企業倫理研究中心</span>
                                <span class="lang-en">Center for ESG & Business Ethics Research</span>
                            </p>
                            <hr class="divider">
                            <ul class="contact-list">
                                <li><i class="fa-solid fa-envelope"></i> <strong>Email:</strong> wslchang@mail.mcu.edu.tw</li>
                                <li><i class="fa-solid fa-building-user"></i> <strong>Office:</strong> <span class="lang-zh">財務金融學系系辦公室</span><span class="lang-en">Department of Finance Office</span></li>
                                <li><i class="fa-solid fa-clock"></i> <strong>Office Hour:</strong> <span class="lang-zh">上網查詢</span><span class="lang-en">Check Online</span></li>
                            </ul>
                        </div>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card mb-4">
                            <h3><i class="fa-solid fa-graduation-cap accent-icon"></i> 
                                <span class="lang-zh">授課方式 (Pedagogical Approach)</span>
                                <span class="lang-en">Pedagogical Approach</span>
                            </h3>
                            <div class="grid-2col mt-3">
                                <div class="info-box">
                                    <h4><i class="fa-solid fa-comments"></i> 
                                        <span class="lang-zh">互動式哈佛案例教學</span>
                                        <span class="lang-en">Interactive Harvard Case Method</span>
                                    </h4>
                                    <p>
                                        <span class="lang-zh">結合真實企業個案討論、Mentimeter即時辯論與小組情境模擬演練。</span>
                                        <span class="lang-en">Integrating real corporate case studies, live Mentimeter debates, and team simulations.</span>
                                    </p>
                                </div>
                                <div class="info-box">
                                    <h4><i class="fa-solid fa-language"></i> 
                                        <span class="lang-zh">EMI 雙語化教學支持</span>
                                        <span class="lang-en">EMI Bilingual Support</span>
                                    </h4>
                                    <p>
                                        <span class="lang-zh">核心專有名詞採雙語對照，培養國際商業倫理與 ESG 報告書解讀能力。</span>
                                        <span class="lang-en">Bilingual key terminology to build global business ethics and ESG report reading skills.</span>
                                    </p>
                                </div>
                            </div>
                        </div>

                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-handshake-angle accent-icon"></i> 
                                <span class="lang-zh">課堂公約與學習期望</span>
                                <span class="lang-en">Class Norms & Expectations</span>
                            </h3>
                            <ul class="styled-list">
                                <li>
                                    <strong class="lang-zh">準時與專注：</strong><strong class="lang-en">Punctuality & Focus: </strong>
                                    <span class="lang-zh">尊重彼此發言，保持批判性思考 (Critical Thinking)。</span>
                                    <span class="lang-en">Respect diverse voices and maintain active Critical Thinking.</span>
                                </li>
                                <li>
                                    <strong class="lang-zh">開放性對話：</strong><strong class="lang-en">Open Dialogue: </strong>
                                    <span class="lang-zh">商業倫理議題常無單一標準答案，重在論證品質與倫理推理架構。</span>
                                    <span class="lang-en">Business ethics dilemmas rarely have single right answers; focus is on ethical reasoning quality.</span>
                                </li>
                                <li>
                                    <strong class="lang-zh">團隊合作：</strong><strong class="lang-en">Teamwork: </strong>
                                    <span class="lang-zh">每次小組討論均為團隊決策機制的實踐。</span>
                                    <span class="lang-en">Every group discussion is a practice in corporate team decision-making mechanisms.</span>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 3: Course Objectives -->
            <section class="slide" id="slide-3" data-title="Slide 3: 課程目標">
                <div class="slide-container center-header-layout">
                    <div class="header-block center-text">
                        <div class="section-tag"><i class="fa-solid fa-bullseye"></i> Learning Objectives</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">完成這門課後，你將具備 5 大核心勝任力</span>
                            <span class="lang-en">5 Core Competencies You Will Master After This Course</span>
                        </h2>
                        <p class="slide-sub">AACSB Assurance of Learning (AoL) Standard Competencies</p>
                    </div>

                    <div class="cards-grid-5">
                        <div class="objective-card glass-card">
                            <div class="icon-header color-1"><i class="fa-solid fa-scale-balanced"></i></div>
                            <h3>
                                <span class="lang-zh">1. 分析倫理事件</span>
                                <span class="lang-en">1. Analyze Ethics</span>
                            </h3>
                            <p>
                                <span class="lang-zh">運用倫理學理論與兩難分析模型，辨識企業營運中的道德風險。</span>
                                <span class="lang-en">Apply ethical frameworks to identify moral risks in business operations.</span>
                            </p>
                        </div>
                        <div class="objective-card glass-card">
                            <div class="icon-header color-2"><i class="fa-solid fa-chart-line"></i></div>
                            <h3>
                                <span class="lang-zh">2. 評估 ESG 策略</span>
                                <span class="lang-en">2. Evaluate ESG</span>
                            </h3>
                            <p>
                                <span class="lang-zh">掌握環境(E)、社會(S)與治理(G)指標對企業長遠競爭力的影響。</span>
                                <span class="lang-en">Master E, S, G metrics and their impact on long-term competitive advantage.</span>
                            </p>
                        </div>
                        <div class="objective-card glass-card">
                            <div class="icon-header color-3"><i class="fa-solid fa-file-invoice"></i></div>
                            <h3>
                                <span class="lang-zh">3. 閱讀永續報告</span>
                                <span class="lang-en">3. Read ESG Reports</span>
                            </h3>
                            <p>
                                <span class="lang-zh">解讀 GRI、SASB、TCFD 標準之永續報告書，判讀漂綠(Greenwashing)風險。</span>
                                <span class="lang-en">Interpret GRI/SASB reports and detect corporate Greenwashing risks.</span>
                            </p>
                        </div>
                        <div class="objective-card glass-card">
                            <div class="icon-header color-4"><i class="fa-solid fa-sitemap"></i></div>
                            <h3>
                                <span class="lang-zh">4. 解讀企業治理</span>
                                <span class="lang-en">4. Interpret Governance</span>
                            </h3>
                            <p>
                                <span class="lang-zh">評估董事會獨立性、內部控管機制與利害關係人溝通管道。</span>
                                <span class="lang-en">Assess board independence, internal controls, and stakeholder engagement.</span>
                            </p>
                        </div>
                        <div class="objective-card glass-card">
                            <div class="icon-header color-5"><i class="fa-solid fa-brain"></i></div>
                            <h3>
                                <span class="lang-zh">5. 建立永續思維</span>
                                <span class="lang-en">5. Build Mindset</span>
                            </h3>
                            <p>
                                <span class="lang-zh">將「社會價值創造」融入企業核心商業模式，奠定未來高階領袖素養。</span>
                                <span class="lang-en">Integrate social value creation into core business models for future leadership.</span>
                            </p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 4: Course Map Flowchart -->
            <section class="slide" id="slide-4" data-title="Slide 4: 課程內容地圖">
                <div class="slide-container">
                    <div class="header-block">
                        <div class="section-tag"><i class="fa-solid fa-map-location-dot"></i> Course Roadmap</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">18 週課程內容地圖</span>
                            <span class="lang-en">18-Week Course Roadmap & Progression</span>
                        </h2>
                        <p class="slide-sub">From Ethical Foundations to Net Zero & Future Business Strategy</p>
                    </div>

                    <div class="roadmap-wrapper glass-card">
                        <div class="flow-steps">
                            <div class="flow-step active-step">
                                <div class="step-num">W1-3</div>
                                <div class="step-icon"><i class="fa-solid fa-balance-scale"></i></div>
                                <h4>Business Ethics</h4>
                                <p><span class="lang-zh">企業倫理理論與道德範式</span><span class="lang-en">Ethical Theories & Frameworks</span></p>
                            </div>
                            <div class="flow-arrow"><i class="fa-solid fa-arrow-right"></i></div>

                            <div class="flow-step">
                                <div class="step-num">W4-6</div>
                                <div class="step-icon"><i class="fa-solid fa-heart-pulse"></i></div>
                                <h4>CSR</h4>
                                <p><span class="lang-zh">企業社會責任與公益價值</span><span class="lang-en">Social Responsibility & Impact</span></p>
                            </div>
                            <div class="flow-arrow"><i class="fa-solid fa-arrow-right"></i></div>

                            <div class="flow-step">
                                <div class="step-num">W7-10</div>
                                <div class="step-icon"><i class="fa-solid fa-seedling"></i></div>
                                <h4>ESG Strategy</h4>
                                <p><span class="lang-zh">環境、社會與治理實務量化</span><span class="lang-en">Quantitative E, S, G Metrics</span></p>
                            </div>
                            <div class="flow-arrow"><i class="fa-solid fa-arrow-right"></i></div>

                            <div class="flow-step">
                                <div class="step-num">W11-13</div>
                                <div class="step-icon"><i class="fa-solid fa-building-columns"></i></div>
                                <h4>Governance</h4>
                                <p><span class="lang-zh">公司治理、誠信經營與防弊</span><span class="lang-en">Board Governance & Compliance</span></p>
                            </div>
                            <div class="flow-arrow"><i class="fa-solid fa-arrow-right"></i></div>

                            <div class="flow-step">
                                <div class="step-num">W14-16</div>
                                <div class="step-icon"><i class="fa-solid fa-earth-americas"></i></div>
                                <h4>Sustainability</h4>
                                <p><span class="lang-zh">循環經濟與淨零轉型</span><span class="lang-en">Circular Economy & Net Zero</span></p>
                            </div>
                            <div class="flow-arrow"><i class="fa-solid fa-arrow-right"></i></div>

                            <div class="flow-step highlight-step">
                                <div class="step-num">W17-18</div>
                                <div class="step-icon"><i class="fa-solid fa-rocket"></i></div>
                                <h4>Future Business</h4>
                                <p><span class="lang-zh">AI倫理與永續商業個案發表</span><span class="lang-en">AI Ethics & Capstone Presentations</span></p>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 5: Assessment & Grading -->
            <section class="slide" id="slide-5" data-title="Slide 5: 評分方式與考核標準">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-calculator"></i> Assessment Criteria</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">多元評分機制與權重</span>
                            <span class="lang-en">Assessment & Grading Criteria</span>
                        </h2>
                        <p class="slide-sub">Holistic Evaluation Scheme</p>
                        <div class="pie-summary glass-card center-text mt-4">
                            <div class="giant-percentage">100%</div>
                            <p class="text-muted">
                                <span class="lang-zh">AACSB 能力導向多元評量 (AoL Scorecard)</span>
                                <span class="lang-en">AACSB Competency Scorecard</span>
                            </p>
                        </div>
                    </div>

                    <div class="main-panel">
                        <div class="grading-grid">
                            <div class="grade-item glass-card">
                                <div class="grade-percent">20%</div>
                                <div class="grade-details">
                                    <h3><i class="fa-solid fa-comments"></i> 
                                        <span class="lang-zh">課堂參與與即時投票 (Class Participation)</span>
                                        <span class="lang-en">Class Participation & Live Polling</span>
                                    </h3>
                                    <p>
                                        <span class="lang-zh">個案提問、Mentimeter 投票反應、課堂思考表達與辯論參與。</span>
                                        <span class="lang-en">Case Q&A, live Mentimeter polling responses, active classroom debates.</span>
                                    </p>
                                </div>
                            </div>
                            <div class="grade-item glass-card">
                                <div class="grade-percent">20%</div>
                                <div class="grade-details">
                                    <h3><i class="fa-solid fa-users-gear"></i> 
                                        <span class="lang-zh">課堂小組活動與個案討論 (Case Workshops)</span>
                                        <span class="lang-en">Case Workshops & Team Activities</span>
                                    </h3>
                                    <p>
                                        <span class="lang-zh">含本週 CEO 決策挑戰賽與新聞倫理分析等課堂實作成果。</span>
                                        <span class="lang-en">Includes CEO Decision Game and News Ethics Analysis workshops.</span>
                                    </p>
                                </div>
                            </div>
                            <div class="grade-item glass-card">
                                <div class="grade-percent">20%</div>
                                <div class="grade-details">
                                    <h3><i class="fa-solid fa-file-signature"></i> 
                                        <span class="lang-zh">期中個案分析報告 (Midterm Case Analysis)</span>
                                        <span class="lang-en">Midterm Case Analysis Report</span>
                                    </h3>
                                    <p>
                                        <span class="lang-zh">針對單一全球企業倫理事件進行 1,200 字深度診斷個人報告。</span>
                                        <span class="lang-en">Individual 1,200-word deep-dive report on a global corporate scandal.</span>
                                    </p>
                                </div>
                            </div>
                            <div class="grade-item glass-card">
                                <div class="grade-percent">20%</div>
                                <div class="grade-details">
                                    <h3><i class="fa-solid fa-display"></i> 
                                        <span class="lang-zh">小組個案簡報 (Group Case Presentation)</span>
                                        <span class="lang-en">Group Case Presentation</span>
                                    </h3>
                                    <p>
                                        <span class="lang-zh">選定特定產業 ESG/倫理爭議，進行 15 分鐘小組分析與課堂 Q&A。</span>
                                        <span class="lang-en">15-minute group pitch and Q&A on selected industry ESG controversy.</span>
                                    </p>
                                </div>
                            </div>
                            <div class="grade-item glass-card highlight-border">
                                <div class="grade-percent">20%</div>
                                <div class="grade-details">
                                    <h3><i class="fa-solid fa-award"></i> 
                                        <span class="lang-zh">期末專題：永續報告書診斷 (ESG Final Capstone)</span>
                                        <span class="lang-en">Final Capstone: ESG Report Audit</span>
                                    </h3>
                                    <p>
                                        <span class="lang-zh">實務解讀國內外企業 ESG 報告書，評估其永續真實度與改進建議。</span>
                                        <span class="lang-en">Audit real corporate ESG reports, evaluate authenticity and Greenwashing.</span>
                                    </p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 6: Warm-up Dilemma -->
            <section class="slide" id="slide-6" data-title="Slide 6: 暖身思考 - 法律與道德">
                <div class="slide-container center-header-layout">
                    <div class="header-block center-text">
                        <div class="section-tag warning-tag"><i class="fa-solid fa-triangle-exclamation"></i> Part II • Why Business Needs Ethics?</div>
                        <h2 class="slide-heading giant-title">
                            <span class="lang-zh">暖身思考：合法，但不道德？</span>
                            <span class="lang-en">Warm-up Dilemma: Legality vs. Morality</span>
                        </h2>
                        <p class="slide-sub">Legality vs. Morality Dilemma in Business</p>
                    </div>

                    <div class="dilemma-box glass-card glow-card">
                        <div class="dilemma-statement">
                            <p class="quote-text">
                                <span class="lang-zh">「如果一家公司的商業行為<strong>完全合法</strong>（沒有違反任何現行法規），但卻高度<strong>違反社會道德與誠信</strong>，身為消費者、投資人或員工的你，<strong>你會支持它嗎？</strong>」</span>
                                <span class="lang-en">"If a business action is <strong>completely legal</strong>, but severely violates <strong>social morality and public trust</strong>, as a consumer, investor, or employee, <strong>would you support it?</strong>"</span>
                            </p>
                        </div>
                        <div class="dilemma-options mt-4">
                            <div class="option-card">
                                <div class="opt-badge">
                                    <span class="lang-zh">選項 A</span><span class="lang-en">Option A</span>
                                </div>
                                <h4>
                                    <span class="lang-zh">支持 / 接受</span>
                                    <span class="lang-en">Support / Accept</span>
                                </h4>
                                <p>
                                    <span class="lang-zh">「法無禁止即可為。企業首要目標是獲利，只要沒觸法即可。」</span>
                                    <span class="lang-en">"What is not forbidden is allowed. Primary goal is profit within law."</span>
                                </p>
                            </div>
                            <div class="vs-badge">VS</div>
                            <div class="option-card">
                                <div class="opt-badge alt">
                                    <span class="lang-zh">選項 B</span><span class="lang-en">Option B</span>
                                </div>
                                <h4>
                                    <span class="lang-zh">抵制 / 反對</span>
                                    <span class="lang-en">Resist / Oppose</span>
                                </h4>
                                <p>
                                    <span class="lang-zh">「法律只是道德的最低底線。失去社會信任的企業難以長久。」</span>
                                    <span class="lang-en">"Law is only the floor. Companies losing public trust cannot survive."</span>
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 7: Purpose of the Firm (Friedman vs Freeman) -->
            <section class="slide" id="slide-7" data-title="Slide 7: 企業的真正目的">
                <div class="slide-container">
                    <div class="header-block">
                        <div class="section-tag"><i class="fa-solid fa-landmark"></i> Theoretical Foundation</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">企業的真正目的究竟是什麼？</span>
                            <span class="lang-en">What is the True Purpose of the Firm?</span>
                        </h2>
                        <p class="slide-sub">Shareholder Primacy vs. Stakeholder Theory</p>
                    </div>

                    <div class="grid-2col gap-4 mt-3">
                        <div class="theory-card glass-card">
                            <div class="theory-header">
                                <span class="year-tag">1970</span>
                                <h3>
                                    <span class="lang-zh">股東至上理論 (Shareholder Primacy)</span>
                                    <span class="lang-en">Shareholder Primacy Theory</span>
                                </h3>
                                <div class="author-name">Milton Friedman (Nobel Laureate)</div>
                            </div>
                            <div class="theory-body">
                                <blockquote class="theory-quote">
                                    "The Social Responsibility of Business is to Increase its Profits."
                                </blockquote>
                                <ul class="bullet-list mt-3">
                                    <li>
                                        <span class="lang-zh">企業唯一的社會責任是在法律規則內<strong>最大化股東財富</strong>。</span>
                                        <span class="lang-en">The sole social responsibility is to <strong>maximize shareholder wealth</strong> within law.</span>
                                    </li>
                                    <li>
                                        <span class="lang-zh">經理人是股東代理人，將公司資源用於社會公益是「盜用股東資金」。</span>
                                        <span class="lang-en">Managers are shareholder agents; using corporate funds for charity is misappropriation.</span>
                                    </li>
                                    <li>
                                        <span class="lang-zh">市場機制會自行調配效率，道德應由個人與政府負責。</span>
                                        <span class="lang-en">Free markets allocate resources efficiently; morality belongs to individuals and state.</span>
                                    </li>
                                </ul>
                            </div>
                        </div>

                        <div class="theory-card glass-card highlight-card">
                            <div class="theory-header">
                                <span class="year-tag alt">1984 ~ Present</span>
                                <h3>
                                    <span class="lang-zh">利害關係人理論 (Stakeholder Theory)</span>
                                    <span class="lang-en">Stakeholder Theory</span>
                                </h3>
                                <div class="author-name">Edward Freeman (Management Guru)</div>
                            </div>
                            <div class="theory-body">
                                <blockquote class="theory-quote">
                                    "Businesses create value for customers, suppliers, employees, communities, and shareholders."
                                </blockquote>
                                <ul class="bullet-list mt-3">
                                    <li>
                                        <span class="lang-zh">企業是社會網絡的一部分，影響並受所有<strong>利害關係人</strong>影響。</span>
                                        <span class="lang-en">Businesses operate in social networks, affecting and affected by <strong>all stakeholders</strong>.</span>
                                    </li>
                                    <li>
                                        <span class="lang-zh">長期獲利來自於平衡員工權益、顧客信任、供應鏈永續與環境和諧。</span>
                                        <span class="lang-en">Long-term profits stem from balancing employee well-being, trust, and environmental harmony.</span>
                                    </li>
                                    <li>
                                        <span class="lang-zh">2019 美國商業圓桌會議 (BRT) 宣言正式轉向利害關係人資本主義。</span>
                                        <span class="lang-en">2019 Business Roundtable statement officially shifted purpose to stakeholder capitalism.</span>
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 8: Defining Business Ethics -->
            <section class="slide" id="slide-8" data-title="Slide 8: 企業倫理的精準定義">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-shapes"></i> Conceptual Framework</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">倫理、道德與法律的層級關聯</span>
                            <span class="lang-en">Ethics, Morality, and Law</span>
                        </h2>
                        <p class="slide-sub">Ethics, Morality, and Law Breakdown</p>
                        <div class="img-wrapper glass-card mt-3">
                            <img src="ethical_dilemma_illustration.jpg" alt="Ethical Framework Illustration" class="slide-img rounded">
                        </div>
                    </div>

                    <div class="main-panel">
                        <div class="venn-breakdown-card glass-card">
                            <div class="concept-item">
                                <div class="concept-badge law-badge">Law (<span class="lang-zh">法律</span><span class="lang-en">Legal Floor</span>)</div>
                                <div class="concept-desc">
                                    <h4><span class="lang-zh">國家強制的「最低道德底線」</span><span class="lang-en">Enforceable Minimum Standard</span></h4>
                                    <p><span class="lang-zh">由立法機關制定，具強制裁罰力。合乎法律不代表合乎道德行為。</span><span class="lang-en">Enforced by state. Compliance with law does not guarantee ethical conduct.</span></p>
                                </div>
                            </div>
                            <hr class="divider">
                            <div class="concept-item">
                                <div class="concept-badge morality-badge">Morality (<span class="lang-zh">道德</span><span class="lang-en">Social Beliefs</span>)</div>
                                <div class="concept-desc">
                                    <h4><span class="lang-zh">社會文化與個人內化的「價值規範」</span><span class="lang-en">Internalized Moral Values</span></h4>
                                    <p><span class="lang-zh">關於對與錯、善與惡的主觀信念，源自文化、宗教與社會慣習。</span><span class="lang-en">Subjective beliefs on right vs wrong derived from culture and social norms.</span></p>
                                </div>
                            </div>
                            <hr class="divider">
                            <div class="concept-item">
                                <div class="concept-badge ethics-badge">Business Ethics (<span class="lang-zh">企業倫理</span><span class="lang-en">Business Ethics</span>)</div>
                                <div class="concept-desc">
                                    <h4><span class="lang-zh">商業情境下的「系統化決策原則」</span><span class="lang-en">Systematic Decision Framework</span></h4>
                                    <p><span class="lang-zh">在組織運作與商業決策中，評估行為是否適當、公正、誠信並善盡社會責任的系統化規範。</span><span class="lang-en">Systematic principles evaluating fairness, integrity, and responsibility in business decisions.</span></p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 9: Daily Ethical Decisions -->
            <section class="slide" id="slide-9" data-title="Slide 9: 企業每天面對的倫理決策">
                <div class="slide-container center-header-layout">
                    <div class="header-block center-text">
                        <div class="section-tag"><i class="fa-solid fa-briefcase"></i> Everyday Business Realities</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">企業營運無處不在的倫理決策</span>
                            <span class="lang-en">Everyday Business Ethical Decisions</span>
                        </h2>
                        <p class="slide-sub">Ethical Decision Points Across Business Functions</p>
                    </div>

                    <div class="cards-grid-3x2">
                        <div class="decision-card glass-card">
                            <div class="dec-icon"><i class="fa-solid fa-users-viewfinder"></i></div>
                            <h4><span class="lang-zh">人力資源 (HR & Hiring)</span><span class="lang-en">HR & Hiring</span></h4>
                            <p><span class="lang-zh">招聘多元包容 (DEI)、無預警大規模裁員程序、同工同酬與職場霸凌預防。</span><span class="lang-en">DEI hiring, mass layoff transparency, equal pay, and anti-harassment policies.</span></p>
                        </div>
                        <div class="decision-card glass-card">
                            <div class="dec-icon"><i class="fa-solid fa-rectangle-ad"></i></div>
                            <h4><span class="lang-zh">行銷與廣告 (Marketing)</span><span class="lang-en">Marketing & Ads</span></h4>
                            <p><span class="lang-zh">誇大不實宣傳、針對弱勢兒童的促銷、綠色漂洗 (Greenwashing) 訊息。</span><span class="lang-en">Deceptive advertising, targeting vulnerable children, and Greenwashing claims.</span></p>
                        </div>
                        <div class="decision-card glass-card">
                            <div class="dec-icon"><i class="fa-solid fa-tags"></i></div>
                            <h4><span class="lang-zh">定價與競爭 (Pricing)</span><span class="lang-en">Pricing & Competition</span></h4>
                            <p><span class="lang-zh">災後聯合壟斷漲價、掠奪性定價打壓新創、不透明隱藏費用。</span><span class="lang-en">Post-disaster price gouging, predatory pricing, and hidden fees.</span></p>
                        </div>
                        <div class="decision-card glass-card">
                            <div class="dec-icon"><i class="fa-solid fa-truck-ramp-box"></i></div>
                            <h4><span class="lang-zh">供應鏈管理 (Supply Chain)</span><span class="lang-en">Supply Chain</span></h4>
                            <p><span class="lang-zh">海外血汗工廠、童工問題、供應商環境污染轉嫁與強制勞動。</span><span class="lang-en">Overseas sweatshops, child labor, pollution outsourcing, and forced labor.</span></p>
                        </div>
                        <div class="decision-card glass-card">
                            <div class="dec-icon"><i class="fa-solid fa-robot"></i></div>
                            <h4><span class="lang-zh">AI 與數據隱私 (AI & Data)</span><span class="lang-en">AI & Data Privacy</span></h4>
                            <p><span class="lang-zh">演算法偏見歧視、未經授權蒐集個資、Deepfake 技術濫用與責任歸屬。</span><span class="lang-en">Algorithmic bias, unauthorized data scraping, Deepfake risks, and AI accountability.</span></p>
                        </div>
                        <div class="decision-card glass-card">
                            <div class="dec-icon"><i class="fa-solid fa-shield-virus"></i></div>
                            <h4><span class="lang-zh">產品安全 (Product Safety)</span><span class="lang-en">Product Safety</span></h4>
                            <p><span class="lang-zh">已知產品瑕疵是否主動召回？過期食品改標？利益與消費者健康的權衡。</span><span class="lang-en">Voluntary recall of defective products vs concealing risks for profit.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 10: Value of Business Ethics -->
            <section class="slide" id="slide-10" data-title="Slide 10: 企業倫理的核心價值">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-gem"></i> Strategic Advantage</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">倫理不是成本，而是核心競爭力</span>
                            <span class="lang-en">Ethics as a Core Competitive Advantage</span>
                        </h2>
                        <p class="slide-sub">How Ethics Drives Long-term Value</p>
                        <div class="stat-highlight-box glass-card mt-3">
                            <span class="big-num">+28%</span>
                            <p><span class="lang-zh">倫理標竿企業 (World's Most Ethical Companies) 長期股票報酬超越標普500指數</span><span class="lang-en">World's Most Ethical Companies outperform S&P 500 stock index by +28%</span></p>
                        </div>
                    </div>

                    <div class="main-panel">
                        <div class="grid-2col gap-3">
                            <div class="value-card glass-card">
                                <div class="v-icon color-1"><i class="fa-solid fa-hand-holding-heart"></i></div>
                                <h3><span class="lang-zh">1. 建立社會信任 (Build Trust)</span><span class="lang-en">1. Build Public Trust</span></h3>
                                <p><span class="lang-zh">信任是商業交易的基石。高誠信企業降低合約交易成本與監督費用。</span><span class="lang-en">Trust is the foundation of business transactions, reducing monitoring costs.</span></p>
                            </div>
                            <div class="value-card glass-card">
                                <div class="v-icon color-2"><i class="fa-solid fa-crown"></i></div>
                                <h3><span class="lang-zh">2. 提升品牌溢價 (Brand Equity)</span><span class="lang-en">2. Enhance Brand Equity</span></h3>
                                <p><span class="lang-zh">消費者願意為具備倫理價值與永續承諾的商品支付高於平均的溢價。</span><span class="lang-en">Consumers pay premium prices for ethically certified products and sustainability.</span></p>
                            </div>
                            <div class="value-card glass-card">
                                <div class="v-icon color-3"><i class="fa-solid fa-shield-cat"></i></div>
                                <h3><span class="lang-zh">3. 顯著降低營運風險 (Risk Mitigation)</span><span class="lang-en">3. Risk Mitigation</span></h3>
                                <p><span class="lang-zh">防範巨額裁罰、訴訟成本、天價賠償與企業形象一夕崩塌的毀滅性打擊。</span><span class="lang-en">Prevent catastrophic litigation costs, regulatory fines, and brand destruction.</span></p>
                            </div>
                            <div class="value-card glass-card">
                                <div class="v-icon color-4"><i class="fa-solid fa-magnet"></i></div>
                                <h3><span class="lang-zh">4. 吸引與留住頂尖人才 (Talent Magnet)</span><span class="lang-en">4. Talent Magnet</span></h3>
                                <p><span class="lang-zh">Gen Z 與千禧世代員工高度關注企業使命 (Purpose)，選擇符合價值的雇主。</span><span class="lang-en">Gen Z and Millennials prefer purpose-driven employers aligned with moral values.</span></p>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 11: Global Corporate Crisis -->
            <section class="slide" id="slide-11" data-title="Slide 11: 全球企業最大的危機">
                <div class="slide-container center-header-layout">
                    <div class="header-block center-text">
                        <div class="section-tag warning-tag"><i class="fa-solid fa-skull-crossbones"></i> Corporate Failure Mode</div>
                        <h2 class="slide-heading giant-title">
                            <span class="lang-zh">全球企業最大的危機，不是產品不好...</span>
                            <span class="lang-en">The Ultimate Threat: Collapse of Trust!</span>
                        </h2>
                        <p class="slide-sub">The Ultimate Threat to Corporate Survival</p>
                    </div>

                    <div class="crisis-card glass-card glow-red">
                        <div class="crisis-main-statement">
                            <h3 class="red-text">
                                <span class="lang-zh">而是「信任崩潰」(Trust Crisis)！</span>
                                <span class="lang-en">It is the "Collapse of Public Trust"!</span>
                            </h3>
                            <p class="crisis-sub-text">
                                <span class="lang-zh">產品不好可以改善技術；但誠信崩潰，企業終將毀於旦夕。</span>
                                <span class="lang-en">Defective products can be engineered; but broken integrity destroys companies overnight.</span>
                            </p>
                        </div>
                        <div class="quote-box-grid mt-4">
                            <div class="quote-item">
                                <i class="fa-solid fa-quote-left quote-icon"></i>
                                <p>
                                    <span class="lang-zh">「建立好名聲需要 20 年，但摧毀它只需要 5 分鐘。如果你想到這一點，做事方式就會截然不同。」</span>
                                    <span class="lang-en">"It takes 20 years to build a reputation and five minutes to ruin it. If you think about that, you'll do things differently."</span>
                                </p>
                                <div class="quote-author">— Warren Buffett (股神 華倫·巴菲特)</div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 12: Activity 1 - CEO Decision Game Scenario -->
            <section class="slide" id="slide-12" data-title="Slide 12: 教學活動一 - CEO 決策挑戰賽 (情境)">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag activity-tag"><i class="fa-solid fa-gamepad"></i> Activity 1 • 15 Minutes</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">CEO 決策挑戰賽</span>
                            <span class="lang-en">Activity 1: CEO Decision Game</span>
                        </h2>
                        <p class="slide-sub">The CEO Dilemma Simulation</p>
                        <div class="rules-card glass-card mt-3">
                            <h4><i class="fa-solid fa-list-check"></i> <span class="lang-zh">活動規則：</span><span class="lang-en">Rules:</span></h4>
                            <ul>
                                <li><span class="lang-zh">全班以 4 人為一組。</span><span class="lang-en">4 students per group.</span></li>
                                <li><span class="lang-zh">時間：15 分鐘 (討論 10m + 投票 5m)。</span><span class="lang-en">15 mins (10m discussion + 5m vote).</span></li>
                                <li><span class="lang-zh">每組推派代表進行最終決策理由說明。</span><span class="lang-en">Nominate a representative to pitch choice.</span></li>
                            </ul>
                        </div>
                    </div>

                    <div class="main-panel">
                        <div class="scenario-card glass-card highlight-border">
                            <div class="scenario-badge"><i class="fa-solid fa-masks-theater"></i> <span class="lang-zh">模擬情境</span><span class="lang-en">Scenario</span></div>
                            <h3><span class="lang-zh">情境描述：生技製藥公司 CEO 的抉擇</span><span class="lang-en">Scenario: Pharma CEO's Ethical Dilemma</span></h3>
                            <p class="scenario-text">
                                <span class="lang-zh">你是上市藥廠 CEO。熱銷保健品單月貢獻 35% 營收。最新內部報告顯示：極少數極端體質者（約萬分之一機率）長期服用可能導致輕微肝功能異常。<strong>現行法規完全合規，政府無強制要求下架。</strong></span>
                                <span class="lang-en">You are CEO of a listed pharma firm. A bestseller yields 35% revenue. Internal labs find a 1-in-10,000 liver risk in extreme body types. <strong>Current laws fully comply and government requires no recall.</strong></span>
                            </p>

                            <div class="options-grid mt-4">
                                <div class="opt-choice">
                                    <div class="choice-tag"><span class="lang-zh">決策 A</span><span class="lang-en">Choice A</span></div>
                                    <h4><span class="lang-zh">全面預防性下架召回</span><span class="lang-en">Full Voluntary Recall</span></h4>
                                    <p><span class="lang-zh">承受數億損毀與股價大跌風險，優先保護少數潛在風險消費者。</span><span class="lang-en">Absorb millions in losses to prioritize consumer health safety.</span></p>
                                </div>
                                <div class="opt-choice">
                                    <div class="choice-tag alt"><span class="lang-zh">決策 B</span><span class="lang-en">Choice B</span></div>
                                    <h4><span class="lang-zh">不下架，僅更新標示警語</span><span class="lang-en">Warning Label Only</span></h4>
                                    <p><span class="lang-zh">保持銷售，於包裝加註微小警語，待政府法規更新再行處理。</span><span class="lang-en">Maintain sales and add small warning font until government mandates.</span></p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 13: Activity 1 - Live Voting & Poll Demo -->
            <section class="slide" id="slide-13" data-title="Slide 13: 活動一 - 全班即時表決">
                <div class="slide-container center-header-layout">
                    <div class="header-block center-text">
                        <div class="section-tag activity-tag"><i class="fa-solid fa-chart-pie"></i> Mentimeter / Slido Interactive Poll</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">全班即時表決：如果你是 CEO，你的選擇？</span>
                            <span class="lang-en">Activity 1: Live Class Poll & Debate</span>
                        </h2>
                        <p class="slide-sub">Cast your vote and observe collective class ethical tendencies</p>
                    </div>

                    <div class="poll-widget-wrapper glass-card">
                        <div class="poll-controls">
                            <button class="poll-vote-btn opt-a" onclick="castVote('A')">
                                <i class="fa-solid fa-box-archive"></i> <span class="lang-zh">選擇 A (全面下架召回)</span><span class="lang-en">Option A (Full Recall)</span>
                            </button>
                            <button class="poll-vote-btn opt-b" onclick="castVote('B')">
                                <i class="fa-solid fa-circle-exclamation"></i> <span class="lang-zh">選擇 B (不下架僅警語)</span><span class="lang-en">Option B (Warning Label)</span>
                            </button>
                            <button class="poll-vote-btn opt-c" onclick="castVote('C')">
                                <i class="fa-solid fa-shield-cat"></i> <span class="lang-zh">選擇 C (條件式替代)</span><span class="lang-en">Option C (Conditional)</span>
                            </button>
                            <button class="poll-vote-btn opt-reset" onclick="resetVote()" title="Reset Votes">
                                <i class="fa-solid fa-rotate-left"></i> <span class="lang-zh">重置</span><span class="lang-en">Reset</span>
                            </button>
                        </div>

                        <div class="poll-results-visualization mt-4">
                            <div class="poll-bar-group">
                                <div class="bar-label"><span class="lang-zh">選項 A：全面下架召回 (Preventive Recall)</span><span class="lang-en">Option A: Preventive Recall</span></div>
                                <div class="bar-track">
                                    <div class="bar-fill fill-a" id="barA" style="width: 0%;">
                                        <span class="bar-percentage" id="percentA">0% (0 票 / 0 votes)</span>
                                    </div>
                                </div>
                            </div>
                            <div class="poll-bar-group mt-3">
                                <div class="bar-label"><span class="lang-zh">選項 B：不下架僅警語 (Warning Label Only)</span><span class="lang-en">Option B: Warning Label Only</span></div>
                                <div class="bar-track">
                                    <div class="bar-fill fill-b" id="barB" style="width: 0%;">
                                        <span class="bar-percentage" id="percentB">0% (0 票 / 0 votes)</span>
                                    </div>
                                </div>
                            </div>
                            <div class="poll-bar-group mt-3">
                                <div class="bar-label"><span class="lang-zh">選項 C：條件式替代方案 (Conditional Action)</span><span class="lang-en">Option C: Conditional Action</span></div>
                                <div class="bar-track">
                                    <div class="bar-fill fill-c" id="barC" style="width: 0%;">
                                        <span class="bar-percentage" id="percentC">0% (0 票 / 0 votes)</span>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <div class="debrief-box mt-4">
                            <i class="fa-solid fa-lightbulb debrief-icon"></i>
                            <div class="debrief-content">
                                <h4><span class="lang-zh">教師觀點帶出 (Key Takeaway)：</span><span class="lang-en">Faculty Debrief:</span></h4>
                                <p>
                                    <span class="lang-zh">「商業倫理決策常沒有絕對標準答案，重點在於<strong>倫理思考與決策論證過程 (Ethical Reasoning)</strong>。當法律沒有強制要求時，你如何排定對利害關係人的責任？」</span>
                                    <span class="lang-en">"Business ethics dilemmas rarely have single right answers. Focus is on <strong>Ethical Reasoning</strong> and stakeholder priority when law is silent."</span>
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 14: Case Study 1 - Enron -->
            <section class="slide" id="slide-14" data-title="Slide 14: 企業倫理失敗案例：Enron">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag warning-tag"><i class="fa-solid fa-building-circle-xmark"></i> Part III • Failure Cases</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">案例一：安隆案 (Enron Collapse)</span>
                            <span class="lang-en">Case Study 1: Enron Collapse</span>
                        </h2>
                        <p class="slide-sub">The Wall Street Titan That Vanished</p>
                        <div class="img-wrapper glass-card mt-3">
                            <img src="corporate_crisis_illustration.jpg" alt="Corporate Failure Visual" class="slide-img rounded">
                        </div>
                    </div>

                    <div class="main-panel">
                        <div class="glass-card feature-card mb-4">
                            <h3><i class="fa-solid fa-skull accent-icon"></i> <span class="lang-zh">發生了什麼事？ (What Happened?)</span><span class="lang-en">What Happened?</span></h3>
                            <p class="lead-p">
                                <span class="lang-zh">Enron 曾是美國第 7 大企業、獲選為「美國最具創新力公司」。然而在 2001 年，這座千億金融帝國卻在短短幾週內宣告破產。</span>
                                <span class="lang-en">Enron was the 7th largest US corporation. In 2001, this energy giant collapsed into bankruptcy in weeks.</span>
                            </p>
                        </div>

                        <div class="grid-2col gap-3">
                            <div class="info-box glass-card">
                                <h4><i class="fa-solid fa-calculator red-text"></i> <span class="lang-zh">會計造假與 SPE 隱瞞債務</span><span class="lang-en">SPE Off-Balance Fraud</span></h4>
                                <p><span class="lang-zh">利用特殊目的實體 (SPE) 隱藏數百億美元債務，透過「Mark-to-Market」將未來估計收益提早認列為當期獲利。</span><span class="lang-en">Used SPEs to hide debt and mark-to-market accounting to inflate current profits.</span></p>
                            </div>
                            <div class="info-box glass-card">
                                <h4><i class="fa-solid fa-masks-theater red-text"></i> <span class="lang-zh">貪婪文化與內部控管失靈</span><span class="lang-en">Culture of Greed</span></h4>
                                <p><span class="lang-zh">倡導極端競爭與短期績效導向（Rank and Yank 淘汰制），高階主管集體隱瞞真相，內部舉報者遭打壓。</span><span class="lang-en">Rank-and-yank culture rewarded greed while whistleblowers were silenced.</span></p>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 15: Enron Timeline & Impact -->
            <section class="slide" id="slide-15" data-title="Slide 15: Enron 時間軸與影響">
                <div class="slide-container">
                    <div class="header-block">
                        <div class="section-tag warning-tag"><i class="fa-solid fa-timeline"></i> Historical Timeline</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">Enron 事件時間軸與制度崩壞的連帶代價</span>
                            <span class="lang-en">Enron Timeline & SOX Regulatory Impact</span>
                        </h2>
                        <p class="slide-sub">Systemic Failure and Regulatory Aftermath</p>
                    </div>

                    <div class="timeline-wrapper glass-card mt-3">
                        <div class="timeline-events">
                            <div class="t-event">
                                <div class="t-year">2000 年</div>
                                <h4><span class="lang-zh">股價歷史新高 $90.75</span><span class="lang-en">Peak Stock $90.75</span></h4>
                                <p><span class="lang-zh">被譽為華爾街最耀眼的能源交易巨擘。</span><span class="lang-en">Acclaimed as Wall Street's most innovative energy titan.</span></p>
                            </div>
                            <div class="t-arrow"><i class="fa-solid fa-chevron-right"></i></div>

                            <div class="t-event">
                                <div class="t-year">2001年 8月</div>
                                <h4><span class="lang-zh">副總裁 Sherron Watkins 舉報</span><span class="lang-en">Whistleblower Memo</span></h4>
                                <p><span class="lang-zh">內部信件警告 CEO「公司將在會計醜聞中爆炸」。</span><span class="lang-en">Warned CEO company would "implode in a wave of accounting scandals."</span></p>
                            </div>
                            <div class="t-arrow"><i class="fa-solid fa-chevron-right"></i></div>

                            <div class="t-event">
                                <div class="t-year">2001年 12月</div>
                                <h4><span class="lang-zh">宣告破產 (Bankruptcy)</span><span class="lang-en">Bankruptcy Filing</span></h4>
                                <p><span class="lang-zh">股價跌至 $0.26，市值蒸發 600 億美元。</span><span class="lang-en">Stock plummeted to $0.26, wiping out $60B market cap.</span></p>
                            </div>
                            <div class="t-arrow"><i class="fa-solid fa-chevron-right"></i></div>

                            <div class="t-event highlight-event">
                                <div class="t-year"><span class="lang-zh">連帶影響</span><span class="lang-en">Aftermath</span></div>
                                <h4><span class="lang-zh">全球會計與法規重塑</span><span class="lang-en">Arthur Andersen & SOX</span></h4>
                                <p><span class="lang-zh">百年名店安達信解體，催生《薩班斯法案》(SOX Act)。</span><span class="lang-en">Arthur Andersen dissolved; triggered Sarbanes-Oxley Act enactment.</span></p>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 16: Case Study 2 - VW Dieselgate -->
            <section class="slide" id="slide-16" data-title="Slide 16: 案例二：Volkswagen 柴油門">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag warning-tag"><i class="fa-solid fa-car-burst"></i> Case 2 • Environmental Deception</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">案例二：福斯汽車柴油門 (Volkswagen Dieselgate)</span>
                            <span class="lang-en">Case Study 2: VW Dieselgate Deception</span>
                        </h2>
                        <p class="slide-sub">Engineering Genius Turned Ethics Disaster</p>
                        <div class="stat-highlight-box glass-card mt-3 glow-red">
                            <span class="big-num">$33B+</span>
                            <p><span class="lang-zh">福斯累積支付賠償金、罰鍰與召回費用超過 330 億歐元</span><span class="lang-en">VW total fines, recalls and legal settlements exceeded €33 Billion</span></p>
                        </div>
                    </div>

                    <div class="main-panel">
                        <div class="glass-card feature-card mb-4">
                            <h3><i class="fa-solid fa-microchip accent-icon"></i> <span class="lang-zh">「作弊軟體」(Defeat Device) 事件始末</span><span class="lang-en">Defeat Device Deception</span></h3>
                            <p>
                                <span class="lang-zh">2015 年美國環保署 (EPA) 揭發福斯在超過 1,100 萬輛柴油車中安裝特別軟體。檢驗時開啟最大減排，常態行駛廢氣排放超標高達 40 倍！</span>
                                <span class="lang-en">In 2015, EPA caught VW using software in 11M diesel cars that activated emission controls only during testing, emitting 40x legal NOx limits normally.</span>
                            </p>
                        </div>

                        <div class="video-news-mockup glass-card">
                            <div class="mockup-header">
                                <i class="fa-solid fa-newspaper"></i> News Snapshot
                            </div>
                            <div class="mockup-body">
                                <h4>"Volkswagen Clean Diesel Propaganda Breakdown"</h4>
                                <p class="text-muted"><span class="lang-zh">主打「Clean Diesel」廣告，實質為史上最大商業詐欺個案之一，重創「德國製造」誠信形象。</span><span class="lang-en">Marketed as "Clean Diesel", it became one of history's largest commercial frauds destroying German engineering trust.</span></p>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 17: VW Root Cause Analysis -->
            <section class="slide" id="slide-17" data-title="Slide 17: VW 根因分析">
                <div class="slide-container center-header-layout">
                    <div class="header-block center-text">
                        <div class="section-tag"><i class="fa-solid fa-magnifying-glass-chart"></i> Root Cause Diagnosis</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">為什麼頂尖工程師與高階主管會做錯決策？</span>
                            <span class="lang-en">VW Root Cause Diagnosis & Failure Modes</span>
                        </h2>
                        <p class="slide-sub">Psychological and Cultural Drivers of Corporate Misconduct</p>
                    </div>

                    <div class="cards-grid-4">
                        <div class="rc-card glass-card">
                            <div class="rc-num">01</div>
                            <h4><span class="lang-zh">高壓極端目標</span><span class="lang-en">1. Unrealistic Targets</span></h4>
                            <p><span class="lang-zh">高層下達「極限技術與成本目標」，不允許工程師表達「技術辦不到」。</span><span class="lang-en">Top management set impossible cost/tech targets without accepting "impossible".</span></p>
                        </div>
                        <div class="rc-card glass-card">
                            <div class="rc-num">02</div>
                            <h4><span class="lang-zh">高層權威恐懼</span><span class="lang-en">2. Toxic Tone at Top</span></h4>
                            <p><span class="lang-zh">權威式管理文化，員工出於恐懼心理而選擇隱瞞瑕疵與合謀作弊。</span><span class="lang-en">Authoritarian fear-driven culture forced engineers into fraudulent compliance.</span></p>
                        </div>
                        <div class="rc-card glass-card">
                            <div class="rc-num">03</div>
                            <h4><span class="lang-zh">倫理盲點與合理化</span><span class="lang-en">3. Ethical Blindspots</span></h4>
                            <p><span class="lang-zh">將「軟體寫碼」視為純技術工程挑戰，脫離了社會責任與空氣污染後果。</span><span class="lang-en">Engineers treated coding as a pure technical puzzle ignoring pollution consequences.</span></p>
                        </div>
                        <div class="rc-card glass-card">
                            <div class="rc-num">04</div>
                            <h4><span class="lang-zh">合規防線失靈</span><span class="lang-en">4. Compliance Breakdown</span></h4>
                            <p><span class="lang-zh">內部稽核與法律合規部門未能發揮制衡作用，缺乏有效獨立舉報管道。</span><span class="lang-en">Internal audit and legal compliance failed as checks; whistleblower channels absent.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 18: Comparative Matrix: Enron vs VW -->
            <section class="slide" id="slide-18" data-title="Slide 18: Enron vs VW 失敗模式比較">
                <div class="slide-container">
                    <div class="header-block">
                        <div class="section-tag"><i class="fa-solid fa-code-compare"></i> Comparative Analysis</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">Enron vs. VW 共同失敗模式比較表</span>
                            <span class="lang-en">Comparative Matrix: Enron vs. Volkswagen</span>
                        </h2>
                        <p class="slide-sub">Common Pattern of Corporate Ethical Disasters</p>
                    </div>

                    <div class="matrix-table-wrapper glass-card mt-3">
                        <table class="custom-matrix-table">
                            <thead>
                                <tr>
                                    <th><span class="lang-zh">分析面向</span><span class="lang-en">Dimension</span></th>
                                    <th>Enron (US Energy)</th>
                                    <th>Volkswagen (German Auto)</th>
                                    <th class="highlight-th"><span class="lang-zh">核心共同根因</span><span class="lang-en">Common Root Cause</span></th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td><strong><span class="lang-zh">作弊手段</span><span class="lang-en">Deceptive Method</span></strong></td>
                                    <td><span class="lang-zh">會計手法 (SPE) 隱匿負債</span><span class="lang-en">SPE Accounting Fraud</span></td>
                                    <td><span class="lang-zh">軟體控制 (Defeat Device) 作弊</span><span class="lang-en">Software Defeat Device</span></td>
                                    <td><span class="badge warning-badge"><span class="lang-zh">利用專業技術壁壘隱瞞真相</span><span class="lang-en">Deception via technical complexity</span></span></td>
                                </tr>
                                <tr>
                                    <td><strong><span class="lang-zh">組織文化</span><span class="lang-en">Corporate Culture</span></strong></td>
                                    <td><span class="lang-zh">貪婪獎勵、高壓排名淘汰</span><span class="lang-en">Greed & Rank-and-yank</span></td>
                                    <td><span class="lang-zh">權威命令、不容許技術失敗</span><span class="lang-en">Authoritarian Fear</span></td>
                                    <td><span class="badge warning-badge"><span class="lang-zh">出於恐懼與利益的合謀沈默</span><span class="lang-en">Culture of fear and silence</span></span></td>
                                </tr>
                                <tr>
                                    <td><strong><span class="lang-zh">治理漏洞</span><span class="lang-en">Governance Flaws</span></strong></td>
                                    <td><span class="lang-zh">董事會受欺瞞、會計師失靈</span><span class="lang-en">Board misled & auditor failed</span></td>
                                    <td><span class="lang-zh">家族股東掌控、內部控管形同虛設</span><span class="lang-en">Family control & weak controls</span></td>
                                    <td><span class="badge warning-badge"><span class="lang-zh">缺乏獨立有效監督機制</span><span class="lang-en">Lack of independent checks</span></span></td>
                                </tr>
                                <tr>
                                    <td><strong><span class="lang-zh">後果代價</span><span class="lang-en">Consequences</span></strong></td>
                                    <td><span class="lang-zh">公司解體破產、高層入獄</span><span class="lang-en">Bankruptcy & prison</span></td>
                                    <td><span class="lang-zh">千億罰金賠償、執行長起訴</span><span class="lang-en">€33B+ fines & CEO indicted</span></td>
                                    <td><span class="badge red-badge"><span class="lang-zh">信任崩潰與品牌致命衝擊</span><span class="lang-en">Fatal collapse of trust</span></span></td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </section>

            <!-- SLIDE 19: AI Ethics -->
            <section class="slide" id="slide-19" data-title="Slide 19: AI 時代的企業倫理">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag tech-tag"><i class="fa-solid fa-brain"></i> Frontier Ethics</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">今天如果是 AI 巨頭呢？</span>
                            <span class="lang-en">Frontier Ethics: Responsible AI & Tech</span>
                        </h2>
                        <p class="slide-sub">Responsible AI & Tech Governance</p>
                        <div class="img-wrapper glass-card mt-3">
                            <img src="esg_ai_future_illustration.jpg" alt="AI & ESG Future Visual" class="slide-img rounded">
                        </div>
                    </div>

                    <div class="main-panel">
                        <div class="grid-2col gap-3">
                            <div class="tech-card glass-card">
                                <div class="tech-logo"><i class="fa-brands fa-google"></i> Google / Meta</div>
                                <h4><span class="lang-zh">數據隱私與演算法偏見</span><span class="lang-en">Data Privacy & Bias</span></h4>
                                <p><span class="lang-zh">廣告精準投放與個人隱私邊界，招聘與信用評估 AI 是否複製人類偏見？</span><span class="lang-en">Targeted ads privacy boundary; recruitment AI replicating gender/race bias.</span></p>
                            </div>
                            <div class="tech-card glass-card">
                                <div class="tech-logo"><i class="fa-solid fa-robot"></i> OpenAI / Anthropic</div>
                                <h4><span class="lang-zh">AI 安全與安全防禦 (Alignment)</span><span class="lang-en">AI Safety & Alignment</span></h4>
                                <p><span class="lang-zh">模型能力快速擴張下，如何防止假訊息暴增、著作權侵權與科技濫用風險？</span><span class="lang-en">Preventing deepfake misinformation, copyright infringement, and dual-use risks.</span></p>
                            </div>
                        </div>

                        <div class="glass-card feature-card mt-3">
                            <h3><i class="fa-solid fa-gavel accent-icon"></i> <span class="lang-zh">負責任 AI 治理 4 大柱石</span><span class="lang-en">4 Responsible AI Pillars</span></h3>
                            <div class="grid-4col mt-2 center-text">
                                <div class="p-item"><i class="fa-solid fa-eye"></i> <strong><span class="lang-zh">透明度 (Transparency)</span><span class="lang-en">Transparency</span></strong></div>
                                <div class="p-item"><i class="fa-solid fa-scale-balanced"></i> <strong><span class="lang-zh">公平性 (Fairness)</span><span class="lang-en">Fairness</span></strong></div>
                                <div class="p-item"><i class="fa-solid fa-user-shield"></i> <strong><span class="lang-zh">隱私保護 (Privacy)</span><span class="lang-en">Privacy</span></strong></div>
                                <div class="p-item"><i class="fa-solid fa-hand-holding-hand"></i> <strong><span class="lang-zh">問責制 (Accountability)</span><span class="lang-en">Accountability</span></strong></div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 20: Activity 2 - Ethics in News -->
            <section class="slide" id="slide-20" data-title="Slide 20: 活動二 - 最新新聞分析">
                <div class="slide-container">
                    <div class="header-block">
                        <div class="section-tag activity-tag"><i class="fa-solid fa-newspaper"></i> Activity 2 • 20 Minutes</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">企業倫理新聞即時分析競賽 (Ethics in News)</span>
                            <span class="lang-en">Activity 2: Ethics in News Competition</span>
                        </h2>
                        <p class="slide-sub">Analyze Contemporary Corporate Scandals Using 4-Step Framework</p>
                    </div>

                    <div class="news-cards-grid mt-3">
                        <div class="news-company-card glass-card">
                            <span class="company-badge">Toyota 豐田</span>
                            <h4><span class="lang-zh">測試認證造假疑雲</span><span class="lang-en">Safety Test Data Fraud</span></h4>
                            <p><span class="lang-zh">品質安全測試數據不實，傳統工匠精神面臨誠信檢驗。</span><span class="lang-en">Falsified collision test data challenging traditional artisan trust.</span></p>
                        </div>
                        <div class="news-company-card glass-card">
                            <span class="company-badge">Meta / FB</span>
                            <h4><span class="lang-zh">青少年心理健康疑慮</span><span class="lang-en">Youth Mental Health Harm</span></h4>
                            <p><span class="lang-zh">演算法推播致成癮，內部研究顯示傷害青少年心理卻維持推播。</span><span class="lang-en">Algorithms driving addiction despite internal research showing teen harm.</span></p>
                        </div>
                        <div class="news-company-card glass-card">
                            <span class="company-badge">Nike 零路</span>
                            <h4><span class="lang-zh">海外供應鏈勞工爭議</span><span class="lang-en">Supply Chain Sweatshops</span></h4>
                            <p><span class="lang-zh">永續宣言與海外代工廠勞動條件、薪資保障之落差。</span><span class="lang-en">Gap between sustainability marketing and overseas factory labor conditions.</span></p>
                        </div>
                        <div class="news-company-card glass-card">
                            <span class="company-badge">Tesla 特斯拉</span>
                            <h4><span class="lang-zh">Autopilot 宣傳與安全</span><span class="lang-en">FSD Marketing & Safety</span></h4>
                            <p><span class="lang-zh">全自動駕駛 (FSD) 行銷用語是否過度誇大導致消費者誤判？</span><span class="lang-en">Exaggerated Full-Self Driving claims leading to consumer safety risks.</span></p>
                        </div>
                    </div>

                    <div class="framework-box glass-card mt-3">
                        <h4><i class="fa-solid fa-list-check accent-icon"></i> <span class="lang-zh">小組討論 4 大核心問題 (4 Questions Framework)：</span><span class="lang-en">4-Step Analysis Framework:</span></h4>
                        <div class="grid-4col mt-2">
                            <div class="f-q"><strong>(1) What happened?</strong><br><span class="lang-zh">事件事實真相？</span><span class="lang-en">Factual overview?</span></div>
                            <div class="f-q"><strong>(2) Who is affected?</strong><br><span class="lang-zh">哪些利害關係人受害？</span><span class="lang-en">Affected stakeholders?</span></div>
                            <div class="f-q"><strong>(3) What to do?</strong><br><span class="lang-zh">企業現有處理措施是否充足？</span><span class="lang-en">Current company response?</span></div>
                            <div class="f-q"><strong>(4) If you were CEO?</strong><br><span class="lang-zh">若你是 CEO 會如何挽回信任？</span><span class="lang-en">Action plan as CEO?</span></div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 21: Activity 2 - Presentations & Feedback -->
            <section class="slide" id="slide-21" data-title="Slide 21: 活動二 - 各組發表與彙整">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag activity-tag"><i class="fa-solid fa-microphone-lines"></i> Team Presentation</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">小組 3 分鐘精準發表</span>
                            <span class="lang-en">Activity 2: Team Pitch & Debrief</span>
                        </h2>
                        <p class="slide-sub">Executive Pitch & Teacher Feedback</p>
                        <div class="timer-box glass-card center-text mt-4">
                            <div class="giant-num">3:00</div>
                            <p><span class="lang-zh">每組發表限時 3 分鐘 (包含問答)</span><span class="lang-en">3 Minutes pitch per team</span></p>
                        </div>
                    </div>

                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-bullseye accent-icon"></i> <span class="lang-zh">教師評析與共同倫理漏洞總結</span><span class="lang-en">Faculty Debrief & Corporate Pitfalls</span></h3>
                            <div class="grid-2col mt-3 gap-3">
                                <div class="summary-card-sm">
                                    <h4><i class="fa-solid fa-triangle-exclamation red-text"></i> <span class="lang-zh">常見企業集體盲點</span><span class="lang-en">Common Blindspots</span></h4>
                                    <ul>
                                        <li><span class="lang-zh">「法律沒禁止就先做」(Legalistic Myopia)</span><span class="lang-en">"Doing whatever law doesn't forbid"</span></li>
                                        <li><span class="lang-zh">「大家都這樣做」(Normalization of Deviance)</span><span class="lang-en">"Normalization of Deviance"</span></li>
                                        <li><span class="lang-zh">「只要業績達標細節不重要」(Result-Oriented)</span><span class="lang-en">"Results over means"</span></li>
                                    </ul>
                                </div>
                                <div class="summary-card-sm">
                                    <h4><i class="fa-solid fa-shield-halved green-text"></i> <span class="lang-zh">高階決策者的倫理解方</span><span class="lang-en">Ethical Solutions</span></h4>
                                    <ul>
                                        <li><span class="lang-zh">建立心理安全感 (Psychological Safety)</span><span class="lang-en">Build Psychological Safety</span></li>
                                        <li><span class="lang-zh">暢通舉報者機制與保護</span><span class="lang-en">Whistleblower Protection</span></li>
                                        <li><span class="lang-zh">將 ESG 永續指標納入高階主管 KPI 考核</span><span class="lang-en">Tie ESG metrics to Executive KPIs</span></li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 22: Ethics to ESG Roadmap -->
            <section class="slide" id="slide-22" data-title="Slide 22: 企業倫理如何變成 ESG">
                <div class="slide-container center-header-layout">
                    <div class="header-block center-text">
                        <div class="section-tag"><i class="fa-solid fa-diagram-project"></i> Part IV • The Sustainable Horizon</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">企業倫理到 ESG 的永續演進藍圖</span>
                            <span class="lang-en">Paradigm Shift: Business Ethics to ESG</span>
                        </h2>
                        <p class="slide-sub">Evolutionary Path from Internal Principles to External Standards</p>
                    </div>

                    <div class="evolution-chain-card glass-card">
                        <div class="chain-items">
                            <div class="c-node">
                                <div class="c-icon"><i class="fa-solid fa-heart"></i></div>
                                <h4>Business Ethics</h4>
                                <p><span class="lang-zh">企業倫理信念 (Moral Compass)</span><span class="lang-en">Internal Moral Compass</span></p>
                            </div>
                            <div class="c-connector"><i class="fa-solid fa-arrow-right-long"></i></div>

                            <div class="c-node">
                                <div class="c-icon"><i class="fa-solid fa-hand-holding-hand"></i></div>
                                <h4>CSR</h4>
                                <p><span class="lang-zh">企業社會責任 (CSR Actions)</span><span class="lang-en">Social Responsibility Actions</span></p>
                            </div>
                            <div class="c-connector"><i class="fa-solid fa-arrow-right-long"></i></div>

                            <div class="c-node active-node">
                                <div class="c-icon"><i class="fa-solid fa-leaf"></i></div>
                                <h4>ESG Data</h4>
                                <p><span class="lang-zh">E、S、G 可量化績效數據</span><span class="lang-en">Quantitative ESG Metrics</span></p>
                            </div>
                            <div class="c-connector"><i class="fa-solid fa-arrow-right-long"></i></div>

                            <div class="c-node highlight-node">
                                <div class="c-icon"><i class="fa-solid fa-tree"></i></div>
                                <h4>Sustainable Enterprise</h4>
                                <p><span class="lang-zh">永續經營與長遠價值創造</span><span class="lang-en">Long-term Value Creation</span></p>
                            </div>
                        </div>

                        <div class="chain-explanation mt-4">
                            <p>
                                <span class="lang-zh">「<strong>企業倫理</strong>是組織的靈魂與內在基因；<strong>CSR</strong>是企業展現的責任行動；<strong>ESG</strong>則是以國際標準將這些行動轉化為資本市場與投資人看得懂的<strong>可量化數據與治理結構</strong>。」</span>
                                <span class="lang-en">"<strong>Business Ethics</strong> is the internal DNA; <strong>CSR</strong> represents social action; <strong>ESG</strong> converts these actions into <strong>measurable data and governance standards</strong> for capital markets."</span>
                            </p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 23: Key Takeaways -->
            <section class="slide" id="slide-23" data-title="Slide 23: 本週重點整理">
                <div class="slide-container center-header-layout">
                    <div class="header-block center-text">
                        <div class="section-tag"><i class="fa-solid fa-bookmark"></i> Key Takeaways</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">Week 1 核心重點總結</span>
                            <span class="lang-en">Week 1 Summary & Key Takeaways</span>
                        </h2>
                        <p class="slide-sub">Summary of Fundamental Concepts</p>
                    </div>

                    <div class="takeaways-grid-4">
                        <div class="t-card glass-card">
                            <div class="t-number">01</div>
                            <h3><span class="lang-zh">企業非僅賺錢機器</span><span class="lang-en">1. Beyond Profit</span></h3>
                            <p><span class="lang-zh">從股東至上轉向利害關係人資本主義，創造社會價值才是長青關鍵。</span><span class="lang-en">Shift from shareholder primacy to stakeholder capitalism creating social value.</span></p>
                        </div>
                        <div class="t-card glass-card">
                            <div class="t-number">02</div>
                            <h3><span class="lang-zh">法律 ≠ 倫理上限</span><span class="lang-en">2. Law ≠ Ethics Limit</span></h3>
                            <p><span class="lang-zh">法律是最低底線，企業倫理要求超越合規，追求社會誠信與公正。</span><span class="lang-en">Law is only the floor; business ethics requires going beyond legal compliance.</span></p>
                        </div>
                        <div class="t-card glass-card">
                            <div class="t-number">03</div>
                            <h3><span class="lang-zh">信任是無形資產</span><span class="lang-en">3. Trust is Asset</span></h3>
                            <p><span class="lang-zh">Enron 與 VW 警示我們：產品失敗可重來，誠信崩潰將招致致命滅頂。</span><span class="lang-en">Enron and VW warn us: Product failure can be fixed; trust collapse is fatal.</span></p>
                        </div>
                        <div class="t-card glass-card">
                            <div class="t-number">04</div>
                            <h3><span class="lang-zh">倫理是 ESG 的基因</span><span class="lang-en">4. Ethics is ESG DNA</span></h3>
                            <p><span class="lang-zh">ESG 與永續轉型不是時尚流行口號，而是扎根於企業誠信治理的實踐。</span><span class="lang-en">ESG is not a trendy slogan, but grounded in genuine governance integrity.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 24: Homework Assignment -->
            <section class="slide" id="slide-24" data-title="Slide 24: 本週課堂作業 (Homework 1)">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag homework-tag"><i class="fa-solid fa-pen-ruler"></i> Homework 1 • Due Next Week</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">課堂作業說明</span>
                            <span class="lang-en">Homework 1 Guidelines & Rubrics</span>
                        </h2>
                        <p class="slide-sub">Individual Case Study Assignment</p>
                        
                        <div class="hw-summary-card glass-card mt-3">
                            <ul class="hw-meta-list">
                                <li><i class="fa-solid fa-file-word"></i> <strong><span class="lang-zh">字數要求：</span><span class="lang-en">Length: </span></strong> 1,000 – 1,200 <span class="lang-zh">字</span><span class="lang-en">words</span></li>
                                <li><i class="fa-solid fa-calendar-xmark"></i> <strong><span class="lang-zh">繳交期限：</span><span class="lang-en">Deadline: </span></strong> <span class="lang-zh">下週上課前 (Moodle 系統)</span><span class="lang-en">Next class before lecture</span></li>
                                <li><i class="fa-solid fa-spell-check"></i> <strong><span class="lang-zh">格式：</span><span class="lang-en">Format: </span></strong> PDF <span class="lang-zh">格式，標註參考文獻</span><span class="lang-en">with references</span></li>
                            </ul>
                        </div>
                    </div>

                    <div class="main-panel">
                        <div class="glass-card feature-card mb-3">
                            <h3><i class="fa-solid fa-question-circle accent-icon"></i> <span class="lang-zh">作業題目與 5 大分析架構</span><span class="lang-en">Assignment Prompt & 5-Step Structure</span></h3>
                            <p class="mb-2"><span class="lang-zh">請選擇一家國內外企業，搜尋近 3 年內發生的倫理、ESG 或公司治理事件，寫作包含：</span><span class="lang-en">Select a firm with an ethical/ESG scandal within 3 years and write:</span></p>
                            <ol class="styled-num-list">
                                <li><strong><span class="lang-zh">事件背景概述 (約 200 字)：</span><span class="lang-en">Background Overview (~200w): </span></strong> <span class="lang-zh">客觀還原時間、地點與事態發酵經過。</span><span class="lang-en">Factual timeline and key events.</span></li>
                                <li><strong><span class="lang-zh">利害關係人圖譜分析 (Stakeholder Mapping)：</span><span class="lang-en">Stakeholder Mapping: </span></strong> <span class="lang-zh">說明受影響的關鍵個體與組織。</span><span class="lang-en">Identify affected individuals & organizations.</span></li>
                                <li><strong><span class="lang-zh">倫理兩難診斷 (Ethical Dilemma)：</span><span class="lang-en">Ethical Dilemma Diagnosis: </span></strong> <span class="lang-zh">剖析為何此事件構成倫理衝突？涉及哪些道德原則？</span><span class="lang-en">Diagnose core moral conflicts and breached principles.</span></li>
                                <li><strong><span class="lang-zh">CEO 替代決策方案 (Action Plan)：</span><span class="lang-en">CEO Action Plan: </span></strong> <span class="lang-zh">若你是 CEO，具體 short-term & long-term 解方？</span><span class="lang-en">Formulate short-term & long-term solutions as CEO.</span></li>
                                <li><strong><span class="lang-zh">個人學習與反思 (Personal Reflection)：</span><span class="lang-en">Personal Reflection: </span></strong> <span class="lang-zh">本個案對你未來管理倫理素養的啟示。</span><span class="lang-en">Personal managerial integrity takeaways.</span></li>
                            </ol>
                        </div>

                        <div class="glass-card rubrics-card">
                            <h4><i class="fa-solid fa-chart-bar accent-icon"></i> AACSB <span class="lang-zh">評分標準</span><span class="lang-en">Rubrics Breakdown</span></h4>
                            <div class="rubrics-bar">
                                <div class="r-seg seg-1" style="width: 20%;"><span class="lang-zh">事件介紹 20%</span><span class="lang-en">Background 20%</span></div>
                                <div class="r-seg seg-2" style="width: 30%;"><span class="lang-zh">倫理分析 30%</span><span class="lang-en">Ethics 30%</span></div>
                                <div class="r-seg seg-3" style="width: 30%;"><span class="lang-zh">解決方案 30%</span><span class="lang-en">Solution 30%</span></div>
                                <div class="r-seg seg-4" style="width: 20%;"><span class="lang-zh">個人反思 20%</span><span class="lang-en">Reflection 20%</span></div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

        </main>

        <!-- Slide Overview Grid Modal (Toggled by G or button) -->
        <div class="grid-modal" id="gridModal">
            <div class="grid-modal-header">
                <h2><i class="fa-solid fa-table-cells"></i> <span class="lang-zh">投影片全覽 (24 Slides Overview)</span><span class="lang-en">24 Slides Overview</span></h2>
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
            <span class="slide-counter"><span id="currentSlideNum">1</span> / <span id="totalSlideNum">24</span></span>
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

with open(r"C:\Users\User\Desktop\第1週_企業為何需要倫理\index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Successfully generated 100% complete bilingual index.html for all 24 slides!")
