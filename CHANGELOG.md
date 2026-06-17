# Morgue — Changelog

---

## [1.3.0] — 2026-06-17

### Search inside screenshots, a safety net for deletes, and bring-your-own AI
- **Text search (OCR)** — Morgue now reads the **text inside your screenshots** on-device, so searching a word that appears in an image surfaces it. No setup, no AI key, nothing leaves your Mac — it just works the next time you search
- **Trash & Restore** — deleting an asset now moves it to a **Trash** instead of removing it for good. Browse the Trash anytime to **Restore** a save or **Delete Forever**, and **Empty Trash** when you're sure. Accidental deletes are now undoable
- **Bring your own AI key** — use **your own AI provider** for name & palette suggestions: **Claude, OpenAI, Gemini**, or a **local model** (Ollama / LM Studio / any OpenAI-compatible endpoint). Pick the provider and model in Settings → AI; the Suggest button shows which one will run
- **AI auto-tagging (optional)** — turn it on and AI suggestions also propose **descriptive tags**, which make assets easier to find in search and sharpen **Find Similar**
- AI remains **fully optional** — every feature works without a key

---

## [1.2.0] — 2026-06-16

### Video & PDF, find similar, font pairings, accessibility & backups
- **Video & PDF support** — save, preview, and **play video** files and open **PDFs** right alongside your images, each with an auto-generated thumbnail so your grid stays scannable
- **Find Similar** — pick any image and **“More like this”** surfaces visually similar saves from your library
- **Font pairings** — get **suggested typeface pairings** for any font, right in the info panel
- **Automatic backups** — schedule **recurring backups** of your library (with how-many-to-keep retention), or back up on demand anytime — full archive or catalog-only
- **High-contrast themes** — accessible **high-contrast light and dark** modes for better legibility
- Improvement: larger, **macOS-native window corners** to match the latest system look

---

## [1.1.0] — 2026-06-12

### Color & type tools, plus sharper filtering
- **Contrast checker** — see the **WCAG contrast ratio** between palette colors, flagged **AA / AAA / Fail**, in the palette builder, the info panel, and on a palette asset — quick checks for accessible text-on-background pairs
- **Export palettes** — copy or save any palette as **CSS variables, SCSS, Tailwind config, JSON, a hex list, or an Adobe `.ase`** swatch file, with a custom variable name so it drops straight into your project
- **Advanced filters** — narrow your library by **date added** (presets or a custom range), **source site** (everything saved from a given domain), and **orientation** (landscape / portrait / square) — all stacking with your existing folder, tag, color, and search filters
- **Faster properties** — image **dimensions** in the details panel now appear instantly instead of waiting on the image to load

---

## [1.0.1] — 2026-06-12

### Asset properties, easier color search & smoother updates
- **Asset properties at a glance** — the details panel and full-screen view now show **dimensions, file size, type, and the dates imported/modified**
- **Color search is easier to find** — type a **hex code** (like `#5B7FFF`) in the search bar to pull up every asset and palette using that color, and a small **color chip** appears so it's clear you're searching by color
- **Copies now show up in clipboard managers** — copying a swatch's hex lands in your clipboard **history** (Paste, etc.), not just on the next paste
- **Check for updates anytime** — a new **Check for updates** option in Settings, and Morgue now re-checks periodically while it's running, so you'll hear about a new version even if you rarely quit the app

---

## [1.0.0] — 2026-06-11

### Morgue 1.0 🎉
Our first stable release. Highlights since the last beta:
- **Color search** — type a **hex code** in the search bar to find every asset and palette using that color; an empty search now shows a clear **"No matches"** state instead of looking like an empty library
- **Accessibility** — the asset grid is **fully keyboard-navigable** (arrows, Home/End, Space, Enter, ⌘A) with visible focus rings, and Morgue now **respects your macOS high-contrast and reduced-motion** settings
- **Toast notifications** — quick, unobtrusive confirmations for actions like export, import, and copy (and clear messages when something fails)
- **Refined window** — rounded corners with native-style window controls and full-screen support
- **Safer imports** — importing a backup no longer **duplicates boards**, and imports are now **all-or-nothing**, so a failed import can't leave a half-imported library
- **Licensing fix** — closed an edge case where an offline or not-yet-activated device could lock itself out
- Plus reliability and polish throughout

---

## [0.21.1] — 2026-06-08

### Extension polish
- The extension popup is a bit **wider** so longer titles and the capture-mode buttons have room to breathe
- The **Visible / Full page / Region** buttons are now properly aligned with the preview and evenly spaced
- Requires extension **v1.0.16**

---

## [0.21.0] — 2026-06-08

