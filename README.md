# Rowlett Group of AA Website

## Project Overview

This is a comprehensive single-page application (SPA) for the Rowlett Group of Alcoholics Anonymous in Garland, TX. The website serves as a complete resource hub for individuals seeking recovery support, providing meeting schedules, educational content, recovery tools, and community information.

**Live URL:** https://www.rowlettaa.org/

**Founded:** 1995

**Location:** 362 Oaks Trail #162, Garland, TX 75043

**Contact:** (972) 925-0096 | rowlettaa@gmail.com

## Table of Contents

1. [Features](#features)
2. [Technical Stack](#technical-stack)
3. [File Structure](#file-structure)
4. [Detailed Component Documentation](#detailed-component-documentation)
5. [JavaScript Functionality](#javascript-functionality)
6. [CSS and Styling](#css-and-styling)
7. [SEO and Accessibility](#seo-and-accessibility)
8. [Content Management Guide](#content-management-guide)
9. [Testing Guidelines](#testing-guidelines)
10. [Deployment Instructions](#deployment-instructions)
11. [Browser Compatibility](#browser-compatibility)
12. [Developer Guide](#developer-guide)

---

## Features

### Core Pages (10 Main Sections)

#### 1. **Home Page** (`#home`)
- Hero section with inspirational imagery
- Serenity Prayer display
- AA Preamble
- Quick call-to-action to meeting schedule
- Today's meetings banner (dynamic based on current day)

#### 2. **What is A.A.?** (`#what-is-aa`)
- Introduction to Alcoholics Anonymous
- 12 Steps with expandable details and explanations
- 12 Traditions with full descriptions
- FAQ accordion with common questions
- "Am I an Alcoholic?" self-assessment questionnaire

#### 3. **Meeting Schedule** (`#schedule`)
- Weekly meeting calendar with 7-day grid
- Multiple meeting types: Discussion, Speaker, Big Book Study, Step Study, etc.
- Meeting details: time, format (open/closed), location
- Special Saturday meetings (morning and evening)
- Sunday beginners meeting
- Weekday lunch meetings
- Color-coded meeting cards for easy identification
- Responsive grid layout

#### 4. **Resources** (`#resources`)
- Recovery calculator with sobriety milestone tracking (17 levels from 24 hours to 40+ years)
- Detailed time calculations (years, months, weeks, days, hours, minutes)
- Milestone badges with emoji indicators
- National AA hotline information
- Dallas AA Central Office contact
- Local group contact details
- Links to external AA resources (aa.org, aadallas.org, neta65.org)

#### 5. **Get Involved** (`#get-involved`)
- Service opportunities with descriptions
- Volunteer positions: Secretary, Treasurer, Literature Coordinator, etc.
- Meeting roles: Greeter, Coffee Maker, etc.
- Committee participation information
- Sponsorship guidance
- Fellowship activities

#### 6. **Literature** (`#literature`)
- Tabbed interface with 4 categories:
  - **Big Book Videos** (28 videos total)
    - Bill's Story through Chapter 11
    - Personal stories (Pioneers and modern)
  - **12 & 12 Videos** (25 videos)
    - All 12 Steps explained
    - All 12 Traditions explained
  - **Step Videos** (12 videos)
    - Step-by-step guidance
  - **Speaker Talks** (8+ inspirational talks)
- Each video card includes:
  - Thumbnail from YouTube
  - Title and description
  - Video length
  - Click to open in modal player
- Modal video player with full-screen option
- Lazy loading for performance
- Scrollable grid for easy browsing

#### 7. **Our Group** (`#our-group`)
- Group history with 30-year timeline
- Key milestones from 1995 to 2025
- Interactive timeline with hover effects
- Information popups on timeline events
- 30th Anniversary announcement (July 26, 2025)
- Event details and location

#### 8. **Study Guide** (`#study-guide`)
- **Interactive Book Reader:**
  - AA Big Book chapter selection
  - Page-by-page navigation
  - Authentic book styling with serif fonts
  - Progress tracking
  - Clean, distraction-free reading experience
- **Meditation Timer:**
  - 1, 3, 5, 10, 15-minute presets
  - Custom duration input
  - Start/Pause/Reset controls
  - Visual countdown display
  - Audio notification on completion
- **Gratitude List:**
  - Add daily gratitude entries
  - Persistent storage (localStorage)
  - Delete individual entries
  - Clear all option
  - Date-stamped entries
- **AA Glossary/Dictionary:**
  - Searchable terms
  - Key AA concepts and phrases
  - Definitions with context
  - Quick reference tool
- **Personal Notes:**
  - Add and save notes
  - Persistent storage
  - Edit and delete capabilities
  - Organized by date
- **HALT Check Tool:**
  - Self-assessment for Hungry, Angry, Lonely, Tired
  - Visual selection interface
  - Personalized recommendations
  - Coping strategies for each state
  - Gentle reminders about self-care

#### 9. **Contact** (`#contact`)
- Phone: (972) 925-0096
- Email: rowlettaa@gmail.com
- Physical address with map link
- Google Maps integration
- Embedded map display
- Directions link
- Mailing information

#### 10. **Contribute** (`#contribute`)
- Venmo QR code for digital donations
- Venmo link (@rowlettaa)
- 7th Tradition explanation
- Self-supporting principle details
- How contributions are used
- Alternative donation methods
- Transparency about fund usage

### Global Features

#### Progressive Web App (PWA)
- Installable on mobile and desktop
- Offline capability with cached resources
- App manifest with icons
- Install banner with dismiss option
- Add to home screen functionality
- Standalone app experience

#### Quick Action Buttons (Floating)
Three persistent floating buttons in bottom-right corner:
1. **Crisis Resources** (Red) - Emergency hotlines and support
2. **Today's Meetings** (Blue) - Jump to current day's schedule
3. **Search** (Green) - Site-wide search functionality

#### Search Functionality
- Modal search interface
- Real-time search across all content
- Searches through:
  - Meeting times and types
  - Literature titles
  - Page content
  - Resources
- Highlighted results
- Click to navigate to content
- Keyboard accessible (Escape to close)

#### Crisis Resources Modal
- National Suicide Prevention Lifeline: 988
- Crisis Text Line: Text HELLO to 741741
- Dallas AA Central Office: (214) 887-6699
- Rowlett Group hotline: (972) 925-0096
- Emergency guidance
- When to call 911 information

#### Navigation System
- Sticky header that stays visible while scrolling
- Desktop navigation (horizontal menu)
- Mobile responsive hamburger menu
- Active page highlighting
- Smooth scroll to sections
- "Skip to main content" accessibility link
- Visual underline animation on hover
- Contribute button with special styling

#### Today's Meetings Banner
- Dynamically displays based on current day of week
- Shows all meetings happening today
- Prominent yellow banner at top of home page
- Automatically updates based on system date
- Includes meeting times, types, and formats

---

## Technical Stack

### Frontend Framework
- **Pure JavaScript** (Vanilla JS) - No framework dependencies
- Single-page application (SPA) architecture
- Component-based design pattern

### CSS Framework
- **Tailwind CSS 3.x** - Utility-first CSS framework loaded via CDN
- Custom CSS for animations and specific components

### External Libraries
- **Font Awesome 6.5.1** - Icon library for UI elements
- **Google Fonts:**
  - Inter (400, 500, 600, 700) - Primary sans-serif font
  - Lora (400, 600, italic) - Secondary serif font for quotes and book pages

### APIs & Integrations
- **YouTube Embedded Player** - Video content delivery
- **Google Maps** - Location and directions
- **Venmo** - Payment integration

### Web Technologies
- **HTML5** - Semantic markup with proper structure
- **CSS3** - Advanced animations, transitions, flexbox, grid
- **JavaScript ES6+** - Modern JavaScript features
- **localStorage** - Client-side data persistence
- **Service Worker Ready** - PWA capabilities

### SEO & Metadata
- **Schema.org Structured Data:**
  - Organization schema
  - FAQPage schema
  - BreadcrumbList schema
  - Schedule/Event schema
  - LocalBusiness schema
- **Open Graph** - Social media preview optimization
- **Twitter Cards** - Twitter-specific metadata
- **Canonical URLs** - Search engine optimization
- **Sitemap** - XML sitemap reference

### Performance Optimizations
- **Resource Hints:**
  - preconnect - CDN connections
  - dns-prefetch - YouTube domains
  - preload - Critical CSS and scripts
- **Lazy Loading** - Images and video thumbnails
- **Async/Defer** - Script loading optimization

---

## File Structure

This is a **single-file application** where everything is contained in `index.html`:

```
index.html
├── <head>
│   ├── Meta Tags (Lines 1-80)
│   │   ├── SEO metadata
│   │   ├── Social media (Open Graph, Twitter)
│   │   ├── Mobile optimization
│   │   ├── Geolocation data
│   │   └── Theme colors
│   ├── External Resources (Lines 69-80)
│   │   ├── Tailwind CSS CDN
│   │   ├── Font Awesome icons
│   │   └── Google Fonts
│   ├── Structured Data (Lines 82-834)
│   │   ├── Organization schema
│   │   ├── FAQ schema
│   │   ├── Breadcrumb schema
│   │   ├── Event/Schedule schema
│   │   └── LocalBusiness schema
│   └── CSS Styles (Lines 295-723)
│       ├── CSS variables/root
│       ├── Component styles
│       ├── Animations
│       ├── Responsive media queries
│       └── Accessibility styles
├── <body>
│   ├── Accessibility (skip link)
│   ├── Header (navigation)
│   ├── Global components (PWA banner, quick actions)
│   ├── Modals (search, crisis)
│   ├── Main content (all pages/sections)
│   └── Scripts (<script> block)
```

### Why Single File Architecture?

1. **Simple Deployment** - Upload one file to any hosting service
2. **No Build Process** - Works immediately without compilation
3. **Easy Maintenance** - All code in one location
4. **Fast Loading** - Single HTTP request for main content
5. **Offline Capable** - Can be cached entirely for PWA

---

## Detailed Component Documentation

### Navigation Component

**Location:** Lines 838-873

**Features:**
- Sticky positioning (stays at top while scrolling)
- Backdrop blur effect for modern aesthetic
- Logo with custom SVG graphic
- Desktop: Horizontal navigation with 7 links
- Mobile: Hamburger menu with slide-down drawer
- Active page highlighting with blue color and underline animation
- Special "Contribute" button with blue background

**How It Works:**
```javascript
// Navigation initialization
app.initNavigation = function() {
    // Mobile menu toggle
    document.getElementById('menu-btn').addEventListener('click', function() {
        const menu = document.getElementById('mobile-menu');
        menu.classList.toggle('hidden');
    });

    // Smooth scrolling to sections
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = this.getAttribute('href');
            app.navigateTo(target);
        });
    });
};
```

**Modification Guide:**
- To add a navigation link: Add `<a>` elements in both desktop (line 847-854) and mobile (line 865-871) sections
- To change logo: Modify SVG code or replace with `<img>` tag (line 841-845)
- To adjust sticky behavior: Modify `sticky top-0` classes in header tag

### PWA Installation Banner

**Location:** Lines 875-893

**Features:**
- Auto-displays on first visit for eligible devices
- Slide-down animation
- Shows app icon, title, and benefits
- Install and Dismiss buttons
- Stores dismissal preference in localStorage

**How It Works:**
```javascript
// PWA install prompt
let deferredPrompt;
window.addEventListener('beforeinstallprompt', (e) => {
    e.preventDefault();
    deferredPrompt = e;

    if (!localStorage.getItem('pwa-dismissed')) {
        document.getElementById('pwa-install-banner').classList.remove('hidden');
    }
});

// Install button click
document.getElementById('pwa-install-btn').addEventListener('click', async () => {
    if (deferredPrompt) {
        deferredPrompt.prompt();
        const { outcome } = await deferredPrompt.userChoice;
        deferredPrompt = null;
        document.getElementById('pwa-install-banner').classList.add('hidden');
    }
});
```

**Modification Guide:**
- To change banner colors: Modify `bg-gradient-to-r from-blue-600 to-blue-700` classes
- To adjust timing: Add delay before showing banner
- To customize text: Edit content in lines 878-882

### Meeting Schedule Component

**Location:** Schedule section in main content

**Features:**
- 7-day weekly grid layout
- Each day card shows:
  - Day name
  - All meetings for that day
  - Meeting time (12-hour format)
  - Meeting type (Discussion, Speaker, Study, etc.)
  - Format badge (Open/Closed)
- Responsive layout: 3 columns on desktop, stacks on mobile
- Sunday card spans full width on large screens (special styling)
- Color-coded backgrounds for visual distinction

**Meeting Data Structure:**
```javascript
const schedule = {
    'Sunday': [
        {
            time: '11:00',
            type: 'Beginners Meeting',
            format: 'Open',
            description: 'Perfect for newcomers'
        }
    ],
    'Monday': [
        {
            time: '12:00',
            type: 'Lunch Discussion',
            format: 'Open'
        },
        {
            time: '19:30',
            type: 'Discussion',
            format: 'Open'
        }
    ],
    // ... etc
};
```

**Modification Guide:**
- To add a meeting: Add object to appropriate day array in schedule data
- To change meeting time: Edit 'time' property (use HH:MM 24-hour format, will auto-convert to 12-hour display)
- To add a new meeting type: Add new object with type, time, format, and optional description
- To change colors: Modify `bg-[color]-50` classes in day cards

### Sobriety Calculator

**Location:** Resources section

**Features:**
- Date input for sobriety date
- Real-time calculation of:
  - Years, months, weeks, days
  - Total hours and minutes
  - Exact duration
- 17 milestone levels with specific badges:
  - 24 Hours (🌅)
  - 1 Week (⭐)
  - 30 Days (🏆)
  - 60 Days (💎)
  - 90 Days (🎯)
  - 6 Months (🌟)
  - 9 Months (💪)
  - 1 Year (🎊)
  - 2 Years (🏅)
  - 3 Years (👑)
  - 5 Years (🌈)
  - 10 Years (💫)
  - 15 Years (🔥)
  - 20 Years (🎖️)
  - 25 Years (⚡)
  - 30 Years (🌠)
  - 40+ Years (🏔️)
- Encouraging messages for each milestone
- Persistent storage of sobriety date

**Calculation Logic:**
```javascript
app.calculateSobriety = function() {
    const inputDate = document.getElementById('sobriety-date').value;
    if (!inputDate) return;

    const sobrietyDate = new Date(inputDate);
    const now = new Date();
    const diffMs = now - sobrietyDate;

    if (diffMs < 0) {
        // Show error for future dates
        return;
    }

    // Calculate all units
    const years = Math.floor(diffMs / (1000 * 60 * 60 * 24 * 365.25));
    const months = Math.floor(diffMs / (1000 * 60 * 60 * 24 * 30.44));
    const weeks = Math.floor(diffMs / (1000 * 60 * 60 * 24 * 7));
    const days = Math.floor(diffMs / (1000 * 60 * 60 * 24));
    const hours = Math.floor(diffMs / (1000 * 60 * 60));
    const minutes = Math.floor(diffMs / (1000 * 60));

    // Determine milestone and show appropriate badge
    // Display results
};
```

**Modification Guide:**
- To add new milestone: Add case in milestone determination logic with appropriate emoji and message
- To change milestone thresholds: Adjust day counts in conditional logic
- To customize messages: Edit text strings in milestone display section
- To add features: Consider adding chip tracker, meeting counter, or savings calculator

### HALT Check Tool

**Location:** Study Guide section

**Features:**
- Self-assessment tool for emotional/physical state
- 4 categories: Hungry, Angry, Lonely, Tired
- Visual selection interface with icons
- Click to select/deselect states
- Submit to get personalized recommendations
- Specific guidance for each combination:
  - Single states: Direct advice (eat, process anger, connect, rest)
  - Multiple states: Prioritized action steps
  - All four: Emergency self-care plan
- Clear selections button
- Educational about HALT acronym

**How It Works:**
```javascript
app.checkHalt = function() {
    const selected = [];
    document.querySelectorAll('.halt-option.selected').forEach(option => {
        selected.push(option.dataset.state);
    });

    if (selected.length === 0) {
        // Show prompt to select at least one
        return;
    }

    let recommendations = [];

    if (selected.includes('hungry')) {
        recommendations.push('Eat a healthy meal or snack...');
    }
    if (selected.includes('angry')) {
        recommendations.push('Take a moment to identify what triggered...');
    }
    if (selected.includes('lonely')) {
        recommendations.push('Reach out to your sponsor or a fellowship member...');
    }
    if (selected.includes('tired')) {
        recommendations.push('Rest is crucial for recovery...');
    }

    // Display recommendations
    app.showNotification(recommendations.join(' '), 'info');
};
```

**Modification Guide:**
- To add new states: Add new halt-option div with data-state attribute
- To customize recommendations: Edit recommendation text in checkHalt function
- To add resources: Link to specific contacts, meetings, or external resources
- To enhance: Add daily tracking feature with localStorage to track patterns

### Literature Video System

**Location:** Literature section

**Features:**
- Tabbed interface with 4 categories
- 63+ total videos organized by type
- Each video card includes:
  - YouTube thumbnail (auto-loaded)
  - Video title
  - Brief description
  - Duration/length
- Click to open modal video player
- Modal features:
  - Full YouTube embed
  - Close button
  - Click outside to close
  - Pause on close
  - Responsive sizing
- Scrollable grid container
- Lazy loading of thumbnails

**Video Data Structure:**
```javascript
const videos = {
    bigbook: [
        {
            id: 'youtube-video-id',
            title: 'Chapter 1: Bill\'s Story',
            description: 'Brief description',
            thumbnail: 'URL or uses YouTube default'
        },
        // ... more videos
    ],
    twelve: [
        // 12 & 12 videos
    ],
    steps: [
        // Step study videos
    ],
    speakers: [
        // Speaker talk videos
    ]
};
```

**Modal Player Implementation:**
```javascript
app.openVideoModal = function(videoId) {
    const modal = document.getElementById('video-modal');
    const iframe = modal.querySelector('iframe');

    // Set YouTube embed URL
    iframe.src = `https://www.youtube.com/embed/${videoId}?autoplay=1`;

    // Show modal
    modal.classList.remove('hidden');
    modal.classList.add('flex');
};

app.closeVideoModal = function() {
    const modal = document.getElementById('video-modal');
    const iframe = modal.querySelector('iframe');

    // Stop video
    iframe.src = '';

    // Hide modal
    modal.classList.add('hidden');
    modal.classList.remove('flex');
};
```

**Modification Guide:**
- To add a video: Add object to appropriate category array with YouTube ID, title, and description
- To add new category: Create new tab button and content section, add to video data structure
- To change layout: Modify grid classes (currently `grid-cols-1 md:grid-cols-2 lg:grid-cols-3`)
- To add playlists: Group videos by sub-categories within each main category
- To enhance: Add favorites feature, watch history, or notes on videos

### Timeline History Component

**Location:** Our Group section

**Features:**
- Vertical timeline with center line
- Alternating left/right layout
- Key milestones from 1995-2025
- Each block includes:
  - Year/date
  - Event title
  - Description
  - Color-coded dots
- Hover effects:
  - Card lift animation
  - Dot scaling
  - Color change
  - Info popup display
- Responsive: Converts to single column on mobile
- Visual line connecting all events

**Timeline Structure:**
```html
<div class="timeline-container">
    <div class="timeline-block left">
        <div class="timeline-content">
            <h3>1995</h3>
            <h4>Group Founded</h4>
            <p>Description...</p>
            <div class="info-popup">Additional info...</div>
        </div>
    </div>
    <div class="timeline-block right">
        <!-- Next event -->
    </div>
</div>
```

**Modification Guide:**
- To add milestone: Add new `timeline-block` div with `left` or `right` class (alternate)
- To change colors: Modify border colors in `timeline-block::after` CSS
- To add images: Include `<img>` tags within timeline-content
- To adjust spacing: Modify padding in timeline-block CSS
- To enhance: Add photo gallery, member testimonials, or video memories

### Search Functionality

**Location:** Global feature, search modal lines 910-926

**Features:**
- Modal overlay interface
- Real-time search as you type
- Searches across:
  - All page titles and headers
  - Meeting information
  - Literature titles
  - Resource descriptions
  - FAQ content
- Results show:
  - Section/page name
  - Matched text with highlighting
  - Click to navigate
- Keyboard shortcuts:
  - Escape to close
  - Enter on result to navigate

**Search Implementation:**
```javascript
app.search = function(query) {
    const searchableContent = [
        { section: 'Schedule', content: document.getElementById('schedule').innerText },
        { section: 'Literature', content: document.getElementById('literature').innerText },
        { section: 'Resources', content: document.getElementById('resources').innerText },
        // ... all sections
    ];

    const results = [];
    const queryLower = query.toLowerCase();

    searchableContent.forEach(item => {
        if (item.content.toLowerCase().includes(queryLower)) {
            // Extract context around match
            const index = item.content.toLowerCase().indexOf(queryLower);
            const start = Math.max(0, index - 50);
            const end = Math.min(item.content.length, index + query.length + 50);
            const excerpt = item.content.substring(start, end);

            results.push({
                section: item.section,
                excerpt: excerpt,
                link: `#${item.section.toLowerCase().replace(' ', '-')}`
            });
        }
    });

    app.displaySearchResults(results);
};
```

**Modification Guide:**
- To improve search: Add fuzzy matching library or implement weighted scoring
- To add filters: Include category checkboxes to limit search scope
- To enhance results: Show more context, add snippets, or include images
- To add features: Implement search history, popular searches, or autocomplete

### Meditation Timer

**Location:** Study Guide section

**Features:**
- Preset durations: 1, 3, 5, 10, 15 minutes
- Custom duration input (in minutes)
- Start/Pause/Reset controls
- Visual countdown display (MM:SS format)
- Progress indicator
- Audio notification on completion
- State persistence during session

**Timer Logic:**
```javascript
app.meditationTimer = {
    duration: 0,
    remaining: 0,
    interval: null,

    start: function(minutes) {
        this.duration = minutes * 60;
        this.remaining = this.duration;
        this.running = true;

        this.interval = setInterval(() => {
            this.remaining--;
            this.updateDisplay();

            if (this.remaining <= 0) {
                this.complete();
            }
        }, 1000);
    },

    pause: function() {
        clearInterval(this.interval);
        this.running = false;
    },

    reset: function() {
        clearInterval(this.interval);
        this.remaining = this.duration;
        this.running = false;
        this.updateDisplay();
    },

    complete: function() {
        clearInterval(this.interval);
        this.playSound();
        app.showNotification('Meditation complete!', 'success');
    },

    updateDisplay: function() {
        const minutes = Math.floor(this.remaining / 60);
        const seconds = this.remaining % 60;
        document.getElementById('timer-display').textContent =
            `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
    }
};
```

**Modification Guide:**
- To add presets: Add new buttons with data-duration attributes
- To add sounds: Include multiple sound options or peaceful music
- To enhance: Add guided meditation audio tracks
- To improve: Add background animations, breathing guides, or nature sounds

### Gratitude List

**Location:** Study Guide section

**Features:**
- Add gratitude entries
- Date-stamped entries
- Persistent storage (localStorage)
- Display all entries with newest first
- Delete individual entries
- Clear all entries option
- Encouraging prompts

**Implementation:**
```javascript
app.gratitudeList = {
    entries: [],

    init: function() {
        // Load from localStorage
        const saved = localStorage.getItem('gratitude-list');
        if (saved) {
            this.entries = JSON.parse(saved);
        }
        this.render();
    },

    add: function(text) {
        const entry = {
            id: Date.now(),
            text: text,
            date: new Date().toLocaleDateString()
        };
        this.entries.unshift(entry);
        this.save();
        this.render();
    },

    remove: function(id) {
        this.entries = this.entries.filter(e => e.id !== id);
        this.save();
        this.render();
    },

    clear: function() {
        if (confirm('Clear all gratitude entries?')) {
            this.entries = [];
            this.save();
            this.render();
        }
    },

    save: function() {
        localStorage.setItem('gratitude-list', JSON.stringify(this.entries));
    },

    render: function() {
        // Display all entries in DOM
    }
};
```

**Modification Guide:**
- To add categories: Include dropdown for gratitude types (people, sobriety, health, etc.)
- To enhance: Add export feature (PDF/email), sharing capability, or daily reminders
- To improve: Add search within gratitudes, tag system, or inspirational quotes
- To expand: Include mood tracking or reflection prompts

---

## JavaScript Functionality

### Main Application Object

The entire application is wrapped in a single `app` object to avoid global namespace pollution:

```javascript
const app = {
    currentPage: 'home',

    // Initialization
    init: function() {
        this.initNavigation();
        this.initPages();
        this.initModals();
        this.initQuickActions();
        this.initSearch();
        this.initPWA();
        this.loadUserData();
        this.showTodaysMeetings();
    },

    // ... all methods
};

// Initialize on page load
document.addEventListener('DOMContentLoaded', function() {
    app.init();
});
```

### Key Functions

#### Navigation System
```javascript
app.navigateTo = function(page) {
    // Hide all pages
    document.querySelectorAll('.page-content').forEach(p => {
        p.classList.add('hidden');
    });

    // Show selected page
    const targetPage = page.replace('#', '');
    document.getElementById(targetPage + '-page').classList.remove('hidden');

    // Update URL hash
    window.location.hash = page;

    // Update navigation active state
    this.updateNavigation(page);

    // Store current page
    this.currentPage = targetPage;

    // Close mobile menu if open
    document.getElementById('mobile-menu').classList.add('hidden');

    // Scroll to top
    window.scrollTo({ top: 0, behavior: 'smooth' });
};
```

#### Page Initialization
```javascript
app.initPages = function() {
    // Initialize all interactive components
    this.initAccordions();
    this.initTabs();
    this.initForms();
    this.initCalculators();
    this.initVideoPlayers();
    this.initTools();

    // Set up event listeners for page-specific features
    // ...
};
```

#### Modal Management
```javascript
app.openModal = function(modalId) {
    const modal = document.getElementById(modalId);
    modal.classList.remove('hidden');
    modal.classList.add('flex');

    // Prevent body scroll
    document.body.style.overflow = 'hidden';
};

app.closeModal = function(modalId) {
    const modal = document.getElementById(modalId);
    modal.classList.add('hidden');
    modal.classList.remove('flex');

    // Restore body scroll
    document.body.style.overflow = '';
};
```

#### Local Storage Management
```javascript
app.saveData = function(key, value) {
    try {
        localStorage.setItem(key, JSON.stringify(value));
    } catch (e) {
        console.error('Failed to save data:', e);
        app.showNotification('Failed to save data', 'error');
    }
};

app.loadData = function(key) {
    try {
        const data = localStorage.getItem(key);
        return data ? JSON.parse(data) : null;
    } catch (e) {
        console.error('Failed to load data:', e);
        return null;
    }
};
```

#### Notification System
```javascript
app.showNotification = function(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `fixed top-20 right-4 p-4 rounded-lg shadow-lg z-50 animate-slide-down ${
        type === 'success' ? 'bg-green-500' :
        type === 'error' ? 'bg-red-500' :
        type === 'warning' ? 'bg-yellow-500' :
        'bg-blue-500'
    } text-white`;
    notification.textContent = message;

    document.body.appendChild(notification);

    setTimeout(() => {
        notification.remove();
    }, 3000);
};
```

#### Utility Functions
```javascript
// Time formatting
app.formatTime = function(time24) {
    const [hours, minutes] = time24.split(':');
    const hour = parseInt(hours);
    const ampm = hour >= 12 ? 'PM' : 'AM';
    const hour12 = hour % 12 || 12;
    return `${hour12}:${minutes} ${ampm}`;
};

// Date calculations
app.daysBetween = function(date1, date2) {
    const oneDay = 24 * 60 * 60 * 1000;
    return Math.round(Math.abs((date1 - date2) / oneDay));
};

// Get current day of week
app.getCurrentDay = function() {
    const days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
    return days[new Date().getDay()];
};
```

### Event Handling

All event listeners are centralized and initialized in the `init()` method:

```javascript
// Navigation clicks
document.querySelectorAll('a[href^="#"]').forEach(link => {
    link.addEventListener('click', function(e) {
        e.preventDefault();
        app.navigateTo(this.getAttribute('href'));
    });
});

// Mobile menu toggle
document.getElementById('menu-btn').addEventListener('click', function() {
    document.getElementById('mobile-menu').classList.toggle('hidden');
});

// Modal close buttons
document.querySelectorAll('[data-close-modal]').forEach(btn => {
    btn.addEventListener('click', function() {
        app.closeModal(this.dataset.closeModal);
    });
});

// Quick action buttons
document.getElementById('crisis-btn').addEventListener('click', () => {
    app.openModal('crisis-modal');
});

document.getElementById('search-btn').addEventListener('click', () => {
    app.openModal('search-modal');
    document.getElementById('search-input').focus();
});

document.getElementById('todays-meetings-btn').addEventListener('click', () => {
    app.navigateTo('#schedule');
});

// Form submissions
document.querySelectorAll('form').forEach(form => {
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        // Handle form submission
    });
});
```

---

## CSS and Styling

### CSS Custom Properties (Variables)

Defined in `:root` for consistent theming:

```css
:root {
    --primary-blue: #1e40af;
    --light-blue: #3b82f6;
    --pale-blue: #eff6ff;
    --text-dark: #1f2937;
    --text-light: #4b5563;
    --background-light: #f9fafb;
    --border-color: #e5e7eb;
    --font-primary: 'Inter', sans-serif;
    --font-serif: 'Lora', serif;
}
```

**Usage:** Referenced throughout CSS with `var(--primary-blue)` syntax.

**To modify colors site-wide:** Change these variable values.

### Typography

- **Primary Font:** Inter - Clean, modern sans-serif for UI and body text
- **Secondary Font:** Lora - Elegant serif for quotes, book pages, and emphasis
- **Responsive Font Sizing:** Uses `clamp()` for fluid typography
  ```css
  html {
      font-size: clamp(14px, 0.5vw+12px, 18px);
  }
  ```

### Animations

#### Fade In (Page transitions)
```css
@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(10px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}
.page-content {
    animation: fadeIn 0.5s ease-in-out;
}
```

#### Slide Down (Banners and notifications)
```css
@keyframes slide-down {
    from {
        transform: translateY(-100%);
        opacity: 0;
    }
    to {
        transform: translateY(0);
        opacity: 1;
    }
}
.animate-slide-down {
    animation: slide-down 0.3s ease-out;
}
```

#### Pulse (Attention drawing)
```css
@keyframes pulse-subtle {
    0%, 100% {
        opacity: 1;
    }
    50% {
        opacity: 0.95;
    }
}
.animate-pulse-subtle {
    animation: pulse-subtle 2s ease-in-out infinite;
}
```

### Interactive States

#### Hover Effects
- **Navigation Links:** Underline animation from center
- **Buttons:** Slight lift with shadow increase
- **Cards:** Elevated shadow and subtle scale
- **Timeline Blocks:** Lift and dot color change

```css
.nav-link::after {
    content: '';
    position: absolute;
    width: 0;
    height: 2px;
    bottom: -5px;
    left: 50%;
    transform: translateX(-50%);
    background-color: var(--light-blue);
    transition: width 0.3s ease;
}
.nav-link:hover::after {
    width: 100%;
}
```

#### Focus States (Accessibility)
All interactive elements have visible focus indicators:
```css
button:focus,
a:focus,
input:focus {
    outline: 2px solid var(--light-blue);
    outline-offset: 2px;
}
```

### Responsive Design

**Breakpoints:**
- Mobile: < 768px
- Tablet: 768px - 1024px
- Desktop: > 1024px

**Key Responsive Patterns:**

1. **Navigation:**
   - Desktop: Horizontal menu
   - Mobile: Hamburger with drawer

2. **Grid Layouts:**
   - Desktop: 3 columns
   - Tablet: 2 columns
   - Mobile: 1 column

3. **Timeline:**
   - Desktop: Alternating left/right with center line
   - Mobile: Single column with left-aligned line

4. **Typography:**
   - Scales down on smaller screens using Tailwind responsive classes
   - `text-2xl sm:text-3xl lg:text-4xl`

### Accessibility Features

1. **Screen Reader Only Class:**
```css
.sr-only {
    position: absolute;
    width: 1px;
    height: 1px;
    padding: 0;
    margin: -1px;
    overflow: hidden;
    clip: rect(0, 0, 0, 0);
    white-space: nowrap;
    border-width: 0;
}
```

2. **Focus Management:**
   - Skip to main content link
   - Visible focus indicators
   - Logical tab order

3. **ARIA Labels:**
   - All interactive elements have labels
   - Icons have `aria-hidden="true"` with text alternatives
   - Modals have proper roles and relationships

4. **Color Contrast:**
   - All text meets WCAG AA standards (4.5:1 minimum)
   - Important actions have higher contrast

5. **Semantic HTML:**
   - Proper heading hierarchy
   - Landmark regions (header, nav, main, section)
   - Lists for navigation and content

---

## SEO and Accessibility

### Meta Tags

#### Basic SEO
```html
<title>Rowlett Group of AA | Alcoholics Anonymous Meetings in Garland, TX</title>
<meta name="description" content="Find free AA meetings in Garland, TX...">
<meta name="keywords" content="AA, Alcoholics Anonymous, Rowlett Group...">
<link rel="canonical" href="https://www.rowlettaa.org/">
```

#### Open Graph (Social Media)
```html
<meta property="og:type" content="website">
<meta property="og:title" content="Rowlett Group of AA...">
<meta property="og:description" content="...">
<meta property="og:image" content="[Image URL]">
<meta property="og:url" content="https://www.rowlettaa.org/">
```

#### Twitter Cards
```html
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="...">
<meta name="twitter:description" content="...">
<meta name="twitter:image" content="...">
```

#### Geolocation
```html
<meta name="geo.region" content="US-TX">
<meta name="geo.placename" content="Garland">
<meta name="geo.position" content="32.912624;-96.638883">
```

### Structured Data (Schema.org)

#### Organization Schema
```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Rowlett Group of Alcoholics Anonymous",
  "url": "https://www.rowlettaa.org/",
  "contactPoint": {
    "@type": "ContactPoint",
    "telephone": "+1-972-925-0096",
    "email": "rowlettaa@gmail.com"
  }
}
```

#### Local Business Schema
Includes address, hours, geo coordinates, and more.

#### FAQ Schema
All FAQ questions and answers structured for rich snippets.

#### Event Schema
Meeting schedule and 30th anniversary event.

### Accessibility Compliance (WCAG 2.1 Level AA)

**Achieved Standards:**
- ✅ Perceivable: Images have alt text, sufficient color contrast
- ✅ Operable: Keyboard navigation, no time limits on content
- ✅ Understandable: Clear language, consistent navigation
- ✅ Robust: Semantic HTML, ARIA attributes, screen reader compatible

**Testing Recommendations:**
- Use WAVE browser extension
- Test with screen readers (NVDA, JAWS, VoiceOver)
- Validate HTML and ARIA
- Check color contrast with tools

---

## Content Management Guide

### How to Update Meeting Schedule

**Location:** Schedule section in HTML

**Steps:**
1. Find the schedule data structure in JavaScript section
2. Locate the day you want to modify
3. Add/edit/remove meeting objects

**Example - Adding a new meeting:**
```javascript
// Find this in the code:
'Wednesday': [
    {
        time: '12:00',
        type: 'Lunch Discussion',
        format: 'Open'
    },
    {
        time: '19:30',
        type: 'Discussion',
        format: 'Open'
    },
    // ADD NEW MEETING HERE:
    {
        time: '14:00',
        type: 'Step Study',
        format: 'Closed',
        description: 'Optional description'
    }
]
```

**Time Format:** Use 24-hour format (HH:MM) - it will automatically convert to 12-hour for display.

### How to Update Contact Information

**Locations to update:**
1. Contact section HTML
2. Crisis modal
3. Schema.org structured data
4. Meta tags in head

**Search for and replace:**
- Phone: `972-925-0096` or `+1-972-925-0096`
- Email: `rowlettaa@gmail.com`
- Address: `362 Oaks Trail #162, Garland, TX 75043`

### How to Add Literature Videos

**Location:** Literature section JavaScript

**Steps:**
1. Get YouTube video ID from URL
   - Example: `https://youtube.com/watch?v=ABC123` → ID is `ABC123`
2. Find the appropriate category array (bigbook, twelve, steps, speakers)
3. Add new video object

**Example:**
```javascript
const videos = {
    bigbook: [
        // Existing videos...
        {
            id: 'YOUR_YOUTUBE_ID',
            title: 'Chapter Title',
            description: 'Brief description of content'
        }
    ]
};
```

**Categories:**
- `bigbook` - Big Book chapters
- `twelve` - 12 Steps and 12 Traditions
- `steps` - Step study videos
- `speakers` - Speaker talks

### How to Update Special Events

**Location:** Home page and Our Group section

**For announcements on home page:**
1. Find the "Today's Meetings" banner section
2. Add event banner above or below existing content
3. Use similar styling with yellow/blue background

**For timeline events:**
1. Locate timeline-container in Our Group section
2. Add new timeline-block div
3. Alternate between `left` and `right` classes

**Example:**
```html
<div class="timeline-block left">
    <div class="timeline-content">
        <h3 class="text-xl font-bold text-cyan-600">2025</h3>
        <h4 class="text-lg font-semibold text-gray-800">Your Event Title</h4>
        <p class="text-gray-600">Event description...</p>
        <div class="info-popup">
            <p>Additional details shown on hover</p>
        </div>
    </div>
</div>
```

### How to Update Service Opportunities

**Location:** Get Involved section

**Steps:**
1. Find the service opportunities list
2. Each opportunity is in a card/div structure
3. Add/edit opportunities with title, description, and optional requirements

**Example:**
```html
<div class="bg-white p-6 rounded-lg shadow-md">
    <h3 class="text-xl font-semibold text-blue-800 mb-3">
        <i class="fas fa-icon-name text-blue-600 mr-2"></i>
        Position Title
    </h3>
    <p class="text-gray-600 mb-3">
        Description of the service position and responsibilities...
    </p>
    <p class="text-sm text-gray-500">
        Requirements: List any requirements or time commitments
    </p>
</div>
```

### How to Update Venmo Information

**Location:** Contribute section

**To update Venmo QR code:**
1. Generate new QR code from Venmo app
2. Upload image to hosting service (or convert to base64)
3. Replace `src` attribute in img tag

**To update Venmo username:**
1. Find all instances of `@rowlettaa`
2. Replace with new username
3. Update link `href` attribute

### How to Add New Pages/Sections

**Steps:**
1. **Create HTML section:**
```html
<section id="new-page-page" class="page-content hidden">
    <div class="container mx-auto px-6 py-12">
        <h1 class="text-4xl font-bold text-blue-800 mb-6">New Page Title</h1>
        <!-- Your content here -->
    </div>
</section>
```

2. **Add navigation link:**
```html
<!-- In desktop nav -->
<a href="#new-page" class="nav-link text-gray-600 hover:text-blue-800 text-sm">New Page</a>

<!-- In mobile nav -->
<a href="#new-page" class="nav-link block py-3 px-4 text-base hover:bg-gray-100">New Page</a>
```

3. **Add to search functionality:**
```javascript
// In app.search function, add:
{ section: 'New Page', content: document.getElementById('new-page-page').innerText }
```

4. **Initialize page features:**
```javascript
// In app.initPages function, add any specific initialization
```

### How to Modify Colors/Branding

**Primary method:** Modify CSS variables in `:root`

```css
:root {
    --primary-blue: #1e40af;     /* Change to your primary color */
    --light-blue: #3b82f6;       /* Change to lighter variant */
    --pale-blue: #eff6ff;        /* Change to background variant */
    /* ... etc */
}
```

**Secondary method:** Find and replace Tailwind classes
- `bg-blue-600` → `bg-[yourcolor]-600`
- `text-blue-800` → `text-[yourcolor]-800`
- Use consistent color scales (50, 100, 200...900)

**Logo:** Replace SVG code in header (line 841-845) or substitute with image file

---

## Testing Guidelines

### Visual Testing Checklist

**Desktop (1920x1080):**
- [ ] Navigation displays horizontally without wrapping
- [ ] Hero image loads and displays properly
- [ ] All sections have appropriate spacing
- [ ] Grid layouts show 3 columns where intended
- [ ] Modal windows are centered and properly sized
- [ ] Video thumbnails display in proper grid
- [ ] Timeline shows alternating left/right layout
- [ ] Footer (if present) spans full width

**Tablet (768x1024):**
- [ ] Navigation may wrap or show hamburger menu
- [ ] Grid layouts reduce to 2 columns
- [ ] Cards stack appropriately
- [ ] Text remains readable
- [ ] Touch targets are at least 44x44px
- [ ] Modals adjust to screen width

**Mobile (375x667):**
- [ ] Hamburger menu appears and functions
- [ ] All content stacks to single column
- [ ] Timeline converts to single column
- [ ] Text is readable without zooming
- [ ] Buttons are easily tappable
- [ ] Forms are easy to fill out
- [ ] Quick action buttons don't overlap content

### Functional Testing Checklist

**Navigation:**
- [ ] All nav links navigate to correct sections
- [ ] Mobile menu opens and closes properly
- [ ] Active page is highlighted correctly
- [ ] Smooth scrolling works
- [ ] Hash updates in URL
- [ ] Browser back/forward buttons work

**Meeting Schedule:**
- [ ] All 7 days display
- [ ] Meeting times show in 12-hour format
- [ ] Format badges (Open/Closed) display
- [ ] Today's meetings banner shows correct day
- [ ] Special meetings (Sunday, Saturday) display properly

**Sobriety Calculator:**
- [ ] Date input accepts dates
- [ ] Future dates show error
- [ ] Calculations are accurate
- [ ] All time units display (years, months, days, hours, minutes)
- [ ] Milestone badge appears
- [ ] Encouragement message shows
- [ ] Results persist on page navigation

**Literature Videos:**
- [ ] All tabs switch correctly
- [ ] Videos load and play in modal
- [ ] Modal closes properly
- [ ] Video stops when modal closes
- [ ] Thumbnails load from YouTube
- [ ] Grid scrolls smoothly

**Study Guide Tools:**
- [ ] **Meditation Timer:**
  - [ ] Preset buttons work
  - [ ] Custom input accepts numbers
  - [ ] Timer counts down accurately
  - [ ] Pause/Resume functions
  - [ ] Reset returns to initial state
  - [ ] Notification shows on completion
- [ ] **HALT Check:**
  - [ ] Options select/deselect on click
  - [ ] Visual feedback on selection
  - [ ] Recommendations appear for all combinations
  - [ ] Clear selections works
- [ ] **Gratitude List:**
  - [ ] Can add entries
  - [ ] Entries display with dates
  - [ ] Can delete individual entries
  - [ ] Clear all works with confirmation
  - [ ] Data persists after refresh
- [ ] **Personal Notes:**
  - [ ] Can add notes
  - [ ] Notes save and display
  - [ ] Can edit and delete notes
  - [ ] Data persists

**Search:**
- [ ] Modal opens from quick action button
- [ ] Search input accepts text
- [ ] Results appear in real-time
- [ ] Results are relevant
- [ ] Clicking result navigates to section
- [ ] Modal closes properly
- [ ] Escape key closes modal

**Modals:**
- [ ] All modals open when triggered
- [ ] Close button works
- [ ] Clicking outside closes modal
- [ ] Escape key closes modal
- [ ] Body scroll is prevented when open
- [ ] Multiple modals don't conflict

**PWA Installation:**
- [ ] Install banner appears on eligible devices
- [ ] Install button triggers prompt
- [ ] Dismiss button hides banner
- [ ] Dismissal is remembered
- [ ] App installs correctly
- [ ] Installed app opens standalone

**Quick Action Buttons:**
- [ ] All three buttons visible
- [ ] Buttons don't overlap content
- [ ] Hover effects work
- [ ] Crisis button opens crisis modal
- [ ] Today's meetings navigates to schedule
- [ ] Search button opens search modal

**Forms:**
- [ ] All inputs accept appropriate data
- [ ] Required fields are validated
- [ ] Error messages display clearly
- [ ] Success messages show
- [ ] Form resets after submission

### Accessibility Testing

**Keyboard Navigation:**
- [ ] Can tab through all interactive elements
- [ ] Focus indicators are visible
- [ ] Skip to main content link works
- [ ] No keyboard traps
- [ ] Logical tab order
- [ ] Enter/Space activate buttons
- [ ] Escape closes modals

**Screen Reader:**
- [ ] All images have alt text
- [ ] Links have descriptive text
- [ ] Buttons have labels
- [ ] Form inputs have labels
- [ ] ARIA attributes are correct
- [ ] Page structure is logical
- [ ] Headings form proper hierarchy

**Color Contrast:**
- [ ] All text meets 4.5:1 contrast ratio
- [ ] Interactive elements meet 3:1 ratio
- [ ] Error states are not color-only
- [ ] Focus indicators are visible

### Performance Testing

**Load Time:**
- [ ] Page loads in under 3 seconds on 3G
- [ ] First Contentful Paint < 1.8s
- [ ] Time to Interactive < 3.8s
- [ ] Cumulative Layout Shift < 0.1

**Resource Loading:**
- [ ] Images are optimized
- [ ] CSS and JS are minified (for production)
- [ ] Fonts load efficiently
- [ ] YouTube embeds don't slow initial load
- [ ] No render-blocking resources

**Responsiveness:**
- [ ] Page responds to user input immediately
- [ ] Animations are smooth (60fps)
- [ ] No janky scrolling
- [ ] Video playback is smooth

### Cross-Browser Testing

Test in:
- [ ] Chrome (latest)
- [ ] Firefox (latest)
- [ ] Safari (latest)
- [ ] Edge (latest)
- [ ] Mobile Safari (iOS)
- [ ] Chrome Mobile (Android)

**Specific checks:**
- [ ] CSS Grid/Flexbox layouts work
- [ ] localStorage functions properly
- [ ] Date inputs work (or have fallback)
- [ ] Custom fonts load
- [ ] Animations perform well

### SEO Testing

**Technical SEO:**
- [ ] Title tag is present and descriptive
- [ ] Meta description is compelling
- [ ] Canonical URL is set
- [ ] Open Graph tags are complete
- [ ] Structured data is valid (test with Google Rich Results Test)
- [ ] Sitemap is accessible
- [ ] Robots meta tag allows indexing

**Content SEO:**
- [ ] H1 tag is present on each main section
- [ ] Heading hierarchy is logical
- [ ] Internal links work
- [ ] External links open in new tabs
- [ ] Images have descriptive alt text
- [ ] URLs are clean (hash navigation)

**Local SEO:**
- [ ] NAP (Name, Address, Phone) is consistent
- [ ] Local business schema is complete
- [ ] Geo meta tags are accurate
- [ ] Google Maps embed works

### Security Testing

- [ ] No sensitive data in client-side code
- [ ] External links have `rel="noopener noreferrer"`
- [ ] No inline JavaScript in production
- [ ] Content Security Policy considered
- [ ] HTTPS enforced
- [ ] No mixed content warnings

---

## Deployment Instructions

### Option 1: Static Hosting (Recommended)

**Platforms:** Netlify, Vercel, GitHub Pages, Cloudflare Pages

**Steps for Netlify:**
1. Create account at netlify.com
2. Click "Add new site" → "Deploy manually"
3. Drag and drop your `index.html` file
4. Site is live immediately
5. Optional: Configure custom domain

**Steps for GitHub Pages:**
1. Create GitHub repository
2. Push `index.html` to repository
3. Go to Settings → Pages
4. Select branch and root folder
5. Save - site will be live at `username.github.io/repo-name`

**Steps for Vercel:**
1. Create account at vercel.com
2. Import project or drag/drop file
3. Deploy - site is live immediately
4. Optional: Add custom domain

### Option 2: Traditional Web Hosting

**Platforms:** Bluehost, HostGator, SiteGround, GoDaddy

**Steps:**
1. Purchase hosting plan
2. Access cPanel or file manager
3. Navigate to `public_html` or `www` folder
4. Upload `index.html` file
5. Ensure file is named `index.html` (lowercase)
6. Access via your domain

### Option 3: Content Delivery Network (CDN)

**Platforms:** Cloudflare, AWS CloudFront

**Benefits:**
- Global distribution
- Faster load times
- DDoS protection
- Automatic caching

### Custom Domain Setup

**If you have a custom domain:**
1. Purchase domain from registrar (Namecheap, Google Domains, etc.)
2. In hosting platform, add custom domain
3. Update DNS records:
   - A record pointing to hosting IP
   - OR CNAME record pointing to hosting URL
4. Wait for DNS propagation (up to 48 hours)
5. Enable HTTPS/SSL certificate (usually automatic)

### Pre-Deployment Checklist

- [ ] Update all contact information
- [ ] Verify all links work
- [ ] Test on multiple devices
- [ ] Optimize images (compress without quality loss)
- [ ] Minify HTML/CSS/JS (optional, improves load time)
- [ ] Set up analytics (Google Analytics, Plausible, etc.)
- [ ] Configure error pages (404)
- [ ] Test PWA installation
- [ ] Verify structured data with Google tools
- [ ] Submit sitemap to Google Search Console

### Post-Deployment

**Monitor:**
- Google Search Console - indexing status, errors
- Google Analytics - traffic, user behavior
- PageSpeed Insights - performance metrics
- Uptime monitor - availability

**Maintain:**
- Update meeting schedules regularly
- Add new literature videos as available
- Respond to contact form submissions (if added)
- Backup site files regularly
- Check for broken links monthly
- Update dependencies (Tailwind, Font Awesome) annually

---

## Browser Compatibility

### Supported Browsers

**Desktop:**
- Chrome 90+ ✅
- Firefox 88+ ✅
- Safari 14+ ✅
- Edge 90+ ✅

**Mobile:**
- iOS Safari 14+ ✅
- Chrome Mobile 90+ ✅
- Firefox Mobile 88+ ✅
- Samsung Internet 14+ ✅

### Known Issues

**Safari (Desktop & Mobile):**
- Date input may render differently - consider custom datepicker for consistency
- Some CSS grid features may need prefixes
- Service worker caching may behave differently

**Internet Explorer 11:**
- ❌ Not supported (EOL June 2022)
- CSS Grid not supported
- Many ES6 features unavailable
- Consider showing upgrade message for IE users

**Older Android Browsers:**
- Android 5.0 and below may have CSS issues
- Recommend Chrome or Firefox for best experience

### Feature Detection & Fallbacks

**localStorage:**
```javascript
if (typeof(Storage) !== "undefined") {
    // Use localStorage
} else {
    // Fallback to cookies or disable feature
    console.warn("localStorage not supported");
}
```

**CSS Grid:**
```css
.grid-container {
    display: flex; /* Fallback */
    flex-wrap: wrap;
}
@supports (display: grid) {
    .grid-container {
        display: grid;
    }
}
```

**IntersectionObserver (for lazy loading):**
```javascript
if ('IntersectionObserver' in window) {
    // Use IntersectionObserver
} else {
    // Load all images immediately
}
```

### Progressive Enhancement Strategy

The site is built with progressive enhancement:
1. **Base:** Works without JavaScript (static content visible)
2. **Enhanced:** JavaScript adds navigation, calculators, interactions
3. **Modern:** PWA features, advanced animations, service worker

---

## Developer Guide

### Architecture Overview

**Pattern:** Single-page application (SPA) with vanilla JavaScript

**Key Principles:**
- **Separation of Concerns:** HTML structure, CSS presentation, JS behavior
- **Component-Based:** Each major feature is self-contained
- **Progressive Enhancement:** Core content works without JS
- **Accessibility First:** WCAG 2.1 AA compliance
- **Performance Optimized:** Minimal dependencies, lazy loading

### Code Organization

**HTML Structure:**
```
<head>
├── Meta tags & SEO
├── External resources (CDN links)
├── Structured data (JSON-LD)
└── Styles (<style> block)

<body>
├── Accessibility (skip link)
├── Header (navigation)
├── Global components (PWA banner, quick actions)
├── Modals (search, crisis)
├── Main content (all pages/sections)
└── Scripts (<script> block)
```

**JavaScript Structure:**
```
const app = {
    // State
    currentPage: 'home',
    userData: {},

    // Initialization
    init() {...},

    // Navigation
    navigateTo() {...},
    updateNavigation() {...},

    // Page management
    initPages() {...},
    showPage() {...},
    hidePage() {...},

    // Features
    calculateSobriety() {...},
    openVideoModal() {...},
    search() {...},
    // etc.

    // Utilities
    formatTime() {...},
    saveData() {...},
    loadData() {...},
    showNotification() {...}
};
```

### Adding New Features

**1. Add a new page:**

```javascript
// In HTML:
<section id="new-feature-page" class="page-content hidden">
    <div class="container mx-auto px-6 py-12">
        <h1>New Feature</h1>
        <!-- Content -->
    </div>
</section>

// In JavaScript:
app.initNewFeature = function() {
    // Set up event listeners
    // Load data
    // Initialize components
};

// Call in app.init():
app.init = function() {
    // ... existing code
    this.initNewFeature();
};
```

**2. Add a modal:**

```html
<div id="new-modal" class="fixed inset-0 bg-black bg-opacity-50 z-50 hidden items-center justify-center p-4">
    <div class="bg-white rounded-lg shadow-2xl max-w-2xl w-full">
        <div class="p-6">
            <div class="flex justify-between items-center mb-4">
                <h2>Modal Title</h2>
                <button type="button" onclick="app.closeModal('new-modal')">
                    <i class="fas fa-times"></i>
                </button>
            </div>
            <!-- Content -->
        </div>
    </div>
</div>
```

**3. Add a localStorage feature:**

```javascript
app.saveUserPreference = function(key, value) {
    const prefs = this.loadData('userPreferences') || {};
    prefs[key] = value;
    this.saveData('userPreferences', prefs);
};

app.loadUserPreference = function(key) {
    const prefs = this.loadData('userPreferences') || {};
    return prefs[key];
};
```

**4. Add a calculator/tool:**

```javascript
app.newCalculator = function() {
    // Get input values
    const input = document.getElementById('calc-input').value;

    // Validate
    if (!input) {
        this.showNotification('Please enter a value', 'warning');
        return;
    }

    // Calculate
    const result = /* your calculation */;

    // Display result
    document.getElementById('calc-result').innerHTML = result;

    // Optional: Save for later
    this.saveData('lastCalculation', result);
};
```

### Best Practices

**JavaScript:**
- Use `const` and `let` instead of `var`
- Add all functions to `app` object to avoid global pollution
- Use arrow functions for callbacks
- Validate all user inputs
- Handle errors gracefully with try/catch
- Use meaningful variable names
- Comment complex logic

**CSS:**
- Use Tailwind utility classes when possible
- Add custom CSS for animations and complex layouts
- Use CSS variables for colors and common values
- Maintain consistent spacing scale
- Test responsive breakpoints
- Consider dark mode (future enhancement)

**HTML:**
- Use semantic elements (`<header>`, `<nav>`, `<main>`, `<section>`)
- Add ARIA labels to interactive elements
- Include alt text for all images
- Use proper heading hierarchy
- Validate HTML regularly

**Accessibility:**
- Always include keyboard navigation
- Test with screen readers
- Maintain focus indicators
- Use sufficient color contrast
- Provide text alternatives for non-text content

### Debugging Tips

**Console Logging:**
```javascript
// Debug navigation
console.log('Navigating to:', page);

// Debug calculations
console.log('Input:', input, 'Result:', result);

// Debug storage
console.log('Saved data:', localStorage.getItem('key'));
```

**Browser DevTools:**
- **Elements tab:** Inspect HTML/CSS, modify live
- **Console tab:** View errors, test JavaScript
- **Network tab:** Check resource loading
- **Application tab:** Inspect localStorage, Service Workers
- **Lighthouse tab:** Performance, accessibility, SEO audits

**Common Issues:**

1. **Page not showing:**
   - Check if section has `hidden` class
   - Verify ID matches navigation hash
   - Check JavaScript console for errors

2. **Data not persisting:**
   - Verify localStorage is available
   - Check for quota exceeded errors
   - Ensure JSON.stringify/parse are working

3. **Modals not closing:**
   - Check event listeners are attached
   - Verify close button IDs match
   - Look for JavaScript errors preventing execution

4. **Styles not applying:**
   - Check Tailwind classes are correct
   - Verify custom CSS syntax
   - Look for specificity issues
   - Check for typos in class names

### Performance Optimization

**Current optimizations:**
- Lazy loading images
- CDN for external resources
- Minified external libraries
- Resource hints (preconnect, dns-prefetch)
- Single file architecture

**Future optimizations:**
- Minify HTML/CSS/JS for production
- Compress images (WebP format)
- Implement service worker for full offline support
- Add resource caching headers
- Consider code splitting for very large sites

### Version Control

**Recommended workflow:**
1. Initialize git repository
2. Create `.gitignore` file
3. Commit initial version
4. Create branches for new features
5. Merge to main when tested
6. Tag releases (v1.0, v1.1, etc.)

**Example `.gitignore`:**
```
.DS_Store
Thumbs.db
*.log
node_modules/
.env
```

### Documentation

**Keep this README updated:**
- Document all new features
- Update testing checklist
- Note breaking changes
- Update deployment instructions as needed
- Document any workarounds or known issues

---

## Additional Resources

### AA Resources
- **AA World Services:** https://www.aa.org/
- **Dallas AA:** https://www.aadallas.org/
- **Northeast Texas Area 65:** https://neta65.org/

### Development Resources
- **Tailwind CSS Docs:** https://tailwindcss.com/docs
- **Font Awesome Icons:** https://fontawesome.com/icons
- **MDN Web Docs:** https://developer.mozilla.org/
- **Schema.org:** https://schema.org/

### Tools
- **Accessibility Testing:** WAVE, aXe DevTools
- **SEO Testing:** Google Search Console, Lighthouse
- **Performance:** PageSpeed Insights, WebPageTest
- **Validation:** W3C HTML Validator, CSS Validator

---

## Changelog

### Version 1.0 (Current)
- Initial release
- 10 main pages/sections
- Meeting schedule with 7 days
- Sobriety calculator
- Literature video library (63+ videos)
- Study guide tools (meditation timer, HALT check, gratitude list, notes)
- PWA capabilities
- Search functionality
- Crisis resources
- Timeline history
- Fully responsive design
- SEO optimized
- WCAG 2.1 AA accessible

### Future Enhancements (Planned)
- Service worker for full offline capability
- Meeting check-in tracker
- Step work journaling
- Daily reflections
- Meeting finder with maps
- Anonymous chat/support
- Multilingual support (Spanish)
- Dark mode
- Email newsletter signup
- Blog/articles section
- Event RSVP system

---

## Support & Contact

**For technical issues with the website:**
- Create an issue in the repository
- Contact the web administrator
- Email: rowlettaa@gmail.com

**For AA support and meeting information:**
- **Phone:** (972) 925-0096
- **Email:** rowlettaa@gmail.com
- **Address:** 362 Oaks Trail #162, Garland, TX 75043

**Emergency Resources:**
- **National Suicide Prevention:** 988
- **Crisis Text Line:** Text HELLO to 741741
- **Dallas AA Hotline:** (214) 887-6699

---

## License

This website is created for the Rowlett Group of Alcoholics Anonymous. The 12 Steps and 12 Traditions are reprinted and adapted with permission of Alcoholics Anonymous World Services, Inc. (AAWS).

**AA Preamble** and related content are copyright © by AA Grapevine, Inc.

---

## Acknowledgments

Special thanks to:
- All members of the Rowlett Group for their service and support
- Alcoholics Anonymous World Services for providing recovery resources
- The open-source community for development tools
- All those in recovery who continue to carry the message

---

**Last Updated:** January 2025

**README Version:** 1.0

**Website Version:** 1.0

---

*Remember: The only requirement for A.A. membership is a desire to stop drinking.*
