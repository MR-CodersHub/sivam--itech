const express = require('express');
const cors = require('cors');
const path = require('path');
const compression = require('compression');

const app = express();
const PORT = process.env.PORT || 5000;

// Enable Gzip compression
app.use(compression());

// Enable CORS
app.use(cors());

// Cache configuration for static assets (1 year)
const staticOptions = {
    maxAge: '1y',
    immutable: true,
    index: false
};

// Serve static images with aggressive caching
app.use('/uploads', express.static(path.join(__dirname, 'uploads'), staticOptions));

// Serve other static files (HTML, CSS, JS) from the root
// HTML files should have shorter cache or no-cache to ensure updates
app.use(express.static(__dirname, {
    maxAge: '1h' // Cache HTML/CSS/JS for 1 hour
}));

// Fallback for SPA or generic routes if needed
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

// Start the server
app.listen(PORT, () => {
    console.log(`Optimized server running at http://localhost:${PORT}`);
});


