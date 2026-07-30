import sys

html_week10 = """<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Week 10: Sustainable Supply Chain & Circular Economy | 永續供應鏈與循環經濟</title>
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
                <h1 class="deck-title">Week 10: Sustainable Supply Chain and Circular Economy</h1>
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
            <a href="第10週_永續供應鏈與循環經濟.docx" download class="btn btn-secondary" title="Download Teaching Facilitation Guide (.docx)">
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
                            <span class="meta-tag alt">Week 10 • Supply Chain Strategy Presentation</span>
                        </div>
                        <h1 class="main-heading">
                            <span class="lang-zh">永續供應鏈管理與循環經濟</span>
                            <span class="lang-en">Sustainable Supply Chain & Circular Economy</span>
                        </h1>
                        <h2 class="sub-heading">
                            <span class="lang-zh">Sustainable Supply Chain and Circular Economy</span>
                            <span class="lang-en">Sustainable Supply Chain and Circular Economy</span>
                        </h2>
                        <p class="lead-text">
                            <span class="lang-zh">Scope 3 價值鏈減碳、負責任採購、5 R's 框架、Patagonia & IKEA 循環商業模式</span>
                            <span class="lang-en">Scope 3 Decarbonization, Responsible Sourcing, 5 R's Framework, Patagonia & IKEA Circular Models</span>
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
                            <img src="week10_supplychain_cover.jpg" alt="Week 10 Cover Visual" class="slide-img">
                            <div class="visual-badge">
                                <i class="fa-solid fa-recycle"></i> Scope 3 • 5 R's • Circular Business
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
                            <span class="lang-zh">課程邏輯主線：進入企業實體營運與供應鏈戰略</span>
                            <span class="lang-en">Course Journey: Entering Corporate Operations Strategy</span>
                        </h2>
                    </div>

                    <div class="evolution-chain-card glass-card">
                        <div class="chain-items">
                            <div class="c-node"><div class="c-icon"><i class="fa-solid fa-heart"></i></div><h4>W1-3 Ethics/CSR</h4><p><span class="lang-zh">倫理基因</span><span class="lang-en">Ethics & CSR</span></p></div>
                            <div class="c-connector"><i class="fa-solid fa-arrow-right-long"></i></div>
                            <div class="c-node"><div class="c-icon"><i class="fa-solid fa-chart-pie"></i></div><h4>W4-7 ESG & E/S/G</h4><p><span class="lang-zh">三大構面</span><span class="lang-en">ESG Pillars</span></p></div>
                            <div class="c-connector"><i class="fa-solid fa-arrow-right-long"></i></div>
                            <div class="c-node"><div class="c-icon"><i class="fa-solid fa-landmark"></i></div><h4>W8-9 Report & Fin</h4><p><span class="lang-zh">揭露與金融</span><span class="lang-en">Reporting & Fin</span></p></div>
                            <div class="c-connector"><i class="fa-solid fa-arrow-right-long"></i></div>
                            <div class="c-node highlight-node"><div class="c-icon"><i class="fa-solid fa-recycle"></i></div><h4>W10 Today</h4><p><span class="lang-zh">Supply Chain (供應鏈)<br>(永續供應鏈與循環經濟)</span><span class="lang-en">Supply Chain<br>(Sustainable Supply Chain)</span></p></div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 3: Warm-up Question -->
            <section class="slide" id="slide-3" data-title="Slide 3: 暖身問題 - Apple 能單靠自己嗎？">
                <div class="slide-container center-header-layout">
                    <div class="header-block center-text">
                        <div class="section-tag warning-tag"><i class="fa-solid fa-truck-fast"></i> Supply Chain Dilemma</div>
                        <h2 class="slide-heading giant-title">
                            <span class="lang-zh">暖身問題：Apple 單靠總部自己，能達成真正 ESG 嗎？</span>
                            <span class="lang-en">Warm-up: Can Apple Achieve ESG Alone Without Suppliers?</span>
                        </h2>
                    </div>

                    <div class="dilemma-box glass-card glow-card">
                        <div class="dilemma-statement">
                            <p class="quote-text">
                                <span class="lang-zh">「Apple 總部就算 100% 用綠電，若全球 200+ 關鍵代工廠繼續用煤電、過勞與排毒，Apple 的 ESG 聲譽將徹底崩盤！<strong>企業 70%–95% 的碳排來自 Scope 3 供應鏈，供應鏈即是企業真正的 ESG 本體！</strong>」</span>
                                <span class="lang-en">"Apple cannot reach ESG alone when 70-95% of emissions are in Scope 3 suppliers!"</span>
                            </p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 4: Scope 3 Dominance -->
            <section class="slide" id="slide-4" data-title="Slide 4: Scope 3 佔比現實">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag warning-tag"><i class="fa-solid fa-industry"></i> Scope 3 Reality</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">Scope 3 碳排放的絕對支配地位</span>
                            <span class="lang-en">Scope 3 Dominance in Global Supply Chains</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-chart-pie accent-icon"></i> <span class="lang-zh">國際品牌巨擘 70%–95% 碳足跡來自範疇 3</span><span class="lang-en">70-95% of Total Emissions Sit in Scope 3</span></h3>
                            <p><span class="lang-zh">Apple, Nike, TSMC, Unilever, IKEA 等全球企業，極大部分的碳排放與人權風險皆集中在範疇 3 價值鏈（原料採購、代工製造、物流運輸與廢棄處理）。</span>
                            <span class="lang-en">Overwhelming carbon and labor risks sit in Scope 3 supply chain upstream and downstream value chains.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 5: Supply Chain IS Corporate ESG -->
            <section class="slide" id="slide-5" data-title="Slide 5: Supply Chain 就是 ESG">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-shield-cat"></i> Core Axiom</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">Supply Chain 就是企業真正的 ESG</span>
                            <span class="lang-en">Supply Chain IS Corporate ESG</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-award accent-icon"></i> <span class="lang-zh">企業的 ESG 聲譽由最脆弱的代工廠決定</span><span class="lang-en">Corporate Reputation Dictated by Supplier Performance</span></h3>
                            <p><span class="lang-zh">資本市場與消費者不再區分「總部」或「外包廠」。代工廠的工安事故、強迫勞動或毒廢水，將直接摧毀品牌價值與 ESG Rating！</span>
                            <span class="lang-en">Investors and consumers hold brands directly accountable for supplier labor abuse or toxic waste.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 6: Traditional vs Sustainable Supply Chain -->
            <section class="slide" id="slide-6" data-title="Slide 6: 傳統 vs 永續供應鏈">
                <div class="slide-container center-header-layout">
                    <div class="header-block center-text">
                        <div class="section-tag"><i class="fa-solid fa-code-compare"></i> Supply Chain Shift</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">Traditional vs. Sustainable Supply Chain 比較表</span>
                            <span class="lang-en">Traditional vs. Sustainable Supply Chain Matrix</span>
                        </h2>
                    </div>

                    <div class="matrix-table-wrapper glass-card mt-3">
                        <table class="custom-matrix-table">
                            <thead>
                                <tr>
                                    <th><span class="lang-zh">比較面向</span><span class="lang-en">Dimension</span></th>
                                    <th>Traditional Supply Chain (傳統供應鏈)</th>
                                    <th class="highlight-th">Sustainable Supply Chain (永續供應鏈)</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td><strong><span class="lang-zh">核心驅動目標</span><span class="lang-en">Primary Goal</span></strong></td>
                                    <td><span class="lang-zh">追求極致最低成本與即時交貨 (Cost/JIT)</span><span class="lang-en">Cost minimization & JIT speed</span></td>
                                    <td><span class="badge warning-badge"><span class="lang-zh">韌性、ESG合規與綠色轉型 (Resilience/ESG)</span><span class="lang-en">Resilience, ESG compliance & greening</span></span></td>
                                </tr>
                                <tr>
                                    <td><strong><span class="lang-zh">供應商關係</span><span class="lang-en">Supplier Relation</span></strong></td>
                                    <td><span class="lang-zh">零和價格割喉、隨時更換代工廠</span><span class="lang-en">Zero-sum price pressure</span></td>
                                    <td><span class="badge warning-badge"><span class="lang-zh">長期共榮夥伴、技術輔導與綠電共購</span><span class="lang-en">Long-term enablement & co-investment</span></span></td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </section>

            <!-- SLIDE 7: Responsible Sourcing -->
            <section class="slide" id="slide-7" data-title="Slide 7: Responsible Sourcing 負責任採購">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-hand-holding-heart"></i> Part II • Management</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">Responsible Sourcing (負責任採購)</span>
                            <span class="lang-en">Responsible Sourcing Principles</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-basket-shopping accent-icon"></i> <span class="lang-zh">將倫理與永續標準導入採購審查</span><span class="lang-en">Integrating Ethics into Purchasing</span></h3>
                            <p><span class="lang-zh">採購團隊不僅看價格與品質，更審查原料來源是否合乎公平貿易 (Fairtrade)、零森林砍伐、無衝突礦產 (Conflict Minerals) 與在地化採購。</span>
                            <span class="lang-en">Purchasing decisions mandating Fairtrade, zero-deforestation, and conflict-free mineral sourcing.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 8: Supplier Code of Conduct -->
            <section class="slide" id="slide-8" data-title="Slide 8: 供應商行為守則">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-file-contract"></i> Code of Conduct</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">Supplier Code of Conduct (行為守則)</span>
                            <span class="lang-en">Supplier Code of Conduct</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-gavel accent-icon"></i> <span class="lang-zh">強制要求代工廠遵守工安與人權標準</span><span class="lang-en">Mandating Factory Safety & Labor Compliance</span></h3>
                            <p><span class="lang-zh">要求所有 Tier 1, 2 供應商簽署行為守則，明確規範禁止童工、禁止強迫勞動、限制每週工時、工安設備與廢水處理。</span>
                            <span class="lang-en">Mandating all Tier 1 & Tier 2 suppliers to sign binding agreements on labor rights, safety, and waste management.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 9: Supplier Audit -->
            <section class="slide" id="slide-9" data-title="Slide 9: 供應商稽核與實地查驗">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-clipboard-check"></i> On-site Audits</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">Supplier Audit (供應商稽核與輔導)</span>
                            <span class="lang-en">Supplier Audit & Verification</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-magnifying-glass accent-icon"></i> <span class="lang-zh">第三方無預警抽查與違規輔導改善</span><span class="lang-en">Unannounced Third-party Audits & Remediation</span></h3>
                            <p><span class="lang-zh">委託獨立專業機構進行無預警實地廠地抽查，針對重大違規給予限期改善要求，嚴重違規者直接剔除合格供應商名單。</span>
                            <span class="lang-en">Conducting unannounced third-party factory audits and removing non-compliant suppliers from qualified lists.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 10: Human Rights in Supply Chains -->
            <section class="slide" id="slide-10" data-title="Slide 10: 供應鏈人權保障">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-person"></i> Labor Rights</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">供應鏈人權與勞工權益保障</span>
                            <span class="lang-en">Human Rights in Global Supply Chains</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-hand-holding-hand accent-icon"></i> <span class="lang-zh">打擊海外代工廠血汗勞動與低薪剝削</span><span class="lang-en">Eliminating Sweatshops and Wage Exploitation</span></h3>
                            <p><span class="lang-zh">確保海外代工廠提供符合當地生活水平的薪資 (Living Wage)、工會代表權與健康安全工作環境，防範現代奴隸。</span>
                            <span class="lang-en">Ensuring living wages, union representation rights, and safe working conditions across offshore suppliers.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 11: Scope 3 Carbon Footprint -->
            <section class="slide" id="slide-11" data-title="Slide 11: 供應鏈碳足跡與減碳">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-smog"></i> Carbon Footprint</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">供應鏈碳足跡與 Scope 3 減碳</span>
                            <span class="lang-en">Supply Chain Carbon Footprint & Scope 3</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-calculator accent-icon"></i> <span class="lang-zh">輔導供應商進行 ISO 14064 盤查與綠電轉型</span><span class="lang-en">Assisting Suppliers with ISO 14064 & Green Power</span></h3>
                            <p><span class="lang-zh">協助供應商核算產品碳足跡 (ISO 14067)，設定 SBTi 減碳目標，並要求代工廠逐步提升綠電使用比例。</span>
                            <span class="lang-en">Helping suppliers account for carbon footprints (ISO 14067) and set science-based targets for renewable energy.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 12: Scope 3 Management Strategies -->
            <section class="slide" id="slide-12" data-title="Slide 12: Scope 3 價值鏈管理策略">
                <div class="slide-container center-header-layout">
                    <div class="header-block center-text">
                        <div class="section-tag"><i class="fa-solid fa-network-wired"></i> Value Chain Strategy</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">Scope 3 價值鏈減碳 4 大策略</span>
                            <span class="lang-en">4 Strategies for Scope 3 Decarbonization</span>
                        </h2>
                    </div>

                    <div class="cards-grid-4">
                        <div class="rc-card glass-card">
                            <div class="rc-num">01</div>
                            <h4>Green Sourcing</h4>
                            <p><span class="lang-zh">綠色採購與低碳原物料</span><span class="lang-en">Low-carbon materials</span></p>
                        </div>
                        <div class="rc-card glass-card">
                            <div class="rc-num">02</div>
                            <h4>Co-PPA</h4>
                            <p><span class="lang-zh">綠電共購與技術輔導</span><span class="lang-en">Co-purchasing green power</span></p>
                        </div>
                        <div class="rc-card glass-card">
                            <div class="rc-num">03</div>
                            <h4>Logistics</h4>
                            <p><span class="lang-zh">低碳物流與運具電動化</span><span class="lang-en">EV fleet & eco-logistics</span></p>
                        </div>
                        <div class="rc-card glass-card">
                            <div class="rc-num">04</div>
                            <h4>Product Design</h4>
                            <p><span class="lang-zh">易拆解與可回收設計</span><span class="lang-en">Design for recycling</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 13: Apple Supplier Clean Energy -->
            <section class="slide" id="slide-13" data-title="Slide 13: Apple 供應鏈綠電案例">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-brands fa-apple"></i> Case Study • Apple</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">Apple Supplier Clean Energy Program</span>
                            <span class="lang-en">Apple Supplier Clean Energy Program</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-solar-panel accent-icon"></i> <span class="lang-zh">帶動全球 200+ 供應商轉用 100% 綠電</span><span class="lang-en">200+ Suppliers Committed to 100% Clean Power</span></h3>
                            <p><span class="lang-zh">Apple 推出 Supplier Clean Energy Program，協助台積電、鴻海、日月光等代工夥伴全面採購綠電，至今已節省數百萬噸碳排放。</span>
                            <span class="lang-en">Apple works directly with key manufacturing partners to transition all Apple production to 100% renewable energy.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 14: Activity 1 - Supply Chain Risk Mapping -->
            <section class="slide" id="slide-14" data-title="Slide 14: 活動一 - 供應鏈風險圖譜">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag activity-tag"><i class="fa-solid fa-gamepad"></i> Activity 1 • 15 Minutes</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">Supply Chain Risk Mapping</span>
                            <span class="lang-en">Supply Chain Risk Mapping</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="scenario-card glass-card highlight-border">
                            <h3><span class="lang-zh">任務：繪製供應鏈流程並找出 3 大 ESG 風險</span><span class="lang-en">Map 5 Steps & Identify 3 ESG Risks</span></h3>
                            <div class="grid-2col mt-3 gap-2">
                                <div class="opt-choice"><p>1. Apple (晶片採購/代工組裝/物流)</p></div>
                                <div class="opt-choice"><p>2. Nike (棉花採購/海外紡織廠/物流)</p></div>
                                <div class="opt-choice"><p>3. TSMC (化學品/電力水資源/廢棄物)</p></div>
                                <div class="opt-choice"><p>4. Starbucks / IKEA / Unilever</p></div>
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
                            <span class="lang-zh">供應鏈風險是永續韌性的來源</span>
                            <span class="lang-en">Activity 1: Risk Management Fuels Resilience</span>
                        </h2>
                    </div>

                    <div class="debrief-box glass-card glow-card">
                        <i class="fa-solid fa-lightbulb debrief-icon"></i>
                        <div class="debrief-content">
                            <h4><span class="lang-zh">教師觀點帶出 (Key Takeaway)：</span><span class="lang-en">Faculty Debrief:</span></h4>
                            <p><span class="lang-zh">「供應鏈 ESG 風險絕非純粹的合規成本，而是確保企業在極端天災、地緣政治與碳關稅衝擊下，依然能持續斷糧營運的防禦力！」</span>
                            <span class="lang-en">"Supply chain ESG risks are strategic resilience drivers that protect business continuity during crises."</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 16: Linear vs Circular Economy -->
            <section class="slide" id="slide-16" data-title="Slide 16: 線性 vs 循環經濟">
                <div class="slide-container center-header-layout">
                    <div class="header-block center-text">
                        <div class="section-tag"><i class="fa-solid fa-recycle"></i> Part III • Circular Economy</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">Linear Economy vs. Circular Economy</span>
                            <span class="lang-en">Linear Economy vs. Circular Economy</span>
                        </h2>
                    </div>

                    <div class="grid-2col gap-4 mt-3">
                        <div class="theory-card glass-card">
                            <div class="theory-header"><h3>Linear Economy (線性經濟)</h3></div>
                            <p class="mt-2"><span class="lang-zh"><strong>Take → Make → Waste</strong> (開採 → 製造 → 拋棄廢棄)<br>導致天然資源快速枯竭與垃圾浩劫。</span><span class="lang-en">Take-Make-Waste model leading to resource depletion.</span></p>
                        </div>
                        <div class="theory-card glass-card highlight-card">
                            <div class="theory-header"><h3>Circular Economy (循環經濟)</h3></div>
                            <p class="mt-2"><span class="lang-zh"><strong>Regenerative by Design</strong> (源頭設計循環)<br>廢棄物即是資源，實現閉環 (Closed-loop) 永久循環。</span><span class="lang-en">Closed-loop model where waste equals resource.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 17: Linear Model Bottlenecks -->
            <section class="slide" id="slide-17" data-title="Slide 17: 線性模式的致命瓶頸">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag warning-tag"><i class="fa-solid fa-triangle-exclamation"></i> Linear Bottlenecks</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">Take–Make–Waste 線性模式的致命瓶頸</span>
                            <span class="lang-en">Take-Make-Waste Model Bottlenecks</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-volcano red-text"></i> <span class="lang-zh">原物料暴漲、廢棄物天價處置費與法規重罰</span><span class="lang-en">Soaring Raw Material Costs & Disposal Fees</span></h3>
                            <p><span class="lang-zh">傳統線性模式面臨原生礦產與原油開採極限、各國禁塑與反一次性拋棄式商品法規，繼續沿用將徹底失去價格競爭力。</span>
                            <span class="lang-en">Traditional linear models hit hard limits: material price spikes, landfill bans, and single-use plastic penalties.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 18: 5 R's Framework -->
            <section class="slide" id="slide-18" data-title="Slide 18: 循環經濟 5 R's 框架">
                <div class="slide-container center-header-layout">
                    <div class="header-block center-text">
                        <div class="section-tag"><i class="fa-solid fa-arrows-spin"></i> 5 R's Hierarchy</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">循環經濟 5 R's 階層框架</span>
                            <span class="lang-en">The 5 R's Circular Hierarchy</span>
                        </h2>
                    </div>

                    <div class="cards-grid-5">
                        <div class="decision-card glass-card"><h4>1. Reduce</h4><p><span class="lang-zh">源頭包材與資源減量</span><span class="lang-en">Reduce resource use</span></p></div>
                        <div class="decision-card glass-card"><h4>2. Reuse</h4><p><span class="lang-zh">產品與零件重複使用</span><span class="lang-en">Reuse products/parts</span></p></div>
                        <div class="decision-card glass-card"><h4>3. Repair</h4><p><span class="lang-zh">提供維修與延長壽命</span><span class="lang-en">Repair & maintain</span></p></div>
                        <div class="decision-card glass-card"><h4>4. Recycle</h4><p><span class="lang-zh">材料回收再造閉環</span><span class="lang-en">Recycle materials</span></p></div>
                        <div class="decision-card glass-card"><h4>5. Recover</h4><p><span class="lang-zh">廢棄物能源回收利用</span><span class="lang-en">Recover energy/valuable</span></p></div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 19: Product Life Cycle LCA -->
            <section class="slide" id="slide-19" data-title="Slide 19: 產品生命週期 LCA">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-arrows-split-up-and-left"></i> Cradle-to-Cradle</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">Product Life Cycle LCA (搖籃到搖籃)</span>
                            <span class="lang-en">Life Cycle Assessment (LCA)</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-shapes accent-icon"></i> <span class="lang-zh">從設計階段考慮 100% 易拆解與可回收性</span><span class="lang-en">Designing for Disassembly & 100% Circularity</span></h3>
                            <p><span class="lang-zh">LCA (從搖籃到搖籃) 強調：80% 的環境衝擊在產品設計階段即已決定！設計師必須採用單一可回收材質與易拆解結構。</span>
                            <span class="lang-en">80% of environmental impacts are determined at the design stage. Design for Disassembly is critical.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 20: Patagonia Case -->
            <section class="slide" id="slide-20" data-title="Slide 20: 案例一：Patagonia">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-shirt"></i> Case 1 • Patagonia</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">案例一：Patagonia Worn Wear 與反快時尚</span>
                            <span class="lang-en">Case 1: Patagonia Worn Wear</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-wrench accent-icon"></i> <span class="lang-zh">「Don't Buy This Jacket」修復與二手回收</span><span class="lang-en">"Don't Buy This Jacket" & Repair Program</span></h3>
                            <p><span class="lang-zh">Patagonia 推出 Worn Wear 計畫，提供免費衣服維修、舊衣回購與二手拍賣，顛覆快時尚拋棄文化，建立極高品牌忠誠度。</span>
                            <span class="lang-en">Patagonia offers free garment repairs and a buyback marketplace to disrupt fast-fashion waste culture.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 21: IKEA Case -->
            <section class="slide" id="slide-21" data-title="Slide 21: 案例二：IKEA">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-couch"></i> Case 2 • IKEA</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">案例二：IKEA 循環家具與舊購回購</span>
                            <span class="lang-en">Case 2: IKEA Circular Furniture</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-arrows-rotate accent-icon"></i> <span class="lang-zh">2030 年 100% 採用再生與可回收原料</span><span class="lang-en">100% Circular & Renewable Materials by 2030</span></h3>
                            <p><span class="lang-zh">IKEA 承諾 2030 前所有家具 100% 使用再生與可回收材質，推出「舊家具買回服務 (Buy Back)」與商業辦公家具租賃服務。</span>
                            <span class="lang-en">IKEA commits to 100% renewable/recycled materials by 2030 and pilots furniture leasing and buyback schemes.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 22: Nike Grind Case -->
            <section class="slide" id="slide-22" data-title="Slide 22: 案例三：Nike Grind">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-shoe-prints"></i> Case 3 • Nike Grind</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">案例三：Nike Grind 廢料再生技術</span>
                            <span class="lang-en">Case 3: Nike Grind Waste Regeneration</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-industry accent-icon"></i> <span class="lang-zh">將舊鞋廢料重製為跑道與新產品</span><span class="lang-en">Transforming Scrap Footwear into Runways</span></h3>
                            <p><span class="lang-zh">Nike 將生產過程產生的邊角廢料與回收舊鞋磨碎，研發成 Nike Grind 再生顆粒，用於鋪設田徑場跑道與打造全新運動鞋。</span>
                            <span class="lang-en">Nike recycles manufacturing scrap and end-of-life shoes into premium Nike Grind materials for athletic surfaces.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 23: Circular Business Models -->
            <section class="slide" id="slide-23" data-title="Slide 23: 循環商業模式">
                <div class="slide-container center-header-layout">
                    <div class="header-block center-text">
                        <div class="section-tag"><i class="fa-solid fa-lightbulb"></i> Part IV • Business Strategy</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">3 大創新 Circular Business Models</span>
                            <span class="lang-en">3 Innovative Circular Business Models</span>
                        </h2>
                    </div>

                    <div class="grid-3col gap-3 mt-3">
                        <div class="value-card glass-card">
                            <div class="v-icon color-1"><i class="fa-solid fa-handshake-simple"></i></div>
                            <h3>Product-as-a-Service</h3>
                            <p><span class="lang-zh">產品即服務：只賣使用權不賣所有權（如燈具/家具租賃）。</span><span class="lang-en">Leasing access instead of selling ownership.</span></p>
                        </div>
                        <div class="value-card glass-card">
                            <div class="v-icon color-2"><i class="fa-solid fa-arrows-spin"></i></div>
                            <h3>Resource Recovery</h3>
                            <p><span class="lang-zh">資源回收再利用：廢棄物回購與閉環再造。</span><span class="lang-en">Closed-loop waste recovery & remanufacturing.</span></p>
                        </div>
                        <div class="value-card glass-card">
                            <div class="v-icon color-3"><i class="fa-solid fa-clock-rotate-left"></i></div>
                            <h3>Life Extension</h3>
                            <p><span class="lang-zh">產品壽命延長：模組化設計、維修與二手拍賣。</span><span class="lang-en">Modular design, repair & resale markets.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 24: ESG Supply Chain Strategy -->
            <section class="slide" id="slide-24" data-title="Slide 24: ESG 供應鏈策略藍圖">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag"><i class="fa-solid fa-roadmap"></i> Strategy Roadmap</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">ESG 永續供應鏈策略藍圖</span>
                            <span class="lang-en">ESG Supply Chain Strategy Roadmap</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-network-wired accent-icon"></i> <span class="lang-zh">建立數位追溯、供應商賦能與利益對齊</span><span class="lang-en">Digital Traceability & Supplier Incentive Alignment</span></h3>
                            <p><span class="lang-zh">結合區塊鏈透明追溯、提供綠色融資獎勵優良代工廠，並與供應商建立利益對齊的長遠永續夥伴關係。</span>
                            <span class="lang-en">Combining digital traceability, green financing incentives, and long-term co-investment with suppliers.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 25: Activity 2 - Circular Business Design -->
            <section class="slide" id="slide-25" data-title="Slide 25: 活動二 - 設計循環企業">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag activity-tag"><i class="fa-solid fa-pen-to-square"></i> Activity 2 • 20 Minutes</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">Circular Business Design</span>
                            <span class="lang-en">Circular Business Design</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="scenario-card glass-card highlight-border">
                            <h3><span class="lang-zh">任務：為下列產品設計一個 Circular Business Model</span><span class="lang-en">Design a Circular Model Canvas</span></h3>
                            <div class="grid-2col mt-3 gap-2">
                                <div class="opt-choice"><p>1. 智慧型手機 (模組化拆解/租賃)</p></div>
                                <div class="opt-choice"><p>2. 運動鞋 (舊鞋磨碎/回收再造)</p></div>
                                <div class="opt-choice"><p>3. 咖啡杯 (循環押金租賃系統)</p></div>
                                <div class="opt-choice"><p>4. 寶特瓶 / 辦公家具 (100%閉環)</p></div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 26: Activity 2 - Team Presentations -->
            <section class="slide" id="slide-26" data-title="Slide 26: 活動二 - 各組簡報">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag activity-tag"><i class="fa-solid fa-microphone"></i> Team Pitches</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">各組 5 分鐘 Canvas 商業模式 Pitch</span>
                            <span class="lang-en">5-Min Circular Canvas Pitches</span>
                        </h2>
                    </div>
                    <div class="main-panel">
                        <div class="glass-card feature-card">
                            <h3><i class="fa-solid fa-check-double accent-icon"></i> <span class="lang-zh">教師點評：兼顧成本、獲利與循環價值</span><span class="lang-en">Balancing Profit, Cost & Circular Value</span></h3>
                            <p><span class="lang-zh">點評重點：循環商業模式必須具備商業自性與財務獲利能力，而非單純仰賴補貼的理想化環保專案！</span>
                            <span class="lang-en">Evaluating whether the circular model is economically viable and self-sustaining beyond green subsidies.</span></p>
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
                            <span class="lang-zh">Week 10 核心重點總結</span>
                            <span class="lang-en">Week 10 Key Takeaways</span>
                        </h2>
                    </div>

                    <div class="takeaways-grid-4">
                        <div class="t-card glass-card">
                            <div class="t-number">01</div>
                            <h3><span class="lang-zh">Supply Chain 是 ESG 本體</span><span class="lang-en">1. Supply Chain is ESG</span></h3>
                            <p><span class="lang-zh">Scope 3 占碳排 80%+，供應鏈防線決定企業 ESG 聲譽。</span><span class="lang-en">Scope 3 accounts for 80%+ emissions; supply chains define ESG.</span></p>
                        </div>
                        <div class="t-card glass-card">
                            <div class="t-number">02</div>
                            <h3><span class="lang-zh">Responsible Sourcing</span><span class="lang-en">2. Responsible Sourcing</span></h3>
                            <p><span class="lang-zh">貫徹行為守則、無預警稽核與供應商人權與綠電賦能。</span><span class="lang-en">Enforcing codes of conduct, audits, and supplier enablement.</span></p>
                        </div>
                        <div class="t-card glass-card">
                            <div class="t-number">03</div>
                            <h3><span class="lang-zh">5 R's 與 LCA 設計</span><span class="lang-en">3. 5 R's & LCA Design</span></h3>
                            <p><span class="lang-zh">從源頭設計實現 5 R's 閉環，擺脫線性 Take-Make-Waste。</span><span class="lang-en">Designing for 5 R's closed-loop to break linear models.</span></p>
                        </div>
                        <div class="t-card glass-card">
                            <div class="t-number">04</div>
                            <h3><span class="lang-zh">Product-as-a-Service</span><span class="lang-en">4. Product-as-a-Service</span></h3>
                            <p><span class="lang-zh">打造具備財務自性與競爭優勢的循環商業模式。</span><span class="lang-en">Building self-sustaining circular business models.</span></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 28: Preview W11 & Homework 10 -->
            <section class="slide" id="slide-28" data-title="Slide 28: Preview W11 & Homework 10">
                <div class="slide-container split-layout">
                    <div class="side-panel">
                        <div class="section-tag homework-tag"><i class="fa-solid fa-forward"></i> Preview W11 & HW10</div>
                        <h2 class="slide-heading">
                            <span class="lang-zh">W11 預告與 Homework 10</span>
                            <span class="lang-en">W11 Preview & Homework 10</span>
                        </h2>
                    </div>

                    <div class="main-panel">
                        <div class="glass-card feature-card mb-2">
                            <h3><i class="fa-solid fa-robot accent-icon"></i> <span class="lang-zh">W11 預告：AI、數位治理與企業倫理</span><span class="lang-en">W11 Preview: AI & Digital Ethics</span></h3>
                            <p class="mb-2"><span class="lang-zh">下一週我們將探討最前沿的《AI、數位治理與企業倫理 (AI, Digital Governance & Corporate Ethics)》！</span><span class="lang-en">Next week we explore cutting-edge AI, Digital Governance & Ethics!</span></p>
                        </div>

                        <div class="glass-card feature-card mb-2">
                            <h3><i class="fa-solid fa-file-invoice accent-icon"></i> <span class="lang-zh">Homework 10：永續供應鏈分析報告 (約 2,000 字)</span><span class="lang-en">Homework 10: Supply Chain Report (~2,000w)</span></h3>
                            <p><span class="lang-zh">選擇一家企業：分析概況與全球供應鏈、Scope 3 減碳與人權稽核、是否導入循環經濟及三項改善建議。</span>
                            <span class="lang-en">Audit a listed firm: supply chain footprint, Scope 3 & human rights, circular economy practices & 3 recommendations.</span></p>
                        </div>

                        <div class="glass-card rubrics-card">
                            <h4><i class="fa-solid fa-chart-bar accent-icon"></i> AACSB <span class="lang-zh">評分標準</span><span class="lang-en">Rubrics Breakdown</span></h4>
                            <div class="rubrics-bar">
                                <div class="r-seg seg-1" style="width: 30%;"><span class="lang-zh">供應鏈分析 30%</span><span class="lang-en">Chain 30%</span></div>
                                <div class="r-seg seg-2" style="width: 25%;"><span class="lang-zh">Scope 3 25%</span><span class="lang-en">Scope3 25%</span></div>
                                <div class="r-seg seg-3" style="width: 20%;"><span class="lang-zh">循環經濟 20%</span><span class="lang-en">Circular 20%</span></div>
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

with open(r"C:\Users\User\Desktop\第1週_企業為何需要倫理\第10週_永續供應鏈與循環經濟.html", "w", encoding="utf-8") as f:
    f.write(html_week10)

print("Successfully generated Week 10 HTML presentation file!")
