// AACSB & ESG Business Ethics Lecture App JS (Bilingual Support: Traditional Chinese / English)
document.addEventListener('DOMContentLoaded', () => {
    // State Variables
    let currentSlide = 1;
    const slides = document.querySelectorAll('.slide');
    const totalSlides = slides.length || 24;
    let currentLang = 'zh'; // 'zh' or 'en'
    let timerSeconds = 110 * 60; // 110 minutes
    let timerInterval = null;

    // DOM Elements
    const prevBtn = document.getElementById('prevSlideBtn');
    const nextBtn = document.getElementById('nextSlideBtn');
    const currentSlideNumEl = document.getElementById('currentSlideNum');
    const totalSlideNumEl = document.getElementById('totalSlideNum');
    const progressBar = document.getElementById('progressBar');
    const slideTitlePreview = document.getElementById('currentSlideTitlePreview');
    const gridModal = document.getElementById('gridModal');
    const gridContainer = document.getElementById('gridContainer');
    const gridToggleBtn = document.getElementById('gridToggleBtn');
    const closeGridBtn = document.getElementById('closeGridBtn');
    const presentBtn = document.getElementById('presentBtn');
    const fullScreenToggleBtn = document.getElementById('fullScreenToggleBtn');
    const printDeckBtn = document.getElementById('printDeckBtn');
    const timerDisplay = document.getElementById('timerDisplay');
    const langToggleBtn = document.getElementById('langToggleBtn');
    const langDisplay = document.getElementById('langDisplay');

    // Initialize Deck
    function initDeck() {
        if (totalSlideNumEl) totalSlideNumEl.textContent = totalSlides;
        document.body.classList.add('lang-zh');
        renderGridModal();
        showSlide(currentSlide);
        startLectureTimer();
    }

    // Get Title from Active Slide Element dynamically
    function getSlideTitle(slideEl, slideNum) {
        if (!slideEl) return `Slide ${slideNum}`;
        const dataTitle = slideEl.getAttribute('data-title');
        const zhHeading = slideEl.querySelector('.slide-heading .lang-zh')?.textContent;
        const enHeading = slideEl.querySelector('.slide-heading .lang-en')?.textContent;
        if (currentLang === 'zh') {
            return dataTitle || zhHeading || `Slide ${slideNum}`;
        } else {
            return enHeading || dataTitle || `Slide ${slideNum}`;
        }
    }

    // Show Specific Slide
    function showSlide(index) {
        if (index < 1) index = 1;
        if (index > totalSlides) index = totalSlides;

        slides.forEach(slide => slide.classList.remove('active'));

        const targetSlide = document.getElementById(`slide-${index}`);
        if (targetSlide) {
            targetSlide.classList.add('active');
            currentSlide = index;

            // Update UI Elements
            if (currentSlideNumEl) currentSlideNumEl.textContent = currentSlide;
            const title = getSlideTitle(targetSlide, currentSlide);
            if (slideTitlePreview) slideTitlePreview.textContent = title;

            // Update Progress Bar
            if (progressBar) {
                const percent = (currentSlide / totalSlides) * 100;
                progressBar.style.width = `${percent}%`;
            }

            // Update Active Thumbnail in Grid
            updateActiveThumbnail(currentSlide);
        }
    }

    // Toggle Language (ZH <-> EN)
    function toggleLanguage() {
        currentLang = currentLang === 'zh' ? 'en' : 'zh';
        if (langDisplay) langDisplay.textContent = currentLang === 'zh' ? '中 / EN' : 'EN / 中';

        document.body.classList.toggle('lang-zh', currentLang === 'zh');
        document.body.classList.toggle('lang-en', currentLang === 'en');

        // Update Slide Titles
        showSlide(currentSlide);
        renderGridModal();
    }
    if (langToggleBtn) langToggleBtn.addEventListener('click', toggleLanguage);

    // Render Grid Modal Thumbnails
    function renderGridModal() {
        if (!gridContainer) return;
        gridContainer.innerHTML = '';
        slides.forEach((slide, idx) => {
            const slideNum = idx + 1;
            const title = getSlideTitle(slide, slideNum);

            const thumb = document.createElement('div');
            thumb.className = `thumb-card ${slideNum === currentSlide ? 'active-thumb' : ''}`;
            thumb.setAttribute('data-slide-index', slideNum);
            thumb.innerHTML = `
                <div class="thumb-num">SLIDE ${slideNum}</div>
                <div class="thumb-title">${title}</div>
            `;

            thumb.addEventListener('click', () => {
                showSlide(slideNum);
                toggleGridModal(false);
            });

            gridContainer.appendChild(thumb);
        });
    }

    function updateActiveThumbnail(slideNum) {
        if (!gridContainer) return;
        const thumbs = gridContainer.querySelectorAll('.thumb-card');
        thumbs.forEach(t => {
            const idx = parseInt(t.getAttribute('data-slide-index'));
            if (idx === slideNum) {
                t.classList.add('active-thumb');
            } else {
                t.classList.remove('active-thumb');
            }
        });
    }

    // Navigation Handlers
    if (prevBtn) prevBtn.addEventListener('click', () => showSlide(currentSlide - 1));
    if (nextBtn) nextBtn.addEventListener('click', () => showSlide(currentSlide + 1));

    // Keyboard Navigation
    document.addEventListener('keydown', (e) => {
        if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;

        switch (e.key) {
            case 'ArrowRight':
            case 'ArrowDown':
            case ' ':
                e.preventDefault();
                showSlide(currentSlide + 1);
                break;
            case 'ArrowLeft':
            case 'ArrowUp':
                e.preventDefault();
                showSlide(currentSlide - 1);
                break;
            case 'g':
            case 'G':
                toggleGridModal();
                break;
            case 'f':
            case 'F':
                toggleFullscreen();
                break;
            case 'l':
            case 'L':
                toggleLanguage();
                break;
            case 'Escape':
                toggleGridModal(false);
                break;
        }
    });

    // Grid Modal Controls
    function toggleGridModal(forceState) {
        if (!gridModal) return;
        if (typeof forceState === 'boolean') {
            gridModal.classList.toggle('open', forceState);
        } else {
            gridModal.classList.toggle('open');
        }
    }
    if (gridToggleBtn) gridToggleBtn.addEventListener('click', () => toggleGridModal());
    if (closeGridBtn) closeGridBtn.addEventListener('click', () => toggleGridModal(false));

    // Fullscreen Mode
    function toggleFullscreen() {
        if (!document.fullscreenElement) {
            document.documentElement.requestFullscreen().catch(err => {
                console.log(`Fullscreen error: ${err.message}`);
            });
        } else {
            if (document.exitFullscreen) {
                document.exitFullscreen();
            }
        }
    }
    if (presentBtn) presentBtn.addEventListener('click', toggleFullscreen);
    if (fullScreenToggleBtn) fullScreenToggleBtn.addEventListener('click', toggleFullscreen);

    // Print Deck
    if (printDeckBtn) {
        printDeckBtn.addEventListener('click', () => {
            window.print();
        });
    }

    // Lecture Timer Count-down
    function startLectureTimer() {
        if (!timerDisplay) return;
        if (timerInterval) clearInterval(timerInterval);
        timerInterval = setInterval(() => {
            if (timerSeconds > 0) {
                timerSeconds--;
                const mins = Math.floor(timerSeconds / 60);
                const secs = timerSeconds % 60;
                timerDisplay.textContent = `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
            }
        }, 1000);
    }

    // Initialize Deck
    initDeck();
});

// Interactive Poll Voting Engine for Slide 13
let pollVotes = { A: 0, B: 0, C: 0 };

function castVote(option) {
    if (pollVotes[option] !== undefined) {
        pollVotes[option]++;
        updatePollUI();
    }
}

function resetVote() {
    pollVotes = { A: 0, B: 0, C: 0 };
    updatePollUI();
}

function updatePollUI() {
    const total = pollVotes.A + pollVotes.B + pollVotes.C;

    const barA = document.getElementById('barA');
    const percentA = document.getElementById('percentA');
    const barB = document.getElementById('barB');
    const percentB = document.getElementById('percentB');
    const barC = document.getElementById('barC');
    const percentC = document.getElementById('percentC');

    if (total === 0) {
        if (barA) barA.style.width = `0%`;
        if (percentA) percentA.textContent = `0% (0 票 / 0 votes)`;
        if (barB) barB.style.width = `0%`;
        if (percentB) percentB.textContent = `0% (0 票 / 0 votes)`;
        if (barC) barC.style.width = `0%`;
        if (percentC) percentC.textContent = `0% (0 票 / 0 votes)`;
        return;
    }

    const pA = Math.round((pollVotes.A / total) * 100);
    const pB = Math.round((pollVotes.B / total) * 100);
    const pC = 100 - pA - pB;

    if (barA) barA.style.width = `${pA}%`;
    if (percentA) percentA.textContent = `${pA}% (${pollVotes.A} 票 / votes)`;

    if (barB) barB.style.width = `${pB}%`;
    if (percentB) percentB.textContent = `${pB}% (${pollVotes.B} 票 / votes)`;

    if (barC) barC.style.width = `${pC}%`;
    if (percentC) percentC.textContent = `${pC}% (${pollVotes.C} 票 / votes)`;
}
