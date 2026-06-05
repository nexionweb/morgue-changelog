# Morgue — Changelog

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
  - Decodes base64 PNG screenshot → saves to `~/Library/Application Support/com.nexion.morgue/library/{uuid}.png`
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
- Bundle identifier updated to `com.nexion.morgue`

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
- Files copied to managed library directory (`~/Library/Application Support/com.nexion.morgue/library/`)
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
