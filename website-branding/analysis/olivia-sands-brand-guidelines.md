# Olivia Sands Brand Guidelines

**Version:** 1.0  
**Last Updated:** October 2025  
**Industry:** Romance Publishing / Author Website

---

## Brand Overview

Olivia Sands is a romance author specializing in heartwarming contemporary cozy small town romance series. The brand identity emphasizes warmth, accessibility, and literary elegance while maintaining a clean, professional appearance that lets the book covers shine.

**Brand Promise:** Heartwarming, cozy romance stories that transport readers to charming small-town settings.

---

## 1. Color System

### Primary Brand Colors

#### Olivia Blue (Primary Action)
- **Hex:** `#243be5`
- **RGB:** `rgb(36, 59, 229)`
- **CMYK:** `C84 M74 Y0 K0`
- **Usage:** Primary call-to-action buttons, interactive elements
- **Accessibility:** WCAG AA compliant on white backgrounds

#### Deep Olivia Blue (Interactive States)
- **Hex:** `#0009b3`
- **RGB:** `rgb(0, 9, 179)`
- **CMYK:** `C100 M95 Y0 K0`
- **Usage:** Button hover states, pressed states, active links
- **Note:** Provides clear visual feedback for user interactions

#### Pure White (Foundation)
- **Hex:** `#ffffff`
- **RGB:** `rgb(255, 255, 255)`
- **Usage:** Primary background, card backgrounds, button text
- **Accessibility:** Provides maximum contrast for readability

### Text Color Palette

#### Primary Text
- **Hex:** `#000000`
- **RGB:** `rgb(0, 0, 0)`
- **Usage:** Headings, body text, navigation links (default state)
- **Contrast Ratio:** 21:1 on white (WCAG AAA)

#### Secondary Text (Hover/Interactive)
- **Hex:** `#666666`
- **RGB:** `rgb(102, 102, 102)`
- **Usage:** Link hover states, secondary information
- **Contrast Ratio:** 5.74:1 on white (WCAG AA)

#### Tertiary Text (Low Emphasis)
- **Hex:** `#aaaaaa`
- **RGB:** `rgb(170, 170, 170)`
- **Usage:** Captions, metadata, disabled states
- **Contrast Ratio:** 2.85:1 on white (use for large text only)

### Extended Palette (Social Media)

#### Facebook Blue
- **Hex:** `#3b5998`
- **Usage:** Facebook social icon backgrounds only

#### Instagram Pink
- **Hex:** `#e4405f`
- **Usage:** Instagram social icon backgrounds only

#### Pinterest Red
- **Hex:** `#c92619`
- **Usage:** Pinterest social icon backgrounds only

#### Cookie Consent Green
- **Hex:** `#61a229`
- **Usage:** Cookie acceptance buttons (system requirement)

#### Cookie Settings Blue
- **Hex:** `#3566bb`
- **Usage:** Cookie settings buttons (system requirement)

### Color Usage Rules

