# 📚 Daily Reflections JSON - How to Use Guide

## Table of Contents
1. [File Structure](#file-structure)
2. [Quick Start](#quick-start)
3. [Frontend Implementation](#frontend-implementation)
4. [Backend Implementation](#backend-implementation)
5. [Database Integration](#database-integration)
6. [Search Functionality](#search-functionality)
7. [Display Formatting](#display-formatting)
8. [Mobile App Integration](#mobile-app-integration)
9. [API Development](#api-development)
10. [Best Practices](#best-practices)
11. [Troubleshooting](#troubleshooting)

---

## File Structure

### JSON Schema
```json
{
  "metadata": {
    "title": "Daily Reflections - Alcoholics Anonymous",
    "description": "A book of reflections by A.A. members for A.A. members",
    "totalEntries": 366,
    "generatedDate": "2025-11-20",
    "version": "9.0 - FINAL COMPLETE",
    "source": "Daily Reflections: A Book of Reflections by A.A. Members for A.A. Members",
    "copyright": "© 1990 by Alcoholics Anonymous World Services, Inc."
  },
  "reflections": [
    {
      "month": "January",
      "monthNumber": 1,
      "day": 1,
      "dateKey": "01-01",
      "dayOfYear": 1,
      "title": ""I AM A MIRACLE"",
      "quote": [
        "First paragraph of quote",
        "Second paragraph if exists"
      ],
      "source": {
        "book": "ALCOHOLICS ANONYMOUS",
        "pages": "25"
      },
      "reflection": [
        "First paragraph of reflection",
        "Second paragraph if exists"
      ],
      "metadata": {
        "hasEllipsis": false,
        "hasEmDash": false,
        "quoteLength": 44,
        "reflectionLength": 75
      }
    }
  ]
}
```

### Key Fields Explained
- **dateKey**: "MM-DD" format for easy date matching
- **dayOfYear**: 1-366 for sequential access
- **quote/reflection**: Arrays of paragraphs (not single strings with \n)
- **metadata**: Additional info for filtering/searching

---

## Quick Start

### 1. Load the JSON File

#### JavaScript/Node.js
```javascript
const dailyReflections = require('./ALL366DR.json');
```

#### Python
```python
import json

with open('ALL366DR.json', 'r', encoding='utf-8') as f:
    daily_reflections = json.load(f)
```

#### PHP
```php
$dailyReflections = json_decode(
    file_get_contents('ALL366DR.json'), 
    true
);
```

### 2. Get Today's Reflection

#### JavaScript
```javascript
function getTodaysReflection() {
  const today = new Date();
  const month = String(today.getMonth() + 1).padStart(2, '0');
  const day = String(today.getDate()).padStart(2, '0');
  const dateKey = `${month}-${day}`;
  
  return dailyReflections.reflections.find(r => r.dateKey === dateKey);
}

const todaysReflection = getTodaysReflection();
console.log(todaysReflection.title);
```

#### Python
```python
from datetime import datetime

def get_todays_reflection():
    today = datetime.now()
    date_key = f"{today.month:02d}-{today.day:02d}"
    
    for reflection in daily_reflections['reflections']:
        if reflection['dateKey'] == date_key:
            return reflection
    return None

todays_reflection = get_todays_reflection()
print(todays_reflection['title'])
```

---

## Frontend Implementation

### Vanilla JavaScript
```html
<!DOCTYPE html>
<html>
<head>
    <title>Daily Reflection</title>
    <style>
        .reflection-container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            font-family: Georgia, serif;
        }
        .date { color: #666; }
        .title { 
            font-size: 24px; 
            font-weight: bold;
            margin: 20px 0;
        }
        .quote {
            font-style: italic;
            background: #f5f5f5;
            padding: 20px;
            margin: 20px 0;
            border-left: 4px solid #333;
        }
        .source {
            text-align: right;
            color: #666;
            margin-top: 10px;
        }
        .reflection {
            line-height: 1.6;
        }
        .reflection p {
            margin-bottom: 15px;
        }
    </style>
</head>
<body>
    <div class="reflection-container" id="reflection"></div>
    
    <script>
        async function loadReflection() {
            const response = await fetch('ALL366DR.json');
            const data = await response.json();
            
            // Get today's reflection
            const today = new Date();
            const dateKey = `${String(today.getMonth() + 1).padStart(2, '0')}-${String(today.getDate()).padStart(2, '0')}`;
            const reflection = data.reflections.find(r => r.dateKey === dateKey);
            
            // Display it
            const container = document.getElementById('reflection');
            container.innerHTML = `
                <div class="date">${reflection.month} ${reflection.day}</div>
                <h1 class="title">${reflection.title}</h1>
                
                <div class="quote">
                    ${reflection.quote.map(p => `<p>${p}</p>`).join('')}
                    <div class="source">
                        — ${reflection.source.book}${reflection.source.pages ? `, p. ${reflection.source.pages}` : ''}
                    </div>
                </div>
                
                <div class="reflection">
                    ${reflection.reflection.map(p => `<p>${p}</p>`).join('')}
                </div>
            `;
        }
        
        loadReflection();
    </script>
</body>
</html>
```

### React Component
```jsx
import React, { useState, useEffect } from 'react';
import dailyReflections from './ALL366DR.json';

function DailyReflection() {
  const [reflection, setReflection] = useState(null);
  const [selectedDate, setSelectedDate] = useState(new Date());

  useEffect(() => {
    const month = String(selectedDate.getMonth() + 1).padStart(2, '0');
    const day = String(selectedDate.getDate()).padStart(2, '0');
    const dateKey = `${month}-${day}`;
    
    const found = dailyReflections.reflections.find(r => r.dateKey === dateKey);
    setReflection(found);
  }, [selectedDate]);

  if (!reflection) return <div>Loading...</div>;

  return (
    <div className="reflection-container">
      <div className="date-selector">
        <input 
          type="date" 
          value={selectedDate.toISOString().split('T')[0]}
          onChange={(e) => setSelectedDate(new Date(e.target.value))}
        />
      </div>
      
      <h1>{reflection.title}</h1>
      
      <blockquote className="quote">
        {reflection.quote.map((paragraph, i) => (
          <p key={i}>{paragraph}</p>
        ))}
        <cite>
          — {reflection.source.book}
          {reflection.source.pages && `, p. ${reflection.source.pages}`}
        </cite>
      </blockquote>
      
      <div className="reflection-text">
        {reflection.reflection.map((paragraph, i) => (
          <p key={i}>{paragraph}</p>
        ))}
      </div>
    </div>
  );
}

export default DailyReflection;
```

### Vue Component
```vue
<template>
  <div class="reflection-container">
    <div class="date-header">
      <input type="date" v-model="selectedDate" @change="loadReflection">
      <h2>{{ reflection.month }} {{ reflection.day }}</h2>
    </div>
    
    <h1 class="title">{{ reflection.title }}</h1>
    
    <blockquote class="quote">
      <p v-for="(paragraph, index) in reflection.quote" :key="`q${index}`">
        {{ paragraph }}
      </p>
      <cite>
        — {{ reflection.source.book }}
        <span v-if="reflection.source.pages">, p. {{ reflection.source.pages }}</span>
      </cite>
    </blockquote>
    
    <div class="reflection-text">
      <p v-for="(paragraph, index) in reflection.reflection" :key="`r${index}`">
        {{ paragraph }}
      </p>
    </div>
  </div>
</template>

<script>
import dailyReflections from './ALL366DR.json';

export default {
  data() {
    return {
      selectedDate: new Date().toISOString().split('T')[0],
      reflection: null
    };
  },
  mounted() {
    this.loadReflection();
  },
  methods: {
    loadReflection() {
      const date = new Date(this.selectedDate);
      const month = String(date.getMonth() + 1).padStart(2, '0');
      const day = String(date.getDate()).padStart(2, '0');
      const dateKey = `${month}-${day}`;
      
      this.reflection = dailyReflections.reflections.find(r => r.dateKey === dateKey);
    }
  }
};
</script>
```

---

## Backend Implementation

### Node.js/Express API
```javascript
const express = require('express');
const app = express();
const dailyReflections = require('./ALL366DR.json');

// CORS middleware
app.use((req, res, next) => {
  res.header('Access-Control-Allow-Origin', '*');
  res.header('Access-Control-Allow-Headers', 'Content-Type');
  next();
});

// Get today's reflection
app.get('/api/reflection/today', (req, res) => {
  const today = new Date();
  const month = String(today.getMonth() + 1).padStart(2, '0');
  const day = String(today.getDate()).padStart(2, '0');
  const dateKey = `${month}-${day}`;
  
  const reflection = dailyReflections.reflections.find(r => r.dateKey === dateKey);
  
  if (reflection) {
    res.json(reflection);
  } else {
    res.status(404).json({ error: 'Reflection not found' });
  }
});

// Get reflection by date
app.get('/api/reflection/:month/:day', (req, res) => {
  const { month, day } = req.params;
  const dateKey = `${month.padStart(2, '0')}-${day.padStart(2, '0')}`;
  
  const reflection = dailyReflections.reflections.find(r => r.dateKey === dateKey);
  
  if (reflection) {
    res.json(reflection);
  } else {
    res.status(404).json({ error: 'Reflection not found' });
  }
});

// Search reflections
app.get('/api/search', (req, res) => {
  const { q } = req.query;
  
  if (!q) {
    return res.status(400).json({ error: 'Search query required' });
  }
  
  const results = dailyReflections.reflections.filter(reflection => {
    const searchText = [
      reflection.title,
      ...reflection.quote,
      ...reflection.reflection
    ].join(' ').toLowerCase();
    
    return searchText.includes(q.toLowerCase());
  });
  
  res.json(results);
});

// Get random reflection
app.get('/api/reflection/random', (req, res) => {
  const randomIndex = Math.floor(Math.random() * dailyReflections.reflections.length);
  res.json(dailyReflections.reflections[randomIndex]);
});

app.listen(3000, () => {
  console.log('Daily Reflections API running on port 3000');
});
```

### Python/Flask API
```python
from flask import Flask, jsonify, request
from flask_cors import CORS
import json
from datetime import datetime
import random

app = Flask(__name__)
CORS(app)

# Load data
with open('ALL366DR.json', 'r', encoding='utf-8') as f:
    daily_reflections = json.load(f)

@app.route('/api/reflection/today')
def get_todays_reflection():
    today = datetime.now()
    date_key = f"{today.month:02d}-{today.day:02d}"
    
    for reflection in daily_reflections['reflections']:
        if reflection['dateKey'] == date_key:
            return jsonify(reflection)
    
    return jsonify({'error': 'Reflection not found'}), 404

@app.route('/api/reflection/<int:month>/<int:day>')
def get_reflection_by_date(month, day):
    date_key = f"{month:02d}-{day:02d}"
    
    for reflection in daily_reflections['reflections']:
        if reflection['dateKey'] == date_key:
            return jsonify(reflection)
    
    return jsonify({'error': 'Reflection not found'}), 404

@app.route('/api/search')
def search_reflections():
    query = request.args.get('q', '').lower()
    
    if not query:
        return jsonify({'error': 'Search query required'}), 400
    
    results = []
    for reflection in daily_reflections['reflections']:
        search_text = ' '.join([
            reflection['title'],
            ' '.join(reflection['quote']),
            ' '.join(reflection['reflection'])
        ]).lower()
        
        if query in search_text:
            results.append(reflection)
    
    return jsonify(results)

@app.route('/api/reflection/random')
def get_random_reflection():
    reflection = random.choice(daily_reflections['reflections'])
    return jsonify(reflection)

if __name__ == '__main__':
    app.run(debug=True)
```

### PHP Implementation
```php
<?php
header('Content-Type: application/json');
header('Access-Control-Allow-Origin: *');

$dailyReflections = json_decode(
    file_get_contents('ALL366DR.json'), 
    true
);

// Router
$requestUri = $_SERVER['REQUEST_URI'];
$requestMethod = $_SERVER['REQUEST_METHOD'];

// Get today's reflection
if (preg_match('/\/api\/reflection\/today/', $requestUri)) {
    $today = new DateTime();
    $dateKey = $today->format('m-d');
    
    foreach ($dailyReflections['reflections'] as $reflection) {
        if ($reflection['dateKey'] === $dateKey) {
            echo json_encode($reflection);
            exit;
        }
    }
    
    http_response_code(404);
    echo json_encode(['error' => 'Reflection not found']);
    exit;
}

// Get reflection by date
if (preg_match('/\/api\/reflection\/(\d+)\/(\d+)/', $requestUri, $matches)) {
    $month = str_pad($matches[1], 2, '0', STR_PAD_LEFT);
    $day = str_pad($matches[2], 2, '0', STR_PAD_LEFT);
    $dateKey = "$month-$day";
    
    foreach ($dailyReflections['reflections'] as $reflection) {
        if ($reflection['dateKey'] === $dateKey) {
            echo json_encode($reflection);
            exit;
        }
    }
    
    http_response_code(404);
    echo json_encode(['error' => 'Reflection not found']);
    exit;
}

// Search
if (preg_match('/\/api\/search/', $requestUri)) {
    $query = strtolower($_GET['q'] ?? '');
    
    if (empty($query)) {
        http_response_code(400);
        echo json_encode(['error' => 'Search query required']);
        exit;
    }
    
    $results = [];
    foreach ($dailyReflections['reflections'] as $reflection) {
        $searchText = strtolower(
            $reflection['title'] . ' ' .
            implode(' ', $reflection['quote']) . ' ' .
            implode(' ', $reflection['reflection'])
        );
        
        if (strpos($searchText, $query) !== false) {
            $results[] = $reflection;
        }
    }
    
    echo json_encode($results);
    exit;
}
?>
```

---

## Database Integration

### MySQL Schema
```sql
CREATE DATABASE IF NOT EXISTS daily_reflections;
USE daily_reflections;

CREATE TABLE reflections (
    id INT AUTO_INCREMENT PRIMARY KEY,
    month VARCHAR(20) NOT NULL,
    month_number INT NOT NULL,
    day INT NOT NULL,
    date_key VARCHAR(5) NOT NULL UNIQUE,
    day_of_year INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    source_book VARCHAR(255),
    source_pages VARCHAR(50),
    has_ellipsis BOOLEAN DEFAULT FALSE,
    has_em_dash BOOLEAN DEFAULT FALSE,
    quote_length INT,
    reflection_length INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_date_key (date_key),
    INDEX idx_month_day (month_number, day)
);

CREATE TABLE quotes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    reflection_id INT NOT NULL,
    paragraph_number INT NOT NULL,
    content TEXT NOT NULL,
    FOREIGN KEY (reflection_id) REFERENCES reflections(id) ON DELETE CASCADE
);

CREATE TABLE reflection_texts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    reflection_id INT NOT NULL,
    paragraph_number INT NOT NULL,
    content TEXT NOT NULL,
    FOREIGN KEY (reflection_id) REFERENCES reflections(id) ON DELETE CASCADE
);

-- Import script
DELIMITER $$
CREATE PROCEDURE import_reflection(
    IN p_month VARCHAR(20),
    IN p_month_number INT,
    IN p_day INT,
    IN p_date_key VARCHAR(5),
    IN p_day_of_year INT,
    IN p_title VARCHAR(255),
    IN p_source_book VARCHAR(255),
    IN p_source_pages VARCHAR(50),
    IN p_has_ellipsis BOOLEAN,
    IN p_has_em_dash BOOLEAN,
    IN p_quote_length INT,
    IN p_reflection_length INT,
    IN p_quotes JSON,
    IN p_reflections JSON
)
BEGIN
    DECLARE reflection_id INT;
    DECLARE i INT DEFAULT 0;
    
    -- Insert main reflection
    INSERT INTO reflections (
        month, month_number, day, date_key, day_of_year,
        title, source_book, source_pages,
        has_ellipsis, has_em_dash, quote_length, reflection_length
    ) VALUES (
        p_month, p_month_number, p_day, p_date_key, p_day_of_year,
        p_title, p_source_book, p_source_pages,
        p_has_ellipsis, p_has_em_dash, p_quote_length, p_reflection_length
    );
    
    SET reflection_id = LAST_INSERT_ID();
    
    -- Insert quotes
    WHILE i < JSON_LENGTH(p_quotes) DO
        INSERT INTO quotes (reflection_id, paragraph_number, content)
        VALUES (reflection_id, i + 1, JSON_UNQUOTE(JSON_EXTRACT(p_quotes, CONCAT('$[', i, ']'))));
        SET i = i + 1;
    END WHILE;
    
    -- Insert reflection texts
    SET i = 0;
    WHILE i < JSON_LENGTH(p_reflections) DO
        INSERT INTO reflection_texts (reflection_id, paragraph_number, content)
        VALUES (reflection_id, i + 1, JSON_UNQUOTE(JSON_EXTRACT(p_reflections, CONCAT('$[', i, ']'))));
        SET i = i + 1;
    END WHILE;
END$$
DELIMITER ;
```

### MongoDB Schema
```javascript
// MongoDB import script
const MongoClient = require('mongodb').MongoClient;
const dailyReflections = require('./ALL366DR.json');

async function importToMongoDB() {
  const client = new MongoClient('mongodb://localhost:27017');
  
  try {
    await client.connect();
    const db = client.db('dailyReflections');
    const collection = db.collection('reflections');
    
    // Clear existing data
    await collection.deleteMany({});
    
    // Insert all reflections
    await collection.insertMany(dailyReflections.reflections);
    
    // Create indexes
    await collection.createIndex({ dateKey: 1 });
    await collection.createIndex({ dayOfYear: 1 });
    await collection.createIndex({ month: 1, day: 1 });
    await collection.createIndex({ 
      title: 'text', 
      quote: 'text', 
      reflection: 'text' 
    });
    
    console.log('Import complete!');
  } finally {
    await client.close();
  }
}

importToMongoDB();
```

---

## Search Functionality

### Full-Text Search Implementation
```javascript
class ReflectionSearch {
  constructor(reflections) {
    this.reflections = reflections;
  }
  
  // Simple text search
  search(query) {
    const lowerQuery = query.toLowerCase();
    
    return this.reflections.filter(reflection => {
      const searchableText = [
        reflection.title,
        ...reflection.quote,
        ...reflection.reflection,
        reflection.source.book
      ].join(' ').toLowerCase();
      
      return searchableText.includes(lowerQuery);
    });
  }
  
  // Advanced search with options
  advancedSearch(options) {
    let results = [...this.reflections];
    
    // Filter by month
    if (options.month) {
      results = results.filter(r => r.month === options.month);
    }
    
    // Filter by source book
    if (options.sourceBook) {
      results = results.filter(r => 
        r.source.book.includes(options.sourceBook)
      );
    }
    
    // Filter by keyword
    if (options.keyword) {
      const keyword = options.keyword.toLowerCase();
      results = results.filter(r => {
        const text = [
          r.title,
          ...r.quote,
          ...r.reflection
        ].join(' ').toLowerCase();
        return text.includes(keyword);
      });
    }
    
    // Filter by special characters
    if (options.hasEllipsis !== undefined) {
      results = results.filter(r => r.metadata.hasEllipsis === options.hasEllipsis);
    }
    
    if (options.hasEmDash !== undefined) {
      results = results.filter(r => r.metadata.hasEmDash === options.hasEmDash);
    }
    
    return results;
  }
  
  // Search with ranking
  searchWithRanking(query) {
    const lowerQuery = query.toLowerCase();
    const words = lowerQuery.split(/\s+/);
    
    const scored = this.reflections.map(reflection => {
      let score = 0;
      const title = reflection.title.toLowerCase();
      const quote = reflection.quote.join(' ').toLowerCase();
      const text = reflection.reflection.join(' ').toLowerCase();
      
      // Score based on location of match
      words.forEach(word => {
        if (title.includes(word)) score += 10;
        if (quote.includes(word)) score += 5;
        if (text.includes(word)) score += 3;
      });
      
      // Bonus for exact phrase match
      if (title.includes(lowerQuery)) score += 20;
      if (quote.includes(lowerQuery)) score += 10;
      if (text.includes(lowerQuery)) score += 5;
      
      return { reflection, score };
    });
    
    // Filter out non-matches and sort by score
    return scored
      .filter(item => item.score > 0)
      .sort((a, b) => b.score - a.score)
      .map(item => item.reflection);
  }
}

// Usage
const searcher = new ReflectionSearch(dailyReflections.reflections);
const results = searcher.searchWithRanking('spiritual awakening');
```

---

## Paragraph Handling

### Understanding the Paragraph Structure

The JSON uses arrays to store paragraphs, making it easy to display properly formatted text:

```javascript
{
  "quote": [
    "First paragraph of the quote.",
    "Second paragraph if it exists.",
    "Third paragraph if needed."
  ],
  "reflection": [
    "First paragraph of the reflection.",
    "Second paragraph showing a new thought or perspective.",
    "Additional paragraphs as needed."
  ]
}
```

### Why Arrays for Paragraphs?

1. **Clean Separation** - No need to parse `\n\n` or other escape sequences
2. **Easy Styling** - Each paragraph can be wrapped in `<p>` tags
3. **Better Accessibility** - Screen readers handle separate paragraphs better
4. **Flexible Display** - Easy to add spacing, indentation, or other styling

### Displaying Multi-Paragraph Content

#### HTML Display
```javascript
function displayQuote(quoteArray) {
  return quoteArray.map(paragraph => `<p>${paragraph}</p>`).join('');
}

// For quotes with multiple paragraphs
function displayQuoteWithBreaks(quoteArray) {
  return quoteArray.map((paragraph, index) => `
    <p class="quote-paragraph ${index === 0 ? 'first' : ''}">
      ${paragraph}
    </p>
  `).join('');
}
```

#### CSS for Proper Spacing
```css
.quote-paragraph {
  margin-bottom: 1em;
}

.quote-paragraph:last-child {
  margin-bottom: 0;
}

.quote-paragraph.first {
  /* Optional: Special styling for first paragraph */
  font-size: 1.1em;
}

.reflection p {
  margin-bottom: 1.2em;
  line-height: 1.6;
}

.reflection p:last-child {
  margin-bottom: 0;
}
```

#### React Component for Multi-Paragraph Display
```jsx
function QuoteDisplay({ quote }) {
  return (
    <blockquote className="daily-quote">
      {quote.map((paragraph, index) => (
        <p key={index} className="quote-paragraph">
          {paragraph}
        </p>
      ))}
    </blockquote>
  );
}

function ReflectionDisplay({ reflection }) {
  return (
    <div className="daily-reflection">
      {reflection.map((paragraph, index) => (
        <p key={index} className="reflection-paragraph">
          {paragraph}
        </p>
      ))}
    </div>
  );
}
```

### Handling Special Cases

#### Single vs Multiple Paragraphs
```javascript
function formatForDisplay(paragraphs) {
  if (paragraphs.length === 1) {
    // Single paragraph - might want different styling
    return `<p class="single-paragraph">${paragraphs[0]}</p>`;
  } else {
    // Multiple paragraphs - add proper spacing
    return paragraphs.map((p, i) => 
      `<p class="paragraph-${i + 1}">${p}</p>`
    ).join('');
  }
}
```

#### Email Templates with Paragraphs
```javascript
function formatEmailQuote(quoteArray) {
  if (quoteArray.length === 1) {
    return `<blockquote style="font-style: italic; padding: 15px;">
      ${quoteArray[0]}
    </blockquote>`;
  } else {
    return `<blockquote style="font-style: italic; padding: 15px;">
      ${quoteArray.map(p => 
        `<p style="margin-bottom: 10px;">${p}</p>`
      ).join('')}
    </blockquote>`;
  }
}
```

#### Plain Text Output
```javascript
function toPlainText(entry) {
  const quote = entry.quote.join('\n\n');
  const reflection = entry.reflection.join('\n\n');
  
  return `${entry.title}
  
QUOTE:
${quote}

SOURCE: ${entry.source.book}, p. ${entry.source.pages}

REFLECTION:
${reflection}`;
}
```

### Paragraph Statistics

Some entries have multiple paragraphs that represent different thoughts or perspectives:

- **Quotes**: Most have 1 paragraph, some have 2-3 for longer passages
- **Reflections**: Range from 1-4 paragraphs, typically 1-2
- **Average**: Reflections tend to have more paragraphs than quotes

### Responsive Design Considerations

```css
/* Mobile: Reduce paragraph spacing */
@media (max-width: 768px) {
  .quote-paragraph,
  .reflection-paragraph {
    margin-bottom: 0.8em;
  }
}

/* Desktop: Full spacing for readability */
@media (min-width: 769px) {
  .quote-paragraph,
  .reflection-paragraph {
    margin-bottom: 1.2em;
    max-width: 65ch; /* Optimal line length */
  }
}
```

### Accessibility with Paragraphs

```html
<article role="article">
  <blockquote aria-label="Daily quote">
    <p>First paragraph of quote.</p>
    <p>Second paragraph of quote.</p>
  </blockquote>
  
  <div role="region" aria-label="Daily reflection">
    <p>First paragraph of reflection.</p>
    <p>Second paragraph of reflection.</p>
    <p>Third paragraph of reflection.</p>
  </div>
</article>
```

---

## Display Formatting

### HTML Formatting
```javascript
function formatReflectionHTML(reflection) {
  return `
    <article class="daily-reflection">
      <header>
        <time datetime="${reflection.monthNumber}-${reflection.day}">
          ${reflection.month} ${reflection.day}
        </time>
        <h1>${escapeHTML(reflection.title)}</h1>
      </header>
      
      <blockquote class="quote">
        ${reflection.quote.map(p => `<p>${escapeHTML(p)}</p>`).join('')}
        <footer>
          <cite>
            — ${escapeHTML(reflection.source.book)}${
              reflection.source.pages ? `, p. ${reflection.source.pages}` : ''
            }
          </cite>
        </footer>
      </blockquote>
      
      <section class="reflection-text">
        ${reflection.reflection.map(p => `<p>${escapeHTML(p)}</p>`).join('')}
      </section>
    </article>
  `;
}

function escapeHTML(str) {
  const div = document.createElement('div');
  div.textContent = str;
  return div.innerHTML;
}
```

### Markdown Formatting
```javascript
function formatReflectionMarkdown(reflection) {
  return `
# ${reflection.month} ${reflection.day}

## ${reflection.title}

${reflection.quote.map(p => `> ${p}`).join('\n>\n')}

*— ${reflection.source.book}${reflection.source.pages ? `, p. ${reflection.source.pages}` : ''}*

---

${reflection.reflection.join('\n\n')}
  `.trim();
}
```

### Plain Text Formatting
```javascript
function formatReflectionText(reflection) {
  const separator = '='.repeat(60);
  
  return `
${separator}
${reflection.month} ${reflection.day}
${reflection.title}
${separator}

QUOTE:
${reflection.quote.join('\n\n')}

SOURCE: ${reflection.source.book}${reflection.source.pages ? `, p. ${reflection.source.pages}` : ''}

REFLECTION:
${reflection.reflection.join('\n\n')}
${separator}
  `.trim();
}
```

### Email Template
```javascript
function formatReflectionEmail(reflection) {
  return {
    subject: `Daily Reflection: ${reflection.month} ${reflection.day} - ${reflection.title}`,
    html: `
      <!DOCTYPE html>
      <html>
      <head>
        <style>
          body { font-family: Georgia, serif; line-height: 1.6; color: #333; }
          .container { max-width: 600px; margin: 0 auto; padding: 20px; }
          h1 { color: #2c3e50; font-size: 24px; }
          .quote { 
            background: #f8f9fa; 
            border-left: 4px solid #007bff; 
            padding: 15px; 
            margin: 20px 0;
            font-style: italic;
          }
          .source { text-align: right; color: #6c757d; }
          .reflection { margin-top: 20px; }
          .footer { 
            margin-top: 40px; 
            padding-top: 20px; 
            border-top: 1px solid #dee2e6;
            font-size: 12px;
            color: #6c757d;
          }
        </style>
      </head>
      <body>
        <div class="container">
          <h1>${reflection.title}</h1>
          <p><strong>${reflection.month} ${reflection.day}</strong></p>
          
          <div class="quote">
            ${reflection.quote.map(p => `<p>${p}</p>`).join('')}
            <p class="source">
              — ${reflection.source.book}${
                reflection.source.pages ? `, p. ${reflection.source.pages}` : ''
              }
            </p>
          </div>
          
          <div class="reflection">
            ${reflection.reflection.map(p => `<p>${p}</p>`).join('')}
          </div>
          
          <div class="footer">
            <p>© 1990 by Alcoholics Anonymous World Services, Inc.</p>
          </div>
        </div>
      </body>
      </html>
    `,
    text: formatReflectionText(reflection)
  };
}
```

---

## Mobile App Integration

### React Native
```jsx
import React, { useState, useEffect } from 'react';
import {
  View,
  Text,
  ScrollView,
  StyleSheet,
  TouchableOpacity,
  Share
} from 'react-native';
import AsyncStorage from '@react-native-async-storage/async-storage';
import dailyReflections from './ALL366DR.json';

const DailyReflectionApp = () => {
  const [reflection, setReflection] = useState(null);
  const [favorites, setFavorites] = useState([]);

  useEffect(() => {
    loadTodaysReflection();
    loadFavorites();
  }, []);

  const loadTodaysReflection = () => {
    const today = new Date();
    const dateKey = `${String(today.getMonth() + 1).padStart(2, '0')}-${String(today.getDate()).padStart(2, '0')}`;
    const found = dailyReflections.reflections.find(r => r.dateKey === dateKey);
    setReflection(found);
  };

  const loadFavorites = async () => {
    try {
      const saved = await AsyncStorage.getItem('favorites');
      if (saved) setFavorites(JSON.parse(saved));
    } catch (error) {
      console.error('Error loading favorites:', error);
    }
  };

  const toggleFavorite = async () => {
    if (!reflection) return;
    
    const dateKey = reflection.dateKey;
    let newFavorites;
    
    if (favorites.includes(dateKey)) {
      newFavorites = favorites.filter(f => f !== dateKey);
    } else {
      newFavorites = [...favorites, dateKey];
    }
    
    setFavorites(newFavorites);
    await AsyncStorage.setItem('favorites', JSON.stringify(newFavorites));
  };

  const shareReflection = async () => {
    if (!reflection) return;
    
    try {
      await Share.share({
        message: `${reflection.title}\n\n${reflection.quote.join('\n\n')}\n\n— ${reflection.source.book}\n\n${reflection.reflection.join('\n\n')}`,
        title: `Daily Reflection - ${reflection.month} ${reflection.day}`
      });
    } catch (error) {
      console.error('Error sharing:', error);
    }
  };

  if (!reflection) {
    return (
      <View style={styles.container}>
        <Text>Loading...</Text>
      </View>
    );
  }

  const isFavorite = favorites.includes(reflection.dateKey);

  return (
    <ScrollView style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.date}>
          {reflection.month} {reflection.day}
        </Text>
        <View style={styles.actions}>
          <TouchableOpacity onPress={toggleFavorite}>
            <Text style={styles.actionButton}>
              {isFavorite ? '❤️' : '🤍'}
            </Text>
          </TouchableOpacity>
          <TouchableOpacity onPress={shareReflection}>
            <Text style={styles.actionButton}>📤</Text>
          </TouchableOpacity>
        </View>
      </View>

      <Text style={styles.title}>{reflection.title}</Text>

      <View style={styles.quote}>
        {reflection.quote.map((paragraph, i) => (
          <Text key={i} style={styles.quoteParagraph}>
            {paragraph}
          </Text>
        ))}
        <Text style={styles.source}>
          — {reflection.source.book}
          {reflection.source.pages && `, p. ${reflection.source.pages}`}
        </Text>
      </View>

      <View style={styles.reflection}>
        {reflection.reflection.map((paragraph, i) => (
          <Text key={i} style={styles.reflectionParagraph}>
            {paragraph}
          </Text>
        ))}
      </View>
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    padding: 20,
  },
  header: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 20,
  },
  date: {
    fontSize: 16,
    color: '#666',
  },
  actions: {
    flexDirection: 'row',
    gap: 15,
  },
  actionButton: {
    fontSize: 24,
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 20,
    color: '#333',
  },
  quote: {
    backgroundColor: '#f5f5f5',
    padding: 15,
    marginBottom: 20,
    borderLeftWidth: 4,
    borderLeftColor: '#007bff',
  },
  quoteParagraph: {
    fontSize: 16,
    fontStyle: 'italic',
    marginBottom: 10,
    lineHeight: 24,
  },
  source: {
    fontSize: 14,
    color: '#666',
    textAlign: 'right',
    marginTop: 10,
  },
  reflection: {
    marginBottom: 30,
  },
  reflectionParagraph: {
    fontSize: 16,
    lineHeight: 24,
    marginBottom: 15,
    color: '#333',
  },
});

export default DailyReflectionApp;
```

### Flutter Implementation
```dart
import 'package:flutter/material.dart';
import 'dart:convert';
import 'package:flutter/services.dart' show rootBundle;
import 'package:intl/intl.dart';

class DailyReflection {
  final String month;
  final int monthNumber;
  final int day;
  final String dateKey;
  final String title;
  final List<String> quote;
  final Map<String, String> source;
  final List<String> reflection;

  DailyReflection({
    required this.month,
    required this.monthNumber,
    required this.day,
    required this.dateKey,
    required this.title,
    required this.quote,
    required this.source,
    required this.reflection,
  });

  factory DailyReflection.fromJson(Map<String, dynamic> json) {
    return DailyReflection(
      month: json['month'],
      monthNumber: json['monthNumber'],
      day: json['day'],
      dateKey: json['dateKey'],
      title: json['title'],
      quote: List<String>.from(json['quote']),
      source: Map<String, String>.from(json['source']),
      reflection: List<String>.from(json['reflection']),
    );
  }
}

class DailyReflectionApp extends StatefulWidget {
  @override
  _DailyReflectionAppState createState() => _DailyReflectionAppState();
}

class _DailyReflectionAppState extends State<DailyReflectionApp> {
  DailyReflection? todaysReflection;
  List<DailyReflection> allReflections = [];

  @override
  void initState() {
    super.initState();
    loadReflections();
  }

  Future<void> loadReflections() async {
    final String jsonString = await rootBundle.loadString('assets/ALL366DR.json');
    final Map<String, dynamic> jsonData = json.decode(jsonString);
    
    setState(() {
      allReflections = (jsonData['reflections'] as List)
          .map((r) => DailyReflection.fromJson(r))
          .toList();
      
      // Get today's reflection
      final now = DateTime.now();
      final dateKey = DateFormat('MM-dd').format(now);
      todaysReflection = allReflections.firstWhere(
        (r) => r.dateKey == dateKey,
        orElse: () => allReflections.first,
      );
    });
  }

  @override
  Widget build(BuildContext context) {
    if (todaysReflection == null) {
      return Scaffold(
        body: Center(child: CircularProgressIndicator()),
      );
    }

    return Scaffold(
      appBar: AppBar(
        title: Text('Daily Reflection'),
        actions: [
          IconButton(
            icon: Icon(Icons.calendar_today),
            onPressed: () => _selectDate(context),
          ),
        ],
      ),
      body: SingleChildScrollView(
        padding: EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(
              '${todaysReflection!.month} ${todaysReflection!.day}',
              style: TextStyle(fontSize: 16, color: Colors.grey),
            ),
            SizedBox(height: 10),
            Text(
              todaysReflection!.title,
              style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
            ),
            SizedBox(height: 20),
            Container(
              padding: EdgeInsets.all(16),
              decoration: BoxDecoration(
                color: Colors.grey[100],
                border: Border(
                  left: BorderSide(color: Colors.blue, width: 4),
                ),
              ),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  ...todaysReflection!.quote.map((p) => 
                    Padding(
                      padding: EdgeInsets.only(bottom: 10),
                      child: Text(
                        p,
                        style: TextStyle(fontStyle: FontStyle.italic),
                      ),
                    ),
                  ),
                  SizedBox(height: 10),
                  Text(
                    '— ${todaysReflection!.source['book']}${todaysReflection!.source['pages']?.isNotEmpty ?? false ? ', p. ${todaysReflection!.source['pages']}' : ''}',
                    style: TextStyle(color: Colors.grey[600]),
                    textAlign: TextAlign.right,
                  ),
                ],
              ),
            ),
            SizedBox(height: 20),
            ...todaysReflection!.reflection.map((p) => 
              Padding(
                padding: EdgeInsets.only(bottom: 15),
                child: Text(
                  p,
                  style: TextStyle(fontSize: 16, height: 1.5),
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }

  Future<void> _selectDate(BuildContext context) async {
    final DateTime? picked = await showDatePicker(
      context: context,
      initialDate: DateTime.now(),
      firstDate: DateTime(2024, 1, 1),
      lastDate: DateTime(2025, 12, 31),
    );
    
    if (picked != null) {
      final dateKey = DateFormat('MM-dd').format(picked);
      final reflection = allReflections.firstWhere(
        (r) => r.dateKey == dateKey,
        orElse: () => allReflections.first,
      );
      
      setState(() {
        todaysReflection = reflection;
      });
    }
  }
}
```

---

## API Development

### RESTful API Structure
```
GET /api/reflection/today          # Today's reflection
GET /api/reflection/{month}/{day}  # Specific date
GET /api/reflection/random         # Random reflection
GET /api/reflections               # All reflections (paginated)
GET /api/reflections/month/{month} # Month's reflections
GET /api/search?q={query}          # Search
GET /api/favorites                 # User's favorites (requires auth)
POST /api/favorites/{dateKey}      # Add favorite
DELETE /api/favorites/{dateKey}    # Remove favorite
```

### GraphQL Schema
```graphql
type Query {
  reflection(month: Int!, day: Int!): Reflection
  todaysReflection: Reflection
  randomReflection: Reflection
  reflections(month: String, limit: Int = 10, offset: Int = 0): [Reflection]
  searchReflections(query: String!): [Reflection]
}

type Reflection {
  month: String!
  monthNumber: Int!
  day: Int!
  dateKey: String!
  dayOfYear: Int!
  title: String!
  quote: [String]!
  source: Source!
  reflection: [String]!
  metadata: Metadata!
}

type Source {
  book: String!
  pages: String
}

type Metadata {
  hasEllipsis: Boolean!
  hasEmDash: Boolean!
  quoteLength: Int!
  reflectionLength: Int!
}
```

---

## Best Practices

### 1. Caching
```javascript
// Browser caching
class ReflectionCache {
  constructor() {
    this.cache = new Map();
    this.cacheTime = 24 * 60 * 60 * 1000; // 24 hours
  }
  
  get(dateKey) {
    const cached = this.cache.get(dateKey);
    if (cached && Date.now() - cached.timestamp < this.cacheTime) {
      return cached.data;
    }
    return null;
  }
  
  set(dateKey, data) {
    this.cache.set(dateKey, {
      data,
      timestamp: Date.now()
    });
  }
}
```

### 2. Error Handling
```javascript
async function getReflection(month, day) {
  try {
    const dateKey = `${String(month).padStart(2, '0')}-${String(day).padStart(2, '0')}`;
    
    // Validate date
    if (month < 1 || month > 12 || day < 1 || day > 31) {
      throw new Error('Invalid date');
    }
    
    // Check for February 30-31, April 31, etc.
    const daysInMonth = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
    if (day > daysInMonth[month - 1]) {
      throw new Error('Invalid date for month');
    }
    
    const reflection = dailyReflections.reflections.find(r => r.dateKey === dateKey);
    
    if (!reflection) {
      throw new Error('Reflection not found');
    }
    
    return reflection;
  } catch (error) {
    console.error('Error getting reflection:', error);
    return null;
  }
}
```

### 3. Performance Optimization
```javascript
// Create lookup maps for faster access
const reflectionsByDate = new Map(
  dailyReflections.reflections.map(r => [r.dateKey, r])
);

const reflectionsByDayOfYear = new Map(
  dailyReflections.reflections.map(r => [r.dayOfYear, r])
);

// Quick access
const todaysReflection = reflectionsByDate.get('01-15');
const dayOfYearReflection = reflectionsByDayOfYear.get(15);
```

### 4. Accessibility
```html
<!-- Semantic HTML with ARIA labels -->
<article role="article" aria-label="Daily Reflection">
  <header>
    <time datetime="2025-01-15">January 15</time>
    <h1 id="reflection-title">Title</h1>
  </header>
  
  <blockquote aria-labelledby="quote-label">
    <span id="quote-label" class="sr-only">Daily Quote</span>
    <!-- Quote content -->
  </blockquote>
  
  <section aria-labelledby="reflection-label">
    <span id="reflection-label" class="sr-only">Daily Reflection</span>
    <!-- Reflection content -->
  </section>
</article>
```

---

## Troubleshooting

### Common Issues

#### Issue: Date not found
```javascript
// Solution: Handle missing dates gracefully
function getReflectionSafe(month, day) {
  const dateKey = `${String(month).padStart(2, '0')}-${String(day).padStart(2, '0')}`;
  
  // Try exact match first
  let reflection = dailyReflections.reflections.find(r => r.dateKey === dateKey);
  
  // If Feb 29 on non-leap year, use Feb 28
  if (!reflection && month === 2 && day === 29) {
    reflection = dailyReflections.reflections.find(r => r.dateKey === '02-28');
  }
  
  // If still not found, return a default or random
  if (!reflection) {
    const randomIndex = Math.floor(Math.random() * dailyReflections.reflections.length);
    reflection = dailyReflections.reflections[randomIndex];
  }
  
  return reflection;
}
```

#### Issue: Character encoding
```javascript
// Ensure UTF-8 encoding
fetch('ALL366DR.json')
  .then(response => response.text())
  .then(text => {
    // Parse with UTF-8
    const data = JSON.parse(text);
    // Use data...
  });
```

#### Issue: Large file size
```javascript
// Implement lazy loading
async function loadReflectionOnDemand(dateKey) {
  // Split JSON into monthly files
  const month = dateKey.substring(0, 2);
  const response = await fetch(`reflections/month-${month}.json`);
  const monthData = await response.json();
  return monthData.find(r => r.dateKey === dateKey);
}
```

---

## License & Attribution

When using this data, please include appropriate attribution:

```html
<!-- HTML -->
<footer>
  <p>Daily Reflections © 1990 by Alcoholics Anonymous World Services, Inc.</p>
</footer>
```

```javascript
// JavaScript
const attribution = "© 1990 by Alcoholics Anonymous World Services, Inc.";
```

---

## Support & Updates

For questions or issues with the JSON file:
1. Check the data structure matches the schema
2. Verify UTF-8 encoding
3. Ensure all 366 entries are present
4. Validate against the sample implementations above

---

*Last Updated: November 20, 2025*
*JSON Version: 9.0 - FINAL COMPLETE*
