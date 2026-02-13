# Browser Extensions - Development Status

## Status: 🟡 IN DEVELOPMENT - NOT WORKING

Browser extensions for Firefox and Chrome are currently in development and not fully functional. The core L-ZIP engine works, but browser integration needs refinement.

## Available Downloads

- **Firefox**: [L-ZIP-Firefox.xpi](./L-ZIP-Firefox.xpi) - IN DEV
- **Chrome**: [L-ZIP-Chrome.zip](./L-ZIP-Chrome.zip) - IN DEV

## Chrome Extension

**Source**: [browser-extension/](./browser-extension/)

### Features (Planned)
- Context menu compression
- Inline tooltip results
- Clipboard integration
- Settings panel
- Token counter

### Known Issues
- ⚠️ Manifest V3 compatibility pending
- ⚠️ Content script injection not reliable
- ⚠️ Cross-domain requests need fixing

### Files
- `manifest.json` - Extension manifest
- `popup.html/js` - Popup UI
- `background.js` - Service worker
- `content.js` - Page content integrat

ion
- `styles.css` - Styling

## Firefox Extension

**Source**: [browser-extension/](./browser-extension/)

### Features (Planned)
- Context menu compression
- Sidebar panel
- Keyboard shortcuts
- Auto-clipboard copy

### Known Issues
- ⚠️ Permissions model needs adjustment
- ⚠️ Background script lifecycle issues
- ⚠️ Storage API not fully working

## VS Code Extension

**Status**: ✅ WORKING

**Source**: [vscode-extension/](./vscode-extension/)

Install from VS Code Marketplace or build locally:

```bash
cd vscode-extension
npm install
vsce package
# Output: lzip-vscode-0.0.1.vsix
```

## Building for Development

### Prerequisites
```bash
Node.js 16+
npm
```

### Build Chrome Extension
```bash
cd browser-extension
npm install
npm run build
# Output: dist/ folder ready for chrome://extensions
```

### Build Firefox Extension
```bash
cd browser-extension
npm install
npm run build:firefox
# Output: L-ZIP-Firefox.xpi
```

## Testing

### Chrome
1. Go to `chrome://extensions`
2. Enable "Developer mode"
3. Click "Load unpacked"
4. Select the extension folder

### Firefox
1. Go to `about:debugging#/runtime/this-firefox`
2. Click "Load Temporary Add-on"
3. Select `L-ZIP-Firefox.xpi`

## Contributing

If you'd like to help fix browser extension issues, please see [CONTRIBUTING.md](./CONTRIBUTING.md)

## Roadmap

- [ ] Fix Manifest V3 compatibility
- [ ] Improve content script reliability
- [ ] Complete permission model
- [ ] Add comprehensive error handling
- [ ] Full marketplace submission
