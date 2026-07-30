import sys

html_week16 = """<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Week 16: The Future of Business Ethics | 企業倫理與永續管理的未來</title>
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
                <h1 class="deck-title">Week 16: The Future of Business Ethics and Sustainable Management</h1>
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
            <a href="第16週_企業倫理與永續的未來.docx" download class="btn btn-secondary" title="Download Teaching Facilitation Guide (.docx)">
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
                            <span class="meta-tag alt">Week 16 • Course Wrap-up & Responsible Leadership</span>
                        </div>
                        <h1 class="main-heading">
                            <span class="lang-zh">企業倫理與永續管理的未來</span>
                            <span class="lang-en">The Future of Business Ethics</span>
                        </h1>
                        <h2 class="sub-heading">
                            <span class="lang-zh">The Future of Business Ethics and Sustainable Management</span>
                            <span class="lang-en">The Future of Business Ethics and Sustainable Management</span>
                        </h2>
                        <p class="lead-text">
                            <span class="lang-zh">16 週知識總融會、AI+ESG 前瞻趨勢、Responsible Leadership 與領導宣言</span>
                            <span class="lang-en">16-Week Knowledge Synthesis, AI+ESG Trends, Responsible Leadership & Manifesto</span>
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
                            <img src="week16_future_cover.jpg" alt="Week 16 Cover Visual" class="slide-img">
                            <div class="visual-badge">
                                <i class="fa-solid fa-graduation-cap"></i> Responsible Leadership • Future
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 2: 16-Week Course Learning Map -->
            <section class="slide" id="slide-2" data-title="Slide 2: 16週全景學習地圖">
                <div class="slide-container center-header-layout">
                    <div class="header-block center-text">
                        <div class="section-tag"><i class="fa-solid fa-map-location-dot"></i> 16-Week Learning Loop</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">本學期 16 週全景學習地圖總融合</span>
                            <span class="lang-en">Full 16-Week Learning Loop Synthesis</span>
                        </h2>
                    </div>

                    <div class="cards-grid-4 mt-3">
                        <div class="rc-card glass-card">
                            <h4>Mod 1: Foundations (W1-3)</h4>
                            <p><span class="lang-zh">Ethics • Theories • CSR/CSV</span><span class="lang-en">Ethics & CSR</span></p>
                        </div>
                        <div class="rc-card glass-card">
                            <h4>Mod 2: ESG Management (W4-8)</h4>
                            <p><span class="lang-zh">ESG • Climate • Stakeholders • Reporting</span><span class="lang-en">ESG Pillars</span></p>
                        </div>
                        <div class="rc-card glass-card">
                            <h4>Mod 3: Strategy & Tech (W9-12)</h4>
                            <p><span class="lang-zh">Finance • Chain • AI • ESG Strategy</span><span class="lang-en">Strategy & Tech</span></p>
                        </div>
                        <div class="rc-card glass-card">
                            <h4>Mod 4: Integration (W13-16)</h4>
                            <p><span class="lang-zh">Cases • Crisis • Capstone • Future</span><span class="lang-en">Capstone & Future</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 3: Evolution of Business Ethics -->
            <section class="slide" id="slide-3" data-title="Slide 3: 企業倫理百年演變歷程">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-timeline"></i> Ethics Evolution</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">企業倫理的百年演變歷程</span>
                            <span class="lang-en">The Evolution of Business Ethics</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-arrow-trend-up accent-icon"></i> <span class="lang-zh">Ethics → CSR → ESG → Sustainability → Responsible Leadership</span><span class="lang-en">Ethics -> CSR -> ESG -> Sustainability -> Responsible Leadership</span></h3>
                            <p><span class="lang-zh">從消極的守法倫理 (Ethics)，走向公關慈善 (CSR)，升級為定量指標 (ESG)，融合為商業策略 (Sustainability)，最終化為女男領導者的核心DNA (Responsible Leadership)！</span>
                            <span class="lang-en">Evolving from passive compliance to purpose-led Responsible Leadership.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 4: 5 Core Values of Responsible Leadership -->
            <section class="slide" id="slide-4" data-title="Slide 4: 負責任領導者 5 大觀念">
                <div class="slide-container center-header-layout">
                    <div class="header-block center-text">
                        <div class="section-tag"><i class="fa-solid fa-heart"></i> 5 Core Values</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">負責任領導者的 5 大觀念柱石</span>
                            <span class="lang-en">5 Core Values of Responsible Leadership</span>
                        </h2>
                    </div>

                    <div class="cards-grid-5">
                        <div class="decision-card glass-card"><h4>1. Integrity</h4><p><span class="lang-zh">誠信：不妥協的道德底線</span><span class="lang-en">Uncompromising ethics</span></p></div>
                        <div class="decision-card glass-card"><h4>2. Transparent</h4><p><span class="lang-zh">透明：公開真實資訊</span><span class="lang-en">Open disclosures</span></p></div>
                        <div class="decision-card glass-card"><h4>3. Accountable</h4><p><span class="lang-zh">問責：勇於承擔決策後果</span><span class="lang-en">Taking responsibility</span></p></div>
                        <div class="decision-card glass-card"><h4>4. Sustainable</h4><p><span class="lang-zh">永續：兼顧跨世代福祉</span><span class="lang-en">Intergenerational value</span></p></div>
                        <div class="decision-card glass-card"><h4>5. Innovation</h4><p><span class="lang-zh">創新：商業突破創造共享</span><span class="lang-en">CSV business breakthroughs</span></p></div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 5: Course Knowledge Integration Matrix -->
            <section class="slide" id="slide-5" data-title="Slide 5: 課程知識全景整合矩陣">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-network-wired"></i> Integration Matrix</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">課程知識全景整合矩陣</span>
                            <span class="lang-en">Course Knowledge Integration Matrix</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-shapes accent-icon"></i> <span class="lang-zh">將概念、資本、營運與數位治理轉化為領導力</span><span class="lang-en">Translating Concepts, Capital & Tech into Leadership</span></h3>
                            <p><span class="lang-zh">你們不再是單一專業的執行者，而是能全盤掌控企業倫理防線、ESG 策略、供應鏈減碳與 AI 數位信任的高階經營者！</span>
                            <span class="lang-en">Empowering you to lead with holistic ethical, strategic, and tech governance vision.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 6: The Future of ESG -->
            <section class="slide" id="slide-6" data-title="Slide 6: Future of ESG 演變趨勢">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-crystal-ball"></i> Part II • Future Trends</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">Future of ESG (ESG 的未來演變趨勢)</span>
                            <span class="lang-en">The Future of ESG</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-chart-line accent-icon"></i> <span class="lang-zh">從被動報告走向系統性企業轉型</span><span class="lang-en">From Passive Reporting to Systemic Transformation</span></h3>
                            <p><span class="lang-zh">未來 10 年，ESG 揭露報告將成為標準基配；真正的競爭優勢在於能否透過商業模式創新實現真正的 Net Zero 與極致社會包容。</span>
                            <span class="lang-en">ESG disclosures will become basic compliance; real edge lies in systemic business model transformation.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 7: AI + ESG Convergence -->
            <section class="slide" id="slide-7" data-title="Slide 7: AI + ESG 雙軸趨勢交會">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag warning-tag"><i class="fa-solid fa-bolt"></i> AI + ESG Fusion</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">AI + ESG 雙軸趨勢的交會與博弈</span>
                            <span class="lang-en">AI + ESG Convergence & Friction</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-robot accent-icon"></i> <span class="lang-zh">用 AI 賦能減碳 vs 控管 AI 資料中心龐大耗電</span><span class="lang-en">Harnessing AI for Decarbonization vs Data Center Power Risks</span></h3>
                            <p><span class="lang-zh">未來的管理者必須同時具備 AI 技術素養與 ESG 氣候警覺，善用 AI 最佳化供應鏈，並控制大模型訓練帶來的碳排與水資源消耗。</span>
                            <span class="lang-en">Balancing AI's climate solution potential against its massive compute power footprint.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 8: Climate Transition Acceleration -->
            <section class="slide" id="slide-8" data-title="Slide 8: 氣候淨零轉型加速">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-fire-flame-curved"></i> Climate Transition</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">Climate Transition (淨零轉型加速)</span>
                            <span class="lang-en">Climate Transition Acceleration</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-temperature-arrow-down accent-icon"></i> <span class="lang-zh">2050 淨零碳排對各國產業鏈的過渡要求</span><span class="lang-en">2050 Net Zero Mandates Mandating Supply Chains</span></h3>
                            <p><span class="lang-zh">各國碳定價、歐盟 CBAM 碳關稅與國際綠電認證將全面強制化，無視氣候轉型的企業將在 5 年內失去國際訂單。</span>
                            <span class="lang-en">Carbon pricing and CBAM tariffs will make decarbonization non-negotiable for global survival.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 9: Nature & Biodiversity (TNFD) -->
            <section class="slide" id="slide-9" data-title="Slide 9: TNFD 自然資本與生物多樣性">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-tree"></i> TNFD Framework</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">Nature & Biodiversity (TNFD 自然資本)</span>
                            <span class="lang-en">Nature & Biodiversity (TNFD)</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-seedling accent-icon"></i> <span class="lang-zh">繼 TCFD 後最新爆發的 TNFD 自然相關揭露</span><span class="lang-en">TNFD Disclosures Following TCFD Mandates</span></h3>
                            <p><span class="lang-zh">企業對天然森林、水資源與生態系的依賴與破壞，將被系統化揭露。守護自然資本 (Natural Capital) 成為全新 ESG 焦點。</span>
                            <span class="lang-en">Taskforce on Nature-related Financial Disclosures (TNFD) mandates reporting on natural capital impacts.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 10: Human Rights & Supply Chain Living Wage -->
            <section class="slide" id="slide-10" data-title="Slide 10: 供應鏈人權與生活薪資">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-hand-holding-hand"></i> Human Rights</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">Human Rights & 供應鏈生活薪資</span>
                            <span class="lang-en">Human Rights & Supply Chain Living Wage</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-person accent-icon"></i> <span class="lang-zh">全球法規要求海外代工廠符合 Living Wage</span><span class="lang-en">Enforcing Living Wages Across Offshore Suppliers</span></h3>
                            <p><span class="lang-zh">歐盟 CSDD (企業永續盡職調查指令) 要求品牌端對全供應鏈的人權、童工、超時加班與 Living Wage (生活薪資) 負起法律責任。</span>
                            <span class="lang-en">EU CSDD mandates legal corporate responsibility for human rights and living wages in global supply chains.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 11: Cybersecurity & Digital Privacy -->
            <section class="slide" id="slide-11" data-title="Slide 11: 資安與數位隱私">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-lock"></i> Cybersecurity</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">Cybersecurity & 數位隱私權保障</span>
                            <span class="lang-en">Cybersecurity & Digital Privacy Rights</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-shield-halved accent-icon"></i> <span class="lang-zh">萬物互聯時代，資安即是核心倫理責任</span><span class="lang-en">Cyber Protection as Core Corporate Ethical Duty</span></h3>
                            <p><span class="lang-zh">保護客戶敏感個資、防範勒索軟體攻擊與建立強韌 IT 備援，是企業獲取客戶信任與維持營運不中斷的底線。</span>
                            <span class="lang-en">Protecting data privacy and guarding against ransomware is an essential ethical requirement.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 12: Digital Trust as Core Equity -->
            <section class="slide" id="slide-12" data-title="Slide 12: Digital Trust 作為核心資產">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-certificate"></i> Digital Trust</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">Digital Trust (數位信任) 作為核心資產</span>
                            <span class="lang-en">Digital Trust as Corporate Core Equity</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-award accent-icon"></i> <span class="lang-zh">2026 企業在 AI 與數據時代的最高品牌壁壘</span><span class="lang-en">The Highest Brand Moat in the AI Era</span></h3>
                            <p><span class="lang-zh">擁有強大數位信任的企業，能在推出新型 AI 產品與數據服務時，獲得消費者最高程度的訂閱與資料共享授權。</span>
                            <span class="lang-en">Firms earning digital trust secure highest user adoption and licensing permissions for AI services.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 13: Global Systemic Risks -->
            <section class="slide" id="slide-13" data-title="Slide 13: 全球系統性風險">
                <div class="slide-container center-header-layout">
                    <div class="header-block center-text">
                        <div class="section-tag warning-tag"><i class="fa-solid fa-earth-americas"></i> Global Systemic Risks</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">全球系統性風險對企業韌性的挑戰</span>
                            <span class="lang-en">Global Systemic Risks Facing Resilience</span>
                        </h2>
                    </div>

                    <div class="cards-grid-4 mt-3">
                        <div class="rc-card glass-card">
                            <h4>Geopolitics</h4>
                            <p><span class="lang-zh">地緣政治衝突與晶片供應鏈脫鉤。</span><span class="lang-en">Geopolitics & decoupling</span></p>
                        </div>
                        <div class="rc-card glass-card">
                            <h4>Macro Inflation</h4>
                            <p><span class="lang-zh">通膨與綠電原物料價格波動。</span><span class="lang-en">Inflation & raw material volatility</span></p>
                        </div>
                        <div class="rc-card glass-card"><h4>Climate Disasters</h4><p><span class="lang-zh">極端天災衝擊廠區營運與物流。</span><span class="lang-en">Extreme weather disruptions</span></p></div>
                        <div class="rc-card glass-card"><h4>AI Outages</h4><p><span class="lang-zh">AI系統失控與全球單點故障。</span><span class="lang-en">AI system failure risks</span></p></div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 14: Activity 1 - Future of Business Workshop -->
            <section class="slide" id="slide-14" data-title="Slide 14: 活動一 - 2035 未來工作坊">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag activity-tag"><i class="fa-solid fa-compass"></i> Activity 1 • 15 Minutes</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">Future of Business Workshop</span>
                            <span class="lang-en">Future of Business Workshop</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="scenario-card glass-card highlight-border">
                            <h3><span class="lang-zh">任務：討論「2035 年，企業最大的倫理與永續挑戰會是什麼？」</span><span class="lang-en">Topic: What is the #1 ESG Challenge in 2035?</span></h3>
                            <div class="grid-2col mt-3 gap-2">
                                <div class="opt-choice"><p>1. 選擇議題 (AI/氣候/地緣/TNFD/資安)</p></div>
                                <div class="opt-choice"><p>2. 精準描述問題細節與衝擊</p></div>
                                <div class="opt-choice"><p>3. 分析對企業營運與估值的影響</p></div>
                                <div class="opt-choice"><p>4. 提出管理者應採取的因應對策</p></div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 15: Activity 1 - Debrief -->
            <section class="slide" id="slide-15" data-title="Slide 15: 活動一 - 答案與點評">
                <div class="slide-container center-header-layout">
                    <div class="header-block center-text">
                        <div class="section-tag activity-tag"><i class="fa-solid fa-comments"></i> Class Debrief</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">未來的管理者必須具備敏銳的宏觀雷達</span>
                            <span class="lang-en">Activity 1: Leaders Need Macro Risk Radars</span>
                        </h2>
                    </div>

                    <div class="debrief-box glass-card glow-card">
                        <i class="fa-solid fa-lightbulb debrief-icon"></i>
                        <div class="debrief-content">
                            <h4><span class="lang-zh">教師觀點帶出 (Key Takeaway)：</span><span class="lang-en">Faculty Debrief:</span></h4>
                            <p><span class="lang-zh">「未來的商業競爭不再是看誰能更低成本地生產，而是看誰具備前瞻雷達，在黑天鵝襲來前率先完成綠色與數位轉型！」</span>
                            <span class="lang-en">"Future business victory belongs to leaders with foresight radars who complete transitions early."</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 16: What is a Responsible Leader -->
            <section class="slide" id="slide-16" data-title="Slide 16: 什麼是 Responsible Leader？">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-user-tie"></i> Part III • Leadership</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">什麼是 Responsible Leader (負責任領導者)？</span>
                            <span class="lang-en">What is a Responsible Leader?</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-heart-pulse accent-icon"></i> <span class="lang-zh">兼顧商業獲利、環境保護與社會正義的領導人</span><span class="lang-en">Balancing Profit, Planet, and Social Justice</span></h3>
                            <p><span class="lang-zh">對接 AACSB 核心概念：負責任領導者不只為股東負責，更以跨世代福祉為己任，用誠信與創新引領企業永續向前。</span>
                            <span class="lang-en">A leader driving economic performance while prioritizing societal well-being and intergenerational ethics.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 17: 5 Core Competencies of Leaders -->
            <section class="slide" id="slide-17" data-title="Slide 17: 未來管理者 5 大能力">
                <div class="slide-container center-header-layout">
                    <div class="header-block center-text">
                        <div class="section-tag"><i class="fa-solid fa-shapes"></i> AACSB 5 Competencies</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">未來管理者必備的 5 大核心能力</span>
                            <span class="lang-en">5 Core Competencies of Future Business Leaders</span>
                        </h2>
                    </div>

                    <div class="cards-grid-5">
                        <div class="decision-card glass-card"><h4>1. Ethical Judgment</h4><p><span class="lang-zh">倫理判斷：堅守誠信底線</span><span class="lang-en">Ethical judgment</span></p></div>
                        <div class="decision-card glass-card"><h4>2. Systems Thinking</h4><p><span class="lang-zh">系統思考：洞察複雜鏈結</span><span class="lang-en">Systems thinking</span></p></div>
                        <div class="decision-card glass-card"><h4>3. Sustainability</h4><p><span class="lang-zh">永續決策：兼顧長線效益</span><span class="lang-en">Sustainable decision</span></p></div>
                        <div class="decision-card glass-card"><h4>4. Collaboration</h4><p><span class="lang-zh">跨界合作：對齊利害關係人</span><span class="lang-en">Cross-sector alignment</span></p></div>
                        <div class="decision-card glass-card"><h4>5. AI Literacy</h4><p><span class="lang-zh">AI 素養：數位治理與信任</span><span class="lang-en">AI & digital literacy</span></p></div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 18: Manager vs Responsible Leader -->
            <section class="slide" id="slide-18" data-title="Slide 18: Manager vs Leader">
                <div class="slide-container center-header-layout">
                    <div class="header-block center-text">
                        <div class="section-tag"><i class="fa-solid fa-arrows-left-right"></i> Leadership Contrast</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">Traditional Manager vs. Responsible Leader 比較表</span>
                            <span class="lang-en">Traditional Manager vs. Responsible Leader</span>
                        </h2>
                    </div>

                    <div class="matrix-table-wrapper glass-card mt-3">
                        <table class="custom-matrix-table">
                            <thead>
                                <tr>
                                    <th><span class="lang-zh">比較維度</span><span class="lang-en">Dimension</span></th>
                                    <th>Traditional Manager (傳統管理者)</th>
                                    <th class="highlight-th">Responsible Leader (負責任領導者)</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td><strong><span class="lang-zh">核心關注焦點</span><span class="lang-en">Focus</span></strong></td>
                                    <td><span class="lang-zh">短期 KPI 達成、季度利潤與內部交易 (Transaction)</span><span class="lang-en">Short-term quarterly EPS & transactions</span></td>
                                    <td><span class="badge warning-badge"><span class="lang-zh">長線使命、社會價值與組織變革 (Transformation)</span><span class="lang-en">Long-term purpose & transformation</span></span></td>
                                </tr>
                                <tr>
                                    <td><strong><span class="lang-zh">對待風險態度</span><span class="lang-en">Risk Attitude</span></strong></td>
                                    <td><span class="lang-zh">被動合規、避開罰款與消極防守</span><span class="lang-en">Passive compliance & fine avoidance</span></td>
                                    <td><span class="badge warning-badge"><span class="lang-zh">前瞻預警、主動創新與建立 VRIO 護城河</span><span class="lang-en">Active innovation & VRIO moats</span></span></td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </section>

            <!-- SLIDE 19: Personal Values -->
            <section class="slide" id="slide-19" data-title="Slide 19: 個人價值觀與領導力">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-fingerprint"></i> Core Identity</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">個人價值觀與領導力靈魂的形塑</span>
                            <span class="lang-en">Personal Values & Leadership Identity</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-gem accent-icon"></i> <span class="lang-zh">誠信、公平與同理心是領導力的靈魂</span><span class="lang-en">Integrity, Fairness & Empathy as the Soul</span></h3>
                            <p><span class="lang-zh">技能可以培訓、工具可以學習；唯有堅定不移的個人倫理價值觀，能在遭遇重大商業利益誘惑與危機衝擊時，指引你做出正確決策！</span>
                            <span class="lang-en">Skills can be taught; core ethical values guide right decisions when facing profit temptations.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 20: Career & Sustainability -->
            <section class="slide" id="slide-20" data-title="Slide 20: 職涯與永續的融合">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-briefcase"></i> Career Integration</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">Career & Sustainability (職涯與永續的融合)</span>
                            <span class="lang-en">Integrating Sustainability into Your Career</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-route accent-icon"></i> <span class="lang-zh">在任何崗位（財務/行銷/HR/營運）實踐永續</span><span class="lang-en">Practicing Sustainability Across Every Function</span></h3>
                            <p><span class="lang-zh">你不需要掛著「永續長」的頭銜才能推動永續！財務官能推動綠色融資、行銷官能打擊漂綠、HR能貫徹 DEI、營運官能推減碳。</span>
                            <span class="lang-en">You don't need a CSO title to champion sustainability; drive green impacts in finance, marketing, or HR.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 21: Activity 2 - My Leadership Manifesto -->
            <section class="slide" id="slide-21" data-title="Slide 21: 活動二 - 我的領導宣言">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag activity-tag"><i class="fa-solid fa-pen-nib"></i> Activity 2 • 30 Minutes</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">My Leadership Manifesto (領導宣言)</span>
                            <span class="lang-en">My Leadership Manifesto Workshop</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="scenario-card glass-card highlight-border">
                            <h3><span class="lang-zh">任務：撰寫與宣讀 1 頁「我的領導宣言」</span><span class="lang-en">Drafting & Reciting Your 1-Page Manifesto</span></h3>
                            <div class="grid-2col mt-3 gap-2">
                                <div class="opt-choice"><p>1. 我希望成為什麼樣的管理者？</p></div>
                                <div class="opt-choice"><p>2. 我最重視的三項價值觀 (Integrity...)</p></div>
                                <div class="opt-choice"><p>3. 我如何看待永續經營與倫理實踐？</p></div>
                                <div class="opt-choice"><p>4. 我未來五年的具體行動計畫</p></div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 22: Manifesto Recitation & Faculty Closing -->
            <section class="slide" id="slide-22" data-title="Slide 22: 宣言宣讀與結業感言">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag activity-tag"><i class="fa-solid fa-microphone"></i> Recitation</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">學生宣言宣讀與教師結業感言</span>
                            <span class="lang-en">Manifesto Recitation & Closing Remarks</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-award accent-icon"></i> <span class="lang-zh">凝聚負責任領導者社群的終極誓言</span><span class="lang-en">Forging a Community of Responsible Leaders</span></h3>
                            <p><span class="lang-zh">聆聽同學宣讀領導宣言，教師總結：本門課不僅給予你們學分與知識，更為你們注入了終生受用的企業倫理與永續領導力魂魄！</span>
                            <span class="lang-en">Synthesizing personal commitments into a lifelong ethical and sustainable leadership mindset.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 23: The 16-Week Learning Loop -->
            <section class="slide" id="slide-23" data-title="Slide 23: 16週學習閉環大總結">
                <div class="slide-container center-header-layout">
                    <div class="header-block center-text">
                        <div class="section-tag"><i class="fa-solid fa-graduation-cap"></i> Course Graduation</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">16 週完整學習閉環大總結</span>
                            <span class="lang-en">The 16-Week Complete Learning Loop</span>
                        </h2>
                    </div>

                    <div class="cards-grid-4 mt-3">
                        <div class="rc-card glass-card">
                            <h4>Phase 1: Foundation</h4><p><span class="lang-zh">倫理思維、CSR 與共享價值</span><span class="lang-en">Ethics & CSV</span></p>
                        </div>
                        <div class="rc-card glass-card">
                            <h4>Phase 2: ESG Management</h4><p><span class="lang-zh">E/S/G 構面與 GRI 揭露</span><span class="lang-en">ESG & Disclosure</span></p>
                        </div>
                        <div class="rc-card glass-card">
                            <h4>Phase 3: Strategy & Tech</h4><p><span class="lang-zh">金融、 Scope 3、AI 與 VRIO</span><span class="lang-en">Finance, Scope 3, AI</span></p>
                        </div>
                        <div class="rc-card glass-card">
                            <h4>Phase 4: Leadership</h4><p><span class="lang-zh">案例診斷、危機與 Capstone</span><span class="lang-en">Cases, Crisis & Capstone</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 24: Recommended Booklist & Videos -->
            <section class="slide" id="slide-24" data-title="Slide 24: 推薦閱讀與影音靈感">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-book-open-reader"></i> Recommended Books</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">推薦經典閱讀與影音靈感</span>
                            <span class="lang-en">Recommended Reading & Video List</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="cards-grid-4">
                            <div class="info-box glass-card"><h4>Net Positive</h4><p>Paul Polman</p></div>
                            <div class="info-box glass-card"><h4>Conscious Capital</h4><p>John Mackey</p></div>
                            <div class="info-box glass-card"><h4>Infinite Game</h4><p>Simon Sinek</p></div>
                            <div class="info-box glass-card"><h4>Doughnut Econ</h4><p>Kate Raworth</p></div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 25: Call to Action & Homework 16 -->
            <section class="slide" id="slide-25" data-title="Slide 25: Take Action & Homework 16">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag homework-tag"><i class="fa-solid fa-flag-checkered"></i> Take Action & HW16</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">Take Action & Homework 16</span>
                            <span class="lang-en">Take Action & Homework 16</span>
                        </h2>
                    </div>

                    <div class="main-panel">
                        <div class="glass-card feature-card mb-2">
                            <h3><i class="fa-solid fa-rocket accent-icon"></i> <span class="lang-zh">Take Action, Lead Responsibly! 結業宣告</span><span class="lang-en">Take Action, Lead Responsibly!</span></h3>
                            <p class="mb-2"><span class="lang-zh">恭喜大家完成 16 週頂尖 AACSB 規格課程！勇敢帶著負責任領導力走入職場，改變商業世界！</span><span class="lang-en">Congratulations on completing this top AACSB-standard course!</span></p>
                        </div>

                        <div class="glass-card feature-card mb-2">
                            <h3><i class="fa-solid fa-file-invoice accent-icon"></i> <span class="lang-zh">Homework 16：期末反思報告 (約 1,500–2,000 字/個人)</span><span class="lang-en">Homework 16: Final Reflection Report (~1,500-2,000w)</span></h3>
                            <p><span class="lang-zh">個人完成：本學期最大收穫、最改變想法的主題、2035 未來企業挑戰、若身為 CEO 的推動策略與個人 Leadership 宣言。</span>
                            <span class="lang-en">Individual report: course takeaways, mindset shifts, 2035 challenges & personal leadership manifesto.</span></p>
                        </div>

                        <div class="glass-card rubrics-card">
                            <h4><i class="fa-solid fa-chart-bar accent-icon"></i> AACSB <span class="lang-zh">評分標準</span><span class="lang-en">Rubrics Breakdown</span></h4>
                            <div class="rubrics-bar">
                                <div class="r-seg seg-1" style="width: 30%;"><span class="lang-zh">整合能力 30%</span><span class="lang-en">Integration 30%</span></div>
                                <div class="r-seg seg-2" style="width: 25%;"><span class="lang-zh">趨勢分析 25%</span><span class="lang-en">Trends 25%</span></div>
                                <div class="r-seg seg-3" style="width: 20%;"><span class="lang-zh">個人反思 20%</span><span class="lang-en">Reflect 20%</span></div>
                                <div class="r-seg seg-4" style="width: 15%;"><span class="lang-zh">領導宣言 15%</span><span class="lang-en">Manifesto 15%</span></div>
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

with open(r"C:\Users\User\Desktop\第1週_企業為何需要倫理\第16週_企業倫理與永續的未來.html", "w", encoding="utf-8") as f:
    f.write(html_week16)

print("Successfully generated Week 16 HTML presentation file!")
