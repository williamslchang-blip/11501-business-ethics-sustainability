import sys

html_week15 = """<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Week 15: ESG Consulting Capstone | ESG企業顧問專題：永續策略提案</title>
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
                <h1 class="deck-title">Week 15: ESG Consulting Capstone Project</h1>
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
            <a href="第15週_ESG企業顧問專題.docx" download class="btn btn-secondary" title="Download Teaching Facilitation Guide (.docx)">
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
                            <span class="meta-tag">Master of Business Administration / AACSB AoL Standard</span>
                            <span class="meta-tag alt">Week 15 • Capstone Consulting Project</span>
                        </div>
                        <h1 class="main-heading">
                            <span class="lang-zh">ESG企業顧問專題：永續策略提案</span>
                            <span class="lang-en">ESG Consulting Capstone Project</span>
                        </h1>
                        <h2 class="sub-heading">
                            <span class="lang-zh">ESG Consulting Capstone Project</span>
                            <span class="lang-en">ESG Consulting Capstone Project</span>
                        </h2>
                        <p class="lead-text">
                            <span class="lang-zh">7 大維度 ESG 健康檢查、2035 策略藍圖、KPI 儀表板與董事會簡報提案大賽</span>
                            <span class="lang-en">7-Dimension ESG Health Check, 2035 Strategy Roadmap & Board Presentation Pitch</span>
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
                            <img src="week15_capstone_cover.jpg" alt="Week 15 Cover Visual" class="slide-img">
                            <div class="visual-badge">
                                <i class="fa-solid fa-graduation-cap"></i> Capstone • Board Pitch • AoL
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 2: W1-W14 Full Journey Synthesis -->
            <section class="slide" id="slide-2" data-title="Slide 2: 14 週全景知識總復習">
                <div class="slide-container center-header-layout">
                    <div class="header-block center-text">
                        <div class="section-tag"><i class="fa-solid fa-diagram-project"></i> 14-Week Knowledge Synthesis</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">W1–W14 全課程 14 週知識脈絡總復習</span>
                            <span class="lang-en">W1-W14 Comprehensive Knowledge Synthesis</span>
                        </h2>
                    </div>

                    <div class="cards-grid-5 mt-3">
                        <div class="decision-card glass-card"><h4>W1-3 Foundations</h4><p><span class="lang-zh">Ethics • CSR • CSV</span><span class="lang-en">Ethics & CSR</span></p></div>
                        <div class="decision-card glass-card"><h4>W4-8 ESG Core</h4><p><span class="lang-zh">E/S/G • Climate • GRI</span><span class="lang-en">ESG Pillars</span></p></div>
                        <div class="decision-card glass-card"><h4>W9-11 Enablers</h4><p><span class="lang-zh">Finance • Chain • AI</span><span class="lang-en">Finance, Chain, AI</span></p></div>
                        <div class="decision-card glass-card"><h4>W12 Strategy</h4><p><span class="lang-zh">VRIO • BMI • PaaS</span><span class="lang-en">VRIO & PaaS</span></p></div>
                        <div class="decision-card glass-card"><h4>W13-14 Practice</h4><p><span class="lang-zh">Cases • Crisis</span><span class="lang-en">Cases & Crisis</span></p></div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 3: Today, You Are ESG Consultants! -->
            <section class="slide" id="slide-3" data-title="Slide 3: 今天，你們是 ESG 顧問！">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-briefcase"></i> Consulting Roleplay</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">今天，你們是頂尖 ESG 策略顧問！</span>
                            <span class="lang-en">Today, You Are ESG Strategy Consultants!</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-user-tie accent-icon"></i> <span class="lang-zh">模擬 McKinsey, BCG, Deloitte, PwC, EY, KPMG 顧問</span><span class="lang-en">Simulating Top Global ESG Management Consultants</span></h3>
                            <p><span class="lang-zh">擺脫學生被動吸收角色！各組化身為頂尖顧問公司，受目標企業董事會重金委託，為其進行全方位的永續健檢與 2035 轉型提案！</span>
                            <span class="lang-en">Stepping into the shoes of elite management consultants presenting to corporate boards.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 4: Capstone Consulting Workflow -->
            <section class="slide" id="slide-4" data-title="Slide 4: Capstone 專案流程 5 步驟">
                <div class="slide-container center-header-layout">
                    <div class="header-block center-text">
                        <div class="section-tag"><i class="fa-solid fa-route"></i> 5-Step Workflow</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">Capstone 顧問專案流程 5 大步驟</span>
                            <span class="lang-en">5-Step Capstone Consulting Workflow</span>
                        </h2>
                    </div>

                    <div class="cards-grid-5 mt-3">
                        <div class="decision-card glass-card"><h4>1. Diagnosis</h4><p><span class="lang-zh">現況健檢診斷</span><span class="lang-en">Health Check</span></p></div>
                        <div class="decision-card glass-card"><h4>2. Analysis</h4><p><span class="lang-zh">SWOT / Materiality</span><span class="lang-en">Root cause audit</span></p></div>
                        <div class="decision-card glass-card"><h4>3. Strategy</h4><p><span class="lang-zh">2035 策略藍圖</span><span class="lang-en">2035 Roadmap</span></p></div>
                        <div class="decision-card glass-card"><h4>4. KPI Design</h4><p><span class="lang-zh">量化儀表板</span><span class="lang-en">KPI Dashboard</span></p></div>
                        <div class="decision-card glass-card"><h4>5. Board Pitch</h4><p><span class="lang-zh">董事會提案簡報</span><span class="lang-en">Board Presentation</span></p></div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 5: The Consultant Mindset -->
            <section class="slide" id="slide-5" data-title="Slide 5: 顧問思維與 ROI 評估">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-lightbulb"></i> Consultant Mindset</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">顧問思維：問題、原因、方案與 ROI</span>
                            <span class="lang-en">Consultant Mindset & ROI Rigor</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-magnifying-glass-chart accent-icon"></i> <span class="lang-zh">精準定位痛點、根因剖析與財務/ESG 雙重回報</span><span class="lang-en">Pinpointing Pain Points & Dual Financial/ESG ROI</span></h3>
                            <p><span class="lang-zh">高階顧問不能給出模糊建議！提案必須包含預期資本支出、年化減碳量、品牌溢價空間與具體的 ROI 財務回收期。</span>
                            <span class="lang-en">Proposals must balance environmental/social impact with rigorous financial ROI feasibility.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 6: Context Audit -->
            <section class="slide" id="slide-6" data-title="Slide 6: 企業背景分析與現況診斷">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-building-user"></i> Context Audit</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">企業背景分析與現況診斷 (Context Audit)</span>
                            <span class="lang-en">Corporate Context & Baseline Audit</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-microscope accent-icon"></i> <span class="lang-zh">梳理目標企業所屬產業與當前永續困境</span><span class="lang-en">Auditing Industry Dynamics & Sustainability Hurdles</span></h3>
                            <p><span class="lang-zh">明確目標企業的營運範疇、主要營收來源、氣候曝險、範疇 3 碳足跡與監管合規痛點，建立基準線 (Baseline)。</span>
                            <span class="lang-en">Establishing baseline carbon footprints, Scope 3 vulnerabilities, and regulatory compliance gaps.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 7: SWOT Analysis -->
            <section class="slide" id="slide-7" data-title="Slide 7: SWOT 工具在 ESG 中的應用">
                <div class="slide-container center-header-layout">
                    <div class="header-block center-text">
                        <div class="section-tag"><i class="fa-solid fa-table-cells-large"></i> Strategic Framework</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">SWOT 分析工具在 ESG 轉型中的應用</span>
                            <span class="lang-en">SWOT Analysis for ESG Transformation</span>
                        </h2>
                    </div>

                    <div class="cards-grid-4">
                        <div class="rc-card glass-card">
                            <h4>Strengths (優勢)</h4>
                            <p><span class="lang-zh">內部綠色研發技術與獨家專利。</span><span class="lang-en">Internal eco-tech & patents</span></p>
                        </div>
                        <div class="rc-card glass-card">
                            <h4>Weaknesses (劣勢)</h4>
                            <p><span class="lang-zh">範疇 3 碳排過高或高管薪酬未綁定。</span><span class="lang-en">High Scope 3 & loose comp</span></p>
                        </div>
                        <div class="rc-card glass-card">
                            <h4>Opportunities (機會)</h4>
                            <p><span class="lang-zh">綠色金融 SLL 優惠與低碳溢價市場。</span><span class="lang-en">Green credit & premium market</span></p>
                        </div>
                        <div class="rc-card glass-card">
                            <h4>Threats (威脅)</h4>
                            <p><span class="lang-zh">歐盟 CBAM 碳關稅與極端天災中斷。</span><span class="lang-en">CBAM tariffs & disaster risks</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 8: PESTEL Analysis -->
            <section class="slide" id="slide-8" data-title="Slide 8: PESTEL 外部環境分析">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-globe"></i> Macro Trends</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">PESTEL 宏觀外部環境分析</span>
                            <span class="lang-en">PESTEL Macro Environmental Audit</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-binoculars accent-icon"></i> <span class="lang-zh">政治、經濟、社會、技術、環境與法律 6 維度</span><span class="lang-en">6 Macro Drivers: Political to Legal</span></h3>
                            <p><span class="lang-zh">全面評估各國氣候政策 (P)、碳定價 (E)、Z世代永續消費觀 (S)、AI與綠能技術 (T)、極端氣候 (E) 與 EU AI Act (L)。</span>
                            <span class="lang-en">Auditing political climate mandates, carbon pricing, tech trends, and EU AI regulations.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 9: Stakeholder Mapping -->
            <section class="slide" id="slide-9" data-title="Slide 9: Stakeholder Mapping">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-users"></i> Stakeholder Alignment</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">Stakeholder Mapping (利害關係人圖譜)</span>
                            <span class="lang-en">Stakeholder Salience & Mapping</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-diagram-nested accent-icon"></i> <span class="lang-zh">運用 Salience Model 識別核心利害關係人期待</span><span class="lang-en">Identifying Priority Expectations via Salience Model</span></h3>
                            <p><span class="lang-zh">將投資人、客戶、代工廠、員工與監管機構分類，明確各群體的關鍵訴求與滿意度指標。</span>
                            <span class="lang-en">Mapping key investor, client, supplier, and regulatory expectations into actionable priorities.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 10: Double Materiality Matrix -->
            <section class="slide" id="slide-10" data-title="Slide 10: 雙重重大性矩陣">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-filter"></i> Double Materiality</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">Double Materiality Matrix (雙重重大性矩陣)</span>
                            <span class="lang-en">Double Materiality Matrix Formulation</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-layer-group accent-icon"></i> <span class="lang-zh">篩選最影響財務與社會衝擊之 5 大議題</span><span class="lang-en">Filtering Top 5 Financially & Societally Material Issues</span></h3>
                            <p><span class="lang-zh">結合財務重大性 (Inside-Out) 與影響重大性 (Outside-In)，繪製 2D 矩陣，確定本專案必須優先解決的 5 大關鍵議題。</span>
                            <span class="lang-en">Constructing a 2D matrix evaluating both Financial and Impact materiality for proposal focus.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 11: Activity 1 - ESG Health Check -->
            <section class="slide" id="slide-11" data-title="Slide 11: 活動一 - 企業 ESG 健檢">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag activity-tag"><i class="fa-solid fa-notes-medical"></i> Activity 1 • 20 Minutes</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">ESG Health Check (企業健檢)</span>
                            <span class="lang-en">ESG Health Check Workshop</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="scenario-card glass-card highlight-border">
                            <h3><span class="lang-zh">任務：完成目標企業的 7 大維度「ESG 健康檢查報告」</span><span class="lang-en">Complete 7-Dimension ESG Health Check</span></h3>
                            <div class="grid-2col mt-3 gap-2">
                                <div class="opt-choice"><p>1. 倫理風險 / ESG 表現</p></div>
                                <div class="opt-choice"><p>2. 利害關係人 / 資訊揭露品質</p></div>
                                <div class="opt-choice"><p>3. AI 與數位治理合規度</p></div>
                                <div class="opt-choice"><p>4. 供應鏈 Scope 3 / 危機應變韌性</p></div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 12: Activity 1 - Presentation & Debrief -->
            <section class="slide" id="slide-12" data-title="Slide 12: 活動一 - 健檢發表與點評">
                <div class="slide-container center-header-layout">
                    <div class="header-block center-text">
                        <div class="section-tag activity-tag"><i class="fa-solid fa-comments"></i> Class Debrief</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">健檢切忌泛泛而談，抓出產業專屬痛點</span>
                            <span class="lang-en">Activity 1: Pinpoint Sector-Specific Pain Points</span>
                        </h2>
                    </div>

                    <div class="debrief-box glass-card glow-card">
                        <i class="fa-solid fa-lightbulb debrief-icon"></i>
                        <div class="debrief-content">
                            <h4><span class="lang-zh">教師觀點帶出 (Key Takeaway)：</span><span class="lang-en">Faculty Debrief:</span></h4>
                            <p><span class="lang-zh">「優秀的健檢報告絕不列出幾十個通用指標，而是精準刺中該產業的致命缺口（如半導體的綠電、金融的氣候放款、科技的 AI 隱私）！」</span>
                            <span class="lang-en">"Top health checks pinpoint the single fatal flaw unique to that industry."</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 13: 2035 ESG Strategy Roadmap -->
            <section class="slide" id="slide-13" data-title="Slide 13: 2035 永續策略藍圖架構">
                <div class="slide-container center-header-layout">
                    <div class="header-block center-text">
                        <div class="section-tag"><i class="fa-solid fa-map-location-dot"></i> 2035 Roadmap</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">2035 ESG Strategy Roadmap 三階段規劃</span>
                            <span class="lang-en">3-Stage 2035 ESG Strategy Roadmap</span>
                        </h2>
                    </div>

                    <div class="cards-grid-3 gap-4 mt-3">
                        <div class="rc-card glass-card">
                            <h4>短期 (1 年期：基線)</h4>
                            <p><span class="lang-zh">ISO 盤查、AI 倫理自審、簽署行為守則。</span><span class="lang-en">Baseline ISO & AI audits</span></p>
                        </div>
                        <div class="rc-card glass-card">
                            <h4>中期 (3 年期：轉型)</h4>
                            <p><span class="lang-zh">PaaS 商業模式試行、供應鏈綠電共購。</span><span class="lang-en">PaaS pilots & Co-PPA</span></p>
                        </div>
                        <div class="rc-card glass-card">
                            <h4>長期 (5-10 年期：領航)</h4>
                            <p><span class="lang-zh">RE100 達標、閉環經濟、淨零排放。</span><span class="lang-en">RE100 & closed-loop net zero</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 14: Environment Pillar -->
            <section class="slide" id="slide-14" data-title="Slide 14: Environment 板塊策略">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-leaf"></i> E Pillar</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">Environment 板塊：淨零、Scope 1-3 與 CBAM</span>
                            <span class="lang-en">Environment Pillar: Net Zero & Scope 1-3</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-solar-panel accent-icon"></i> <span class="lang-zh">制定 SBTi 減碳路徑與供應鏈共購綠電</span><span class="lang-en">Setting SBTi Targets & Supplier Co-PPA</span></h3>
                            <p><span class="lang-zh">提出具體廠區能效提升、綠電採購 (PPA) 時程、低碳原物料替換與應對歐盟 CBAM 碳關稅預算。</span>
                            <span class="lang-en">Planning energy efficiency upgrades, renewable PPAs, and CBAM tax mitigation budgets.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 15: Social Pillar -->
            <section class="slide" id="slide-15" data-title="Slide 15: Social 板塊策略">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-users"></i> S Pillar</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">Social 板塊：DEI、人權與生活薪資</span>
                            <span class="lang-en">Social Pillar: DEI & Supply Chain Human Rights</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-hand-holding-heart accent-icon"></i> <span class="lang-zh">多元平等包含 (DEI) 與海外代工廠人權</span><span class="lang-en">DEI Policies & Offshore Supplier Living Wage</span></h3>
                            <p><span class="lang-zh">設定高階主管女性與多元族群比例、貫徹海外代工廠 Living Wage (生活薪資) 與消除血汗工廠勞動。</span>
                            <span class="lang-en">Setting executive diversity metrics and guaranteeing living wages across global supply chains.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 16: Governance Pillar -->
            <section class="slide" id="slide-16" data-title="Slide 16: Governance 板塊策略">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-gavel"></i> G Pillar</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">Governance 板塊：董事會監督與高管薪酬</span>
                            <span class="lang-en">Governance Pillar: Board & Executive Pay</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-building-shield accent-icon"></i> <span class="lang-zh">獨立董事席次、高管獎金與 ESG KPI 綁定</span><span class="lang-en">Independent Directors & ESG Comp Alignment</span></h3>
                            <p><span class="lang-zh">設立董事會永續委員會、提升獨立董事專業席次，並將 20% 高管變動年終獎金與減碳 KPI 強制綁定。</span>
                            <span class="lang-en">Establishing a Board Sustainability Committee and tying executive bonuses directly to ESG targets.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 17: AI Governance Pillar -->
            <section class="slide" id="slide-17" data-title="Slide 17: AI Governance 板塊策略">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-robot"></i> AI Pillar</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">AI Governance 板塊：Responsible AI 原則</span>
                            <span class="lang-en">AI Governance: Responsible AI Principles</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-shield-halved accent-icon"></i> <span class="lang-zh">對接 Responsible AI 5 原則與 EU AI Act</span><span class="lang-en">Responsible AI 5 Principles & EU AI Act</span></h3>
                            <p><span class="lang-zh">頒布企業 Responsible AI 指南、建立演算法偏誤審查機制與保護客戶數據隱私，防範 AI 幻覺與侵權訴訟。</span>
                            <span class="lang-en">Implementing Responsible AI guidelines, algorithmic bias audits, and EU AI Act risk compliance.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 18: Supply Chain Pillar -->
            <section class="slide" id="slide-18" data-title="Slide 18: Supply Chain 板塊策略">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-truck-ramp-box"></i> Supply Chain Pillar</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">Supply Chain 板塊：Scope 3 減碳與採購</span>
                            <span class="lang-en">Supply Chain: Scope 3 & Sourcing</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-handshake accent-icon"></i> <span class="lang-zh">行為守則、無預警稽核與綠色金融激勵</span><span class="lang-en">Code of Conduct, Audits & Green Credit</span></h3>
                            <p><span class="lang-zh">要求 Tier 1, 2 供應商簽署行為守則、進行第三方實地無預警稽核，並聯合銀行提供低利 SLL 貸款鼓勵代工廠減碳。</span>
                            <span class="lang-en">Mandating supplier codes of conduct, third-party audits, and green financing incentives.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 19: Business Model Innovation Pillar -->
            <section class="slide" id="slide-19" data-title="Slide 19: Business Model 板塊策略">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-arrows-spin"></i> BMI Pillar</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">Business Model 板塊：PaaS 與循環經濟</span>
                            <span class="lang-en">Business Model: PaaS & Circular Economy</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-rotate-left accent-icon"></i> <span class="lang-zh">試行 Product-as-a-Service 訂閱與資源回收閉環</span><span class="lang-en">Piloting Product-as-a-Service & Closed-Loops</span></h3>
                            <p><span class="lang-zh">推動產品即服務 (PaaS) 訂閱制、產品維修與舊機買回拍賣，將廢棄物處置費用翻轉為高價值再生原料收入。</span>
                            <span class="lang-en">Transitioning product sales into PaaS subscriptions and closed-loop material recycling.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 20: ESG KPI Dashboard -->
            <section class="slide" id="slide-20" data-title="Slide 20: ESG KPI Dashboard 設計">
                <div class="slide-container center-header-layout">
                    <div class="header-block center-text">
                        <div class="section-tag"><i class="fa-solid fa-gauge-high"></i> Dashboard Formulation</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">ESG KPI Dashboard (量化儀表板設計)</span>
                            <span class="lang-en">ESG KPI Dashboard Formulation</span>
                        </h2>
                    </div>

                    <div class="matrix-table-wrapper glass-card mt-3">
                        <table class="custom-matrix-table">
                            <thead>
                                <tr>
                                    <th><span class="lang-zh">維度</span><span class="lang-en">Pillar</span></th>
                                    <th><span class="lang-zh">量化指標 (Quantifiable KPI)</span><span class="lang-en">Quantifiable KPI</span></th>
                                    <th><span class="lang-zh">3年目標</span><span class="lang-en">3-Yr Target</span></th>
                                    <th><span class="lang-zh">5年目標</span><span class="lang-en">5-Yr Target</span></th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td><strong>Environment</strong></td>
                                    <td>Scope 1-3 總碳排放量減幅 %</td>
                                    <td>-25%</td>
                                    <td>-50% (SBTi)</td>
                                </tr>
                                <tr>
                                    <td><strong>Governance</strong></td>
                                    <td>高管獎金與 ESG KPI 掛鉤比例 %</td>
                                    <td>15%</td>
                                    <td>25%</td>
                                </tr>
                                <tr>
                                    <td><strong>Supply Chain</strong></td>
                                    <td>Tier 1 供應商使用綠電比例 %</td>
                                    <td>50%</td>
                                    <td>100% (RE100)</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </section>

            <!-- SLIDE 21: Activity 2 - ESG Consulting Pitch -->
            <section class="slide" id="slide-21" data-title="Slide 21: 活動二 - 董事會提案大賽">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag activity-tag"><i class="fa-solid fa-chalkboard-user"></i> Activity 2 • 35 Minutes</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">ESG Consulting Pitch (董事會提案)</span>
                            <span class="lang-en">ESG Consulting Board Presentation Pitch</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="scenario-card glass-card highlight-border">
                            <h3><span class="lang-zh">任務：各組以顧問角色進行 10 分鐘董事會簡報提案</span><span class="lang-en">Deliver 10-Min Strategy Proposal to Board</span></h3>
                            <div class="grid-2col mt-3 gap-2">
                                <div class="opt-choice"><p>1. 企業現況與 3 大致命關鍵問題</p></div>
                                <div class="opt-choice"><p>2. 2035 ESG Strategy Roadmap 藍圖</p></div>
                                <div class="opt-choice"><p>3. 3 年期行動計畫與 KPI 儀表板</p></div>
                                <div class="opt-choice"><p>4. 預期效益與 ROI 財務回收評估</p></div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 22: Faculty Feedback & Board Q&A -->
            <section class="slide" id="slide-22" data-title="Slide 22: 董事會質詢與教師回饋">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-gavel"></i> Board Q&A</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">董事會質詢與教師評語 (Board Q&A)</span>
                            <span class="lang-en">Board Room Q&A & Faculty Interrogation</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-question-circle accent-icon"></i> <span class="lang-zh">針對資本預算、風險控管與 ROI 進行高強度質詢</span><span class="lang-en">Rigorous Interrogation on Budget, Risk & ROI</span></h3>
                            <p><span class="lang-zh">教師與同學扮演董事會獨立董事與機構投資人，針對簡報中的可行性、預算合理性與潛在風險提出高強度挑戰問答！</span>
                            <span class="lang-en">Simulating board directors challenging consultants on capital budget, risk, and feasibility.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 23: Peer Review & Board Scoring -->
            <section class="slide" id="slide-23" data-title="Slide 23: 同儕評分與最佳團隊票選">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag activity-tag"><i class="fa-solid fa-check-double"></i> Peer Scoring</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">同儕評分與最佳顧問團隊票選</span>
                            <span class="lang-en">Peer Scoring & Best Team Voting</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-star accent-icon"></i> <span class="lang-zh">評選最深具戰略遠見與商業說服力之團隊</span><span class="lang-en">Awarding Most Strategic & Persuasive Team</span></h3>
                            <p><span class="lang-zh">全班填寫同儕評分表：評分維度包含診斷完整性 (25%)、策略設計 (30%)、KPI規劃 (20%) 與簡報說服力 (15%)。</span>
                            <span class="lang-en">Peer scoring across diagnosis, strategy, KPIs, and pitch persuasiveness.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 24: Module 4 Capstone Key Findings -->
            <section class="slide" id="slide-24" data-title="Slide 24: Capstone 專案核心成果梳理">
                <div class="slide-container center-header-layout">
                    <div class="header-block center-text">
                        <div class="section-tag"><i class="fa-solid fa-trophy"></i> Capstone Synthesis</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">Capstone 專案核心學習成果梳理</span>
                            <span class="lang-en">Capstone Project Core Findings Synthesis</span>
                        </h2>
                    </div>

                    <div class="cards-grid-4">
                        <div class="rc-card glass-card">
                            <h4>Audit Competency</h4>
                            <p><span class="lang-zh">具備獨立進行企業 ESG 健康檢查能力。</span><span class="lang-en">Independent ESG health check skills</span></p>
                        </div>
                        <div class="rc-card glass-card"><h4>Roadmap Design</h4><p><span class="lang-zh">建構 2035 轉型策略藍圖與 VRIO。</span><span class="lang-en">2035 roadmap & VRIO design</span></p></div>
                        <div class="rc-card glass-card"><h4>KPI Rigor</h4><p><span class="lang-zh">設計可量化管控之 Dashboard。</span><span class="lang-en">Quantifiable KPI dashboard</span></p></div>
                        <div class="rc-card glass-card"><h4>Board Persuasion</h4><p><span class="lang-zh">具備向董事會簡報提案之說服力。</span><span class="lang-en">Board presentation persuasiveness</span></p></div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 25: Preview W16 & Homework 15 -->
            <section class="slide" id="slide-25" data-title="Slide 25: Preview W16 & Homework 15">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag homework-tag"><i class="fa-solid fa-flag-checkered"></i> Preview W16 & HW15</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">W16 結業預告與 Homework 15</span>
                            <span class="lang-en">W16 Preview & Homework 15</span>
                        </h2>
                    </div>

                    <div class="main-panel">
                        <div class="glass-card feature-card mb-2">
                            <h3><i class="fa-solid fa-award accent-icon"></i> <span class="lang-zh">W16 結業預告：課程回顧、永續領導力與未來趨勢</span><span class="lang-en">W16 Preview: Course Reflection & Leadership</span></h3>
                            <p class="mb-2"><span class="lang-zh">下一週我們將迎來學期大結業：《課程回顧、永續領導力與未來趨勢 (Course Reflection, Sustainable Leadership & Future Trends)》！</span><span class="lang-en">Next week we celebrate our final Course Reflection & Graduation!</span></p>
                        </div>

                        <div class="glass-card feature-card mb-2">
                            <h3><i class="fa-solid fa-file-contract accent-icon"></i> <span class="lang-zh">Homework 15：期末專題書面報告 (約 4,000–5,000 字/組)</span><span class="lang-en">Homework 15: Team Capstone Report (~4,000-5,000w)</span></h3>
                            <p><span class="lang-zh">小組完成：概況、ESG 診斷、短中長期行動方案、至少 5 項量化 KPI 儀表板與預期財務/永續效益評估。</span>
                            <span class="lang-en">Team Capstone Report: firm profile, ESG diagnosis, 3-stage roadmap, 5 KPIs & financial ROI analysis.</span></p>
                        </div>

                        <div class="glass-card rubrics-card">
                            <h4><i class="fa-solid fa-chart-bar accent-icon"></i> AACSB <span class="lang-zh">評分標準</span><span class="lang-en">Rubrics Breakdown</span></h4>
                            <div class="rubrics-bar">
                                <div class="r-seg seg-1" style="width: 25%;"><span class="lang-zh">診斷 25%</span><span class="lang-en">Audit 25%</span></div>
                                <div class="r-seg seg-2" style="width: 30%;"><span class="lang-zh">策略 30%</span><span class="lang-en">Strat 30%</span></div>
                                <div class="r-seg seg-3" style="width: 20%;"><span class="lang-zh">KPI 20%</span><span class="lang-en">KPI 20%</span></div>
                                <div class="r-seg seg-4" style="width: 15%;"><span class="lang-zh">簡報 15%</span><span class="lang-en">Pitch 15%</span></div>
                                <div class="r-seg seg-5" style="width: 10%;"><span class="lang-zh">報告 10%</span><span class="lang-en">Report 10%</span></div>
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

with open(r"C:\Users\User\Desktop\第1週_企業為何需要倫理\第15週_ESG企業顧問專題.html", "w", encoding="utf-8") as f:
    f.write(html_week15)

print("Successfully generated Week 15 HTML presentation file!")
