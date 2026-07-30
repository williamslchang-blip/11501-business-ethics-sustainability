import sys

html_week3 = """<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Week 3: Corporate Social Responsibility & CSV | 企業社會責任與共享價值</title>
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
                <h1 class="deck-title">Week 3: Corporate Social Responsibility (CSR) & Creating Shared Value (CSV)</h1>
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
            <a href="第3週_企業社會責任與共享價值.docx" download class="btn btn-secondary" title="Download Teaching Facilitation Guide (.docx)">
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
                            <span class="meta-tag alt">Week 03 • Lecture Presentation</span>
                        </div>
                        <h1 class="main-heading">
                            <span class="lang-zh">企業社會責任與共享價值</span>
                            <span class="lang-en">Corporate Social Responsibility & Creating Shared Value</span>
                        </h1>
                        <h2 class="sub-heading">
                            <span class="lang-zh">從企業倫理邁向 CSR、CSV 與永續競爭力</span>
                            <span class="lang-en">From Business Ethics to CSR, CSV, and Sustainable Advantage</span>
                        </h2>
                        <p class="lead-text">
                            <span class="lang-zh">Carroll 4 階金字塔、Michael Porter 共享價值與綠色漂洗 (Greenwashing) 實務診斷</span>
                            <span class="lang-en">Carroll's CSR Pyramid, Porter's Creating Shared Value, and Greenwashing Audit</span>
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
                            <img src="week3_csr_pyramid_cover.jpg" alt="Week 3 Cover Visual" class="slide-img">
                            <div class="visual-badge">
                                <i class="fa-solid fa-hand-holding-heart"></i> CSR • CSV • Greenwashing
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 2: Roadmap Evolution -->
            <section class="slide" id="slide-2" data-title="Slide 2: 課程轉折與演進">
                <div class="slide-container center-header-layout">
                    <div class="header-block center-text">
                        <div class="section-tag"><i class="fa-solid fa-diagram-project"></i> Strategic Pivot</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">整門課的重要轉折點：從倫理到 CSR</span>
                            <span class="lang-en">Strategic Pivot: Business Ethics to CSR</span>
                        </h2>
                        <p class="slide-sub">Bridging Moral Foundations to Corporate Value Creation</p>
                    </div>

                    <div class="evolution-chain-card glass-card">
                        <div class="chain-items">
                            <div class="c-node">
                                <div class="c-icon"><i class="fa-solid fa-heart"></i></div>
                                <h4>W1 - W2</h4>
                                <p><span class="lang-zh">Business Ethics<br>(企業倫理內在基因)</span><span class="lang-en">Business Ethics<br>(Internal Moral DNA)</span></p>
                            </div>
                            <div class="c-connector"><i class="fa-solid fa-arrow-right-long"></i></div>

                            <div class="c-node highlight-node">
                                <div class="c-icon"><i class="fa-solid fa-hand-holding-hand"></i></div>
                                <h4>W3 Today</h4>
                                <p><span class="lang-zh">CSR & CSV<br>(責任行動與共享價值)</span><span class="lang-en">CSR & CSV<br>(Actions & Shared Value)</span></p>
                            </div>
                            <div class="c-connector"><i class="fa-solid fa-arrow-right-long"></i></div>

                            <div class="c-node">
                                <div class="c-icon"><i class="fa-solid fa-leaf"></i></div>
                                <h4>W4 Next</h4>
                                <p><span class="lang-zh">ESG Strategy<br>(可量化永續治理數據)</span><span class="lang-en">ESG Strategy<br>(Quantitative ESG Metrics)</span></p>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 3: Warm-up Question -->
            <section class="slide" id="slide-3" data-title="Slide 3: 暖身問題">
                <div class="slide-container center-header-layout">
                    <div class="header-block center-text">
                        <div class="section-tag warning-tag"><i class="fa-solid fa-lightbulb"></i> Warm-up Discussion</div>
                        <h2 class="slide-heading giant-title">
                            <span class="lang-zh">暖身思考：沒違法、沒不道德，就算好企業嗎？</span>
                            <span class="lang-en">Warm-up Question: Is Compliance Enough?</span>
                        </h2>
                    </div>

                    <div class="dilemma-box glass-card glow-card">
                        <div class="dilemma-statement">
                            <p class="quote-text">
                                <span class="lang-zh">「如果一家企業<strong>完全沒有違法</strong>，也<strong>沒有做不道德的事</strong>，但它對社會、環境與在地社區沒有貢獻任何積極價值，<strong>它算是一間『好企業』嗎？</strong>」</span>
                                <span class="lang-en">"If a company is <strong>completely legal</strong> and <strong>does nothing immoral</strong>, but contributes zero positive value to society and environment, <strong>is it a 'good company'?</strong>"</span>
                            </p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 4: Changing Role of the Firm -->
            <section class="slide" id="slide-4" data-title="Slide 4: 企業角色的時代演進">
                <div class="slide-container center-header-layout">
                    <div class="header-block center-text">
                        <div class="section-tag"><i class="fa-solid fa-timeline"></i> Historical Shift</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">企業角色的時代演進 (1960 → 1980 → 2020)</span>
                            <span class="lang-en">Evolution of Corporate Purpose (1960 - 2020)</span>
                        </h2>
                    </div>

                    <div class="cards-grid-3x2">
                        <div class="decision-card glass-card">
                            <div class="dec-icon"><i class="fa-solid fa-sack-dollar"></i></div>
                            <h4>1960s: Profit Only</h4>
                            <p><span class="lang-zh">單純追求利潤最大化，忽視外部性。</span><span class="lang-en">Pure profit maximization, ignoring externalities.</span></p>
                        </div>
                        <div class="decision-card glass-card highlight-border">
                            <div class="dec-icon"><i class="fa-solid fa-hands-holding-child"></i></div>
                            <h4>1980s: CSR Era</h4>
                            <p><span class="lang-zh">企業社會責任興起，關注利害關係人與公益。</span><span class="lang-en">Rise of CSR, focus on stakeholders and charity.</span></p>
                        </div>
                        <div class="decision-card glass-card">
                            <div class="dec-icon"><i class="fa-solid fa-seedling"></i></div>
                            <h4>2020s: ESG & CSV</h4>
                            <p><span class="lang-zh">共享價值與量化 ESG 數據成為資本市場核心。</span><span class="lang-en">Shared value and ESG metrics drive capital markets.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 5: Definition of CSR -->
            <section class="slide" id="slide-5" data-title="Slide 5: CSR 定義">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-book"></i> Part II • CSR Theories</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">CSR 的精準定義</span>
                            <span class="lang-en">What is Corporate Social Responsibility?</span>
                        </h2>
                        <p class="slide-sub">Definition & International Standards</p>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-earth-americas accent-icon"></i> <span class="lang-zh">ISO 26000 國際組織定義</span><span class="lang-en">ISO 26000 Definition</span></h3>
                            <p class="lead-p">
                                <span class="lang-zh">「企業在追求利潤的同時，承擔對社會與環境影響的責任行動。透由透明與道德的行為，為社會福祉、永續發展與利害關係人福祉做出貢獻。」</span>
                                <span class="lang-en">"The responsibility of an organization for the impacts of its decisions and activities on society and environment, through transparent and ethical behavior."</span>
                            </p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 6: History of CSR -->
            <section class="slide" id="slide-6" data-title="Slide 6: CSR 發展歷史">
                <div class="slide-container">
                    <div class="header-block">
                        <div class="section-tag"><i class="fa-solid fa-clock-rotate-left"></i> Milestones</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">CSR 的四大演進里程碑</span>
                            <span class="lang-en">Four Milestones of CSR History</span>
                        </h2>
                    </div>

                    <div class="timeline-wrapper glass-card mt-3">
                        <div class="timeline-events">
                            <div class="t-event">
                                <div class="t-year">1953 年</div>
                                <h4>Howard Bowen</h4>
                                <p><span class="lang-zh">出版《商人社會責任》，被譽為 CSR 之父。</span><span class="lang-en">Published Social Responsibilities of Businessman.</span></p>
                            </div>
                            <div class="t-arrow"><i class="fa-solid fa-chevron-right"></i></div>

                            <div class="t-event">
                                <div class="t-year">1991 年</div>
                                <h4>Archie Carroll</h4>
                                <p><span class="lang-zh">提出 Carroll CSR Pyramid 金字塔模型。</span><span class="lang-en">Formulated Carroll's CSR Pyramid.</span></p>
                            </div>
                            <div class="t-arrow"><i class="fa-solid fa-chevron-right"></i></div>

                            <div class="t-event">
                                <div class="t-year">2006 年</div>
                                <h4>Porter & Kramer</h4>
                                <p><span class="lang-zh">提出 CSV (Creating Shared Value) 共享價值。</span><span class="lang-en">Pioneered Creating Shared Value (CSV).</span></p>
                            </div>
                            <div class="t-arrow"><i class="fa-solid fa-chevron-right"></i></div>

                            <div class="t-event highlight-event">
                                <div class="t-year">Today</div>
                                <h4>ESG & Net Zero</h4>
                                <p><span class="lang-zh">全球資本市場要求量化 ESG 指標。</span><span class="lang-en">Global ESG & Net Zero metrics integration.</span></p>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 7: Carroll CSR Pyramid -->
            <section class="slide" id="slide-7" data-title="Slide 7: Carroll CSR Pyramid">
                <div class="slide-container center-header-layout">
                    <div class="header-block center-text">
                        <div class="section-tag"><i class="fa-solid fa-cubes-stacked"></i> Classic Model</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">Carroll 企業社會責任金字塔 (CSR Pyramid)</span>
                            <span class="lang-en">Archie Carroll's CSR Pyramid (1991)</span>
                        </h2>
                    </div>

                    <div class="pyramid-container glass-card">
                        <div class="p-tier tier-4">
                            <div class="t-label">Philanthropic Responsibility (<span class="lang-zh">慈善責任</span><span class="lang-en">Philanthropic</span>)</div>
                            <div class="t-desc"><span class="lang-zh">Be a good corporate citizen (企業公民公益慈善)</span><span class="lang-en">Be a good corporate citizen</span></div>
                        </div>
                        <div class="p-tier tier-3">
                            <div class="t-label">Ethical Responsibility (<span class="lang-zh">倫理責任</span><span class="lang-en">Ethical</span>)</div>
                            <div class="t-desc"><span class="lang-zh">Be ethical; do what is right and fair (超越法律，做對的事)</span><span class="lang-en">Be ethical; do what is right and fair</span></div>
                        </div>
                        <div class="p-tier tier-2">
                            <div class="t-label">Legal Responsibility (<span class="lang-zh">法律責任</span><span class="lang-en">Legal</span>)</div>
                            <div class="t-desc"><span class="lang-zh">Obey the law (遵守國家所有法律規章)</span><span class="lang-en">Obey the law</span></div>
                        </div>
                        <div class="p-tier tier-1">
                            <div class="t-label">Economic Responsibility (<span class="lang-zh">經濟責任 - 底座基礎</span><span class="lang-en">Economic Floor</span>)</div>
                            <div class="t-desc"><span class="lang-zh">Be profitable (保持獲利，企業生存基礎)</span><span class="lang-en">Be profitable; the foundation</span></div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 8: Economic Responsibility -->
            <section class="slide" id="slide-8" data-title="Slide 8: 經濟責任">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-coins"></i> Tier 1 • Foundation</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">1. 經濟責任 (Economic)</span>
                            <span class="lang-en">1. Economic Responsibility</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-chart-line accent-icon"></i> <span class="lang-zh">企業生存與獲利的根本</span><span class="lang-en">Foundation of Corporate Survival</span></h3>
                            <p><span class="lang-zh">獲利是企業最根本的社會責任。連年虧損破產的企業無法提供員工薪資保障、無法為股東創造回報，本身就是對社會的巨大傷害。</span><span class="lang-en">Profit is the essential foundation. Bankrupt firms cannot pay employees or provide shareholder returns, burdening society.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 9: Legal Responsibility -->
            <section class="slide" id="slide-9" data-title="Slide 9: 法律責任">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-gavel"></i> Tier 2 • Required</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">2. 法律責任 (Legal)</span>
                            <span class="lang-en">2. Legal Responsibility</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-scale-balanced accent-icon"></i> <span class="lang-zh">遵守社會強制的底線法規</span><span class="lang-en">Compliance with Mandatory Laws</span></h3>
                            <p><span class="lang-zh">依法納稅、遵守勞基法、環境保護法、消費者保護法與反壟斷法。法律是社會對企業運作規定的強制邊界。</span><span class="lang-en">Paying taxes, complying with labor laws, environmental regulations, and consumer safety codes required by law.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 10: Ethical Responsibility -->
            <section class="slide" id="slide-10" data-title="Slide 10: 倫理責任">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-shield-heart"></i> Tier 3 • Expected</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">3. 倫理責任 (Ethical)</span>
                            <span class="lang-en">3. Ethical Responsibility</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-heart accent-icon"></i> <span class="lang-zh">超越法律，做公正與對的事情</span><span class="lang-en">Going Beyond Legal Mandates</span></h3>
                            <p><span class="lang-zh">在法律未明文規定處，主動展現公平誠信。例如：主動給予高於法規的產假、推動公平貿易採購、保護供應鏈人權。</span><span class="lang-en">Doing what is fair and moral beyond legal minimums (e.g. fair trade sourcing, enhanced parental leave, supply chain human rights).</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 11: Philanthropic Responsibility -->
            <section class="slide" id="slide-11" data-title="Slide 11: 慈善責任">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-hand-holding-dollar"></i> Tier 4 • Desired</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">4. 慈善責任 (Philanthropic)</span>
                            <span class="lang-en">4. Philanthropic Responsibility</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-hands-praying accent-icon"></i> <span class="lang-zh">做個優良的企業公民 (Corporate Citizenship)</span><span class="lang-en">Good Corporate Citizenship</span></h3>
                            <p><span class="lang-zh">主動撥款投入社區發展、偏鄉教育補助、員工志工服務日與大地震急難救助等公益慈善事業。</span><span class="lang-en">Voluntary contributions to community development, education grants, employee volunteering, and disaster relief.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 12: Applied CSR Pyramid -->
            <section class="slide" id="slide-12" data-title="Slide 12: CSR 金字塔企業案例">
                <div class="slide-container center-header-layout">
                    <div class="header-block center-text">
                        <div class="section-tag"><i class="fa-solid fa-table-cells"></i> Matrix Application</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">CSR 金字塔企業實務對照矩陣</span>
                            <span class="lang-en">Applied CSR Pyramid Case Matrix</span>
                        </h2>
                    </div>

                    <div class="matrix-table-wrapper glass-card mt-3">
                        <table class="custom-matrix-table">
                            <thead>
                                <tr>
                                    <th><span class="lang-zh">金字塔層級</span><span class="lang-en">Tier Level</span></th>
                                    <th><span class="lang-zh">核心精神</span><span class="lang-en">Core Essence</span></th>
                                    <th><span class="lang-zh">企業行為範例</span><span class="lang-en">Real Corporate Examples</span></th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td><strong>Philanthropic</strong></td>
                                    <td><span class="lang-zh">企業公民 / 公益慈善</span><span class="lang-en">Corporate Citizen</span></td>
                                    <td><span class="lang-zh">設立偏鄉教育基金會、提供員工有薪志工假</span><span class="lang-en">Education foundations, paid volunteer days</span></td>
                                </tr>
                                <tr>
                                    <td><strong>Ethical</strong></td>
                                    <td><span class="lang-zh">超越法律 / 追求公正</span><span class="lang-en">Beyond Law / Fair</span></td>
                                    <td><span class="lang-zh">公平貿易咖啡採購、主動披露全供應鏈碳足跡</span><span class="lang-en">Fair Trade coffee sourcing, full supply carbon audit</span></td>
                                </tr>
                                <tr>
                                    <td><strong>Legal</strong></td>
                                    <td><span class="lang-zh">遵守法規 / 法律底線</span><span class="lang-en">Obey Laws / Baseline</span></td>
                                    <td><span class="lang-zh">依法納稅、符合勞基法工時限制與食安標準</span><span class="lang-en">Tax compliance, labor hour limits, safety codes</span></td>
                                </tr>
                                <tr>
                                    <td><strong>Economic</strong></td>
                                    <td><span class="lang-zh">保持獲利 / 生存基礎</span><span class="lang-en">Profitable / Survival</span></td>
                                    <td><span class="lang-zh">創造股東報酬、維持穩定就業與健全現金流</span><span class="lang-en">Shareholder returns, stable employment, cash flow</span></td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </section>

            <!-- SLIDE 13: Activity 1 - CSR Classification Game -->
            <section class="slide" id="slide-13" data-title="Slide 13: 活動一 - CSR 分類遊戲">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag activity-tag"><i class="fa-solid fa-gamepad"></i> Activity 1 • 15 Minutes</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">CSR Classification Game</span>
                            <span class="lang-en">CSR Classification Game</span>
                        </h2>
                        <p class="slide-sub">Categorize 20 Corporate Action Cards into Carroll's Pyramid</p>
                    </div>

                    <div class="main-panel">
                        <div class="scenario-card glass-card highlight-border">
                            <h3><span class="lang-zh">活動題目：將下列企業行為貼至金字塔正確區域</span><span class="lang-en">Categorize 20 Corporate Action Cards</span></h3>
                            <div class="grid-2col mt-3 gap-2">
                                <div class="opt-choice"><p><span class="lang-zh">1. 依法繳納營業稅 (Tax Paying)</span><span class="lang-en">1. Paying Corporate Tax</span></p></div>
                                <div class="opt-choice"><p><span class="lang-zh">2. 提撥 1% 獲利救災 (Disaster Relief)</span><span class="lang-en">2. 1% Profit for Disaster Relief</span></p></div>
                                <div class="opt-choice"><p><span class="lang-zh">3. 主動提升工安標準 20% (Safety)</span><span class="lang-en">3. 20% Safety Upgrade Above Law</span></p></div>
                                <div class="opt-choice"><p><span class="lang-zh">4. 透過海外避稅港合憲避稅 (Tax Haven)</span><span class="lang-en">4. Tax Haven Avoidance</span></p></div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 14: Activity 1 - Class Discussion -->
            <section class="slide" id="slide-14" data-title="Slide 14: 活動一 - 討論與點評">
                <div class="slide-container center-header-layout">
                    <div class="header-block center-text">
                        <div class="section-tag activity-tag"><i class="fa-solid fa-comments"></i> Class Debrief</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">全班討論與迷思澄清</span>
                            <span class="lang-en">Activity 1: Debrief & Common Myths</span>
                        </h2>
                    </div>

                    <div class="debrief-box glass-card glow-card">
                        <i class="fa-solid fa-lightbulb debrief-icon"></i>
                        <div class="debrief-content">
                            <h4><span class="lang-zh">教師觀點帶出 (Key Takeaway)：</span><span class="lang-en">Faculty Debrief:</span></h4>
                            <p>
                                <span class="lang-zh">「做公益 (Philanthropic) 不能洗白違法與不道德行為！如果一家公司一方面租用避稅港避稅 (Legal 灰色地帶)，另一方面捐幾百萬做公益，這不是真實的 CSR，而是公關洗白。」</span>
                                <span class="lang-en">"Philanthropy cannot wash away illegal or unethical acts. Donating millions while avoiding tax in havens is PR washing, not genuine CSR."</span>
                            </p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 15: CSR vs CSV -->
            <section class="slide" id="slide-15" data-title="Slide 15: CSR vs CSV 深度對比">
                <div class="slide-container center-header-layout">
                    <div class="header-block center-text">
                        <div class="section-tag"><i class="fa-solid fa-scale-balanced"></i> Part III • Creating Shared Value</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">CSR vs. CSV 根本理念差異</span>
                            <span class="lang-en">CSR vs. Creating Shared Value (CSV)</span>
                        </h2>
                    </div>

                    <div class="grid-2col gap-4 mt-3">
                        <div class="theory-card glass-card">
                            <div class="theory-header">
                                <h3>CSR (Corporate Social Responsibility)</h3>
                                <div class="author-name"><span class="lang-zh">善後補償與公關預算 (Cost Center)</span><span class="lang-en">After-profit Responsibility (Cost Center)</span></div>
                            </div>
                            <ul class="bullet-list mt-3">
                                <li><span class="lang-zh">理念：做善事，回應社會壓力。</span><span class="lang-en">Motivation: Doing good under social pressure.</span></li>
                                <li><span class="lang-zh">模式：撥出賺來的利潤做公益捐款。</span><span class="lang-en">Model: Spending earned profits on charity.</span></li>
                                <li><span class="lang-zh">範例：購買「公平貿易」咖啡豆。</span><span class="lang-en">Example: Buying Fair Trade certified coffee.</span></li>
                            </ul>
                        </div>

                        <div class="theory-card glass-card highlight-card">
                            <div class="theory-header">
                                <h3>CSV (Creating Shared Value)</h3>
                                <div class="author-name"><span class="lang-zh">融入核心商業模式 (Value Center)</span><span class="lang-en">Core Business Integration (Value Center)</span></div>
                            </div>
                            <ul class="bullet-list mt-3">
                                <li><span class="lang-zh">理念：連結社會需求與商業利潤。</span><span class="lang-en">Motivation: Aligning societal needs with profit.</span></li>
                                <li><span class="lang-zh">模式：透過解決社會問題來賺取財富。</span><span class="lang-en">Model: Generating profit by solving social issues.</span></li>
                                <li><span class="lang-zh">範例：直接技術輔導咖啡農 (Direct Sourcing)。</span><span class="lang-en">Example: Direct Sourcing & training coffee farmers.</span></li>
                            </ul>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 16: Porter & Kramer CSV Framework -->
            <section class="slide" id="slide-16" data-title="Slide 16: Porter CSV 3 大途徑">
                <div class="slide-container center-header-layout">
                    <div class="header-block center-text">
                        <div class="section-tag"><i class="fa-solid fa-cubes"></i> CSV Framework</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">Michael Porter 重塑共享價值的 3 大途徑</span>
                            <span class="lang-en">3 Routes to Creating Shared Value</span>
                        </h2>
                    </div>

                    <div class="cards-grid-3x2">
                        <div class="decision-card glass-card">
                            <h4>1. <span class="lang-zh">重塑產品與市場</span><span class="lang-en">Reconceiving Products</span></h4>
                            <p><span class="lang-zh">開發能解決社會與環境需求的新商品（如平價營養品、綠能車）。</span><span class="lang-en">Developing products that meet societal/environmental needs.</span></p>
                        </div>
                        <div class="decision-card glass-card">
                            <h4>2. <span class="lang-zh">重新定義價值鏈生產力</span><span class="lang-en">Redefining Productivity</span></h4>
                            <p><span class="lang-zh">改善供應鏈能源使用、物流效率與員工健康以降低成本。</span><span class="lang-en">Improving energy, logistics, and worker health to cut costs.</span></p>
                        </div>
                        <div class="decision-card glass-card">
                            <h4>3. <span class="lang-zh">建立在地產業聚落</span><span class="lang-en">Enabling Local Clusters</span></h4>
                            <p><span class="lang-zh">扶植在地供應商與基礎建設，提升整體生態系競爭力。</span><span class="lang-en">Supporting local suppliers and infrastructure for cluster growth.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 17: Case 1 - Nestlé CSV -->
            <section class="slide" id="slide-17" data-title="Slide 17: Nestlé CSV 案例">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-mug-hot"></i> Case 1 • Nestlé CSV</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">案例一：Nestlé 雀巢農業直接採購</span>
                            <span class="lang-en">Case 1: Nestlé Direct Sourcing CSV</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-seedling accent-icon"></i> <span class="lang-zh">輔導農民 ＝ 穩定優質品質原料</span><span class="lang-en">Farmer Empowerment = Quality Supply</span></h3>
                            <p><span class="lang-zh">Nestlé 在開發中國家派駐農業專家，直接提供咖啡農技術指導與無息貸款。農民產量與收入倍增 (社會效益)，Nestlé 獲得穩定高質量原料 (商業效益)，創造雙贏共享價值！</span>
                            <span class="lang-en">Nestlé provides agronomist support and zero-interest loans directly to coffee farmers. Farmers double yields while Nestlé secures premium supplies.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 18: Case 2 - Unilever USLP -->
            <section class="slide" id="slide-18" data-title="Slide 18: Unilever 永續生活計畫">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-soap"></i> Case 2 • Unilever USLP</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">案例二：Unilever 永續生活計畫</span>
                            <span class="lang-en">Case 2: Unilever Sustainable Living Plan</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-leaf accent-icon"></i> <span class="lang-zh">業務成長翻倍，環境足跡減半</span><span class="lang-en">Double Business, Halve Footprint</span></h3>
                            <p><span class="lang-zh">Unilever 旗下 Lifebuoy 肥皂在印度推廣洗手衛生教育，降低兒童傳染病 (社會價值)，同時讓 Lifebuoy 成為銷售額破十億歐元的大品牌 (商業價值)！</span>
                            <span class="lang-en">Lifebuoy soap promoted handwashing hygiene education across rural India, dropping disease rates while growing into a billion-euro brand.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 19: Case 3 - Patagonia -->
            <section class="slide" id="slide-19" data-title="Slide 19: Patagonia 震撼廣告">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-shirt"></i> Case 3 • Patagonia</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">案例三：Patagonia "Don't Buy This Jacket"</span>
                            <span class="lang-en">Case 3: Patagonia Radical Transparency</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-ban accent-icon"></i> <span class="lang-zh">反過利主義的極致誠信行銷</span><span class="lang-en">Don't Buy This Jacket Campaign</span></h3>
                            <p><span class="lang-zh">黑色星期五刊登廣告呼籲顧客「不要買這件外套，除非你真的需要」，並提供免費修補服務。極致的透明與理念堅持，換來品牌忠誠度與營收大增！</span>
                            <span class="lang-en">Patagonia ran ads on Black Friday telling customers not to buy unneeded clothes, providing lifetime repairs and winning unrivaled loyalty.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 20: What is Greenwashing? -->
            <section class="slide" id="slide-20" data-title="Slide 20: 什麼是 Greenwashing 漂綠？">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag warning-tag"><i class="fa-solid fa-mask"></i> Part IV • Greenwashing Audit</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">什麼是 Greenwashing (漂綠)？</span>
                            <span class="lang-en">What is Greenwashing?</span>
                        </h2>
                        <p class="slide-sub">Deceptive Eco-Marketing</p>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-spray-can accent-icon"></i> <span class="lang-zh">行銷包裝 vs 實際行動的巨大落差</span><span class="lang-en">Deceptive Eco-Marketing Gap</span></h3>
                            <p><span class="lang-zh">企業透過誇大、不實或誤導性的宣傳，將自己塑造為環保永續，但實際營運行動卻高度破壞環境或違反倫理的欺罔手段。</span><span class="lang-en">Exaggerated or false environmental claims designed to mislead consumers while core business operations continue polluting.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 21: Common Greenwashing Buzzwords -->
            <section class="slide" id="slide-21" data-title="Slide 21: 常見漂綠模糊用語">
                <div class="slide-container center-header-layout">
                    <div class="header-block center-text">
                        <div class="section-tag warning-tag"><i class="fa-solid fa-triangle-exclamation"></i> 7 Sins of Greenwashing</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">常見漂綠模糊用語與 7 Sins 的審查</span>
                            <span class="lang-en">Greenwashing Buzzwords & 7 Sins</span>
                        </h2>
                    </div>

                    <div class="cards-grid-3x2">
                        <div class="decision-card glass-card">
                            <h4>"Carbon Neutral?"</h4>
                            <p><span class="lang-zh">宣稱碳中和，實質僅購買品質存疑的廉價碳權抵換。</span><span class="lang-en">Claiming neutrality solely via unverified cheap offsets.</span></p>
                        </div>
                        <div class="decision-card glass-card">
                            <h4>"100% Eco-Friendly?"</h4>
                            <p><span class="lang-zh">模糊籠統字眼，缺乏任何第三方數據證明。</span><span class="lang-en">Vague marketing terms without third-party proof.</span></p>
                        </div>
                        <div class="decision-card glass-card">
                            <h4>"Natural & Bio?"</h4>
                            <p><span class="lang-zh">標榜天然，但生產過程卻釋放大量毒性廢水。</span><span class="lang-en">Labeling natural while manufacturing pollutes rivers.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 22: Greenwashing Failure Cases -->
            <section class="slide" id="slide-22" data-title="Slide 22: 漂綠失敗案例剖析">
                <div class="slide-container center-header-layout">
                    <div class="header-block center-text">
                        <div class="section-tag warning-tag"><i class="fa-solid fa-skull"></i> Scandals Audit</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">國際三大震撼漂綠失敗案例</span>
                            <span class="lang-en">Three Famous Greenwashing Scandals</span>
                        </h2>
                    </div>

                    <div class="cards-grid-4">
                        <div class="rc-card glass-card">
                            <div class="rc-num">01</div>
                            <h4>H&M Conscious</h4>
                            <p><span class="lang-zh">舊衣回收計畫被揭發多數焚燒或丟棄海外廢棄物山。</span><span class="lang-en">Recycling scheme caught dumping clothes in African landfills.</span></p>
                        </div>
                        <div class="rc-card glass-card">
                            <div class="rc-num">02</div>
                            <h4>Volkswagen Clean</h4>
                            <p><span class="lang-zh">主打「Clean Diesel」行銷，實質安裝作弊軟體。</span><span class="lang-en">Marketed "Clean Diesel" while installing defeat software.</span></p>
                        </div>
                        <div class="rc-card glass-card">
                            <div class="rc-num">03</div>
                            <h4>Shell Net-Zero Ads</h4>
                            <p><span class="lang-zh">天價廣告推廣綠能，實質綠能支出不足總額 1%。</span><span class="lang-en">Big green energy ads despite green spending <1% of capital.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 23: Activity 2 - Greenwashing Detective -->
            <section class="slide" id="slide-23" data-title="Slide 23: 活動二 - 漂綠偵探社">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag activity-tag"><i class="fa-solid fa-magnifying-glass"></i> Activity 2 • 20 Minutes</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">Greenwashing Detective</span>
                            <span class="lang-en">Greenwashing Detective Workshop</span>
                        </h2>
                        <p class="slide-sub">Audit Real Corporate ESG Ads for Greenwashing</p>
                    </div>

                    <div class="main-panel">
                        <div class="scenario-card glass-card highlight-border">
                            <h3><span class="lang-zh">小組審查任務：分析下列企業 ESG 廣告</span><span class="lang-en">Audit Corporate ESG Advertisements</span></h3>
                            <div class="grid-2col mt-3 gap-2">
                                <div class="opt-choice"><p>1. H&M Conscious Collection</p></div>
                                <div class="opt-choice"><p>2. Coca-Cola World Without Waste</p></div>
                                <div class="opt-choice"><p>3. Starbucks Strawless Lid Campaign</p></div>
                                <div class="opt-choice"><p>4. Apple Carbon Neutral Watch</p></div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 24: Activity 2 - Team Pitch -->
            <section class="slide" id="slide-24" data-title="Slide 24: 活動二 - 發表與改善">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag activity-tag"><i class="fa-solid fa-microphone"></i> Team Pitch</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">各組 3 分鐘 Pitch 與改善方案</span>
                            <span class="lang-en">Team Pitches & Remediation Plans</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-check-double accent-icon"></i> <span class="lang-zh">如何從漂綠轉化為真實 CSR？</span><span class="lang-en">Turning Greenwashing into Genuine CSR</span></h3>
                            <p><span class="lang-zh">1. 資訊極致透明 (Full Transparency)；<br>2. 第三方可驗證數據 (Verified Data)；<br>3. 核心業務實質減碳非僅公關發言。</span>
                            <span class="lang-en">1. Full Transparency; 2. Third-party Verified Data; 3. Real Decarbonization in Core Operations.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 25: Homework 3 & Summary -->
            <section class="slide" id="slide-25" data-title="Slide 25: 重點整理與課堂作業">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag homework-tag"><i class="fa-solid fa-pen-ruler"></i> Homework 3 • Due Next Week</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">本週總結與 Homework 3 作業</span>
                            <span class="lang-en">Summary & Homework 3 Guidelines</span>
                        </h2>
                    </div>

                    <div class="main-panel">
                        <div class="glass-card feature-card mb-3">
                            <h3><i class="fa-solid fa-question-circle accent-icon"></i> <span class="lang-zh">Homework 3 題目：CSR 與漂綠診斷個案 (1,200-1,500字)</span><span class="lang-en">Homework 3: CSR & Greenwashing Audit (1,200-1,500w)</span></h3>
                            <p><span class="lang-zh">選擇一家企業，分析其 3 項 CSR 措施、套用 Carroll 金字塔、評估是否符合 CSV 共享價值與是否存在漂綠疑慮，並提出 2 項改善建議。</span>
                            <span class="lang-en">Select a firm, analyze 3 CSR actions, apply Carroll Pyramid, audit CSV alignment and Greenwashing risks, and propose 2 improvements.</span></p>
                        </div>
                        <div class="glass-card rubrics-card">
                            <h4><i class="fa-solid fa-chart-bar accent-icon"></i> AACSB <span class="lang-zh">評分標準</span><span class="lang-en">Rubrics Breakdown</span></h4>
                            <div class="rubrics-bar">
                                <div class="r-seg seg-1" style="width: 20%;"><span class="lang-zh">資料蒐集 20%</span><span class="lang-en">Data 20%</span></div>
                                <div class="r-seg seg-2" style="width: 25%;"><span class="lang-zh">CSR分析 25%</span><span class="lang-en">CSR 25%</span></div>
                                <div class="r-seg seg-3" style="width: 20%;"><span class="lang-zh">金字塔應用 20%</span><span class="lang-en">Pyramid 20%</span></div>
                                <div class="r-seg seg-4" style="width: 20%;"><span class="lang-zh">CSV與漂綠 20%</span><span class="lang-en">CSV 20%</span></div>
                                <div class="r-seg seg-5" style="width: 15%;"><span class="lang-zh">反思與建議 15%</span><span class="lang-en">Reflect 15%</span></div>
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

with open(r"C:\Users\User\Desktop\第1週_企業為何需要倫理\第3週_企業社會責任與共享價值.html", "w", encoding="utf-8") as f:
    f.write(html_week3)

print("Successfully generated Week 3 HTML presentation file!")