### Full-page & region capture (extension)
- The extension can now capture in **three modes**, chosen from buttons above the preview:
  - **Visible** — the current viewport (as before)
  - **Full page** — scrolls the whole page and stitches it into one tall screenshot (fixed/sticky headers are hidden after the first slice so they don't repeat)
  - **Region** — drag a box over any part of the page to grab just that area
- Full-page capture shows live progress; region capture lets you draw a selection right on the page (Esc to cancel)
- Requires extension **v1.0.15**

---

## [0.20.0] — 2026-06-08

### Web fonts preview true-to-type
- Fonts captured from the web (not just local fonts) now **preview in their real typeface** across the sidebar, grid, and boards — the app stores a loadable font URL when there's no local file and loads the actual face
- Falls back gracefully to a system copy, then a default, when a font genuinely can't be loaded
- Applies to **newly captured** fonts going forward

---

## [0.19.0] — 2026-06-08

### Board templates
- New boards can **start from a template** instead of a blank canvas — pick one from the empty board's "Start from a template" row
- Four layouts to begin with: **Comparison** (A/B), **Before / After**, **Brand Board** (logo / color / type / imagery), and **Three Sections** (inspiration / direction / references)
- Templates drop in labeled heading sections, centered in view — then you fill each area with assets, notes, and connectors as usual

---

## [0.18.0] — 2026-06-08

### AI focuses on name + palette (no more auto-tags)
- AI now suggests just a **name and a color palette** — the two things it's reliably great at. **Tagging is fully manual** again, so your tags stay meaningful and intentional
- Desktop: the AI panel shows a **Suggested name** (one click to apply) alongside the suggested palette
- Extension: the AI/auto-suggest fills the **name and palette** only; it no longer injects guessed tags into your tag field
- Requires extension **v1.0.14** and an app rebuild

---

## [0.17.6] — 2026-06-08

### AI tags: fewer, and about why you saved it
- AI now suggests **3–5 tags, fewer is better** — capped at 5 — instead of an exhaustive description
- It recognizes **non-UI work** (illustration, packaging, posters, branding, product photos) and tags the **design discipline** a designer would save it for — e.g. *packaging design*, *label illustration*, *craft beer* — rather than generic photo descriptors
- **No more near-duplicates** (e.g. not both *product photography* and *food photography*), and photography-genre tags are only used when the photography itself is the point

---

## [0.17.5] — 2026-06-08

### AI tags now lead with the design type
- AI now **identifies what kind of UI/design it is first** — e.g. *saas landing page*, *dashboard ui*, *pricing page*, *login screen*, *mobile app*, *blog layout* — then the major components, then the industry
- **Incidental atoms aren't tagged anymore** — *button*, *logo*, *icon*, *input*, *menu*, *badge*, etc. are dropped *unless that element is the whole point of the shot* (a dedicated logo or button/icon showcase keeps them)
- Fewer, more meaningful tags overall

---

## [0.17.4] — 2026-06-08

### Even tighter AI tags
- AI no longer suggests **bare fragments** like *landing*, *page*, *section*, *cloud*, *header*, *grid*, or *card* — it must use the complete component name (*landing page*, *hero section*, *logo cloud*, *bento grid*, *blog cards*)
- **Brand / business noise** is filtered out too — *studio*, *brand*, *content*, *platform*, *product*, *template*, *company*, and similar are dropped (and the model is told not to tag the brand's own name)
- A few more mood adjectives joined the block-list (*bold*, *vibrant*, *premium*, *luxury*, …); when there isn't enough concrete detail, the AI now returns fewer tags instead of padding with filler

---

## [0.17.3] — 2026-06-08

### Fix: auto-suggest now lands before save
- With **Auto-suggest on capture** enabled, hitting **Save to Morgue** now waits for the AI to finish so the suggested **tags and palette are included in the capture** — previously a fast save could beat the AI and store nothing
- The Save button shows **"Analyzing…"** briefly while it waits
- Requires extension **v1.0.13**

---

## [0.17.2] — 2026-06-08

### Fix: "Server error 413" when capturing
- Captures and AI analysis with large screenshots no longer fail with **413 (payload too large)** — the local bridge now accepts much bigger images (up to 64 MB) instead of the previous 2 MB cap
- Requires updating/relaunching the desktop app

---

## [0.17.1] — 2026-06-08

### Auto-suggest on capture (extension)
- New **"Auto-suggest on capture"** toggle in the browser extension — when on, AI runs automatically as the popup opens and pre-fills the name, palette, and (smarter) tags, so you can just hit Save
- Off by default and remembered between captures, so there's no surprise API usage
- Requires extension **v1.0.12**

---

## [0.17.0] — 2026-06-08

### Smarter AI tags
- AI tag suggestions now name **concrete, recognizable things** in the image — UI components and layout patterns like *blog cards*, *news cards*, *pricing table*, *hero section*, *bento grid*, *testimonial grid*, plus the kind of page/product and its industry
- **Generic filler is gone** — vague aesthetic/mood tags like *modern*, *minimal*, *clean*, *modern typography*, *ui*, and *inspiration* are no longer suggested (and are filtered out even if the model returns them)
- Applies everywhere AI suggestions appear — the desktop info panel and the browser extension (both share the same engine)

---

## [0.16.2] — 2026-06-08

### True-to-type font previews everywhere
- The real typeface now renders for fonts **on the grid and on boards** too — not just the sidebar — loading the actual font file when it's known
- Grid font cards show a larger **Aa** specimen in the font's own face
- Consistent graceful fallback (system copy → default) when a font has no local file

---

## [0.16.1] — 2026-06-08

### True-to-type font previews
- Fonts in the sidebar now preview using their **actual font file** when it's a local font — the app loads the real typeface instead of relying on a system copy being installed under the same name
- Falls back gracefully to a system-installed copy (then a default) when no font file is available (e.g. fonts captured from the web)

---

## [0.16.0] — 2026-06-08

### Browse your library by font
- New **Fonts** section in the sidebar lists every typeface across your library — saved fonts plus fonts detected on your assets — each previewed **in its own typeface** with a count
- **Click a font** to filter the grid to everything that uses it (the saved font swatch and any asset it appears on)
- The list updates automatically as you capture new fonts, and the section collapses like Folders/Boards/Tags

---

## [0.15.0] — 2026-06-08

### Unified search
- The library search now matches across **name, source site, notes, tags, and fonts** — not just names. So you can find everything you saved from a site by typing its domain, or pull up every asset using a given typeface
- **Fonts are now searchable** — search a font family and you'll get the saved font plus any asset it was detected on
- **Multi-word search** narrows results: every word you type must match somewhere (e.g. `figma hero` finds assets that match both)

---

## [0.14.3] — 2026-06-08

### Board drag polish
- Boards now show a **drag-handle (grip dots)** on the left, matching folders — grab it to reorder
- A **floating label of the board's name** follows your cursor while dragging, so it's clear what you're moving

---

## [0.14.2] — 2026-06-08

### Fix: board drag-reordering
- **Dragging boards now actually works** — switched to the same pointer-based drag the folders use (the webview doesn't fire native drag events), so reordering is reliable. Double-click-to-rename and click-to-open are unaffected

---

## [0.14.1] — 2026-06-08

### Reorder boards
- **Drag boards** in the sidebar to reorder them — a drop indicator shows where it'll land, and the order is saved

---

## [0.14.0] — 2026-06-08

### Board: connectors & arrows
- **Connect two items** with a line or arrow — select exactly two items and hit **Connect** in the toolbar
- Connectors **follow their items** as you move and resize them, anchoring to the nearest edge
- **Click a connector** to select it, then recolor it (5 presets), **toggle the arrowhead** on/off, or remove it (**Delete**)
- Removing an item automatically cleans up any connectors attached to it
- Connectors are **included in board exports** (and print to PDF) just like everything else

---

## [0.13.0] — 2026-06-08

### Board: floating toolbar + multi-select
- The board tools now live in a **floating toolbar at the bottom** of the canvas instead of the header — it stays out of the way and surfaces contextual controls (size, color, layering, duplicate, remove) only when something is selected
- **Multi-select**: shift-click items to add/remove from the selection, or **shift-drag on empty canvas** to rubber-band a group. Move the whole group together in one drag (with snapping)
- **Duplicate** selected items with the toolbar button or **⌘D**
- **Copy / paste** items with **⌘C / ⌘V**
- **Select all** with **⌘A**; **Delete/Backspace** removes everything selected; **Esc** clears the selection
- Layering (forward/back), text size, and note color now apply to **all selected items** at once

---

## [0.12.1] — 2026-06-08

### Board snapping + collapsible sidebar
- Boards now have **snapping with alignment guides** — drag an item and it snaps to other items' edges and centers, with orange guide lines showing the alignment. Toggle it on/off with the **Snap** button
- The sidebar's **Folders, Boards, and Tags sections collapse** (click the section title) so you can hide what you're not using — your choices are remembered
- Long lists now **cap their height and scroll** instead of pushing everything else off-screen

---

## [0.12.0] — 2026-06-08

### Text & sticky notes on boards
- Add **text labels** and **sticky notes** to a board from the toolbar — for headers, captions, and annotations alongside your assets
- **Double-click to edit** any text or note; pick from **Heading / Body / Caption** sizes, and choose a **sticky-note color** from a handful of presets
- Text and notes **resize freely** (assets still keep their aspect ratio)
- Text and notes are included when you **export a board** (and print to PDF), positioned just like on the canvas

---

## [0.11.4] — 2026-06-08

### Boards remember their view
- Each board now **remembers its pan position and zoom level** — reopen a board and it's exactly where you left it

---

## [0.11.3] — 2026-06-08

### Board zoom control
- The board zoom **+ / −** buttons now step in clean **5% increments**
- You can also **type an exact zoom %** right in the box (Enter to apply, Esc to cancel)

---

## [0.11.2] — 2026-06-08

### Board polish
- Added a **zoom control** in the bottom-right of boards — current percentage on top, **+ / −** below (click the percentage to reset to 100%)
- The right info panel is now **hidden on boards**, giving the canvas the full width
- Fixed **color palettes (and color blocks) disappearing when saving a board or gallery to PDF** — background colors now print correctly

---

## [0.11.1] — 2026-06-08

### Board improvements
- Assets now drop onto a board at their **real aspect ratio** (no more cropped hero images), and resizing **keeps that ratio** so the whole image stays visible as you scale
- Board images now show in full (contained) rather than cropped to fill
- New **Export** button on boards — saves the board's spatial layout as a self-contained, shareable HTML page (with a Save as PDF button), preserving each item's position, size, and stacking

---

## [0.11.0] — 2026-06-08

### Moodboards
- New **Boards** section in the sidebar — create freeform canvases to arrange your inspiration spatially instead of in a grid
- **Add assets from your library** onto a board, then **drag to move, drag the corner to resize, and layer** them (bring forward / send back)
- **Pan** by dragging the canvas and **zoom** with the scroll wheel (zoom centers on your cursor); a reset button returns to 100%
- Select an item to move/resize/layer/remove it; **Delete** removes it from the board (the asset stays in your library). Everything is saved automatically
- Rename a board by double-clicking it; delete a board without touching its assets

---

## [0.10.1] — 2026-06-08

### Export & branding polish
- Exported galleries now have a **Save as PDF** button right on the page — click it to open the print dialog straight to PDF, no menu-hunting
- The **Morgue app icon** (rounded like an app icon) now appears on exported galleries, the changelog, and the privacy policy, replacing the old generated mark

---

## [0.10.0] — 2026-06-08

### Export gallery
- New **Export** button in the toolbar turns the current view into a **self-contained, shareable HTML gallery** — one file, no dependencies, perfect for sending a client or teammate
- Exports exactly what you see: any folder, tag, color filter, or All Assets — images, palettes, and fonts together, titled by the current view
- Each item carries its **source link, attached color swatches, fonts, and tags**; images are embedded directly so the file works offline and anywhere
- Themed to match Morgue (and **print-to-PDF friendly** — open it and Save as PDF for a polished deck)
- After exporting, the file is revealed in Finder

---

## [0.9.10] — 2026-06-08

### Hover font inspector (extension)
- New **Hover & pick from page** button in the extension's font section turns on an on-page inspector: hover any text to see its **font family, weight, and size** in a tooltip, and click to grab it
- Grabbed fonts are remembered and **pre-selected the next time you open Morgue** on that page, ready to attach to the saved asset (they're badged Local / Google / Web like auto-detected fonts)
- A floating banner shows while inspecting; press **Esc** or click **Done** to exit. Links don't navigate while the inspector is active

---

## [0.9.9] — 2026-06-08

### Quick wins
- **Click a palette swatch to filter by that color.** In an asset's Color Palettes section, clicking any swatch jumps to All Assets filtered to that color — a one-click bridge from "I like this color" to "show me everything with it"
- **Open an asset's source URL straight from the grid.** Hovering a card with a source URL now shows an open-in-browser button, so you can jump to the original page without opening the asset first (the lightbox and details panel already supported this)

---

## [0.9.8] — 2026-06-08

### Font detection in the extension
- The Morgue browser extension now **detects the fonts used on the page you're saving**. A "Fonts on this page" list shows each typeface (with a live preview), ranked by how much it's used
- Each font is badged **Local** (installed on your machine), **Google** (matched against your Google Fonts catalog, if a key is set), or **Web**
- Tap the fonts you want and they're **attached to the saved asset**, showing up in its Fonts section — alongside the screenshot, tags, and palette
- Fonts are read only when you open the extension on a page (via `activeTab`), so nothing runs in the background

---

## [0.9.7] — 2026-06-07

### Fixes
- Fixed the delete confirmation appearing **behind** the duplicate finder (and other modals) — confirmation dialogs now always sit on top, so deleting a duplicate works as expected

---

## [0.9.6] — 2026-06-07

### Better duplicate detection
- Replaced the difference-hash with a **DCT-based perceptual hash**, which is much more reliable on flat, mostly-white screenshots (like landing-page heroes) where the old hash missed obvious near-duplicates
- Retuned the Strict / Normal / Loose sensitivity for the new hash; hashes recompute once on the next scan

---

## [0.9.5] — 2026-06-07

### Clickable source URLs
- The **Source URL** in the asset details panel (and lightbox) is now a real link — click it to open the page in your browser, with a dedicated open-in-browser button next to it
- Editing the URL moved to a small pencil button, so a single click opens the page instead of dropping into edit mode
- Bare URLs without a scheme are opened as `https://` automatically

---

## [0.9.4] — 2026-06-07

### Fixes & polish
- **Duplicate finder now actually finds duplicates.** Perceptual hashing moved from the browser canvas (which couldn't reliably read image pixels) to native Rust image decoding — identical and near-identical screenshots are detected correctly. Existing hashes are reset once so they recompute accurately
- Moved the **keyboard-shortcuts** button out of the toolbar (where it sat awkwardly between the item count and column controls) to the top-right of the page header

---

## [0.9.3] — 2026-06-07

### Duplicate finder
- New **Find Duplicates** entry in the sidebar opens a finder that spots near-identical images across your whole library — not just exact copies, but crops, re-saves, and lightly edited versions
- Uses a perceptual hash (dHash) computed once per image and cached, so repeat scans are instant
- **Strict / Normal / Loose** sensitivity lets you dial how aggressively similar images are grouped
- Each group keeps the **oldest copy** highlighted; delete extras individually or with one click ("Keep oldest · Delete N"), always behind a confirmation
- Hashes are computed locally on your machine — nothing leaves your device

---

## [0.9.2] — 2026-06-07

### Keyboard-first navigation
- A **keyboard shortcuts** reference now lives in Settings → **Keys**, with a quick-access keyboard icon in the grid toolbar
- Drive the whole grid from the keyboard:
  - **Arrow keys** move a focus ring cell-by-cell (Left/Right) and row-by-row (Up/Down); **Home/End** jump to the first/last asset
  - **Shift + arrows** extend a multi-selection as you move
  - **Space** toggles the focused asset in/out of the selection
  - **Enter** opens the focused image in the lightbox (or selects non-images)
  - **F** stars/unstars the focused asset; **⌘A / Ctrl+A** selects everything visible
  - **Delete / Backspace** removes the focused asset or the whole selection
- The focused cell always scrolls into view, and clicking a card moves keyboard focus there too — so mouse and keyboard stay in sync

---

## [0.9.1] — 2026-06-07

### Bulk operations
- The multi-select bar now does more than delete. Select multiple assets (Cmd-click / Shift-click) and you can:
  - **Star / Unstar** the whole selection in one click (toggles based on whether they're all already favorited)
  - **Add to folder** — pick any folder from a nested list
  - **Tag** — type to filter existing tags or create a new one on the fly, applied to every selected asset
- Inline confirmation flashes after each action; selection stays put so you can chain operations (star → tag → move)

---

## [0.9.0] — 2026-06-07

### Color search
- **Filter your whole library by color.** A new **Color** control in the filter bar opens a swatch board built from the colors actually in your library — click one (or pick a custom color) to show every asset whose palette contains that color
- Matching uses perceptual color distance with **Exact / Close / Loose** tolerance, so "find me everything with this orange" works even when shades differ slightly
- Composable with everything else — color stacks on top of folder, tag, favorites, and text-search filters
- Matches across both images with extracted palettes and standalone palette assets

---

## [0.8.13] — 2026-06-05

### Custom domain
- Changelog + privacy pages moving to `morgueapp.com` (`changelog.morgueapp.com`, `privacy.morgueapp.com`); in-app Changelog link now points to `changelog.morgueapp.com`

---

## [0.8.12] — 2026-06-05

### Menu-bar icon
- Replaced the full-color app icon in the menu bar with a monochrome ghost **template** icon, so it adapts to light/dark menu bars and matches the system's other icons (instead of looking out of place)

---

## [0.8.11] — 2026-06-04

### Version + changelog links
- Small footer in the Settings panel showing the app version and a **Changelog** link (opens the hosted changelog page)
- Sidebar footer now shows the version + a Changelog link alongside the library location
- Version is read from `package.json` so it stays in sync automatically

---

## [0.8.10] — 2026-06-04

### Run in the background (menu-bar app)
- Closing the window now **hides** Morgue instead of quitting, so the local capture bridge keeps serving the Chrome extension
- Added a **menu-bar (tray) icon** with **Open Morgue** / **Quit Morgue** — quit fully from there (or Cmd+Q)
- Clicking the dock icon reopens the window when it's hidden (macOS)
- Extension tab note updated to explain the background behavior

---

## [0.8.9] — 2026-06-04

### Icons
- "Add to Chrome" button now uses a globe icon
- The "Palette" option in the dashboard Add menu now uses a palette icon

---

## [0.8.8] — 2026-06-04

### Settings — Browser Extension tab
- New **Extension** tab in Settings with an **"Add to Chrome"** button (opens the Chrome Web Store listing in the default browser) and a live **capture-bridge status** indicator (pings `localhost:57432`)
- Wired to the real listing (item ID `mcbapocgkibpbpdkccpkakdcnobjdmhk`); the link goes live once the listing is approved

---

## [0.8.6] — 2026-06-04

### Extension — Web Store prep
- Removed the unused `scripting` permission from the extension manifest (unnecessary permissions get rejected in review)
- Bundled the Space Mono + Inter fonts **locally** in the extension (`extension/fonts/`, latin subset, ~115KB) and switched `popup.html`/`popup.css` to local `@font-face` — no more `fonts.googleapis.com` requests, so the popup works offline and avoids remote-resource scrutiny
- Extension bumped to 1.0.9 — re-zip and re-upload the package

---

## [0.8.4] — 2026-06-04

### Fix — drag-and-drop now uses pointer events (works in the Tauri WebView)
- Real cause found: Tauri's OS-level drag-drop handler (kept on so images can be dragged in from Finder) intercepts native HTML5 drags — hence the green "+" cursor and drops never landing
- Reworked in-app dragging to use pointer events instead (new `lib/drag.ts`): a floating ghost follows the cursor, folder rows are detected via `data-folder-id`, and drops are resolved manually
  - Folder grip (⠿): drag to reorder (top/bottom edge) or nest (middle)
  - Asset cards: drag onto a folder to add it there
- Finder → app image import (the OS drag-drop) is unaffected
- Disabled native dragging on thumbnail images so it can't re-trigger the OS drag

---

## [0.8.3] — 2026-06-04

### Fix — folder drag-and-drop (for real this time)
- Root cause: making the folder *row* `draggable` stopped it from receiving drop events in the WebView, which broke folder dragging AND asset-to-folder drops
- Folder rows are now plain drop targets again (restoring asset-to-folder), and dragging is done via a dedicated **grip handle** (⠿) on the left of each row — drag it to reorder (top/bottom edge) or nest (middle)

---

## [0.8.2] — 2026-06-04

### AI — auto-generated asset names (extension)
- The extension's "✨ Suggest" now also generates a concise, descriptive **name** from the page context (title + URL) plus the screenshot, and fills the name field — button relabeled "Suggest Name, Palette & Tags"
- Claude's analysis returns a `name` alongside palette + tags; the `/ai/analyze` bridge accepts optional page title/URL as context
- Settings AI tab: moved this from "Planned" to "Enabled by your keys"

---

## [0.8.1] — 2026-06-04

### Fix — folder & asset drag-and-drop
- Drag-and-drop was broken (folders couldn't be dragged/nested, and asset-to-folder stopped working). Cause: `dataTransfer.types.includes()` threw in the WebView (where `types` is a `DOMStringList`), aborting the drop handlers. Now uses an internal drag ref to tell folder vs asset drags apart — no reliance on the `types` API

---

## [0.8.0] — 2026-06-04

### Folders — sorting & drag-and-drop
- New sort menu (next to the + in the Folders header): **Newest first** (default), **A → Z**, **Z → A**, and **Manual**
- Drag folders to reorder (drop on the top/bottom edge of a row) or nest them (drop on the middle of a row) — reordering switches to Manual sort and is persisted; guards against cycles and the 4-level depth limit
- Sort preference persists across launches

### Tags — alphabetical
- Tags in the sidebar are now always sorted A → Z (no more count-based ordering)

### Fonts — add to folders without favoriting
- Each font card has an **add-to-folder** button (folder picker) — adds the font to a folder even if it's not favorited (e.g. a client's brand font you need handy but don't want starred)
- Favoriting and library-membership are now decoupled: the star toggles **favorite** only; a font added to a folder lives in the library un-favorited; un-favoriting a font that isn't in any folder removes it from the library

---

## [0.7.3] — 2026-06-04

### Settings — clickable console links
- The "console.cloud.google.com" and "console.anthropic.com" references in the AI tab are now real links that open in your default browser (via the opener plugin) — Google's goes straight to the Web Fonts Developer API page, Anthropic's to the API keys page

---

## [0.7.2] — 2026-06-04

### Google Fonts in the font browser
- Add your Google Fonts API key in Settings → AI (Web Fonts Developer API)
- Font browser gains a **LOCAL / GOOGLE** toggle; Google mode previews the full catalog (sorted by popularity), searchable, with live remote previews
- Google font cards show a small "G" badge in the name box; save them to your library like local fonts
- Catalog fetched through the Rust backend (key stays local); `http://` file URLs rewritten to `https://` for the webview; renders the first 90 results with search to narrow down
- Backend: `set_google_fonts_key` / `google_fonts_key_status` / `google_fonts_list`; API-key config refactored to hold multiple keys in one file

---

## [0.7.1] — 2026-06-04

### AI — switched to Claude Haiku
- AI palette/tag analysis now uses `claude-haiku-4-5` — faster and cheaper, with equivalent quality for this task

### Palettes — editable after creation
- Edit any palette in place: rename, change colors, add or remove swatches
- Edit from the **asset details panel** (pencil next to each assigned palette) or from a **palette's own details** (pencil in the header)
- Edits apply everywhere the palette is used; the palette builder reused for both create & edit (`updatePalette`)

---

## [0.7.0] — 2026-06-04

### AI — Claude palette + tag suggestions (app + extension)
- **Settings → AI:** add your Anthropic (Claude) API key. Stored locally in `ai_config.json`, never sent anywhere but Anthropic, and shared with the extension via the local bridge. Connected/replace/remove states; key is never read back to the UI.
- **App (asset details):** new "✨ Suggest Palette & Tags" on image assets — analyzes the image with Claude (vision) and returns a suggested color palette + descriptive tags. Save & assign the palette in one click; add tags individually or all at once (already-applied tags are marked).
- **Extension popup:** "✨ Suggest Palette & Tags" analyzes the captured screenshot; suggested tags merge into the tags field and a suggested palette is saved & attached to the capture automatically (clearable).
- **Backend:** new `ai` module (Anthropic Messages API, `claude-sonnet-4-6`), Tauri commands `set_ai_key` / `ai_key_status` / `ai_analyze_image`, and a `/ai/analyze` bridge endpoint. Capture endpoint extended to persist an attached palette.

### App icon — temporarily disabled
- Custom app-icon switching is disabled for now (still being refined); the app uses its default icon. The switcher is shown greyed-out in Settings.

---

## [0.6.9] — 2026-06-04

### Dock icon — actually persists on first change now
- The Dock caches a non-running app's icon and only re-reads it on the app's next launch — which is why an icon change only "stuck" after reopening. After writing the icon to the bundle, the Dock is now restarted (`killall Dock`, it relaunches instantly) so the change is reflected immediately, including the closed state
- Removed the launch-time re-apply (no longer needed now that the icon lives on the `.app` bundle) so the Dock isn't restarted on every app open

---

## [0.6.8] — 2026-06-04

### Dock icon — fix first-change persistence & live revert
- After writing the icon to the `.app` bundle, the icon cache is now invalidated (`noteFileSystemChanged:`) so the Dock/Finder pick it up **immediately** — previously the change only stuck after a relaunch (the Dock kept the icon it cached at launch)
- The live running tile is now set from the bundle's *current* icon (`iconForFile:`), so selecting **Default** reverts the icon right away instead of waiting for a restart

---

## [0.6.7] — 2026-06-04

### Dock icon — persists even when the app is closed
- Selecting a custom icon now also writes it onto the `.app` bundle via `NSWorkspace setIcon:forFile:` (same mechanism as Finder's "paste custom icon" — uses extended attributes, doesn't touch the signed bundle contents), so the Dock & Finder keep showing your chosen icon after quitting
- Choosing "Default" clears the custom bundle icon, restoring the original
- Fixed a latent bug: icon paths are now passed to `initWithUTF8String:` as null-terminated `CString`s
- Note: bundle persistence only applies to the built `.app` (not `tauri dev`)

### Lightbox — palette builder z-index
- "Create New Palette" now opens above the full-screen image viewer (was rendering behind it)

---

## [0.6.6] — 2026-06-04

### Dock icon — persists across launches
- The selected app icon (3D / Dark) is now re-applied on every launch — macOS resets the dock icon to the bundle default each time, so we restore the saved choice on startup

### Library — relocate to any folder + move assets
- New **"Choose New Location"** in Settings → Library: move your library to an external drive or a cloud-synced folder (Google Drive, Dropbox, OneDrive…)
- A `Morgue Library` folder is created inside the chosen location; all asset files are moved (instant rename on same volume, copy+delete across drives) and their DB paths re-linked automatically
- Library root is persisted in `library_location.txt` and resolved fresh for imports + extension captures, so the new location takes effect immediately
- Asset protocol scope broadened to include `/Volumes/**` (external drives); cloud drives under the home folder were already covered

### Fonts — favoriting
- Favoriting (saving) a font now also adds it to **Favorites**, not just All Assets

### Planned (noted)
- Google Fonts API key support — let users add their own key to browse & preview Google Fonts in the font browser

---

## [0.6.5] — 2026-06-04

### App icons — size match
- 3D / Dark dock icons inset to the macOS icon grid (content at ~80.5% of the tile, standard transparent margin) so they match the Default icon's footprint instead of reading oversized

---

## [0.6.4] — 2026-06-04

### App icons — new options + proper dock rendering
- Icon options are now **Default / 3D Ghost / Dark**
  - Default = the original flat orange ghost
  - 3D Ghost = new sculpted ghost on orange squircle (`morgue-3d`)
  - Dark = cream ghost glowing on dark navy (`morgue-dark-clipped`)
- **Default now restores the real bundle icon** at runtime (`setApplicationIconImage: nil`) instead of loading a low-res PNG — so it's crisp, rounded, and correctly sized in the dock
- 3D / Dark dock icons regenerated as full-bleed **1024px squircle PNGs** with transparent macOS-radius corners (no more white corners on 3D, no more square edges on Dark) so they read as true app icons
- Removed the now-unused `icon-flat.png` bundled resource

### Settings — gear icon
- Replaced the header Settings gear with a cleaner icon, stroke-weighted to match the other header icons

---

## [0.6.1] — 2026-06-04

### Fix — picker width in lightbox sidebar
- PalettePicker/FontPicker width now calculated from the parent panel (`aside` or `[data-theme]`) not the tiny `+` button
- Min width 220px enforced so pickers are always readable

---

## [0.6.0] — 2026-06-04

### Settings modal
- Gear icon restored to header — opens Settings modal
- Three tabs: Appearance, Library, AI
- **Appearance tab:**
  - App icon switcher — Flat / 3D / Ghost, persisted across restarts
  - Theme default — visual light/dark previews, same toggle as header
  - Icon change note (takes effect on next launch)
- **Library tab:**
  - Shows full library path
  - "OPEN" button reveals the library folder in Finder via `open -R`
  - "Relocate Library" placeholder — coming next release
- **AI tab:**
  - Coming soon placeholder with planned features listed
  - Claude + OpenAI key input, palette extraction, tag suggestions, extension integration
- New Rust command: `reveal_in_finder(path)` — opens Finder with the path selected

---

## [0.5.6] — 2026-06-04

### App — tag section spacing
- Assigned tags now appear above the input (not below suggestion chips)
- 10px gap between assigned tags and the add-tag input
- 8px gap between suggestions and input
- Clearer visual hierarchy: existing tags → input → suggestions

---

## [0.5.5] — 2026-06-04

### App — palette/font picker z-index fix
- PalettePicker and FontPicker now render via `ReactDOM.createPortal` attached to `document.body` with `position: fixed` — they no longer get clipped by the info panel's `overflow: auto` scroll container
- Anchor position calculated with `getBoundingClientRect()` so dropdowns open directly below their trigger button regardless of scroll position

### App — tag suggestions in info panel
- TagAdder now shows existing tags as clickable chips when opened
- Chips filter as you type — helps avoid duplicates like `#footer` vs `#Footer`
- Click a chip to add instantly; type and press Enter to create a new tag
- Tags fetched from DB on open

---

## Extension 1.0.5 — 2026-06-04

### Extension — icon updated to 3D transparent ghost
- Using `morgue-3d-transparent.png` — rounded square, cleaner edges

---

## [0.5.4] — 2026-06-04 · Extension 1.0.4

### Extension — icon updated to 3D ghost (1.0.4)
- Switched back to 3D ghost icon (`morgue-3d.png`) — orange rounded square with cream cloth ghost

---

## [0.5.4] — 2026-06-04 · Extension 1.0.3

### App — sidebar selection fix
- Clicking a folder or tag now clears the selected asset — folder/tag panel shows immediately even if an image was previously selected
- `selectLib`, `selectFolder`, `selectTag` in Sidebar all call `setSelectedAsset(null)`

### Extension — new icon (1.0.3)
- Updated to flat 2D ghost icon — cleaner at small toolbar sizes
- 16/48/128px all regenerated from new source

---

## [0.5.3] — 2026-06-04 · Extension 1.0.2

### App — folder rename sidebar fix
- Renaming a folder now updates the left sidebar immediately — `loadFolders()` added to the `assetVersion` effect so folder names sync on every mutation

### Extension — polish (1.0.2)
- Ghost icon applied to extension toolbar (16/48/128px)
- Popup rounded corners (`border-radius: 12px`) — no more sharp square popup
- White bleed removed — `html` background set to transparent, header clips to rounded top corners

---

## [0.5.2] — 2026-06-04 · Extension 1.0.1

### App — folder & tag rename
- Right info panel now shows a folder detail view when a folder is selected (no asset selected)
- Right info panel shows a tag detail view when a tag is selected
- Folder name editable inline — click to rename, Enter/blur saves, propagates everywhere
- Tag name editable inline — `#` is fixed, edit the word part only, updates all assets instantly
- Both panels show asset count and a hint about rename propagation
- New DB functions: `updateFolderName`, `updateTagName`, `fetchFolderById`, `fetchTagById`

### Extension — custom folder dropdown (1.0.1)
- Replaced native `<select>` with custom overlay dropdown matching the app's "Add New" menu style
- Folder icon, checkmark on selected item, animated chevron, closes on outside click
- Dark/light themed, matches Morgue aesthetic

---

## [0.5.1] — 2026-06-04 · Extension 1.0.0

### App
- Sidebar and info panel height restored to full height after resize handle refactor
- Layout simplified — panels are direct flex children, `height: 100%` resolves correctly

### Extension — v1.0.0
- First stable release of the Morgue Chrome Extension
- Matches full Morgue app theme (light + dark mode)
- One-click capture with screenshot, name, URL, folder, and tag assignment
- Tag suggestions pulled live from your Morgue library
- Offline queue — captures saved locally and synced when app reopens
- Right-click context menu for pages, images, and links
- ⌘⇧M keyboard shortcut

---

## [0.5.0] — 2026-06-04

### App — sidebar drag fix
- Rewrote drag handles to use direct DOM style mutation during drag — no React re-renders, completely smooth
- Sidebar and info panel now always fill 100% height (fixed `minHeight: 0` + `height: 100%` on flex containers)
- Widths only commit to Zustand store on `mouseUp`, not every pixel of movement

### App — HTTP server `/tags` endpoint
- New `GET /tags` endpoint returns all existing tag names from SQLite
- Used by extension to populate tag suggestions

### Extension — tag improvements
- Existing tags fetched from Morgue app and shown as clickable chip suggestions below the tags input
- Chips update dynamically as you type — shows matching tags, filtered by current input
- Click a chip to add it; click again to remove it
- Tags correctly styled in dark mode (used CSS variables throughout)

### Extension — dark mode polish
- Select/dropdown dark mode: chevron arrow recoloured for dark bg, `option` elements inherit theme colours
- Tag chips use `var(--accent)` and `var(--border)` — work correctly in both themes

### Extension — screenshot rounded corners
- Preview image and container now have `border-radius: 8px` for a softer feel

### Extension — version → 0.5.0

---

## [0.4.0] — 2026-06-04

### Extension — dark mode toggle
- Sun/moon toggle button in popup header
- Dark theme CSS variables (`[data-theme="dark"]`) added to `popup.css`
- Preference persisted in `chrome.storage.local` — survives browser restarts
- Toggle applies instantly without page reload

### App — real-time extension sync
- HTTP server now emits a Tauri event (`morgue-asset-added`) after every `/capture`
- React frontend listens via `@tauri-apps/api/event` and calls `invalidateAssets()`
- Assets, tags, and counts update instantly when extension saves — no restart needed

### App — resizable sidebars
- Left sidebar and right info panel are now drag-resizable
- Drag handle on the inner border of each panel — `col-resize` cursor
- Left sidebar: 200px min → 400px max
- Right info panel: 220px min → 440px max
- Widths persisted in Zustand store (saved across restarts)
- Grid columns reflow dynamically as sidebar width changes

### Crash fix
- Fixed `tokio::spawn` panic in `.setup()` — Tauri's setup runs before its tokio runtime
- Now uses `std::thread::spawn` + `tokio::runtime::Runtime::new()` for the HTTP server thread
- App no longer crashes on launch with 0.3.0 binary

---

## [0.3.0] — 2026-06-04

### Chrome Extension
- New `extension/` directory — manifest v3 Chrome extension
- **Popup** matches full Morgue editorial theme (Space Mono, warm off-white, orange accent, grain overlay)
- 4 popup states: offline (Morgue not running), main capture form, success, error
- Auto-captures visible tab screenshot via `chrome.tabs.captureVisibleTab()`
- Pre-fills name (page title) and source URL from active tab
- Folder picker dropdown (populated from Morgue's real folder list)
- Tags input with `#tag` syntax
- `⌘⇧M` keyboard shortcut to open popup
- Right-click context menu: "Save page / image / link to Morgue"
- Offline queue — if Morgue is closed, captures are stored in `chrome.storage.local` and auto-flushed when the app comes back online (retries every 30s)
- Extension icons: 16px, 48px, 128px from Morgue icon set

### Localhost HTTP server (port 57432)
- Axum HTTP server starts automatically when Morgue launches
- CORS permissive — works with any Chrome extension origin
- `GET /status` — returns `{ok, version}`, used by extension to detect if app is open
- `GET /folders` — returns full folder tree from SQLite for the popup picker
- `POST /capture` — fully wired end-to-end:
  - Decodes base64 PNG screenshot → saves to `~/Library/Application Support/com.morgue.morgue/library/{uuid}.png`
  - Inserts `assets` record (type = image) with name, source URL, file path
  - Assigns to folder via `asset_folders` if folder selected
  - Upserts tags into `tags` + `asset_tags` tables
  - Assets appear in Morgue grid immediately on next refresh
- Dependencies added: `axum 0.7`, `tokio 1` (full), `tower-http 0.5` (CORS), `base64 0.22`, `sqlx 0.8` (sqlite + runtime-tokio)

### Other
- Morgue app icon applied to extension icons
- Version bumped 0.2.0 → 0.3.0 to reflect new compiled binary with HTTP server

---

## [0.2.0] — 2026-06-04

### App renamed
- Renamed from **InspoSaver** to **Morgue**
- New app icon set applied (all sizes: 16, 32, 64, 128, 256, 512, 1024px + .icns + .ico)
- DB renamed from `insposaver.db` → `morgue.db`
- Bundle identifier updated to `com.morgue.morgue`

### Core infrastructure
- Tauri 2 + React + TypeScript + SQLite (embedded, zero infra)
- Fully frameless window — custom traffic light buttons wired to Tauri window commands
- Light / dark mode with instant toggle, persisted across restarts (no flash on load)
- Grain texture overlay on background (CSS SVG noise, theme-aware)
- Global autocorrect / autocapitalize disabled on all inputs

### Asset grid
- Import images via drag & drop (OS-level, catches files dropped anywhere on window) or file picker
- Duplicate drag import fixed — single global listener, React StrictMode-safe
- Grid column count (4 / 5 / 6) persisted in store across restarts
- Asset type filters: ALL / IMAGES / PALETTES / FONTS
- Sidebar search wired to FTS5 full-text index (name, URL, notes)
- **Multi-select**: ⌘/Ctrl+Click to add, Shift+Click for range, Escape to clear
- Bulk delete with confirmation dialog when multiple selected
- Keyboard Delete/Backspace to delete selected asset(s)
- Favorite star on card hover (top-left); filled orange when favorited; always visible when active
- Hover delete (×) button (top-right), turns red on hover
- Double-click image card opens full lightbox viewer

### Asset types

#### Images
- Real thumbnails via Tauri asset protocol (`convertFileSrc`)
- Files copied to managed library directory (`~/Library/Application Support/com.morgue.morgue/library/`)
- UUID-named files on disk, display name editable separately

#### Palettes
- Manual palette builder: name + up to 12 colour swatches
- Colour picker (native OS) + hex input per swatch
- Live stripe preview as you add/edit colours
- Palette cards show colour stripe bands in the grid
- Deleting a palette asset also removes the underlying palette record (no ghost on restart)

#### Fonts
- System font scanner: reads `/Library/Fonts`, `/System/Library/Fonts`, `~/Library/Fonts`
- Deduplication by (family, style) — fonts installed in multiple dirs shown once
- Live `@font-face` injection — each card renders in the actual font
- Editable preview text field (applies to all cards)
- Favorites filter (SAVED button) to show only saved fonts
- Star button matches main grid style

### Info panel (right sidebar)
- Favorite star toggle
- Editable filename (click to rename — updates grid card immediately)
- Editable source URL (hidden for palettes/fonts — used internally)
- Folder assignment (assign/remove asset from any folder)
- Color palette assignment picker (assign saved palettes; create new from picker)
- Font assignment picker (assign saved fonts; navigate to Browse Fonts from picker)
- Tags (add inline, click to remove)
- Notes (textarea, saves on blur)
- Date added
- DELETE ASSET button (hidden for font assets — system files not managed by app)

### Folders
- Real SQLite-backed folders (not hardcoded)
- Hierarchical tree, up to 4 levels deep
- Inline input to create root folders (no native dialog — works in Tauri WebKit)
- Subfolder creation: hover any folder → `+` button appears inline
- Folder counts show number of assets assigned
- Drag asset card from grid → drop on sidebar folder to assign
- Click folder → filters grid to that folder's assets
- Auto-assigns newly imported images to the current folder when viewing one
- Delete folder (with confirmation): removes folder, not assets
- Folder counts refresh when assets are modified

### Tags
- Real tags with counts loaded from DB
- Click tag in sidebar → filters grid
- Tags list refreshes when new tags are added (no restart needed)
- Delete tag (with confirmation): removes from all assets, not the assets themselves
- Tags also editable per-asset in the info panel

### Lightbox (full image viewer)
- Two-panel: dark image area (left) + metadata sidebar (right)
- Sidebar respects app theme (light/dark)
- Keyboard: ← → to navigate images, Escape to close
- Prev/Next arrow buttons with frosted dark circle style
- N / total counter
- Sidebar fully editable: filename, source URL, folders, palettes, fonts, tags, notes
- Favorite star in sidebar header
- Palette assets show colour stripe view instead of image
- Navigation limited to image-type assets (palettes/fonts excluded)

### Color palette builder modal
- Triggered from ADD menu or from Palette picker in info panel
- After creation, auto-assigns to the asset that opened the picker

### Confirmation dialogs
- Delete asset, delete folder, delete tag, bulk delete — all gated behind confirm
- Escape cancels, Enter confirms
- Each dialog explains what will/won't be deleted

### Bug fixes
- React hooks violation fixed (IIFE `useState` in JSX → extracted to proper components)
- `morgue.db` migration mismatch fixed (`lib.rs` now registers migrations for correct DB name)
- Palette ghost-on-restart fixed (deleting palette asset now cascades to `palettes` table)
- Font unfavorite fixed (delete button correctly removes DB record)
- `window.prompt` replaced with inline inputs (blocked in Tauri WebKit)
- Sidebar tags now refresh immediately when new tags are added

---

## [0.1.0] — 2026-06-03

### Initial build (InspoSaver)
- Tauri 2 scaffold with React + TypeScript + Tailwind CSS v4
- SQLite schema with migrations: assets, tags, folders, palettes, palette_colors, asset_fonts, asset_palettes, asset_folders, FTS5 virtual table
- Basic asset grid with placeholder mock data
- Sidebar layout with hardcoded folders/tags
- Info panel shell
- Light/dark theme toggle with CSS custom properties
- Custom frameless window with traffic light buttons
- Font scanner (Rust) reading system font directories
- Font browser with `@font-face` live preview
