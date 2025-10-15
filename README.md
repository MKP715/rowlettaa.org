# Rowlett Group of AA - Website Documentation

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Technical Stack](#technical-stack)
- [File Structure](#file-structure)
- [Detailed Component Documentation](#detailed-component-documentation)
- [JavaScript Functionality](#javascript-functionality)
- [CSS and Styling](#css-and-styling)
- [SEO and Accessibility](#seo-and-accessibility)
- [Content Management](#content-management)
- [Testing Guidelines](#testing-guidelines)
- [Deployment Instructions](#deployment-instructions)
- [Browser Compatibility](#browser-compatibility)
- [Developer Guide](#developer-guide)

---

## Project Overview

### Title
**Rowlett Group of AA - Alcoholics Anonymous Meetings in Garland, TX**

### Description
This is a comprehensive single-page application (SPA) website for the Rowlett Group of Alcoholics Anonymous in Garland, Texas. The website serves as a complete resource hub for individuals seeking help with alcoholism, providing meeting schedules, literature, recovery tools, and information about the fellowship.

### Purpose
The website aims to:
- Provide easy access to AA meeting information and schedules
- Offer educational resources about Alcoholics Anonymous
- Help newcomers understand what to expect at meetings
- Provide recovery tools (sobriety tracker, meditation timer, gratitude list, HALT check)
- Share AA literature and educational videos
- Connect people with support resources and crisis help
- Build community through service opportunities and group history

---

## Features

### 1. Home Page
- **Hero Section**: Beautiful mountain sunrise image with inspirational quote
- **Serenity Prayer**: Prominently displayed
- **AA Preamble**: Complete text with proper attribution
- **Responsibility Declaration**: With helpful tooltip explaining its significance
- **Today's Meetings Banner**: Dynamic display showing current day's meeting schedule

### 2. What is A.A.? Page
- Comprehensive introduction for newcomers
- Explanation of AA fellowship and program
- Meeting types breakdown (Discussion, Literature Study, Speaker, Men's/Women's, Group Conscience)
- Open vs Closed meeting distinctions
- What AA does and doesn't do
- Court programs and attendance verification information
- Self-assessment link to AA.org

### 3. Schedule Page
- **Complete Weekly Schedule**: All meetings organized by day
- **Meeting Filters**: Filter by All, Open, or Closed meetings
- **Today's Meetings Highlight**: Current day's meetings displayed prominently
- **Location Information**: In-person address with map link
- **Zoom Details**: Meeting ID and password for virtual attendance
- **Special Events**: Dynamic display of upcoming anniversaries and celebrations
- **Group Conscience Meeting**: Automatically calculated 3rd Monday date
- **First Visit Information**: Extensive FAQ accordion with common questions

### 4. Resources Page
- **Big Book Study Guide**: Comprehensive study methodology and tools
- **Sobriety Calculator**: Track sobriety with milestone achievements
  - Days/months/years breakdown
  - 17 milestone levels (24 hours to 30 years)
  - Progress bar showing next milestone
  - Persistent storage using localStorage
- **HALT Check**: Interactive tool for self-assessment (Hungry, Angry, Lonely, Tired)
- **Meditation Timer**: Configurable timer (5, 10, or 15 minutes) for Step 11 practice
- **Gratitude List**: Persistent note-taking tool for daily gratitude

### 5. Get Involved Page
- **Service Opportunities**: Information on speakers, sponsors, and phone answering
- **Facility Commitments**:
  - The Magdalen House (Women's Discussion)
  - Rockwall County Jail (Men's and Women's meetings)
  - Salvation Army (Men's Short Story)
  - Medical City Green Oaks Hospital (Mixed Short Story)
- **Dynamic Date Calculation**: Automatically updates Magdalen House meeting dates

### 6. Literature Page
- **Big Book**: Read or watch (ASL videos)
- **Twelve Steps and Twelve Traditions**: Read or watch (ASL videos)
- **How It Works**: Complete text from the Big Book
- **Twelve Promises**: Full list with introduction
- **Twelve Traditions**: Both Short and Long forms
- **Accordion Interface**: Collapsible sections for easy navigation
- **Tab System**: Switch between reading and watching content
- **Video Grid**: Organized display of ASL literature videos
- **Video Modal**: Full-screen video player with YouTube integration
- **Daily Reflection Link**: Direct link to AA.org's daily reflection

### 7. Our Group Page
- **Interactive Timeline**: Visual history of the Rowlett Group
- **Hover Tooltips**: Additional information on timeline events
- **Founding Story**: Complete narrative from 1995 to present
- **Declaration of Unity**: Prominent display with explanation

### 8. Study Guide Page
- **Dictionary Lookup Tool**: Real-time word definitions using Dictionary API
- **Personal Study Notes**: Create, edit, search, and delete notes with timestamps
- **Color-Coding System**: 5-category system for highlighting (Problem, Solution, Program, Result, Personal Resonance)
- **Annotation Key**: Advanced symbols for deeper study
- **Sample Annotated Page**: Visual example of study methodology
- **1930s Dictionary Guidance**: Historical context for original text

### 9. Contact Page
- **Contact Information**: Phone, email, and physical address
- **Interactive Map**: Embedded Google Maps for location
- **Google Form**: Embedded contact form for messages
- **Al-Anon Information**: Resources for family and friends
- **Alateen Resources**: Support for young people
- **Twelfth Tradition**: Explanation of anonymity principle

### 10. Contribute Page
- **Zelle Payment**: With QR code for easy mobile donations
- **Check Payment**: Mailing address for traditional contributions
- **Seventh Tradition**: Complete explanation with Long Form quote

### 11. Global Features

#### Navigation System
- **Sticky Header**: Always accessible navigation bar
- **Mobile Menu**: Hamburger menu for small screens
- **Active Page Highlighting**: Visual indication of current page
- **Hash-based Routing**: URL updates with page changes
- **Smooth Scrolling**: Enhanced user experience

#### Quick Action Buttons (Floating)
- **Crisis Resources**: Immediate access to emergency contacts
  - National Suicide Prevention Lifeline (988)
  - Crisis Text Line
  - Dallas AA Central Office
  - Rowlett Group contact
- **Today's Meetings**: Jump to today's schedule
- **Search Function**: Site-wide search with keyword matching

#### Progressive Web App (PWA)
- **Installation Prompt**: Dismissible banner for app installation
- **Service Worker**: Offline caching for basic functionality
- **Manifest**: PWA configuration with icons
- **Offline Support**: Basic content available without internet

#### Accessibility Features
- **Skip to Content Link**: Keyboard navigation support
- **ARIA Labels**: Screen reader compatibility
- **Semantic HTML**: Proper heading hierarchy
- **Focus Management**: Logical tab order
- **Alt Text**: All images have descriptive alternative text
- **Color Contrast**: WCAG compliant color schemes

#### Search System
- **Real-time Search**: Debounced search with 300ms delay
- **Keyword Matching**: Searches across all pages
- **Relevance Scoring**: Prioritizes exact matches
- **Modal Interface**: Non-intrusive search overlay

---

## Technical Stack

### Frontend Technologies
- **HTML5**: Semantic markup for accessibility and SEO
- **CSS3**: Modern styling with custom properties
- **Tailwind CSS**: Utility-first CSS framework (via CDN)
- **JavaScript (ES6+)**: Vanilla JavaScript, no frameworks

### External Libraries & Services
- **Tailwind CSS v3**: CDN-based styling framework
- **Font Awesome v6.5.1**: Icon library
- **Google Fonts**: Inter and Lora font families
- **Dictionary API**: Free dictionary definitions (dictionaryapi.dev)
- **YouTube Embed**: ASL video integration
- **Google Maps**: Location embedding
- **Google Forms**: Contact form integration
- **Zelle**: Payment integration with QR code

### Browser APIs Used
- **Service Worker API**: PWA offline support
- **localStorage API**: Persistent data storage
- **History API**: Hash-based routing
- **Fetch API**: Dictionary lookup requests
- **Intersection Observer**: Potential for lazy loading
- **beforeinstallprompt**: PWA installation handling

### Data Storage
- **localStorage**: Client-side persistent storage for:
  - Sobriety date and calculations
  - Study guide notes
  - Gratitude list entries
  - PWA installation dismissal preference
- **No Backend**: Fully static website
- **No Database**: All data stored client-side

---

## File Structure

### Single File Architecture
The entire website is contained in **one HTML file** (`index.html`) with inline CSS and JavaScript.

```
index.html
├── HEAD Section
│   ├── Meta tags (SEO, social media, mobile)
│   ├── Schema.org structured data (JSON-LD)
│   ├── External stylesheets (Tailwind, Font Awesome, Google Fonts)
│   └── Custom CSS styles
├── BODY Section
│   ├── Skip link (accessibility)
│   ├── Header (navigation)
│   ├── PWA install banner
│   ├── Quick action buttons
│   ├── Modals (search, crisis, video)
│   ├── Main content sections (9 pages)
│   ├── Footer with A.A. resources
│   └── Notification container
└── SCRIPT Section
    ├── Utility functions
    ├── Main app object
    ├── Event listeners
    └── Notification system
```

### Content Organization
All content is organized into sections with IDs:
- `#home-page`
- `#what-is-aa-page`
- `#schedule-page`
- `#resources-page`
- `#get-involved-page`
- `#literature-page`
- `#our-group-page`
- `#study-guide-page`
- `#contact-page`
- `#contribute-page`

---

## Detailed Component Documentation

### Header and Navigation

#### Desktop Navigation
- Logo with SVG icon
- 7 main navigation links
- Special "Contribute" button with distinct styling
- Active page highlighting

#### Mobile Navigation
- Hamburger menu button
- Slide-down menu panel
- Touch-friendly link sizing
- Automatic close on navigation

#### Implementation Details
```javascript
// Navigation is hash-based
window.addEventListener('hashchange', () => {
    const pageId = (window.location.hash.substring(1) || 'home') + '-page';
    this.showPage(pageId);
});
```

### PWA Installation System

#### Features
- Detects installation capability
- Shows dismissible banner
- Handles user choice
- Persists dismissal preference
- Success notification

#### Trigger Events
- `beforeinstallprompt`: Shows banner
- `appinstalled`: Confirms installation

### Service Worker

#### Caching Strategy
- Cache-first for offline support
- Caches index.html and root path
- Automatic cache versioning
- Old cache cleanup on activation

#### Version
Current: `rowlett-aa-cache-v2`

### Meeting Schedule System

#### Data Structure
```javascript
{
    day: "Monday",
    dayIndex: 1,
    meetings: [
        {
            time: "12:00 PM",
            type: "closed",
            name: "Discussion Meeting"
        }
    ]
}
```

#### Dynamic Features
- Today's meeting highlighting (blue background)
- Automatic date calculations (Group Conscience, Special Events)
- Meeting type filtering
- Study guide link integration

#### Special Event Handling
- Static events (with specific dates)
- Recurring events (e.g., last Saturday of month)
- Automatic future event filtering
- Dynamic date display

### Sobriety Calculator

#### Milestone System
17 milestones from 24 hours to 30 years:
- 24 Hours (🌟)
- 1 Week (⭐)
- 1 Month (🎯)
- 2 Months (💎)
- 3 Months (🏅)
- 6 Months (🎖️)
- 9 Months (🥇)
- 1 Year (🏆)
- 18 Months (💫)
- 2 Years (🌟)
- 3 Years (⚡)
- 5 Years (🔥)
- 10 Years (👑)
- 15 Years (💎)
- 20 Years (🌈)
- 25 Years (✨)
- 30 Years (🎆)

#### Calculation Logic
```javascript
const calculateDaysSober = (sobrietyDate) => {
    const today = new Date();
    today.setHours(0, 0, 0, 0);
    const startDate = new Date(sobrietyDate);
    startDate.setHours(0, 0, 0, 0);
    const diffTime = Math.abs(today - startDate);
    return Math.floor(diffTime / (1000 * 60 * 60 * 24));
};
```

#### Progress Tracking
- Visual progress bar to next milestone
- Days/months/years breakdown
- Color-coded milestone achievements
- Animated gradient backgrounds for achieved milestones

### HALT Check Tool

#### Categories
- **Hungry** (🍎): Nutrition check
- **Angry** (😠): Emotional state
- **Lonely** (😔): Social connection
- **Tired** (😴): Rest assessment

#### Interaction
- Multiple selection allowed
- Dynamic recommendations
- Visual selection feedback
- Personalized advice for each state

### Meditation Timer

#### Configuration
- 3 preset durations: 5, 10, 15 minutes
- Visual time selection
- Large display format (MM:SS)
- Start/stop controls

#### Implementation
```javascript
window.meditationInterval = setInterval(() => {
    meditationTime--;
    updateTimerDisplay();
    if (meditationTime <= 0) {
        // Timer complete
        clearInterval(window.meditationInterval);
        showNotification('Meditation complete!', 'success');
    }
}, 1000);
```

### Gratitude List

#### Features
- Add unlimited gratitude items
- 200 character limit per item
- Timestamp for each entry
- Persistent storage
- Search/filter capability
- Delete individual items
- Clear all function

#### Storage
Uses localStorage with key: `rowlettAA_gratitudeList`

### Study Guide Tools

#### Dictionary Lookup
- Real-time API calls to dictionaryapi.dev
- Phonetic pronunciation display
- Multiple definitions
- Example sentences
- Part of speech categorization
- Offline detection

#### Personal Notes System
- Create, edit, delete notes
- Timestamp tracking (created and edited)
- Search functionality
- Clear search button
- Persistent storage
- Rich text display with whitespace preservation

#### Note Structure
```javascript
{
    id: Date.now(),
    content: "Note text",
    created: Date.now(),
    edited: null
}
```

### Literature Video System

#### Content Organization
Videos organized by book:
- **Big Book** (`bb`)
- **Twelve Steps and Twelve Traditions** (`tt`)

#### Video Modal
- Full-screen overlay
- YouTube iframe integration
- Escape key to close
- Click outside to close
- Automatic video stop on close

#### Data Structure
```javascript
{
    book: "bb",
    title: "The Doctor's Opinion",
    url: "https://www.youtube.com/embed/[VIDEO_ID]"
}
```

### Search System

#### Search Algorithm
1. Query normalization (lowercase)
2. Title exact match (100 points)
3. Title partial match (50 points per word)
4. Keyword exact match (30 points)
5. Keyword partial match (10 points per word)
6. Sort by score (descending)
7. Filter results with score > 0

#### Search Data
Each page has:
- Title
- Hash URL
- Keywords array (comprehensive list)

#### Debouncing
300ms delay to prevent excessive searching during typing

### Accordion System

#### Types
1. **Main Accordions**: Large section toggles
2. **Sub Accordions**: Nested content areas

#### Animation
- Max-height transition (0.5s ease-out)
- Icon rotation (180 degrees)
- Smooth parent height adjustment
- Recursive parent updates for nested accordions

#### Implementation
```javascript
if (isOpen) {
    content.style.maxHeight = content.scrollHeight + "px";
    updateAllParentAccordions(content);
} else {
    content.style.maxHeight = "0px";
}
```

---

## JavaScript Functionality

### Main Application Object

#### Structure
```javascript
const app = {
    cachedElements: {},
    initialized: {
        resources: false,
        schedule: false,
        literature: false,
        ourGroup: false,
        studyGuide: false
    },
    searchData: { pages: [...] },
    init: function() { ... },
    // ... other methods
}
```

#### Initialization Sequence
1. Service Worker registration
2. PWA install prompt setup
3. Navigation system initialization
4. Modal system setup
5. Quick action buttons
6. General event listeners
7. Initial page load
8. Copyright year update

#### Element Caching
Improves performance by storing DOM element references:
```javascript
getElement: function(id) {
    if (!this.cachedElements[id]) {
        this.cachedElements[id] = document.getElementById(id);
    }
    return this.cachedElements[id];
}
```

### Page Initialization Functions

#### Lazy Initialization
Pages initialize their content only when first visited, preventing unnecessary processing and improving initial load time.

#### Pattern
```javascript
initSchedulePage: function() {
    if (this.initialized.schedule) return; // Skip if already loaded
    // ... initialization code
    this.initialized.schedule = true;
}
```

### Utility Functions

#### Date Calculations
```javascript
// Calculate 3rd Monday of month
function getThirdMonday(year, month) {
    const d = new Date(year, month, 1);
    const day = d.getDay();
    let firstMonday = 1 + (1 - day + 7) % 7;
    const thirdMondayDate = firstMonday + 14;
    return new Date(year, month, thirdMondayDate);
}

// Calculate last Saturday of month
function getLastSaturday(year, month) {
    const d = new Date(year, month + 1, 0);
    const lastDayOfMonth = d.getDate();
    const dayOfWeek = d.getDay();
    const diff = (dayOfWeek - 6 + 7) % 7;
    return new Date(year, month, lastDayOfMonth - diff);
}
```

#### Accordion Height Management
```javascript
function updateParentAccordionHeight(element) {
    setTimeout(() => {
        let parent = element.parentElement;
        while (parent) {
            if (parent.classList.contains('accordion-content')) {
                const parentHeader = parent.previousElementSibling;
                if (parentHeader?.classList.contains('open')) {
                    parent.style.maxHeight = parent.scrollHeight + "px";
                }
            }
            parent = parent.parentElement;
        }
    }, 50);
}
```

### Notification System

#### Function
```javascript
function showNotification(message, type = 'info') {
    // Types: success, error, info, warning
    // Auto-dismisses after 5 seconds
    // Manual dismiss button
    // Positioned top-right
}
```

#### Usage Throughout App
- Form submissions
- Data save/delete operations
- Error messages
- Success confirmations
- Warning alerts

### Event Handling

#### Global Event Delegation
Uses event delegation on document.body for efficiency:
```javascript
document.body.addEventListener('click', (e) => {
    const accordionHeader = e.target.closest('.accordion-header');
    if (accordionHeader) {
        // Handle accordion toggle
    }
});
```

#### Specific Event Handlers
- Navigation clicks
- Modal open/close
- Form submissions
- Button clicks
- Keyboard events (Escape, Enter)
- Input changes (debounced)

### Local Storage Management

#### Storage Keys
- `rowlettAA_sobrietyDate`: Sobriety calculator date
- `rowlettAA_studyNotes`: Study guide notes array
- `rowlettAA_gratitudeList`: Gratitude items array
- `rowlettAA_pwaInstallDismissed`: PWA prompt dismissal

#### Error Handling
```javascript
try {
    localStorage.setItem(key, value);
} catch (error) {
    if (error.name === 'QuotaExceededError') {
        showNotification('Storage quota exceeded...', 'error');
    }
}
```

#### Data Persistence
All user data persists across sessions and survives page refreshes.

---

## CSS and Styling

### CSS Custom Properties

#### Color Scheme
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

#### Typography
- **Primary Font**: Inter (sans-serif) - modern, clean, highly readable
- **Serif Font**: Lora - for quotes, preamble, and literary content
- **Base Size**: Fluid sizing (clamp(14px, 0.5vw+12px, 18px))

### Responsive Design

#### Breakpoints
- **Mobile**: < 768px
- **Tablet**: 768px - 1023px
- **Desktop**: ≥ 1024px

#### Mobile Optimizations
- Hamburger navigation menu
- Stacked layouts
- Touch-friendly button sizes
- Simplified timeline layout
- Adjusted quick action button positioning

### Custom Scrollbar
```css
html {
    scrollbar-width: thin;
    scrollbar-color: var(--light-blue) var(--background-light);
}

::-webkit-scrollbar {
    width: 12px;
}

::-webkit-scrollbar-thumb {
    background-color: var(--light-blue);
    border-radius: 6px;
}
```

### Animations

#### Keyframe Animations
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

@keyframes pulse-subtle {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.95; }
}

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
```

#### Applied Animations
- Page content fade-in
- PWA banner slide-down
- Milestone pulse effect
- Button hover effects
- Timeline hover effects

### Navigation Styling

#### Active Link Indicator
```css
.nav-link::after {
    content: '';
    position: absolute;
    width: 0;
    height: 2px;
    background-color: var(--light-blue);
    transition: width 0.3s ease;
}

.nav-link:hover::after,
.nav-active::after {
    width: 100%;
}
```

### Timeline Component

#### Visual Design
- Vertical line down the center
- Alternating left/right blocks
- Circular markers at connection points
- Hover effects (scale, shadow, color change)
- Popup information boxes
- Color-coded by era

#### Responsive Behavior
On mobile (<768px):
- Single column layout
- Line moves to left side
- All blocks align left
- Markers stay with left line

### Highlight System

#### Color Categories
```css
.highlight-red { background-color: rgba(255, 159, 159, 0.4); }
.highlight-blue { background-color: rgba(159, 197, 255, 0.4); }
.highlight-green { background-color: rgba(168, 255, 159, 0.4); }
.highlight-yellow { background-color: rgba(255, 251, 159, 0.5); }
.highlight-purple { background-color: rgba(210, 159, 255, 0.4); }
```

#### Underline Styles
```css
.wavy-underline {
    text-decoration: wavy underline;
    text-decoration-color: #ef4444;
}

.green-underline {
    text-decoration: underline;
    text-decoration-color: #22c55e;
}
```

### Tooltip System

#### Structure
```css
.has-tooltip {
    position: relative;
    cursor: help;
}

.tooltip {
    visibility: hidden;
    opacity: 0;
    position: absolute;
    bottom: 125%;
    left: 50%;
    transform: translateX(-50%);
    /* ... styling ... */
}

.has-tooltip:hover .tooltip {
    visibility: visible;
    opacity: 1;
}
```

### Accessibility Classes

#### Screen Reader Only
```css
.sr-only {
    position: absolute;
    width: 1px;
    height: 1px;
    padding: 0;
    margin: -1px;
    overflow: hidden;
    clip: rect(0, 0, 0, 0);
}

.sr-only:focus {
    /* Becomes visible when focused */
    position: static;
    width: auto;
    height: auto;
    /* ... */
}
```

---

## SEO and Accessibility

### Search Engine Optimization

#### Meta Tags
```html
<title>Rowlett Group of AA | Alcoholics Anonymous Meetings in Garland, TX</title>
<meta name="description" content="Find free AA meetings in Garland, TX...">
<meta name="keywords" content="AA, Alcoholics Anonymous, Rowlett Group...">
<link rel="canonical" href="https://www.rowlettaa.org/">
```

#### Open Graph (Facebook/Social Media)
```html
<meta property="og:type" content="website">
<meta property="og:title" content="Rowlett Group of AA...">
<meta property="og:description" content="...">
<meta property="og:image" content="[logo URL]">
<meta property="og:url" content="https://www.rowlettaa.org/">
```

#### Twitter Cards
```html
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="...">
<meta name="twitter:description" content="...">
<meta name="twitter:image" content="...">
```

#### Geographic Metadata
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
    "contactType": "support",
    "email": "rowlettaa@gmail.com"
  }
}
```

#### FAQ Schema
Structured data for common questions helps Google display rich snippets.

#### LocalBusiness Schema
```json
{
  "@type": "LocalBusiness",
  "name": "Rowlett Group of AA",
  "address": { ... },
  "telephone": "972-925-0096",
  "priceRange": "Free",
  "openingHoursSpecification": [ ... ]
}
```

#### Event Schema
30th Anniversary event structured data for Google event listings.

#### Schedule Schema
Meeting schedule structured data for better search visibility.

#### BreadcrumbList Schema
Helps search engines understand site structure.

### Accessibility Features

#### ARIA Labels
```html
<button aria-label="Open Menu">...</button>
<iframe title="Map showing location of Rowlett Group">...</iframe>
<span class="sr-only">Crisis Resources</span>
```

#### Landmark Roles
```html
<main id="main-content">
<nav>
<footer>
```

#### Skip Navigation
```html
<a href="#main-content" class="sr-only">Skip to main content</a>
```

#### Focus Management
- Logical tab order
- Visible focus indicators
- Focus trap in modals
- Return focus after modal close

#### Semantic HTML
- Proper heading hierarchy (h1 → h2 → h3)
- Lists for navigation and content
- Buttons for actions, links for navigation
- Form labels associated with inputs

#### Color Contrast
All text meets WCAG AA standards:
- Large text: 3:1 minimum
- Normal text: 4.5:1 minimum
- Active elements: clearly distinguishable

#### Keyboard Navigation
- All interactive elements accessible via keyboard
- Escape key closes modals
- Enter key submits forms
- Tab key moves through elements logically

#### Screen Reader Compatibility
- ARIA live regions for notifications
- Hidden decorative elements (aria-hidden="true")
- Descriptive link text
- Form error announcements

---

## Content Management

### How to Update Meeting Schedule

**Location**: Find the `meetingSchedule` array in `initSchedulePage` function

```javascript
const meetingSchedule = [
    {
        day: "Sunday",
        dayIndex: 0,
        meetings: [
            {
                time: "11:00 AM",
                type: "open",
                name: "Discussion Meeting"
            }
        ]
    },
    // ... more days
];
```

**Steps to Add/Modify Meetings**:
1. Locate the day object
2. Add to the `meetings` array
3. Include: `time`, `type` (open/closed), `name`
4. Optionally add `note` field for special instructions

### How to Update Special Events

**Location**: Find the `specialEvents` array in `initSchedulePage` function

```javascript
const specialEvents = [
    {
        date: '2025-07-26',
        title: 'Event Name',
        time: '5:00 PM',
        location: 'Venue Name<br>Address',
        speaker: 'Speaker Name (optional)',
        bgColor: 'bg-yellow-50',
        borderColor: 'border-yellow-400',
        textColor: 'text-yellow-900'
    }
];
```

**For Recurring Events**:
```javascript
{
    date: 'recurring-last-saturday',
    timeParts: { '6:30 PM': 'Potluck', '7:30 PM': 'Celebration' },
    // ... rest of properties
}
```

### How to Update Contact Information

**Phone Number**: Search for `972-925-0096` and update all instances
**Email**: Search for `rowlettaa@gmail.com` and update
**Address**: Search for `362 Oaks Trail #162` and update

**Important**: Also update:
- Meta tags in head
- Schema.org structured data
- Footer contact section
- Contact page details

### How to Update Literature Videos

**Location**: Find the literature data arrays in `initLiteraturePage` function

```javascript
const bigBookVideos = [
    {
        title: "Video Title",
        url: "https://www.youtube.com/embed/VIDEO_ID"
    }
];
```

**Steps**:
1. Get YouTube video URL
2. Convert to embed format: `youtube.com/embed/VIDEO_ID`
3. Add to appropriate array (`bigBookVideos` or `ttVideos`)
4. Video will automatically appear in the grid

### How to Update Group History

**Location**: `initOurGroupPage` function, within the `blogPostHTML` string

**Structure**: Timeline blocks alternate between left and right
```html
<div class="timeline-block left">
    <div class="timeline-content bg-[color]-50">
        <div class="info-popup">
            <h4>Popup Title</h4>
            <p>Additional details...</p>
        </div>
        <h2>Main Heading</h2>
        <p>Description...</p>
    </div>
</div>
```

**Color Themes Available**:
- `bg-blue-50` with `text-blue-800`
- `bg-green-50` with `text-green-800`
- `bg-amber-50` with `text-amber-800`
- `bg-red-50` with `text-red-800`
- `bg-indigo-50` with `text-indigo-800`
- `bg-purple-50` with `text-purple-800`

### How to Update Service Opportunities

**Location**: `initGetInvolvedPage` function

**Magdalen House Dates**: Automatically calculated, but initial data structure:
```javascript
const magdalenDates = calculateMagdalenDates();
// Calculates next 8 instances of bi-weekly Tuesday meetings
```

**To Add New Facility**:
1. Find the facility section HTML
2. Copy an existing facility block
3. Update: name, address, website, phone, meeting details
4. Adjust border color class: `border-t-4 border-[color]-500`

### How to Modify Study Guide Content

**Color Coding Table**: In `study-guide-page` section
- Edit the table rows to add/remove categories
- Update color classes and descriptions

**Annotation Key**: Same section
- Modify table to add new annotation types
- Update examples and purposes

**Sample Page**: Hardcoded example in HTML
- Update text content to show different passages
- Adjust highlighting classes

### How to Update Sobriety Milestones

**Location**: `initResourcesPage` function, `milestones` array

```javascript
const milestones = [
    {
        days: 1,
        name: '24 Hours',
        icon: '🌟',
        color: 'from-yellow-400 to-orange-400'
    },
    // ... more milestones
];
```

**To Add Milestone**:
1. Insert object in correct chronological order
2. Specify days (total days)
3. Add emoji icon
4. Choose Tailwind gradient colors

### How to Update Footer Resources

**Location**: Footer section near end of HTML

```html
<div class="grid grid-cols-1 md:grid-cols-3 gap-8">
    <div class="p-6 bg-white rounded-lg shadow-md">
        <h3>Resource Name</h3>
        <p>Description</p>
        <a href="URL">Link text →</a>
    </div>
</div>
```

### How to Update PWA Settings

**Service Worker Cache**: In `initServiceWorker` function
```javascript
const CACHE_NAME = 'rowlett-aa-cache-v2'; // Increment version
const URLS_TO_CACHE = ['/', '/index.html']; // Add more URLs
```

**Manifest Data**: Base64 encoded in head section
- Decode the base64 string
- Modify JSON
- Re-encode to base64
- Replace in link tag

---

## Testing Guidelines

### Pre-Deployment Checklist

#### Visual Testing
- [ ] Test on multiple screen sizes (mobile, tablet, desktop)
- [ ] Verify all images load correctly
- [ ] Check all colors and contrast
- [ ] Ensure fonts load properly
- [ ] Verify spacing and alignment
- [ ] Check for text overflow issues

#### Functional Testing
- [ ] Test all navigation links
- [ ] Verify hash routing works
- [ ] Test mobile menu open/close
- [ ] Verify all accordions expand/collapse
- [ ] Test modal open/close (search, crisis, video)
- [ ] Check quick action buttons
- [ ] Test all form submissions

#### Feature-Specific Testing

**Schedule Page**:
- [ ] Verify today's meetings display correctly
- [ ] Test meeting type filters
- [ ] Check special event dates calculate correctly
- [ ] Verify Group Conscience date is correct
- [ ] Test Zoom link functionality
- [ ] Verify map link works

**Resources Page**:
- [ ] Test sobriety calculator with various dates
- [ ] Verify milestones calculate correctly
- [ ] Test HALT check selections
- [ ] Test meditation timer start/stop
- [ ] Add/edit/delete gratitude items
- [ ] Verify localStorage persistence

**Study Guide**:
- [ ] Test dictionary lookup (online)
- [ ] Verify offline message (offline)
- [ ] Create/edit/delete notes
- [ ] Test note search functionality
- [ ] Verify localStorage persistence

**Literature Page**:
- [ ] Test all accordion sections
- [ ] Switch between Read and Watch tabs
- [ ] Test video modal open/close
- [ ] Verify YouTube videos load
- [ ] Test external link to Daily Reflection

**Search System**:
- [ ] Test search with various queries
- [ ] Verify debouncing (no immediate search)
- [ ] Check result relevance
- [ ] Test clicking search results

**PWA Features**:
- [ ] Test install prompt (if available)
- [ ] Verify service worker registration
- [ ] Test offline functionality
- [ ] Check dismissal persistence

#### Accessibility Testing
- [ ] Navigate site using only keyboard
- [ ] Test with screen reader (NVDA, JAWS, VoiceOver)
- [ ] Verify all images have alt text
- [ ] Check color contrast ratios
- [ ] Test skip navigation link
- [ ] Verify form labels
- [ ] Check ARIA attributes

#### Performance Testing
- [ ] Test initial page load time
- [ ] Check page size (should be reasonable despite single file)
- [ ] Test on slow 3G connection
- [ ] Verify lazy loading of page content
- [ ] Check for console errors
- [ ] Test memory usage (Developer Tools)

#### Browser Testing
- [ ] Chrome/Edge (latest)
- [ ] Firefox (latest)
- [ ] Safari (latest, iOS and macOS)
- [ ] Samsung Internet (Android)
- [ ] Check browser console for errors

#### Data Persistence Testing
- [ ] Add data (sobriety date, notes, gratitude)
- [ ] Refresh page
- [ ] Verify data persists
- [ ] Test localStorage quota handling
- [ ] Test with localStorage disabled

#### Error Handling
- [ ] Test dictionary lookup with invalid words
- [ ] Test with no internet connection
- [ ] Test with full localStorage
- [ ] Test form validation
- [ ] Verify error messages display

### Common Issues to Check

#### Typography
- Check for orphaned text
- Verify proper line height
- Ensure readable font sizes on mobile
- Check for text overflow in containers

#### Layout
- Verify no horizontal scrolling on mobile
- Check grid/flex alignment
- Ensure proper spacing between sections
- Verify footer stays at bottom

#### Interactive Elements
- Ensure buttons have hover states
- Verify touch targets are large enough (mobile)
- Check for proper focus indicators
- Ensure disabled states are visible

#### Content
- Verify phone numbers are clickable (tel: links)
- Check email links work (mailto:)
- Ensure external links open in new tabs
- Verify all dates display correctly

---

## Deployment Instructions

### Prerequisites
- Web server with HTTPS (required for PWA and service workers)
- Domain name (optional but recommended)
- FTP/SFTP access or Git deployment

### Deployment Steps

#### Option 1: Simple File Upload (FTP/SFTP)
1. **Prepare the file**:
   - Ensure `index.html` is the final version
   - Verify all content is updated
   - Test locally

2. **Upload**:
   - Connect to web server via FTP/SFTP
   - Upload `index.html` to web root (usually `public_html` or `www`)
   - Ensure file is named `index.html` (case-sensitive on Linux)

3. **Set permissions**:
   - File permission: 644 (readable by web server)
   - Directory permission: 755

4. **Verify**:
   - Visit website URL
   - Test all functionality
   - Check HTTPS is working

#### Option 2: Static Site Hosting (Recommended)

**GitHub Pages**:
1. Create GitHub repository
2. Push `index.html` to repository
3. Enable GitHub Pages in repository settings
4. Set custom domain (optional)
5. HTTPS is automatic

**Netlify**:
1. Create Netlify account
2. Drag and drop `index.html` (or connect Git)
3. Site deploys automatically
4. Set custom domain (optional)
5. HTTPS is automatic
6. Benefit: Form handling, analytics, redirects

**Vercel**:
1. Create Vercel account
2. Import project (Git or direct upload)
3. Deploy with one click
4. Set custom domain (optional)
5. HTTPS is automatic

**Cloudflare Pages**:
1. Create Cloudflare account
2. Create new Pages project
3. Upload `index.html` or connect Git
4. Deploy automatically
5. HTTPS is automatic
6. Benefit: CDN, DDoS protection

#### Option 3: Traditional Web Hosting
1. Choose hosting provider (Bluehost, HostGator, SiteGround, etc.)
2. Set up hosting account
3. Point domain to hosting server
4. Upload `index.html` via cPanel, FTP, or hosting dashboard
5. Enable HTTPS (Let's Encrypt usually free)

### Post-Deployment Configuration

#### SSL/HTTPS Setup
**Why needed**: Required for PWA, service workers, geolocation

**Setup**:
- Most modern hosts offer free Let's Encrypt certificates
- Enable in hosting control panel
- Set up automatic renewal
- Redirect HTTP to HTTPS

#### Domain Configuration
1. Point domain to hosting/service
2. Set up DNS records:
   - A record for root domain
   - CNAME for www subdomain
3. Wait for DNS propagation (up to 48 hours)

#### Service Worker Considerations
- Service worker only works over HTTPS (or localhost)
- Service worker caches the specified URLs
- Update cache version when deploying changes
- Clear browser cache after major updates

### Environment-Specific Updates

#### Production URL Updates
Search and replace throughout `index.html`:
- `https://www.rowlettaa.org/` → Your actual domain
- Update canonical link
- Update Open Graph URLs
- Update schema.org URLs
- Update sitemap reference

#### Analytics Setup (Optional)
Add Google Analytics or similar:
```html
<!-- Add before closing </head> tag -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_ID');
</script>
```

#### Sitemap Creation
Create `sitemap.xml`:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://www.rowlettaa.org/</loc>
    <lastmod>2025-01-15</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://www.rowlettaa.org/#schedule</loc>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <!-- Add more pages -->
</urlset>
```

#### Robots.txt
Create `robots.txt`:
```
User-agent: *
Allow: /
Sitemap: https://www.rowlettaa.org/sitemap.xml
```

### Performance Optimization

#### Before Deployment
1. **Minify CSS and JavaScript** (optional, reduces file size):
   - Extract inline styles and scripts
   - Minify using tools like cssnano, UglifyJS
   - Re-embed into HTML

2. **Optimize Images**:
   - All images are external URLs (Google Photos, Unsplash)
   - No local image optimization needed

3. **Enable Compression**:
   - Gzip or Brotli compression on server
   - Configure via .htaccess (Apache) or hosting settings

#### .htaccess Configuration (Apache)
```apache
# Enable Gzip compression
<IfModule mod_deflate.c>
  AddOutputFilterByType DEFLATE text/html text/plain text/xml text/css text/javascript application/javascript application/json
</IfModule>

# Browser caching
<IfModule mod_expires.c>
  ExpiresActive On
  ExpiresByType text/html "access plus 1 hour"
  ExpiresByType text/css "access plus 1 month"
  ExpiresByType application/javascript "access plus 1 month"
</IfModule>

# Force HTTPS
RewriteEngine On
RewriteCond %{HTTPS} off
RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
```

### Update Procedures

#### For Content Updates
1. Modify `index.html` locally
2. Test changes locally (open in browser)
3. Upload updated file to server
4. Clear browser cache to see changes
5. Verify changes on live site

#### For Service Worker Updates
1. Update cache version: `rowlett-aa-cache-v2` → `v3`
2. Deploy updated file
3. Service worker will automatically update on next visit
4. Users may need to refresh twice to see changes

#### For Emergency Updates
1. Make changes to live file directly (if urgent)
2. Update local copy to match
3. Document changes for version control

### Monitoring

#### What to Monitor
- Uptime (use service like UptimeRobot)
- Page load speed (Google PageSpeed Insights)
- Broken links (check quarterly)
- SSL certificate expiration
- Form submissions (if using external service)

#### Search Engine Monitoring
- Google Search Console (submit sitemap, check indexing)
- Google Analytics (track visitors)
- Check search rankings for key terms

---

## Browser Compatibility

### Supported Browsers

#### Fully Supported (Latest Versions)
- ✅ Chrome 90+
- ✅ Edge 90+
- ✅ Firefox 88+
- ✅ Safari 14+
- ✅ Opera 76+
- ✅ Samsung Internet 14+

#### Mobile Browsers
- ✅ Chrome Mobile (Android)
- ✅ Safari Mobile (iOS 14+)
- ✅ Firefox Mobile
- ✅ Samsung Internet

### Feature Compatibility

#### Modern JavaScript (ES6+)
- Arrow functions
- Template literals
- Const/let declarations
- Async/await
- Fetch API
- Spread operator

**Compatibility**: All modern browsers (IE not supported)

#### CSS Features
- CSS Custom Properties (variables)
- Flexbox
- Grid Layout
- CSS Transitions/Animations
- Backdrop Filter
- Clip Path

**Compatibility**: All modern browsers

#### HTML5 Features
- Semantic elements (header, nav, main, footer)
- Form input types (date, email, tel)
- Local Storage
- Service Workers

**Compatibility**: All modern browsers

### Browser-Specific Considerations

#### Safari Quirks
- Service Worker support since Safari 11.1
- Date input displays differently (native picker)
- Smooth scrolling may behave differently
- Font rendering variations

**Testing**: Always test on real iOS devices

#### Firefox Quirks
- Custom scrollbar styles (use `scrollbar-width` property)
- Some CSS vendor prefixes needed for older versions
- Date picker styling differs

#### Mobile Considerations
- Touch events vs. mouse events (handled automatically)
- Virtual keyboard affects viewport height
- Orientation changes need testing
- Network connectivity varies (test on slow connections)

### Polyfills and Fallbacks

#### Service Worker
```javascript
if ('serviceWorker' in navigator) {
    // Register service worker
} else {
    // Graceful degradation - site still works without offline support
}
```

#### LocalStorage
```javascript
try {
    localStorage.setItem(key, value);
} catch (error) {
    // Fallback: site works, just doesn't persist data
    console.warn('localStorage not available');
}
```

#### Fetch API
No polyfill included. Feature detection:
```javascript
if (!navigator.onLine) {
    // Show offline message
}
```

### Known Limitations

#### Internet Explorer
**Not Supported**. Reasons:
- Requires ES6+ JavaScript
- Uses CSS Custom Properties
- No Fetch API polyfill
- IE end of life (June 2022)

#### Old Mobile Browsers
- Android Browser < 5.0: Limited support
- iOS Safari < 12: Limited support

#### Progressive Enhancement
Site follows progressive enhancement:
1. **Basic Level**: Content is accessible, navigation works
2. **Enhanced Level**: Animations, accordions, advanced styling
3. **Full Experience**: PWA installation, service worker, all features

### Testing Recommendations

#### Browser Testing Tools
- **BrowserStack**: Test on multiple browsers/devices
- **LambdaTest**: Real-time cross-browser testing
- **Chrome DevTools**: Device emulation
- **Firefox Developer Tools**: Responsive design mode

#### Manual Testing Checklist
- [ ] Desktop: Chrome, Firefox, Safari, Edge
- [ ] Mobile: iOS Safari, Chrome Android
- [ ] Tablet: iPad Safari, Android Chrome
- [ ] Different screen sizes
- [ ] Portrait and landscape orientations

---

## Developer Guide

### Getting Started

#### Setting Up Development Environment
1. **Code Editor**: VS Code, Sublime Text, or similar
2. **Extensions** (VS Code):
   - Live Server (for local testing)
   - HTML CSS Support
   - JavaScript (ES6) code snippets
   - Prettier (code formatting)

3. **Local Testing**:
   - Open `index.html` directly in browser, OR
   - Use Live Server extension for live reload

#### Understanding the Codebase

**Single File Structure**: Everything is in one HTML file
- **Lines 1-835**: Head section (meta, styles, schemas)
- **Lines 836-2123**: Body structure (header, sections, footer)
- **Lines 2124-3968**: JavaScript (main app logic)
- **Lines 3969-4001**: Notification system

### Code Organization

#### Section Markers
Use comments to find sections:
```javascript
// Main app initialization
app.init()

// Schedule page initialization
initSchedulePage()

// Resources page initialization
initResourcesPage()
```

#### Naming Conventions
- **Variables**: camelCase (`sobrietyDate`, `meditationTime`)
- **Functions**: camelCase (`calculateDaysSober`, `renderNotes`)
- **CSS Classes**: kebab-case (`nav-link`, `meeting-item`)
- **IDs**: kebab-case (`sobriety-date`, `search-modal`)

### Common Modifications

#### Adding a New Page

1. **Create HTML Section**:
```html
<section id="new-page-page" class="page-content hidden">
    <div class="container mx-auto px-4 sm:px-6 py-12 sm:py-16">
        <h1>New Page Title</h1>
        <!-- Page content -->
    </div>
</section>
```

2. **Add Navigation Link**:
```html
<!-- Desktop nav -->
<a href="#new-page" class="nav-link text-gray-600">New Page</a>

<!-- Mobile nav -->
<a href="#new-page" class="nav-link block py-3 px-4">New Page</a>
```

3. **Add Initialization Function**:
```javascript
initNewPagePage: function() {
    if (this.initialized.newPage) return;

    // Initialization code here

    this.initialized.newPage = true;
}
```

4. **Call in showPage**:
```javascript
showPage: function(pageId) {
    // ... existing code
    if (pageId === 'new-page-page') this.initNewPagePage();
}
```

5. **Add to Search Data**:
```javascript
searchData: {
    pages: [
        // ... existing pages
        {
            title: "New Page",
            hash: "#new-page",
            keywords: ["keyword1", "keyword2", "..."]
        }
    ]
}
```

#### Adding a New Modal

1. **Create Modal HTML**:
```html
<div id="new-modal" class="fixed inset-0 bg-black bg-opacity-50 z-50 hidden items-center justify-center p-4">
    <div class="bg-white rounded-lg shadow-2xl max-w-2xl w-full">
        <div class="p-6 border-b">
            <div class="flex justify-between items-center">
                <h2 class="text-2xl font-bold">Modal Title</h2>
                <button type="button" id="close-new-modal" class="text-gray-500 hover:text-gray-700">
                    <i class="fas fa-times text-2xl"></i>
                </button>
            </div>
        </div>
        <div class="p-6">
            <!-- Modal content -->
        </div>
    </div>
</div>
```

2. **Add Trigger Button**:
```html
<button type="button" id="new-modal-btn" class="bg-blue-600 text-white px-4 py-2 rounded">
    Open Modal
</button>
```

3. **Initialize Modal**:
```javascript
initModals: function() {
    // ... existing modals
    this.setupModal('new-modal-btn', 'new-modal', 'close-new-modal');
}
```

#### Adding a New Feature to Existing Page

Example: Adding a new tool to Resources page

1. **Design HTML Structure**:
```html
<div class="bg-gradient-to-br from-blue-50 to-indigo-50 rounded-lg shadow-lg p-8 border border-blue-200">
    <h2 class="text-3xl font-bold text-blue-800 mb-4">New Tool</h2>
    <p class="text-gray-700 mb-6">Description of the tool</p>

    <!-- Tool interface -->
    <div class="max-w-md mx-auto">
        <input type="text" id="new-tool-input" class="w-full px-4 py-2 border rounded">
        <button type="button" id="new-tool-btn" class="bg-blue-600 text-white px-6 py-2 rounded">
            Submit
        </button>
    </div>

    <!-- Results area -->
    <div id="new-tool-results" class="mt-4"></div>
</div>
```

2. **Add JavaScript Logic**:
```javascript
initResourcesPage: function() {
    // ... existing code

    // New tool initialization
    const newToolInput = document.getElementById('new-tool-input');
    const newToolBtn = document.getElementById('new-tool-btn');
    const newToolResults = document.getElementById('new-tool-results');

    if (newToolBtn && newToolInput && newToolResults) {
        newToolBtn.addEventListener('click', () => {
            const value = newToolInput.value.trim();
            if (!value) {
                showNotification('Please enter a value', 'warning');
                return;
            }

            // Process and display results
            const result = processNewTool(value);
            newToolResults.innerHTML = result;
            showNotification('Success!', 'success');
        });
    }

    // ... rest of initialization
}
```

3. **Add Helper Function**:
```javascript
const processNewTool = (value) => {
    // Processing logic
    return `<p>Result: ${value}</p>`;
};
```

### Debugging Tips

#### Console Logging
```javascript
// Add strategic console.logs
console.log('Schedule initialized:', this.initialized.schedule);
console.log('Sobriety date:', loadSobrietyDate());
console.log('Search results:', results);
```

#### Common Issues

**Page not showing**:
- Check if section has correct ID format: `[name]-page`
- Verify `hidden` class is toggled correctly
- Check console for JavaScript errors

**Data not persisting**:
- Check localStorage is available (not in private/incognito mode)
- Verify try-catch blocks are handling errors
- Check for QuotaExceededError

**Modal not opening**:
- Verify IDs match in HTML and JavaScript
- Check if modal setup is called in `initModals`
- Ensure z-index is high enough (50+)

**Accordion not working**:
- Check if element has correct class: `.accordion-header` or `.main-accordion-header`
- Verify corresponding content has: `.accordion-content` or `.main-accordion-content`
- Check for JavaScript errors preventing event delegation

**Service Worker not updating**:
- Increment cache version number
- Force refresh (Ctrl+Shift+R or Cmd+Shift+R)
- Check Application tab in DevTools → Service Workers
- Click "Unregister" and refresh

### Best Practices

#### Code Style
- Use consistent indentation (2 or 4 spaces)
- Add comments for complex logic
- Keep functions small and focused
- Use descriptive variable names

#### Performance
- Avoid DOM queries in loops
- Cache element references
- Use event delegation for dynamic content
- Debounce frequent events (scroll, input)

#### Accessibility
- Always add ARIA labels to buttons without text
- Provide text alternatives for icons
- Maintain logical heading hierarchy
- Test with keyboard navigation

#### Maintenance
- Document all major changes
- Keep a changelog
- Test thoroughly before deployment
- Back up working version before major changes

### Version Control (Optional)

#### Git Setup
```bash
git init
git add index.html
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/username/rowlett-aa.git
git push -u origin main
```

#### Commit Messages
Use clear, descriptive messages:
- `feat: Add sobriety calculator`
- `fix: Correct schedule date calculation`
- `style: Update color scheme`
- `docs: Update README with deployment instructions`
- `refactor: Simplify accordion logic`

### Resources

#### Documentation
- [MDN Web Docs](https://developer.mozilla.org/): HTML, CSS, JavaScript reference
- [Tailwind CSS Docs](https://tailwindcss.com/docs): Utility classes
- [Font Awesome Icons](https://fontawesome.com/icons): Icon reference
- [Schema.org](https://schema.org/): Structured data

#### Testing Tools
- [Chrome DevTools](https://developer.chrome.com/docs/devtools/): Debug and test
- [Lighthouse](https://developers.google.com/web/tools/lighthouse): Performance audit
- [WAVE](https://wave.webaim.org/): Accessibility checker
- [PageSpeed Insights](https://pagespeed.web.dev/): Performance testing

#### Design Resources
- [Can I Use](https://caniuse.com/): Browser compatibility
- [Color Contrast Checker](https://webaim.org/resources/contrastchecker/): WCAG compliance
- [TinyPNG](https://tinypng.com/): Image optimization (if adding images)

---

## Changelog

### Version 1.0 (Current)
- Complete single-page application
- 9 main pages with comprehensive content
- Progressive Web App capabilities
- Full localStorage integration
- Interactive recovery tools
- Video literature library
- Study guide with dictionary and notes
- Timeline-based group history
- Crisis resources quick access
- Search functionality
- Mobile-responsive design
- Full accessibility support

### Future Enhancements (Potential)

#### Planned Features
- User accounts (optional authentication)
- Online meeting attendance tracking
- Downloadable literature PDFs
- Print-friendly meeting schedule
- Audio versions of literature
- Spanish language version
- Prayer/meditation library
- Meeting location finder (nearby groups)
- Event calendar with reminders
- Step working guide
- Sponsorship matching tool

#### Technical Improvements
- Service worker caching for external resources
- Offline dictionary (indexed DB)
- Push notifications for meetings
- Better mobile app experience
- Performance optimizations
- Automated testing
- Content Management System integration

---

## Support and Contact

### For Website Issues
- **Technical Support**: Contact website developer at Info@Manpasand.com
- **Content Updates**: Contact Rowlett Group directly

### For A.A. Related Questions
- **Rowlett Group**: (972) 925-0096
- **Email**: rowlettaa@gmail.com
- **Dallas AA Intergroup**: (214) 887-6699
- **National A.A.**: https://www.aa.org/

### For Emergencies
- **National Suicide Prevention Lifeline**: 988
- **Crisis Text Line**: Text HELLO to 741741
- **Emergency Services**: 911

---

## License and Copyright

### Website Copyright
© 2025 Rowlett Group of AA. All Rights Reserved.

### A.A. Literature Copyright
All Alcoholics Anonymous literature, including:
- The Big Book (Alcoholics Anonymous)
- Twelve Steps and Twelve Traditions
- The Preamble
- The Twelve Promises
- The Twelve Traditions

Copyright © Alcoholics Anonymous World Services, Inc.
Reproduced with permission.

### Third-Party Resources
- **Tailwind CSS**: MIT License
- **Font Awesome**: Font Awesome Free License
- **Google Fonts**: Open Font License
- **Dictionary API**: Free for non-commercial use

---

## Acknowledgments

### Development
- Designed & Developed by: Info@Manpasand.com
- Built with love and dedication to support recovery

### A.A. Community
- Rowlett Group members past and present
- Dallas AA Intergroup
- Alcoholics Anonymous World Services

### Recovery Resources
Special thanks to all those who contribute to making A.A. resources available online and to everyone working to help the still-suffering alcoholic.

---

## Appendix

### Keyboard Shortcuts
- **Tab**: Navigate between interactive elements
- **Enter**: Activate buttons, submit forms
- **Escape**: Close modals
- **Ctrl/Cmd + F**: Find on page (browser default)

### localStorage Keys Reference
```javascript
{
    'rowlettAA_sobrietyDate': 'ISO date string',
    'rowlettAA_studyNotes': '[{id, content, created, edited}, ...]',
    'rowlettAA_gratitudeList': '[{id, content, created}, ...]',
    'rowlettAA_pwaInstallDismissed': 'true/false'
}
```

### Color Palette
```css
Primary Blue:     #1e40af
Light Blue:       #3b82f6
Pale Blue:        #eff6ff
Text Dark:        #1f2937
Text Light:       #4b5563
Background Light: #f9fafb
Border:           #e5e7eb

Success Green:    #22c55e
Warning Yellow:   #eab308
Error Red:        #ef4444
Info Blue:        #3b82f6
```

### Contact Information Quick Reference
- **Phone**: (972) 925-0096
- **Email**: rowlettaa@gmail.com
- **Address**: 362 Oaks Trail #162, Garland, TX 75043
- **Zoom ID**: 890 3935 7234
- **Zoom Password**: freedom
- **Website**: https://www.rowlettaa.org/

### External Links
- [AA.org](https://www.aa.org/) - Official A.A. Website
- [AA Dallas](https://www.aadallas.org/) - Dallas Intergroup
- [NETA 65](https://neta65.org/) - Northeast Texas Area 65
- [Al-Anon](https://al-anon.org/) - For families and friends

---

**Document Version**: 1.0
**Last Updated**: January 2025
**Maintained By**: Rowlett Group Web Team

For questions or updates to this documentation, please contact Info@Manpasand.com