**DO:**
- Use Olivia Blue (#243be5) for all primary CTAs
- Maintain white backgrounds for maximum book cover visibility
- Use black (#000000) for all primary text
- Reserve social media colors exclusively for their respective icons

**DON'T:**
- Don't use Olivia Blue for text (poor readability)
- Don't use colored backgrounds behind book covers
- Don't mix social media brand colors in main UI
- Don't use gray text below #666666 for body copy (accessibility)

---

## 2. Typography System

### Font Families

#### Display Font: Rochester
- **Category:** Script / Cursive
- **Weight:** 400 (Regular only)
- **Source:** Google Fonts
- **Link:** `https://fonts.googleapis.com/css?family=Rochester:400`
- **Fallback:** Brush Script MT, cursive, serif

**Usage:**
- Site title/logo (if used)
- Special decorative headings
- Romantic emphasis elements

**Do NOT use for:**
- Body text (readability issues)
- Long headings (legibility issues)
- All-caps text (loses character)

#### Body Font: Lora
- **Category:** Serif
- **Weights Available:** 400, 400 italic, 700, 700 italic
- **Source:** Google Fonts
- **Link:** `https://fonts.googleapis.com/css?family=Lora:400,400i,700,700i`
- **Fallback:** Georgia, Times New Roman, serif

**Usage:**
- All body text
- Book descriptions
- Blog posts and articles
- Navigation menu items
- Standard headings

### Typography Scale

#### H1 - Page Titles
- **Font:** Lora
- **Weight:** 700 (Bold)
- **Size:** 36-42px
- **Line Height:** 1.2
- **Color:** #000000
- **Usage:** Main page title ("Books", "Blog", etc.)

#### H2 - Site Tagline / Section Headers
- **Font:** Lora or Rochester (for tagline)
- **Weight:** 400-700
- **Size:** 24-30px
- **Line Height:** 1.3
- **Color:** #000000
- **Usage:** "Heartwarming Romance ❤ Olivia Sands"

#### H3 - Series Names
- **Font:** Lora
- **Weight:** 700 (Bold)
- **Size:** 20-24px
- **Line Height:** 1.4
- **Color:** #000000
- **Text Align:** Center
- **Usage:** "Snowberry Hill", "Dovetail Lake"

#### H5 - Strong CTAs
- **Font:** Lora
- **Weight:** 700 (Bold)
- **Size:** 16-18px
- **Line Height:** 1.5
- **Color:** #000000
- **Text Transform:** Uppercase for emphasis
- **Usage:** "CLICK HERE TO GET A FREE BOOK"

#### Body Text
- **Font:** Lora
- **Weight:** 400 (Regular)
- **Size:** 16-18px
- **Line Height:** 1.6-1.8
- **Color:** #000000
- **Usage:** Paragraphs, descriptions, general content

#### Small Text
- **Font:** Lora
- **Weight:** 400 (Regular)
- **Size:** 14px
- **Line Height:** 1.5
- **Color:** #666666 or #aaaaaa
- **Usage:** Captions, copyright, metadata

### Typography Usage Rules

**DO:**
- Use Lora for all standard text needs
- Maintain generous line-height (1.6+) for readability
- Use bold (700) weights sparingly for emphasis
- Center-align headings for symmetry with layout

**DON'T:**
- Don't use Rochester for body text
- Don't use font sizes smaller than 14px for body copy
- Don't use more than 2 font families on the site
- Don't use light gray text (#aaaaaa) for small text

---

## 3. Button System

### Primary Button (CTA)

**Specifications:**
- **Background:** #243be5 (Olivia Blue)
- **Text Color:** #ffffff (White)
- **Font:** Lora
- **Font Weight:** 400 (Regular)
- **Font Size:** 14-16px
- **Padding:** 10-12px 20-24px
- **Border Radius:** 3-4px (slight rounding)
- **Border:** None
- **Text:** "More Details »" (with right arrow)

**Hover State:**
- **Background:** #0009b3 (Deep Olivia Blue)
- **Text Color:** #ffffff (White)
- **Transition:** 0.2-0.3s ease
- **Cursor:** Pointer

**Implementation (CSS):**
```css
.novelist-button {
    background-color: #243be5;
    color: #ffffff;
    font-family: 'Lora', Georgia, serif;
    font-weight: 400;
    font-size: 16px;
    padding: 12px 24px;
    border-radius: 4px;
    border: none;
    text-decoration: none;
    display: inline-block;
    transition: background-color 0.3s ease;
    cursor: pointer;
}

.novelist-button:hover {
    background-color: #0009b3;
    color: #ffffff;
}
```

**Usage Rules:**
- Use for "More Details" on book listings
- Use for primary conversion actions
- Always include right arrow symbol (»)
- Minimum 2-3 buttons visible on screen

---

## 4. Link System

### Default Link Style

**Specifications:**
- **Color:** #000000 (Black)
- **Text Decoration:** None
- **Font:** Inherits from parent (typically Lora)
- **Cursor:** Pointer

**Hover State:**
- **Color:** #666666 (Dark Gray)
- **Text Decoration:** None
- **Transition:** 0.2s ease

**Implementation (CSS):**
```css
a {
    color: #000000;
    text-decoration: none;
    transition: color 0.2s ease;
}

a:hover,
a:focus {
    color: #666666;
    text-decoration: none;
}
```

**Usage Rules:**
- All navigation links use this style
- All in-content links use this style
- Book title links use this style
- Exception: Buttons use button styling (not link styling)

---

## 5. Social Media Icons

### Specifications

**Size:** 18px font size  
**Padding:** 8px all sides  
**Shape:** Circular  
**Display:** Inline with spacing

**Color Mapping:**
- **Facebook:** Background #3b5998
- **Instagram:** Background #e4405f
- **Pinterest:** Background #c92619

**Implementation Note:**
Use icon font (socicon) with colored circular backgrounds. Maintain brand-specific colors for immediate recognition.

---

## 6. Layout & Grid System

### Framework
- **Base:** Bootstrap 3.0
- **Container Width:** 1170px max (Bootstrap default)
- **Responsive Breakpoints:** Bootstrap standard

### Content Alignment
- **Primary Rule:** Center alignment for all main content
- **Headers:** Center-aligned
- **Book Grids:** Center-aligned
- **Text Content:** Center or left (depending on context)

### Book Display Grid

**Bundle Display (Hero):**
- **Columns:** 2 columns
- **Gap:** Standard Bootstrap gutter (30px)
- **Alignment:** Center

**Series Display:**
- **Columns:** 6 columns on desktop
- **Columns (Tablet):** 3-4 columns
- **Columns (Mobile):** 2 columns
- **Gap:** Standard Bootstrap gutter
- **Alignment:** Center

### Spacing System

**Vertical Spacing:**
- **Between Series Sections:** 60-80px
- **After Series Title:** 30-40px
- **Between Books in Grid:** Bootstrap gutter (30px)

**Horizontal Spacing:**
- **Page Margins:** Bootstrap container (15px each side)
- **Content Width:** Container-constrained (max 1170px)

---

## 7. Navigation System

### Top Navigation Bar

**Structure:**
- Horizontal menu bar
- Center-aligned items
- Language flags with emoji
- Dropdown menus for VIP section

**Menu Items Format:**
- Emoji + Text (🇺🇸 ENGLISH)
- Font: Lora
- Color: #000000
- Hover: #666666

**Secondary Menu:**
- Icons: ✏️ Blog, 📖 List, 💌 V.I.P.
- Same styling as main menu

**Implementation:**
- Bootstrap navbar component
- Collapsible on mobile
- Fixed or static positioning (not sticky)

---

## 8. Decorative Elements

### Emoji Usage

**Approved Emojis:**
- ❤ (Heart) - In tagline, romantic emphasis
- 🇺🇸 🇨🇵 🇩🇪 etc. - Language/country flags in navigation
- ✏️ (Pencil) - Blog section
- 📖 (Book) - List section
- 💌 (Love Letter) - VIP section
- » (Right Arrow) - Button text

**Usage Rules:**
- Use sparingly for functional purposes
- Always pair with text (never standalone)
- Maintain consistent sizing with text
- Use native system emoji (no custom images)

### Heart Symbol (❤)

**Primary Usage:** Site tagline
**Format:** "Heartwarming Romance ❤ Olivia Sands ❤ Romance douce"
**Purpose:** Emotional connection, brand warmth
**Color:** Inherits text color (typically #000000 or red depending on system)

---

## 9. Image Guidelines

### Book Cover Display

**Format:**
- 3D mockups with e-reader devices preferred
- High-resolution (minimum 1500px on longest side)
- Consistent aspect ratio (standard book proportions)
- Portrait orientation

**Display Rules:**
- No filters or overlays
- No hover effects on covers
- Maintain aspect ratio (no stretching)
- Lazy loading for performance
- Responsive srcset for multiple sizes

**Grid Display:**
- Uniform sizing within each grid
- Center-aligned
- Even spacing (Bootstrap gutter)
- Clean presentation (no shadows or borders added in CSS)

---

## 10. Responsive Design Rules

### Mobile (< 768px)
- 2-column book grid
- Collapsible navigation
- Maintain center alignment
- Reduce heading sizes proportionally
- Stack elements vertically

### Tablet (768px - 1024px)
- 3-4 column book grid
- Full navigation visible
- Maintain center alignment
- Standard font sizes

### Desktop (> 1024px)
- 6-column book grid for series
- 2-column for bundles
- Full navigation
- Maximum container width (1170px)

---

## 11. Accessibility Standards

### Color Contrast
- **Primary Text on White:** 21:1 (AAA) ✓
- **Secondary Text on White:** 5.74:1 (AA) ✓
- **Button Text on Blue:** 9.8:1 (AAA) ✓

### Typography
- Minimum body text size: 16px
- Maximum line length: 75 characters
- Line height minimum: 1.5
- Sufficient color contrast for all text

### Interactive Elements
- All buttons keyboard accessible
- Clear focus states
- Descriptive link text
- Alt text on all images

---

## 12. Technical Implementation

### Font Loading

**Google Fonts Link:**
```html
<link href="https://fonts.googleapis.com/css?family=Rochester:400|Lora:400,400i,700,700i" rel="stylesheet">
```

**CSS Font Stack:**
```css
/* Display Font */
font-family: 'Rochester', 'Brush Script MT', cursive, serif;

/* Body Font */
font-family: 'Lora', Georgia, 'Times New Roman', serif;
```

### CSS Variables (Recommended Implementation)

```css
:root {
    /* Colors */
    --color-olivia-blue: #243be5;
    --color-deep-blue: #0009b3;
    --color-white: #ffffff;
    --color-black: #000000;
    --color-gray-dark: #666666;
    --color-gray-light: #aaaaaa;
    
    /* Typography */
    --font-display: 'Rochester', cursive, serif;
    --font-body: 'Lora', Georgia, serif;
    
    /* Spacing */
    --spacing-xs: 8px;
    --spacing-sm: 16px;
    --spacing-md: 24px;
    --spacing-lg: 40px;
    --spacing-xl: 60px;
}
```

---

## 13. Brand Voice & Messaging

### Tone of Voice
- **Warm:** Welcoming, friendly, approachable
- **Romantic:** Heartfelt, emotional, cozy
- **Professional:** Polished, organized, trustworthy
- **Accessible:** Clear, inclusive, multilingual

### Key Brand Phrases

**Primary Tagline:**
"Heartwarming Romance ❤ Olivia Sands ❤ Romance douce"

**Genre Description:**
"Heartwarming Contemporary Cozy Small Town Romance Series"

**CTAs:**
- "CLICK HERE TO GET A FREE BOOK"
- "More Details »"

### Writing Style
- Use warm, inviting language
- Keep sentences clear and readable
- Emphasize emotional connection
- Highlight "cozy" and "small-town" themes
- Maintain professional tone while being friendly

---

## 14. Dos and Don'ts Summary

### DO:
✓ Use Olivia Blue (#243be5) for all primary CTAs  
✓ Maintain white backgrounds throughout  
✓ Use Lora for all standard text needs  
✓ Center-align main content sections  
✓ Include emoji thoughtfully for warmth  
✓ Optimize images for web performance  
✓ Maintain multilingual accessibility  
✓ Follow accessibility contrast guidelines  

### DON'T:
✗ Don't use Olivia Blue for text  
✗ Don't add colored backgrounds behind books  
✗ Don't use Rochester for body text  
✗ Don't use more than 2 font families  
✗ Don't use font sizes below 14px for body  
✗ Don't add shadows or borders to book covers  
✗ Don't compromise on contrast ratios  
✗ Don't use light gray for important information  

---

## Version History

**Version 1.0** (October 2025)
- Initial brand guidelines documentation
- Based on current oliviasands.com implementation
- Formalized existing design system
- Added accessibility standards
- Included technical implementation details

---

**For questions or clarification on these brand guidelines, contact the brand design team.**
